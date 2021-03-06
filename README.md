### Background
The universe of the [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is a two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, or "populated" or "unpopulated". Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

- Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick (in other words, each generation is a pure function of the preceding one). The rules continue to be applied repeatedly to create further generations.

## Dependencies
1. [NumPy](https://numpy.org/)

## Installation
- Install requirements.txt (```pip install -r requirements.txt```)

### Milestone 1
To run the script use the following command:
```
$ cat 'INPUT_PATTERN' | python gameoflife.py
```

### Milestone 2
To run the script use the following command:
```
$ cat 'INPUT_PATTERN' | python gameoflife.py --rulestring 'RULESTRING' 
```

