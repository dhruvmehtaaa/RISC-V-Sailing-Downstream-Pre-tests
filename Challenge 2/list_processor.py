def process_list(input_list):
    if not all(isinstance(num, int) for num in input_list):
        print("Error: The input list must contain only integers.")
        return None

    if len(input_list) % 10 != 0:
        print("Error: The length of the list must be a multiple of 10.")
        return None

    modified_list = [num for i, num in enumerate(input_list, start=1) if i % 2 != 0 and i % 3 != 0]
    return modified_list

if __name__ == "__main__":
    try:
        numbers = [int(num) if isinstance(num, (int, str)) and num.isdigit() else num for num in input("Enter a list of integers separated by spaces: ").split()]
        result = process_list(numbers)

        if result is not None:
            print("Original List:", numbers)
            print("Modified List:", result)
    except ValueError:
        print("Invalid input. Please enter a valid list of integers.")
