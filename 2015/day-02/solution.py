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
    def __init__(self, data: str) -> None:
        self.data = data

    @property
    def __p1_solution(self) -> int:
        total = 0

        for line in self.data.splitlines():
            l, w, h = map(int, line.split('x'))

            side_1 = l * w
            side_2 = w * h
            side_3 = h * l

            total += (2 * side_1) + (2 * side_2) + (2 * side_3)
            total += min(side_1, side_2, side_3)

        return total

    @property
    def __p2_solution(self) -> int:
        total = 0

        for line in self.data.splitlines():
            l, w, h = map(int, line.split('x'))
            dimensions = sorted([l, w, h])[:2]

            total += (2 * dimensions[0]) + (2 * dimensions[1])
            total += l * w * h

        return total

    def __call__(self, part: int) -> int:
        if part == 1:
            return self.__p1_solution
        elif part == 2:
            return self.__p2_solution
        else:
            raise ValueError(f'Invalid part number: {part}')


if __name__ == '__main__':
    with InputReader(CWD / 'puzzle.in') as puzzle:
        sol = PuzzleSolver(puzzle)

        print(f'Part 1: {sol(1)}')
        print(f'Part 2: {sol(2)}')
