def calculate_sum_with_corrected_digit_handling(file_path):
    # Mapping of spelled-out numbers to digits
    number_words = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    total_sum = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace

                # Process the first character of the line
                first_digit = line[0] if line[0].isdigit() else None
                for word, digit in number_words.items():
                    if line.startswith(word):
                        first_digit = digit
                        break

                # Process the last character of the line
                last_digit = line[-1] if line[-1].isdigit() else None
                for word, digit in number_words.items():
                    if line.endswith(word):
                        last_digit = digit
                        break

                # Combine the first and last digits to form a two-digit number
                if first_digit and last_digit:
                    calibration_value = int(first_digit + last_digit)
                    total_sum += calibration_value
    except Exception as e:
        return f"Error while processing the file: {str(e)}"
    return total_sum

# Use the function with the path to your file
file_path = 'input.txt'  # Replace with the actual path to your file
result = calculate_sum_with_corrected_digit_handling(file_path)
print("Sum of calibration values:", result)
