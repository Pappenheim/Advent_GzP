def analyze_games(file_path):
    possible_game_ids = []

    # Limits for each cube color
    limits = {'red': 12, 'green': 13, 'blue': 14}

    with open(file_path, 'r') as file:
        for line in file:
            # Split the line to extract the game ID and the subsets
            parts = line.split(':')
            game_id = int(parts[0].split()[1])  # Extract the game ID
            subsets = parts[1].split(';')

            # Flag to check if the game is possible
            is_possible = True

            for subset in subsets:
                # Parse the number of cubes of each color in this subset
                counts = {'red': 0, 'green': 0, 'blue': 0}
                for color in counts.keys():
                    if color in subset:
                        # Find the number preceding the color word
                        words = subset.strip().split(',')
                        for word in words:
                            if color in word:
                                count = int(word.split()[0])  # Extract the number of cubes for this color
                                counts[color] = count
                                break

                # Check if the counts exceed the limits
                for color, count in counts.items():
                    if count > limits[color]:
                        is_possible = False
                        break

                if not is_possible:
                    break

            if is_possible:
                possible_game_ids.append(game_id)

    # Return the sum of the IDs of possible games
    return sum(possible_game_ids)

# Use the function with the path to your file
file_path = 'input.txt'
result = analyze_games(file_path)
print("Sum of the IDs of possible games:", result)
