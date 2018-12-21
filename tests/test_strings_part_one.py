# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
from python_practice.strings_part_one import *


class TestIsMyArgumentAString(object):

    def test_with_string(self):
        assert is_my_argument_a_string('hello world') is True

    def test_none(self):
        assert is_my_argument_a_string(None) is False

    def test_list(self):
        assert is_my_argument_a_string(['hello', 'world']) is False

    def test_empty_string(self):
        assert is_my_argument_a_string('') is True


class TestConcatonateMyArguments(object):

    def test_concatenation(self):
        observed = concatonate_my_arguments('supercali', 'fragilistic', 'expialidocious')
        assert 'supercalifragilisticexpialidocious' == observed

    def test_empty_strings(self):
        observed = concatonate_my_arguments('', '', '')
        assert '' == observed


class TestAllNumbers(object):

    def test_just_numbers(self):
        assert all_numbers('0123456789') is True

    def test_white_space(self):
        assert all_numbers('12345 67890') is False

    def test_newline_at_end(self):
        assert all_numbers("123456789\n") is False

    def test_word_characters(self):
        assert all_numbers('1two3four') is False


class TestSubstringTest(object):

    def test_legit_substring(self):
        assert substring_test('hello', 'hello world') is True

    def test_bad_substring(self):
        assert substring_test('hi', 'hello world') is False

    def test_case_sensitivity(self):
        assert substring_test('WORLD', 'hello world') is True

    def test_empty_string(self):
        assert substring_test('', 'hello world') is True

    def test_empty_string_two(self):
        assert substring_test('', '') is True
