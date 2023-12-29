def sum_part_numbers(file_path):
    # Read the file and store the engine schematic in a 2D array
    with open(file_path, 'r') as file:
        schematic = [list(line.strip()) for line in file]

    # Directions to check for adjacent symbols (8 directions)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    rows, cols = len(schematic), len(schematic[0])
    part_sum = 0

    # Function to check if there's a symbol adjacent to the given position
    def has_adjacent_symbol(x, y, schematic):
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and schematic[nx][ny] not in ['.', ' ']:
                return True
        return False

    # Traverse the grid and sum the part numbers
    for i in range(rows):
        j = 0
        while j < cols:
            if schematic[i][j].isdigit():
                # Check if the number is adjacent to a symbol
                if not has_adjacent_symbol(i, j, schematic):
                    # Extracting complete numbers instead of individual digits
                    num_str = schematic[i][j]
                    k = j + 1
                    while k < cols and schematic[i][k].isdigit():
                        num_str += schematic[i][k]
                        k += 1
                    part_sum += int(num_str)
                    j = k  # Skip past the full number
                else:
                    j += 1
            else:
                j += 1

    return part_sum

# Path to the input file
file_path = 'test.txt'  # Replace with the actual path to your input file
total_part_sum = sum_part_numbers(file_path)
print("Sum of all part numbers:", total_part_sum)
