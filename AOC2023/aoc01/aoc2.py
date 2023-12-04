def sum_calibration_values_with_text(input_document):
    digit_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    total_sum = 0
    for line in input_document:
        line = line.strip()
        left_num = None
        right_num = None
        idx = 0
        while idx < len(line):
            skip_size = 1
            if line[idx].isdigit():
                if left_num is None:
                    left_num = line[idx]
                right_num = line[idx]
            else:
                for text_digit, num_digit in digit_map.items():
                    if line[idx:].startswith(text_digit):
                        if left_num is None:
                            left_num = num_digit
                        right_num = num_digit
                        skip_size = len(text_digit) - 1
            idx += skip_size
        print(f"{line=}")
        print(f"{left_num=} {right_num=}")
        calibration_value = int(left_num + right_num)
        total_sum += calibration_value

    return total_sum


# Example usage
input_document = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]
input_document = open("AOC2023/aoc01/input.txt").readlines()
result = sum_calibration_values_with_text(input_document)
print("Sum of calibration values:", result)
