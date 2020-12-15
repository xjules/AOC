numbers = [0, 12, 6, 13, 20, 1, 17]

turn = 0
spoken_numbers = {i: [] for i in numbers}
for id, value in enumerate(numbers):
    spoken_numbers[value].append(id + 1)

last_number = numbers[-1]
turn = len(numbers)
while True:
    turn += 1
    if last_number in spoken_numbers and len(spoken_numbers[last_number]) > 1:
        spoken_number = (
            spoken_numbers[last_number][-1] - spoken_numbers[last_number][-2]
        )
    else:
        spoken_number = 0
    if spoken_number in spoken_numbers:
        spoken_numbers[spoken_number].append(turn)
    else:
        spoken_numbers[spoken_number] = [turn]
    last_number = spoken_number
    if turn % 100000 == 0:
        print(f"turn={turn} spoken_number={spoken_number}")
    if turn == 30000000:
        print(f"part II spoken_number={spoken_number}")
        break
    if turn == 2020:
        print(f"part I spoken_number={spoken_number}")
