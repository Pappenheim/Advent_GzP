def calculate_sum_of_calibration_values(file_path):
    total_sum = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Find the first and last digit in each line
                digits = [char for char in line if char.isdigit()]
                if digits:
                    # Combine the first and last digits to form a two-digit number
                    calibration_value = int(digits[0] + digits[-1])
                    total_sum += calibration_value
    except Exception as e:
        return f"Error while processing the file: {str(e)}"
    return total_sum

# Use the function with the path to your file
file_path = 'output.txt'  # Replace with the actual path to your file
result = calculate_sum_of_calibration_values(file_path)
print("Sum of calibration values:", result)