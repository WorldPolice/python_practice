# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
from python_practice.looping import *


class TestLoopingChallengeOne(object):

    def test_prints(self, capfd):
        """Test that it prints"""
        looping_challenge_one()
        out, err = capfd.readouterr()
        assert out, 'No printing to stdout was observed'

    def test_prints_one_through_ten(self, capfd):
        """Test that it prints 1-10"""
        looping_challenge_one()
        out, err = capfd.readouterr()
        for number in range(1, 10):
            assert str(number) in out, "The number {} was not observed in stdout".format(str(number))

    def test_separate_lines(self, capfd):
        """Test that the output is on separate lines"""
        looping_challenge_one()
        out, err = capfd.readouterr()
        assert len(str(out).split('\n')) >= 10, 'Ten new lines where not observed in stdout'


class TestLoopingChallengeTwo(object):

    def test_every_other_color(self, capfd):
        """Test that every other color is printed to stdout"""
        looping_challenge_two()
        out, err = capfd.readouterr()
        o = str(out).rstrip()
        observed = str(o).split('\n')

        list_one = ['Indigo', 'Green', 'Orange']
        list_two = ['Violet', 'Blue', 'Yellow', 'Red']
        assert observed == list_one or observed == list_two, 'The printed colors did not match the expected output'


class TestLoopingChallengeThree(object):

    def test_numbers_separated_by_newline(self, capfd):
        """Tests that we print to stdout on separate lines"""
        looping_challenge_three()
        out, err = capfd.readouterr()
        o = str(out).rstrip()
        observed = str(o).split('\n')

        assert len(observed) >= 8, 'Nine new lines where not observed in stdout'

    def test_correct_number_order(self, capfd):
        """Test that the numbers appear in the correct order"""
        looping_challenge_three()
        out, err = capfd.readouterr()
        o = str(out).rstrip()
        observed = str(o).split('\n')

        expected = [1, 2, 3, 4, 4, 3, 2, 1]
        assert expected == [int(number) for number in observed]
