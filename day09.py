import time
from typing import Iterator
from functools import reduce
import operator


# def lowpoints(data: list[str]) -> Iterator[int]:  # for task1
def lowpoints(data: list[str]) -> Iterator[tuple[int, int, int]]:  # for task2
    max_height, max_width = len(data) - 1, len(data[0]) - 1
    for i, row in enumerate(data):
        for j, elem in enumerate(row):
            # compare w/left
            if j > 0 and int(elem) >= int(row[j-1]):
                continue
            # compare w/right
            if j < max_width and int(elem) >= int(row[j+1]):
                continue
            # compare w/up
            if i > 0 and int(elem) >= int(data[i-1][j]):
                continue
            # compare w/down
            if i < max_height and int(elem) >= int(data[i+1][j]):
                continue

            # # task1
            # yield int(elem) + 1

            # task2
            yield int(elem), i, j


def task1(data: list[str]) -> int:
    return sum(lowpoints(data))


def basins(data: list[str], row: int, col: int, previous: int,
           visited: set[tuple[int, int]],
           counter: int = 0) -> int:
    if row >= len(data) or col >= len(data[0]):
        return 0

    if col < 0 or row < 0:
        return 0

    assert row < len(data)
    assert col < len(data[0])

    current = int(data[row][col])
    if current == 9 or current <= previous:
        return 0

    if (row, col) in visited:
        return 0
    visited.add((row, col))

    return sum([
        1,
        basins(data, row, col+1, current, visited, counter+1),
        basins(data, row+1, col, current, visited, counter+1),
        basins(data, row, col-1, current, visited, counter+1),
        basins(data, row-1, col, current, visited, counter+1),
    ])


def task2(data: list[str]) -> int:
    basin_list = []
    for num, row, col in lowpoints(data):
        basin_list.append(basins(data, row, col, num - 1, set([])))

    three_largest = sorted(list(basin_list))[-1:-4:-1]
    return reduce(operator.mul, three_largest, 1)


def main() -> None:
    # with open('./data/test.txt') as f:
    with open('./data/day09.txt') as f:
        data = [i for i in f.read().split('\n')]

    t = time.process_time()

    # print(f'Result of the 1st subtask: {task1(data)}')
    print(f'Result of the 2nd subtask: {task2(data)}')

    elapsed_time = time.process_time() - t
    print(f'time: {elapsed_time}')


if __name__ == '__main__':
    main()
