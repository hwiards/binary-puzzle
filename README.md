# Binary Puzzle Solver

A simple solver for [Binary-Puzzles](https://www.binarypuzzle.com). 

## Rules

1. Every cell contains either a zero or a one.
2. More than two equal numbers next to or above each other are not allowed. 
3. There is an equal number of ones and zeros in each row and column.
4. Each row and column is unique.

## Usage

Right now the script assumes, that the inputfile is placed in the ```ìnput``` folder. For example the file ````6x6_e_1.txt``

```
python3 main.py 6x6_e_1.txt
```