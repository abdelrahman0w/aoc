import pathlib


CWD = pathlib.Path(__file__).parent.absolute()


class InputReader:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @property
    def __content(self) -> str:
        with open(self.file_name) as input_file:
            return input_file.read()

    def __enter__(self) -> str:
        return self.__content

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is not None:
            print(f'Error: {exc_value}')
            print(exc_traceback)


class PuzzleSolver:
    def __init__(self, data: str, sol: int = 1) -> None:
        self.data = data
        self.sol = sol

    @property
    def __solution_1(self) -> int:
        return self.data.count('(') - self.data.count(')')

    @property
    def __solution_2(self) -> int:
        open_parentheses, close_parentheses = 0, 0

        for char in self.data:
            if char == '(':
                open_parentheses += 1
            elif char == ')':
                close_parentheses += 1

        return open_parentheses - close_parentheses

    @property
    def __p2_solution(self) -> int:
        floor = 0

        for pos, char in enumerate(self.data, start=1):
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1

            if floor == -1:
                return pos

    def __call__(self, part: int, *args) -> int:
        if args:
            self.sol = args[0]

        if part == 1:
            if self.sol == 1:
                return self.__solution_1
            elif self.sol == 2:
                return self.__solution_2
            else:
                raise ValueError(f'Invalid solution number: {self.sol}')
        elif part == 2:
            return self.__p2_solution
        else:
            raise ValueError(f'Invalid part number: {part}')


if __name__ == '__main__':
    with InputReader(CWD / 'puzzle.in') as puzzle:
        sol = PuzzleSolver(puzzle)

        print(f'Part 1: {sol(1)}')
        print(f'Part 2: {sol(2)}')
