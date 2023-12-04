def sum_calibration_values(input_document):
    total_sum = 0
    for line in input_document:
        digits = [char for char in line if char.isdigit()]
        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]
            calibration_value = int(first_digit + last_digit)
            total_sum += calibration_value
    return total_sum


# Example usage
input_document = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
input_document = open("AOC2023/aoc01/input.txt").readlines()

result = sum_calibration_values(input_document)
print("Sum of calibration values:", result)
