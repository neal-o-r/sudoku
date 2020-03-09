from typing import Dict, List

Sudoku = str
Digit = str
Square = str
Grid = Dict[Square, Digit]

def cross(A: list, B: list) -> list:
    return [a+b for a in A for b in B]


sudoku = '53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79'
cols = '123456789'
rows = 'ABCDEFGHI'
squares = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u])
             for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)

grid = dict(zip(squares, sudoku))


def chunks(string: Sudoku, n: int) -> list:
    return [list(string[i : i + n]) for i in range(0, len(string), n)]


def display(grid: Grid):
    for i, l in enumerate(chunks("".join(grid.values()), 9)):
        if i % 3 is 0 and i != 0: print('-'*21)
        print(" | ".join(" ".join(a) for a in chunks(l, 3)))


def is_possible(square: Square, n: Digit, grid: Grid) -> bool:
    return n not in [grid[s] for s in peers[square]]


def solve(grid: Grid):
    empty = {k: v for k, v in grid.items() if v is '.'}
    if empty == {}:
        display(grid)

    for sq, digit in empty.items():
        for n in cols:
            if is_possible(sq, n, grid):
                grid[sq] = n
                solve(grid)
                grid[sq] = '.'
        return


if __name__ == "__main__":
    solve(grid)
