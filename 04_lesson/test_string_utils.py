import pytest
from string_utils import StringUtils


class TestStringUtils:

    def test_capitalize_positive(self):
        utils = StringUtils()
        assert utils.capitalize("skypro") == "Skypro"
        assert utils.capitalize("hello world") == "Hello world"
        assert utils.capitalize("a") == "A"
        assert utils.capitalize("python") == "Python"

    def test_capitalize_negative(self):
        utils = StringUtils()
        assert utils.capitalize("") == ""
        assert utils.capitalize(" ") == " "
        assert utils.capitalize("123") == "123"
        assert utils.capitalize("sKyPro") == "Skypro"

    def test_trim_positive(self):
        utils = StringUtils()
        assert utils.trim("   skypro") == "skypro"
        assert utils.trim("  hello  ") == "hello  "
        assert utils.trim(" \t\nhello") == "hello"

    def test_trim_negative(self):
        utils = StringUtils()
        assert utils.trim("") == ""
        assert utils.trim("skypro") == "skypro"
        assert utils.trim("skypro   ") == "skypro   "

    def test_contains_positive(self):
        utils = StringUtils()
        assert utils.contains("SkyPro", "S") == True
        assert utils.contains("SkyPro", "y") == True
        assert utils.contains("Hello World", " ") == True

    def test_contains_negative(self):
        utils = StringUtils()
        assert utils.contains("SkyPro", "U") == False
        assert utils.contains("", "S") == False
        assert utils.contains("SkyPro", "") == False
        assert utils.contains(" ", "S") == False

    def test_delete_symbol_positive(self):
        utils = StringUtils()
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
        assert utils.delete_symbol("Hello World", " ") == "HelloWorld"

    def test_delete_symbol_negative(self):
        utils = StringUtils()
        assert utils.delete_symbol("SkyPro", "X") == "SkyPro"
        assert utils.delete_symbol("", "S") == ""
        assert utils.delete_symbol("SkyPro", "") == "SkyPro"