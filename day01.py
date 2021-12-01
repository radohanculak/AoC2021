
def task1(depths: list[int]) -> int:
    counter = 0

    for i in range(1, len(depths)):
        if depths[i] > depths[i-1]:
            counter += 1

    return counter


def task2(depths: list[int]) -> int:
    counter = 0

    for i in range(2, len(depths) - 1):
        current_window = sum(depths[i-1:i+2])
        previous_window = sum(depths[i-2:i+1])

        if current_window > previous_window:
            counter += 1

    return counter


def main() -> None:
    with open('./data/day01.txt') as f:
        data = list(map(int, f.read().split()))

    print(f'Result of the 1st subtask: {task1(data)}.')
    print(f'Result of the 2nd subtask: {task2(data)}.')


if __name__ == '__main__':
    main()
