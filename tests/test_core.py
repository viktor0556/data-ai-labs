import unittest

from cleaner.core import cleaner

class TestCleanLines(unittest.TestCase):
  def test_split(self):
    outputLines = (" alma", "# ez komment", "  körte", "", "barack", 
                " # komment whitespace előtt", "szilva", "banán", "",
                " # még egy komment", " ananász", "mangó", "", "eper",
                "citrom", "#", "    #", "lime", "   narancs", "mandarin")
    
    cleaned, stats = cleaner(outputLines)
    cleaned_expected = ["alma", "körte", "barack", "szilva", 
                        "banán", "ananász", "mangó", "eper", 
                        "citrom", "lime", "narancs", "mandarin"]
    cleaned_before = 20
    cleaned_after = 12
    
    self.assertEqual(cleaned, cleaned_expected)
    self.assertEqual(stats["before"], cleaned_before)
    self.assertEqual(stats["after"], cleaned_after)
    
if __name__ == '__main__':
  unittest.main()