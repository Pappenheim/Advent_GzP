def is_symbol(char):
    """Check if the character is a symbol (not a number or a period)."""
    return not char.isdigit() and char not in ['\n', '.'] #return char.isalpha() or char in ['*', '#', '+', '$']

def sum_part_numbers_corrected(grid):
    """Sum all part numbers in the engine schematic, considering whole numbers and adjacency to symbols."""
    sum_parts = 0
    rows, cols = len(grid), len(grid[0])

    # Helper function to check if a cell is adjacent to a symbol
    def is_adjacent_to_symbol(x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if 0 <= x + dx < rows and 0 <= y + dy < cols:
                    if is_symbol(grid[x + dx][y + dy]):
                        return True
        return False

    for x in range(rows):
        y = 0
        while y < cols:
            if grid[x][y].isdigit():
                # Extract the whole number
                start_y = y
                while y < cols and grid[x][y].isdigit():
                    y += 1
                number = int("".join(grid[x][start_y:y]))

                # Check if the number is adjacent to a symbol
                if any(is_adjacent_to_symbol(x, yy) for yy in range(start_y, y)):
                    sum_parts += number
            else:
                y += 1

    return sum_parts

# Read the file and create the grid
file_path = 'input.txt'
with open(file_path, 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

# Calculate the sum
sum_of_part_numbers_corrected = sum_part_numbers_corrected(grid)
print(sum_of_part_numbers_corrected)
