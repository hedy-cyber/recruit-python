import pytest
from project import Calculation


@pytest.fixture
def calculation_instance():
    """ Fixture for creating an instance of the Calculation class for testing.
    Returns
        Calculation: An instance of the Calculation class.
    """
    return Calculation()


def test_basic_file(capsys):
    """ Test case for the basic file input. """
    # Call the file name in the examples folder
    calc = Calculation(["examples/basic.txt"])
    # Called print_values method to calculate and print values
    calc.print_values()
    # Capture the output
    captured = capsys.readouterr()
    # Check if the expected output is correct in the captured output for basic.txt
    assert "basic.txt 4 33.0 20.0 8.25" in captured.out


def test_mixed_file(capsys):
    """ Test case for the mixed file input. """
    # Call the file name in the examples folder
    calc = Calculation(["examples/mixed.txt"])
    # Called print_values method to calculate and print values
    calc.print_values()
    # Capture the output
    captured = capsys.readouterr()
    # Check if the expected output is correct in the captured output for mixed.txt
    assert "mixed.txt 5 0.0 2.0 0.0" in captured.out


def test_negative_file(capsys):
    """ Test case for the negative file input. """
    # Call the file name in the examples folder
    calc = Calculation(["examples/negative.txt"])
    # Called print_values method to calculate and print values
    calc.print_values()
    # Capture the output
    captured = capsys.readouterr()
    # Check if the expected output is correct in the captured output for negative.txt
    assert "negative.txt 5 -15.0 -1.0 -3.0" in captured.out


def test_single_file(capsys):
    """ Test case for the single file input. """
    # Call the file name in the examples folder
    calc = Calculation(["examples/single.txt"])
    # Called print_values method to calculate and print values
    calc.print_values()
    # Capture the output
    captured = capsys.readouterr()
    # Check if the expected output is correct in the captured output for single.txt
    assert "single.txt 1 42.0 42.0 42.0" in captured.out


def test_file_not_found(capsys):
    """ Test case for a file which does not exist. """
    # This file is not present in the folder
    calc = Calculation(["NotFound.txt"])
    # Called print_values method to calculate and print values
    calc.print_values()
    # Capture the output
    captured = capsys.readouterr()
    # Check if expected output is an Error message which says file is not found
    assert "This file is not present: NotFound.txt" in captured.out


def test_multiple_files(capsys):
    """ Test case for multiple files as the argument. """
    # list of the files to be passed through the Calculation object
    calc = Calculation([
        "examples/basic.txt",
        "examples/mixed.txt",
        "examples/negative.txt",
        "examples/single.txt"])

    # Called print_values method to calculate and print values
    calc.print_values()
    # Capture the output
    captured = capsys.readouterr()
    # Check if the expected output is correct in the captured output for all the files
    assert "basic.txt 4 33.0 20.0 8.25" in captured.out
    assert "mixed.txt 5 0.0 2.0 0.0" in captured.out
    assert "negative.txt 5 -15.0 -1.0 -3.0" in captured.out
    assert "single.txt 1 42.0 42.0 42.0" in captured.out
