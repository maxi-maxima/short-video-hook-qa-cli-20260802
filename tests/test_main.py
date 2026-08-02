import unittest

import main


class TestShortVideoHookQA(unittest.TestCase):
    def test_good_script_scores_high(self):
        text = "Stop scrolling.\nScene 1: open with code review.\nCTA: save this.\n"
        result = main.score_script(text)
        self.assertGreaterEqual(result["score"], 90)
        self.assertEqual(result["issues"], [])

    def test_weak_script_is_flagged(self):
        text = "This is a video about software.\nWe will discuss tools.\n"
        result = main.score_script(text)
        self.assertIn("opening hook is weak", result["issues"])
        self.assertIn("call to action is missing", result["issues"])
        self.assertIn("scene guidance is missing", result["issues"])


if __name__ == "__main__":
    unittest.main()
