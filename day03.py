

def invert(data: list[list[str]]) -> list[str]:
    # basically a matrix transposition
    return [''.join((row[i] for row in data)) for i in range(len(data[0]))]


def reconstruct_number(data: list[str], inverted: bool = False) -> int:
    res_string = ''

    for col in data:
        res_string += '0' if col.count('0') > len(col) // 2 else '1'

    if inverted:
        res_string = ''.join(('0' if x == '1' else '1' for x in res_string))

    return int(res_string, 2)


def task1(data: list[list[str]]) -> int:
    data_cols = invert(data)
    gamma = reconstruct_number(data_cols)
    epsilon = reconstruct_number(data_cols, inverted=True)

    return gamma * epsilon


def get_column(data: list[list[str]], idx: int) -> str:
    return ''.join([elem[idx] for elem in data])


def oxy_generator_rating(data: list[list[str]]) -> int:
    idx = 0
    while len(data) > 1:
        col = get_column(data, idx)

        if col.count('1') >= col.count('0'):
            data = list(filter(lambda x: x[idx] == '1', data))
        else:
            data = list(filter(lambda x: x[idx] == '0', data))

        idx += 1

    assert len(data) == 1
    return int(''.join(*data), 2)


def co2_scrubber_rating(data: list[list[str]]) -> int:
    idx = 0
    while len(data) > 1:
        col = get_column(data, idx)

        if col.count('0') <= col.count('1'):
            data = list(filter(lambda x: x[idx] == '0', data))
        else:
            data = list(filter(lambda x: x[idx] == '1', data))

        idx += 1

    assert len(data) == 1
    return int(''.join(*data), 2)


def task2(data: list[list[str]]) -> int:
    return oxy_generator_rating(data) * co2_scrubber_rating(data)


def main() -> None:
    with open('./data/day03.txt') as f:
        data = list(map(list, f.read().split('\n')))

    print(f'Result of the 1st subtask: {task1(data)}')
    print(f'Result of the 2nd subtask: {task2(data)}')


if __name__ == '__main__':
    main()
