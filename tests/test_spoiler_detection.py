import unittest
from src.spoiler_detection import detect_spoilers
from src.config import SPOILER_KEYWORDS

class TestSpoilerDetection(unittest.TestCase):
    def test_detect_spoilers(self):
        content = "This is a spoiler for the movie."
        result = detect_spoilers(content, SPOILER_KEYWORDS)
        self.assertIn("spoiler", result)

if __name__ == '__main__':
    unittest.main()
