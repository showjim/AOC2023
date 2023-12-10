"""To optimize the code for handling large datasets, we can make the following changes:

Avoid Unnecessary List Conversions: Use generators to avoid converting the entire mapping into a list, which can be memory-intensive.

Optimize Translation Logic: Instead of iterating through all mappings for each seed, we can break early if a match is found.

Reduce Function Calls: Minimize the number of function calls within tight loops.

Optimize Seed Generation: Use a generator expression to create seeds instead of a list.

Here is the optimized code:"""

def parse_map(mapping_lines):
    for line in mapping_lines:
        parts = line.split()
        yield int(parts[1]), int(parts[1]) + int(parts[2]), int(parts[0])

def translate(number, mapping_gen):
    for source_start, source_end, destination_start in mapping_gen:
        if source_start <= number < source_end:
            return destination_start + (number - source_start)
    return number

def full_translation(seed, maps):
    for map_gen in maps:
        seed = translate(seed, map_gen)
    return seed

def process_input(input_data):
    sections = input_data.strip().split('\n\n')
    seeds_section = sections[0]
    seeds_range = map(int, seeds_section.replace('seeds:', '').strip().split())

    # Use a generator expression for seeds
    seeds = (i for start, length in zip(seeds_range, seeds_range) for i in range(start, start + length))

    # Create a generator of generators for the maps
    maps = (parse_map(section.split('\n')[1:]) for section in sections[1:])

    return seeds, maps

def find_lowest_location_number(input_data):
    seeds, maps = process_input(input_data)

    # Initialize the lowest location with a high number
    lowest_location = float('inf')
    for seed in seeds:
        final_location = full_translation(seed, maps)
        if final_location < lowest_location:
            lowest_location = final_location

    return lowest_location

# Input data string (truncated for brevity)
input_data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

# Run the code to find the lowest location number
lowest_location_number = find_lowest_location_number(input_data)
print("The lowest location number is:", lowest_location_number)