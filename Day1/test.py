import re

def match_number_word_from_right(string):
    # Regular expression with words ordered by length
    pattern = re.compile(r'(eight|seven|three|four|five|nine|six|one|two)')

    # Dictionary to convert words to numbers
    word_to_number = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    # Find all matches in the string
    matches = list(pattern.finditer(string))
    if matches:
        # If matches are found, return the number corresponding to the last match
        return word_to_number[matches[-1].group()]
    else:
        # If no matches are found, return None
        return None

# Test the function
test_string = "oneight"
matched_number = match_number_word_from_right(test_string)
print(f"Matched number from right: {matched_number}")