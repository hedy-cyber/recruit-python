# Python Coding Excercise

## Phase 1

Write a python script that takes one or more filenames as command line arguments.
Read each file as a sequence of numbers, one per line. For each file,
calculate the count, sum, max, and average for all values in the file. Print
the filename along with the results to standard output. Some example files are
provided.

## Phase 2

Create a pytest suite that can be used to test your script with the
input files provided.

#### Overview of the `project.py` script

---

This script reads the numbers from the files provided as the command line argument, and calculate total count of numbers, their sum, the highest number, and the average. It prints the results for each file in the argument.

The script has a Calculation class, which includes three key methods:

- `read_file`: This method opens a file, read the content, and extract the numeric values of a file.
- `calculate_values`: It takes the numeric values from `read_file` and perform the calculations.
- `print_values`: This method uses both the `read_file` and `calculate_values` methods for each file in order to print the results.

In order to run the script, I have assumed that the files to be passed as arguments will be in the same directory as the `project.py` script.

example: `python project.py test.txt`

#### Overview of the `project_test.py` script

---

This script includes test cases using pytest to verify the example files provided as input and to check if the error messages function correctly.

For future work, I would like to modify the output so that file names are displayed without the .txt extension for a better result.
