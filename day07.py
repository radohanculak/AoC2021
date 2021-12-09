from statistics import median, mean
import time


def task1(data: list[int]) -> int:
    med = median(data)
    res = sum([abs(i - med) for i in data])
    return res


def sequence_sum(first: int, last: int) -> int:
    return sum(range(first, last + 1))


def task2(data: list[int]) -> int:

    airthmetic_mean = int(mean(data))
    print(airthmetic_mean)
    res = sum([sequence_sum(0, abs(i - airthmetic_mean)) for i in data])
    return res


def main() -> None:
    with open('./data/day07.txt') as f:
        data = [int(i) for i in f.read().split(',')]

    t = time.process_time()

    print(f'Result of the 1st subtask: {task1(data)}')
    print(f'Result of the 2nd subtask: {task2(data)}')

    elapsed_time = time.process_time() - t
    print(f'time: {elapsed_time}')


if __name__ == '__main__':
    main()
