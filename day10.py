import time


BRACKETS = {')': '(',
            ']': '[',
            '>': '<',
            '}': '{',
            }

SCORE = {')': 3,
         ']': 57,
         '}': 1197,
         '>': 25137,
         }

SCORE2 = {'(': 1,
          '[': 2,
          '{': 3,
          '<': 4,
          }


def check_line(line: str) -> int:
    stack = []
    for idx, char in enumerate(line):
        if char in '([<{':
            stack.append(idx)
        elif BRACKETS[char] == line[stack[-1]]:
            stack.pop()
        else:
            return SCORE[char]
    return 0


def task1(data: list[str]) -> int:
    return sum([check_line(line) for line in data])


def evaluate_line(line: str) -> int:
    stack = []
    for idx, char in enumerate(line):
        if char in '([<{':
            stack.append(idx)
        elif BRACKETS[char] == line[stack[-1]]:
            stack.pop()

    total = 0
    for idx in reversed(stack):
        total *= 5
        total += SCORE2[line[idx]]

    return total


def task2(data: list[str]) -> int:
    score_list = [evaluate_line(line)
                  for line in data if check_line(line) == 0]
    return sorted(score_list)[len(score_list) // 2]


def main() -> None:
    # with open('./data/test.txt') as f:
    with open('./data/day10.txt') as f:
        data = [i for i in f.read().split('\n')]

    # print(data)
    t = time.process_time()

    print(f'Result of the 1st subtask: {task1(data)}')
    print(f'Result of the 2nd subtask: {task2(data)}')

    elapsed_time = time.process_time() - t
    print(f'time: {elapsed_time}')


if __name__ == '__main__':
    main()
