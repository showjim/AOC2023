def sum_part_numbers(schematic):
    # Define the symbols that count (excluding the period)
    symbols = set('*#$+')

    # Convert the schematic into a list of lists (2D array)
    schematic_lines = schematic.strip().split('\n')
    schematic_array = [list(line) for line in schematic_lines]

    # Find the dimensions of the schematic
    rows = len(schematic_array)
    cols = len(schematic_array[0]) if rows else 0

    # Function to check if a position is within the bounds of the schematic
    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # Function to find all adjacent numbers to a symbol
    def find_adjacent_numbers(x, y):
        adjacent_numbers = set()
        # Check all adjacent positions including diagonals
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Skip the symbol itself
                nx, ny = x + dx, y + dy
                if in_bounds(nx, ny) and schematic_array[nx][ny].isdigit():
                    # If the adjacent position is a digit, add it to the set
                    number = schematic_array[nx][ny]
                    # Expand to capture multi-digit numbers
                    # Check left and right for multi-digit numbers
                    left, right = ny, ny
                    while left - 1 >= 0 and schematic_array[nx][left - 1].isdigit():
                        left -= 1
                    while right + 1 < cols and schematic_array[nx][right + 1].isdigit():
                        right += 1
                    number = ''.join(schematic_array[nx][left:right + 1])
                    adjacent_numbers.add(int(number))
        return adjacent_numbers

    # Set to store all unique part numbers
    part_numbers = set()

    # Iterate over the schematic to find symbols and their adjacent numbers
    for x in range(rows):
        for y in range(cols):
            if schematic_array[x][y] in symbols:
                part_numbers.update(find_adjacent_numbers(x, y))

    # Return the sum of all unique part numbers
    return sum(part_numbers)

# Example input
schematic = """
467..11456
...*...*..
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

# Calculate the sum of part numbers
sum_of_parts = sum_part_numbers(schematic)
print(f"The sum of the part numbers is: {sum_of_parts}")