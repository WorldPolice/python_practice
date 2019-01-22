# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
from python_practice.strings_part_two import *


class TestCommaSeparatedStrings(object):

    def test_three_strings(self):
        assert 'foobarbaz' == concat_list_of_strings(['foo', 'bar', 'baz'])

    def test_one_string(self):
        assert 'hello' == concat_list_of_strings(['hello'])

    def test_empty_list(self):
        assert '' == concat_list_of_strings([])

    def test_non_string_type(self):
        assert concat_list_of_strings(['hello', {'oops': 'bad'}]) == ''


class TestSearchForSubstringsInList(object):

    def test_all_strings_remove_one(self):
        sub = 'hello'
        stuff = ['hello world', 'hello darkness my old friend', 'hi']
        assert ['hello world', 'hello darkness my old friend'] == search_for_substrings_in_list(sub, stuff)

    def test_empty_list(self):
        sub = 'hello'
        stuff = []
        assert [] == search_for_substrings_in_list(sub, stuff)

    def test_some_strings_some_not(self):
        sub = 'hello'
        stuff = ['hello world', {'hello': 'world'}, 'hello darkness my old friend']
        assert ['hello world', 'hello darkness my old friend'] == search_for_substrings_in_list(sub, stuff)

    def test_all_strings_remove_none(self):
        sub = 'hello'
        stuff = ['hello world', 'hello darkness my old friend', 'hello']
        assert ['hello world', 'hello darkness my old friend', 'hello'] == search_for_substrings_in_list(sub, stuff)


class TestIsPalindrome(object):

    def test_palindrome_one(self):
        """Even palindrome with mixed case"""
        assert is_palindrome('A Santa dog lived as a devil God at NASA.') is True

    def test_palindrome_two(self):
        """Even palindrome"""
        assert is_palindrome('A nut for a jar of tuna.') is True

    def test_palindrome_three(self):
        """Punctuation in the middle of the string"""
        assert is_palindrome('A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!') is True

    def test_not_a_palindrome(self):
        """Not a palindrome"""
        assert is_palindrome('This is not a palindrome') is False

    def test_not_a_palindrome_two(self):
        """Substring is palindrome"""
        assert is_palindrome('A nut for a jar of tunas.') is False


class TestRemoveTrailingWhitespaceCharacters(object):

    def test_trailing_witespace_one(self):
        test_string = '"Rah, rah, ah, ah, ah, roma, roma, ma. Gaga, ooh, la, la...      '
        expected_string = "Rah, rah, ah, ah, ah, roma, roma, ma. Gaga, ooh, la, la..."
        assert expected_string == remove_trailing_whitespace_characters(test_string)

    def test_trailing_witespace_two(self):
        test_string = "Sun-kissed skin, so hot, we'll melt your popsicle!\n\n\n"
        expected_string = "Sun-kissed skin, so hot, we'll melt your popsicle!"
        assert expected_string == remove_trailing_whitespace_characters(test_string)

    def test_trailing_witespace_four(self):
        test_string = "There's vomit on his sweater already, mom's spaghetti!\t\t\t"
        expected_string = "There's vomit on his sweater already, mom's spaghetti!"
        assert expected_string == remove_trailing_whitespace_characters(test_string)

    def test_trailing_witespace_four(self):
        test_string = "My milkshake brings all the boys to the yard\r\r\r"
        expected_string = "My milkshake brings all the boys to the yard"
        assert expected_string == remove_trailing_whitespace_characters(test_string)


class TestReplaceWithYourName(object):

    def test_madlib(self):
        madlib = """
        <name> is killing it at Python.  I mean can you
        believe how awesome <name> is!?!  <name> is
        destined for programming greatness.
        """
        expected = """
        Bob is killing it at Python.  I mean can you
        believe how awesome Bob is!?!  Bob is
        destined for programming greatness.
        """
        assert expected == remove_trailing_whitespace_characters('Bob', madlib)

    def test_nothing_to_do(self):
        expected = """
        Jim is killing it at Python.  I mean can you
        believe how awesome Jim is!?!  Jim is
        destined for programming greatness.
        """
        assert expected == remove_trailing_whitespace_characters('Bob', expected)

