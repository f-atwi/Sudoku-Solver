class SudokuSolver:
    def __init__(self) -> None:
        self.sudoku = [[[i for i in range(1, 10)]
                        for i in range(9)] for i in range(9)]

    def defineCell(self, row: int, col: int, value: int) -> None:
        if not(-1 < row < 9 and -1 < col < 9):
            raise IndexError("Index not in sudoku range")
        if not(0 < value < 10 and int(value) == value):
            raise ValueError("Value is not an Integer or not 1-9")
        self.sudoku[row][col] = [value]

    def defineHints(self, args: list) -> None:
        for entry in args:
            if len(entry) != 3:
                raise ValueError("One of the entries is not of size 3")
            else:
                self.defineCell(entry[0], entry[1], entry[2])

    def removeFromRow(self, x, y, value):
        for c, cell in enumerate(self.sudoku[x]):
            if c != y and value in cell:
                cell.remove(value)

    def removeFromCol(self, x, y, value):
        for r, row in enumerate(self.sudoku):
            if r != x and value in row[y]:
                row[y].remove(value)

    def removeFromBlock(self, x, y, value):
        for i in range(x - x % 3, x - x % 3 + 3):
            for j in range(y - y % 3, y - y % 3 + 3):
                if i != x and j != y and value in self.sudoku[i][j]:
                    self.sudoku[i][j].remove(value)

    def eliminatePossibilities(self):
        definites = self.getDefinites()
        for i, j, k in definites:
            self.removeFromRow(i, j, k)
            self.removeFromCol(i, j, k)
            self.removeFromBlock(i, j, k)

    def getDefinites(self):
        definites = []
        for i, row in enumerate(self.sudoku):
            for j, cell in enumerate(row):
                if len(cell) == 1:
                    definites.append([i, j, cell[0]])
        return definites

    def rowSolver(self):
        for i, row in enumerate(self.sudoku):
            for j, cell in enumerate(row):
                for p in cell:
                    if len([c for c in row if p in c]) == 1:
                        self.removeFromRow(i, j, p)

    # def colSolver(self):
    #     for j in range(9):
    #         union = [p for ]

    #     for i, row in enumerate(self.sudoku):
    #         union = [p for cell in row for p in cell]
    #         for p in union:
    #             if union.count(p)==1:
    #                 j=[j for j, cell in enumerate(row) if p in cell][0]
    #                 self.removeFromCol(i,j,p)

    def isSolved(self) -> bool:
        return all([all(len(cell) == 1 for cell in row) for row in self.sudoku])

    def __str__(self) -> str:
        sudoku = '╔═══════════╦═══════════╦═══════════╗\n'
        for index, row in enumerate(self.sudoku):
            sudoku += '║ {} | {} | {} ║ {} | {} | {} ║ {} | {} | {} ║\n'.format(
                *[x[0] if len(x) == 1 else ' ' for x in row])
            if index in [2, 5]:
                sudoku += '╠═══════════╬═══════════╬═══════════╣\n'
            elif index == 8:
                sudoku += '╚═══════════╩═══════════╩═══════════╝\n'
            else:
                sudoku += '║---+---+---║---+---+---║---+---+---║\n'
        return sudoku

    def __repr__(self) -> str:
        wide_edge = ['║', '║', '║']
        slim_edge = ['|', '|', '|']
        sudoku = '╔═══════════════════════╦═══════════════════════╦═══════════════════════╗\n'
        for index, row in enumerate(self.sudoku):
            constructor = wide_edge
            for index2, cell in enumerate(row):
                block = ' 1 2 3 \n 4 5 6 \n 7 8 9 '
                for char in block:
                    if char.isdigit() and not(int(char) in cell):
                        block = block.replace(char, ' ')
                constructor = zip(constructor, block.split('\n'), wide_edge)if index2 % 3 == 2 else zip(
                    constructor, block.split('\n'), slim_edge)
                constructor = [x + y+z for x, y, z in constructor]
            constructor = '\n'.join(constructor)
            constructor += '\n'
            sudoku += constructor
            if index in [2, 5]:
                sudoku += '╠═══════════════════════╬═══════════════════════╬═══════════════════════╣\n'
            elif index == 8:
                sudoku += '╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\n'
            else:
                sudoku += '║-------+-------+-------║-------+-------+-------║-------+-------+-------║\n'
        return sudoku


def main():
    sudoku = SudokuSolver()
    sudoku.defineHints([[0, 1, 2], [0, 4, 3], [0, 7, 4], [1, 0, 6], [1, 8, 3], [2, 2, 4], [2, 6, 5], [3, 3, 8], [3, 5, 6], [4, 0, 8], [
        4, 4, 1], [4, 8, 6], [5, 3, 7], [5, 5, 5], [6, 2, 7], [6, 6, 6], [7, 0, 4], [7, 8, 8], [8, 1, 3], [8, 4, 4], [8, 7, 2]])
    # sudoku.defineHints([[2,2,4]])
    print(sudoku)
    print(repr(sudoku))

    sudoku.eliminatePossibilities()

    # sudoku.rowSolver()
    # sudoku.colSolver()

    print(repr(sudoku))


if __name__ == "__main__":
    main()
