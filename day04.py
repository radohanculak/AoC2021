import time


class Board():
    def __init__(self, board: list[str]) -> None:
        self.fields = [[[int(col), False] for col in row.split()]
                       for row in board.split('\n')]

    def mark_field(self, num: int) -> None:
        for row in self.fields:
            for elem in row:
                if elem[0] == num:
                    elem[1] = True
                    return

    def check(self) -> bool:
        for row in self.fields:
            if all(list(map(lambda x: x[1], row))):
                return True

        reversed = ((row[i] for row in self.fields) for i in range(5))
        for col in reversed:
            if all(list(map(lambda x: x[1], col))):
                return True

        return False

    def unmarked_sum(self) -> int:
        res = 0
        for row in self.fields:
            for elem in row:
                if not elem[1]:
                    res += elem[0]
        return res


def task1(boards: list[Board], randoms: list[int]):
    for num in randoms:
        for board in boards:
            board.mark_field(num)
            if board.check():
                return num * board.unmarked_sum()


def task2(boards: list[Board], randoms: list[int]):
    # random, will be overwritten
    last_board = boards[0]
    last_num = 0
    winning_boards = set([])

    for num in randoms:
        for board in boards:
            if id(board) not in winning_boards:
                board.mark_field(num)
            if id(board) not in winning_boards and board.check():
                winning_boards.add(id(board))
                last_num = num
                last_board = board

    return last_board.unmarked_sum() * last_num


def main() -> None:
    with open('./data/day04.txt') as f:
        data = f.read().split('\n\n')

    t = time.process_time()

    randoms, *boards = data
    boards: list[Board] = list(map(Board, boards))
    randoms: list[int] = list(map(int, randoms.split(',')))

    print(f'Result of the 1st subtask: {task1(boards, randoms)}')
    print(f'Result of the 2nd subtask: {task2(boards, randoms)}')

    elapsed_time = time.process_time() - t
    print(f'time: {elapsed_time}')


if __name__ == '__main__':
    main()
