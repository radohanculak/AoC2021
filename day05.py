import time
import re
from typing import Iterator


Coords = tuple[int, int, int, int]


class FloorMap():
    def __init__(self) -> None:
        self.diagram = [[0 for _ in range(1000)] for _ in range(1000)]

    def mark_positions(self, data: list[Coords]) -> None:
        for elem in data:
            for x, y in coords_to_mark(elem):
                self.diagram[y][x] += 1

    def unsafe_points(self) -> int:
        return sum([1 for row in self.diagram for col in row if col > 1])
        # return sum([len([col for col in row if col > 1]) for row in self.diagram])
        # return sum(map(lambda r: len(list(filter(lambda x: x > 1, r))), self.diagram))


def coords_to_mark(coords: Coords) -> Iterator[tuple[int, int]]:
    x1, y1, x2, y2 = coords

    if x1 < x2:
        horizontal = [i for i in range(x1, x2 + 1)]
    else:
        horizontal = [i for i in range(x1, x2 - 1, -1)]

    if y1 < y2:
        vertical = [i for i in range(y1, y2 + 1)]
    else:
        vertical = [i for i in range(y1, y2 - 1, -1)]

    if len(horizontal) < len(vertical):
        horizontal.extend([horizontal[0]] * (len(vertical) - len(horizontal)))
    else:
        vertical.extend([vertical[0]] * (len(horizontal) - len(vertical)))

    yield from zip(horizontal, vertical)


def get_coords(line: str) -> Coords:
    res = re.match('^([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)$', line)
    if not res:
        raise ValueError
    return tuple(map(int, res.groups()))


def task1(data: list[Coords]) -> int:
    # remove diagonals
    data = list(filter(lambda x: x[0] == x[2] or x[1] == x[3], data))
    floor_map = FloorMap()
    floor_map.mark_positions(data)

    return floor_map.unsafe_points()


def task2(data: list[Coords]) -> int:
    floor_map = FloorMap()
    floor_map.mark_positions(data)

    return floor_map.unsafe_points()


def main() -> None:
    with open('./data/day05.txt') as f:
        data = list(map(get_coords, f.read().split('\n')))

    t = time.process_time()

    print(f'Result of the 1st subtask: {task1(data)}')
    print(f'Result of the 2nd subtask: {task2(data)}')

    elapsed_time = time.process_time() - t
    print(f'time: {elapsed_time}')


if __name__ == '__main__':
    main()
