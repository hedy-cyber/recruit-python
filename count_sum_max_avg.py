'''
README

HOW TO RUN
    - python3 count_sum_max_avg.py

EXAMPLE INPUT(s)
    1. q
    2. Q
    3. examples/basic.txt
    4. examples/basic.txt examples/single.txt
'''

def main():
    menu_input = menu()
    while(menu_input != 'q' and menu_input != 'Q'):
        files = menu_input.strip().split()

        for file in files:
            if not menu_input.strip():
                # catch empty inputs or inputs with only whitespace
                print("[ERROR] No empty inputs allowed")
                break
            read_file(file)

        menu_input = menu()
    print("Exited.")

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            print(f'[LOG] Reading {file_path}')
            file_lines = file.readlines()

            # calculating count, sum, max, avg
            print(f'\tCount: {calc_count(file_lines)}')
            file_lines_int = [int(num) for num in file_lines]
            print(f'\tSum: {calc_sum(file_lines_int)}')
            print(f'\tMax: {calc_max(file_lines_int)}')
            print(f'\tAverage: {calc_avg(file_lines_int)}')
            return file_lines_int
    except FileNotFoundError:
        print(f"[ERROR] {file_path} not found...")

def calc_avg(file_lines_int):
    if (calc_count(file_lines_int) == 0):
        return "N/A"
    return calc_sum(file_lines_int) / calc_count(file_lines_int)

def calc_max(file_lines_int):
    if (calc_count(file_lines_int) == 0):
        return "N/A"
    return max(file_lines_int)

def calc_sum(file_lines_int):
    if (calc_count(file_lines_int) == 0):
        return "N/A"
    return sum(file_lines_int)

def calc_count(file_lines):
    if len(file_lines) == 0:
        return 0
    return len(file_lines)

def menu():
    print("\nCalculate the count, sum, max, and average of contents in file(s)")
    print("Options:")
    print("\tEnter Q or q to quit program.")
    print(f"\tEnter a file(s): ")
    file_inputs = input("Enter file(s) or quit: ")
    print()
    return file_inputs

if __name__ == "__main__":
    main()
