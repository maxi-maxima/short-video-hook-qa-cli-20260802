from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HOOK_WORDS = {"stop", "watch", "why", "secret", "mistake", "here", "before", "how", "don't"}
CTA_WORDS = {"cta", "subscribe", "follow", "save", "comment", "link in bio", "try this"}


def load_text(path: Path | None) -> str:
    if path is None:
        return sys.stdin.read()
    return path.read_text(encoding="utf-8")


def score_script(text: str) -> dict:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    first_two = " ".join(lines[:2]).lower() if lines else ""
    later = " ".join(lines[2:]).lower() if len(lines) > 2 else ""
    issues = []
    hook_strong = any(word in first_two for word in HOOK_WORDS) or first_two.endswith("?") or "!" in first_two
    cta_present = any(word in later for word in CTA_WORDS) or any(word in text.lower() for word in CTA_WORDS)
    scene_mentions = len(re.findall(r"\b(scene|shot|b-roll|on screen)\b", text, flags=re.IGNORECASE))

    score = 100
    if not hook_strong:
        issues.append("opening hook is weak")
        score -= 25
    if not cta_present:
        issues.append("call to action is missing")
        score -= 20
    if scene_mentions == 0:
        issues.append("scene guidance is missing")
        score -= 15
    if len(text) > 1200:
        issues.append("script is long for a short-form format")
        score -= 5
    score = max(0, min(100, score))
    return {
        "score": score,
        "hook": "strong" if hook_strong else "weak",
        "cta": "present" if cta_present else "missing",
        "scene_mentions": scene_mentions,
        "issues": issues,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Score short-video scripts.")
    parser.add_argument("--file", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = score_script(load_text(args.file))
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"score: {result['score']}")
        print(f"hook: {result['hook']}")
        print(f"cta: {result['cta']}")
        print(f"issues: {len(result['issues'])}")
        for issue in result["issues"]:
            print(f"- {issue}")
    return 0 if result["score"] >= 70 else 1


if __name__ == "__main__":
    raise SystemExit(main())
