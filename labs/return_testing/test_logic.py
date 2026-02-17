import unittest
from logic import keep_nonempty

class TestStringMethods(unittest.TestCase):
    def test_split(self):
      inputList = [" Egy ", "kettő", " Három", ""]

      cleaned, stats = keep_nonempty(inputList)
      expected_clean = (['Egy', 'kettő', 'Három'])
      expected_before = 4
      expected_after = 3
      self.assertEqual(cleaned, expected_clean)
      self.assertEqual(stats["before"], expected_before)
      self.assertEqual(stats["after"], expected_after)

if __name__ == '__main__':
    unittest.main()

