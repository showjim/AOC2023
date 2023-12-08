import re

def sum_calibration_values(text_lines):
    total_sum = 0
    for line in text_lines:
        # Find all digits in the current line
        digits = re.findall(r'\d', line)
        if digits:
            # Combine the first and last digit to form a two-digit number
            calibration_value = int(digits[0] + digits[-1])
            total_sum += calibration_value
    return total_sum

# Example input
example_lines = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

# Calculate the sum of calibration values
sum_of_values = sum_calibration_values(example_lines)
print(sum_of_values)