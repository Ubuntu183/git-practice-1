import subprocess
import sys
import unittest
from script1 import make_greeting

class GreetingTests(unittest.TestCase):
    def test_original_greeting(self):
        self.assertEqual(make_greeting(), "HELLO, FROM PERSON3!")
    def test_script_output(self):
        result = subprocess.run(
            [sys.executable, "script1.py"],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout.strip(), "HELLO, FROM PERSON3!")

if __name__ == "__main__":
    unittest.main()