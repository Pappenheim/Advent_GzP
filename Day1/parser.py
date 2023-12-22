import re

def replace_spelled_numbers_with_digits_using_regex(input_file_path, output_file_path):
    # Regex pattern to match digits and spelled-out numbers
    pattern = re.compile(r'\b(one|two|three|four|five|six|seven|eight|nine|\d)\b')

    number_words = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    try:
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            for line in input_file:
                matches = pattern.finditer(line)

                # Two pointers: one from the start and one from the end
                left, right = 0, len(line) - 1
                for match in matches:
                    start, end = match.span()
                    digit = match.group()
                    if start <= left:
                        # Replace spelled-out digit at the beginning
                        line = line[:start] + number_words.get(digit, digit) + line[end:]
                        left = end
                    elif start >= right:
                        # Replace spelled-out digit at the end
                        line = line[:start] + number_words.get(digit, digit) + line[end:]
                        right = start
                        break  # No need to check further

                output_file.write(line)
        return f"File processed successfully. Output written to {output_file_path}"
    except Exception as e:
        return f"Error while processing the file: {str(e)}"

# Paths for the input and output files
input_file_path = 'input.txt'  # Replace with the actual path to your input file
output_file_path = 'output.txt'  # Replace with the desired path for your output file

# Run the function and output the result
result = replace_spelled_numbers_with_digits_using_regex(input_file_path, output_file_path)
print(result)
