

def new_position(instruction: str, depth: int, horisontal_pos: int) \
        -> tuple[int, int]:
    if instruction.startswith('forward'):
        horisontal_pos += int(instruction.split()[-1])
    elif instruction.startswith('up'):
        depth -= int(instruction.split()[-1])
    elif instruction.startswith('down'):
        depth += int(instruction.split()[-1])

    return depth, horisontal_pos


def task1(instructions: list[str]) -> int:
    depth, horizontal_pos = 0, 0

    for elem in instructions:
        depth, horizontal_pos = new_position(elem, depth, horizontal_pos)

    return depth * horizontal_pos


def new_position_task2(instruction: str, depth: int, horisontal_pos: int,
                       aim: int) -> tuple[int, int, int]:
    if instruction.startswith('forward'):
        horisontal_pos += int(instruction.split()[-1])
        depth += aim * int(instruction.split()[-1])
    elif instruction.startswith('up'):
        aim -= int(instruction.split()[-1])
    elif instruction.startswith('down'):
        aim += int(instruction.split()[-1])

    return depth, horisontal_pos, aim


def task2(instructions: list[str]) -> int:
    depth, horizontal_pos, aim = 0, 0, 0

    for elem in instructions:
        depth, horizontal_pos, aim = new_position_task2(
            elem, depth, horizontal_pos, aim)

    return depth * horizontal_pos


def main() -> None:
    with open('./data/day02.txt') as f:
        data = f.read().split('\n')

    print(f'Result of the 1st subtask: {task1(data)}')
    print(f'Result of the 2nd subtask: {task2(data)}')


if __name__ == '__main__':
    main()
