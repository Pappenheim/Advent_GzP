def calculate_minimum_set_power(file_path):
    game_powers = []

    with open(file_path, 'r') as file:
        for line in file:
            subsets = line.split(':')[1].split(';')
            # Initialize minimum counts for each color
            min_counts = {'red': 0, 'green': 0, 'blue': 0}

            for subset in subsets:
                # Temporary counts for the current subset
                temp_counts = {'red': 0, 'green': 0, 'blue': 0}
                for color in min_counts.keys():
                    if color in subset:
                        # Find the number preceding the color word
                        words = subset.strip().split(',')
                        for word in words:
                            if color in word:
                                count = int(word.split()[0])  # Extract the number of cubes for this color
                                temp_counts[color] = count
                                break

                # Update the minimum counts if the current subset has more
                for color in min_counts.keys():
                    min_counts[color] = max(min_counts[color], temp_counts[color])

            # Calculate the power of the set of cubes for this game
            game_power = 1
            for count in min_counts.values():
                game_power *= count

            game_powers.append(game_power)

    # Return the sum of the powers of the minimum sets of cubes
    return sum(game_powers)

# Use the function with the path to your file
file_path = 'input.txt'  # Path to the input file
total_power = calculate_minimum_set_power(file_path)
print("Sum of the power of minimum sets of cubes:", total_power)
