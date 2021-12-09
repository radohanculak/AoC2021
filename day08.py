import time


def count_unique(data: str) -> int:
    print(data)
    return len([i for i in data.split(' ') if len(i) in {2, 3, 4, 7}])


def task1(data: list[str]) -> int:
    s = sum([count_unique(second) for _, second in data])
    return s


def main() -> None:
    with open('./data/day08.txt') as f:
        data = [i.split('|') for i in f.read().split('\n')]

    print(data[0])

    t = time.process_time()

    print(f'Result of the 1st subtask: {task1(data)}')
    # print(f'Result of the 2nd subtask: {task2(data)}')

    elapsed_time = time.process_time() - t
    print(f'time: {elapsed_time}')


if __name__ == '__main__':
    main()
