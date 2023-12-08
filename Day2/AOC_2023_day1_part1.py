import re

def parse_game_data(game_data):
    # This pattern matches the game ID and the counts of each color of cubes
    pattern = re.compile(r'Game (\d+):((?: \d+ (?:red|green|blue),?)+);?')

    # Dictionary to hold the game data
    games = {}

    # Find all matches for games
    for match in pattern.finditer(game_data):
        game_id = int(match.group(1))
        cubes = match.group(2).split(';')

        # Parse each subset of cubes
        subsets = []
        for subset in cubes:
            # Count the cubes of each color
            counts = {'red': 0, 'green': 0, 'blue': 0}
            for color in ['red', 'green', 'blue']:
                color_pattern = re.compile(r'(\d+) ' + color)
                color_match = color_pattern.search(subset)
                if color_match:
                    counts[color] = int(color_match.group(1))
            subsets.append(counts)

        games[game_id] = subsets

    return games

def check_games(games, red_cubes, green_cubes, blue_cubes):
    possible_games = []

    # Check each game
    for game_id, subsets in games.items():
        possible = True
        # Check each subset of cubes
        for subset in subsets:
            if (subset['red'] > red_cubes or
                subset['green'] > green_cubes or
                subset['blue'] > blue_cubes):
                possible = False
                break
        if possible:
            possible_games.append(game_id)

    return possible_games

# Example input
game_data = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

# Parse the game data
games = parse_game_data(game_data)

# Check which games are possible
possible_games = check_games(games, 12, 13, 14)

# Calculate the sum of the IDs of the possible games
sum_of_ids = sum(possible_games)

print(f"The possible games are: {possible_games}")
print(f"The sum of the IDs of the possible games is: {sum_of_ids}")