import sys
import unittest
from pathlib import Path

TOOL_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIR))

from text_cleaner import clean_text


class CleanTextTests(unittest.TestCase):
    def test_empty_text_stays_empty(self):
        self.assertEqual(clean_text(""), "")

    def test_normalizes_crlf_and_carriage_returns_to_line_feeds(self):
        self.assertEqual(clean_text("第一行\r\n第二行\r第三行\n第四行"), "第一行\n第二行\n第三行\n第四行")

    def test_replaces_each_tab_with_one_space(self):
        self.assertEqual(clean_text("A\tB\t\tC"), "A B  C")

    def test_converts_full_width_letters_numbers_spaces_and_punctuation(self):
        self.assertEqual(clean_text("ＡＢＣ　１２３，。！？（）"), "ABC 123,.!?()")

    def test_converts_common_cjk_punctuation_to_ascii(self):
        self.assertEqual(clean_text("、【】《》“”‘’—…～"), ",[]<>\"\"''-...~")

    def test_preserves_letters_numbers_marks_and_punctuation(self):
        self.assertEqual(clean_text("中文 English 123,.;:!? café"), "中文 English 123,.;:!? café")

    def test_removes_emoji_decorative_currency_and_math_symbols(self):
        self.assertEqual(clean_text("文本😀★◆￥€＋＝∑结束"), "文本+=结束")

    def test_removes_control_and_format_characters_except_line_feed(self):
        self.assertEqual(clean_text("A\x00B\u200bC\ufeffD\nE"), "ABCD\nE")

    def test_keeps_multiple_and_trailing_line_feeds(self):
        self.assertEqual(clean_text("A\r\n\r\nB\r"), "A\n\nB\n")


if __name__ == "__main__":
    unittest.main()
