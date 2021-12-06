from collections import deque
import time


def task1(data: list[int], days: int = 80) -> int:

    # idx == age
    fish_list: list[int] = [0 for _ in range(9)]
    for i in data:
        fish_list[i] += 1

    fish_list = deque(fish_list)

    for _ in range(days):
        new_born_count = fish_list[0]

        fish_list.rotate(-1)
        fish_list[6] += new_born_count

    return sum(fish_list)


def main() -> None:
    with open('./data/day06.txt') as f:
        data = [int(i) for i in f.read().split(',')]

    t = time.process_time()

    print(f'Result of the 1st subtask: {task1(data, 80)}')
    print(f'Result of the 2nd subtask: {task1(data, 256)}')

    elapsed_time = time.process_time() - t
    print(f'time: {elapsed_time}')


if __name__ == '__main__':
    main()
