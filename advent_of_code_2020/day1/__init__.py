from pathlib import Path

with (Path(".") / "input.txt").open() as numbers_file:
    numbers = [int(num.strip()) for num in numbers_file.readlines()]

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if i == j:
                continue
            if numbers[i] + numbers[j] == 2020:
                print(numbers[i] * numbers[j])
