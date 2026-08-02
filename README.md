# short-video-hook-qa-cli

A lightweight script checker for short-form video. It scores the opening hook, call-to-action coverage, and scene pacing so creators can fix weak drafts before recording.

## Pain point
Short-video scripts fail fast when the first line is slow, the CTA is missing, or the scene plan is too vague.

## Why now
Content teams are shipping more AI-assisted videos, and a simple QA pass helps prevent obvious retention mistakes.

## Install
No dependencies. Use Python 3.11+.

## Run
```bash
python main.py --file script.txt
```

## Example
Input:
```text
Stop scrolling.
Today I will show you a faster way to review code.
Scene 1: screen share.
CTA: save this for later.
```

Output:
```text
score: 94
hook: strong
cta: present
issues: 0
```

## Test
```bash
python -m unittest discover -s tests -v
```

## Roadmap
- Add genre-specific templates
- Add JSON output and batch mode
- Add word-count thresholds for shorts and reels
