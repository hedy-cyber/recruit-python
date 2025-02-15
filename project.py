import sys


class Calculation:
    """ A class to perform calculations on the values from the files provided as the arguments.

    This class reads data from multiple files, performs basic calculations like count, sum, maximum, and average on the data, and prints the results.

    Attributes:
        file_list (list of string): A list of file names that the class will process.
    """

    def __init__(self, file_list):
        """ Initialize the Calculation object with a list of file names.

        Args:
            file_list (list of str): List of file names to be processed.
        """
        # Store the list of file names which got passed as an argument.
        self.file_list = file_list

    def read_file(self, file_list):
        """ Reads numbers from a file and returns them as a list of floats.

        This method reads each line of the file. It will convert the values into a float, and appends valid values to the list. If a non-numeric value is found, an error message is printed, and the program exits.

        Args:
            file_list (string): The name of the file from which numbers are to be read.

        Returns:
            numbers (list of float): A list of numbers extracted from the file.

        Raises:
            FileNotFoundError: If the file is not found.
            ValueError: If a line cannot be converted to a float. If the value is non-numeric.
        """
        # Create an empty list to store the numbers read from the file
        numbers = []
        try:
            # Open the file to read
            with open(file_list, 'r') as file:
                # Read each line in the file
                for line in file:
                    # Remove any whitespace from the line is any present
                    line = line.strip()
                    # If the line is not empty, then only process
                    if line:
                        try:
                            # Extarct the value of the line as Float
                            store_value = float(line)
                            # Append the valid number to the list
                            numbers.append(store_value)
                        except ValueError:
                            # Print an error if the value is non-numeric
                            print(f"This is an inappropriate value: '{line}'")
                            # Exit the program with an error code 1
                            sys.exit(1)

        except FileNotFoundError:
            # Print an error message if the file is not found
            print(f"This file is not present: {file_list}")
        # Returns the list of numbers present in the file
        return numbers

    def calculate_values(self, numbers):
        """ Calculates basic statistics for the given list of numbers.

        This method calculates the count, sum, maximum, and average of the numbers in the list.

        Args:
            numbers (list of float): The list of numbers to be analyzed.

        Returns:
            dict: A dictionary with the calculated values (count, sum, max, avg).
        """
        # If the list is empty, then return None
        if not numbers:
            return None

        # Count the number of elements in the list
        count = len(numbers)
        # Calculate the sum of elements in the list
        total = sum(numbers)
        # Calculate the maximum number in the list
        maximum = max(numbers)
        # Calculate the average of elements in the list
        average = total / count
        # Return a dictionary with the calculated values in it
        return {
            "count": count,
            "sum": total,
            "max": maximum,
            "avg": average
        }

    def print_values(self):
        """ Processes each file, calculates values, and prints the results.

        This method iterates over each file in the list of file names, calls the required methods to read the data, calculate the statistics, and then prints the results for each file.

        Side effects:
            Writes to stdout: Prints the results of calculations.
        """
        # Iterate through each file name in the list
        for filename in self.file_list:
            # Read the numbers from the file
            numbers = self.read_file(filename)
            # Calculate the statistics for the numbers
            cal_values = self.calculate_values(numbers)
            # If no valid numbers were found, then the default values will be 0
            if cal_values is None:
                cal_values = {"count": 0, "sum": 0, "max": 0, "avg": 0}

            # Print the result as the file name and the calculated values
            print(
                f"{filename} {cal_values['count']} {cal_values['sum']} {cal_values['max']} {cal_values['avg']}")


def main():
    """ Main function to process the command-line arguments and initiate the calculations.

    This function checks for the presence of file arguments passed via the command line, creates a Calculation object, and then prints the calculated values for each file.

    Side effects:
        Writes to stdout: Prints error messages or calculation results.
    """
    # If there are less than 2 arguments then it will give error because there is no argumrnt provided as the script name is the first argument
    if len(sys.argv) < 2:
        # Print an error message if no file is provided in the argument
        print(f"Code Error: No file argument given")
        # Exit the program with the error code 1
        sys.exit(1)

    # Get all the arguments from the command line except for the script name
    arguments = sys.argv[1:]

    # Calculation object with the provided file names and print the results
    Calculation(file_list=arguments).print_values()


if __name__ == "__main__":
    main()
