import numpy as np
import argparse
import sys
import io


def first_generation(input_pattern: io.TextIOWrapper) -> np.ndarray:
    pattern: List = []
    line: str
    for line in input_pattern:
        line = line.rstrip('\r\n')
        if '!' not in line:
            pattern.append(line)
    n_rows: int = len(pattern)
    if n_rows == 0:
        print('File not found, exiting!')
        sys.exit(-1)   
    n_cells: int = len(pattern[0])
    pattern_np: np.ndarray = np.zeros((n_rows, n_cells), dtype=np.int32)
    row_idx: int
    row: str
    cell_idx: int
    cell: str
    for row_idx, row in enumerate(pattern):
        for cell_idx, cell in enumerate(row):
            if cell == 'O':
                pattern_np[row_idx, cell_idx] = 1
            elif cell == '.':
            	pass
            else:
                print('Invalid character on input pattern, exiting!')
                sys.exit(-1)   
    return pattern_np


def pad_array(arr: np.ndarray) -> np.ndarray:
    len_x: int
    len_y: int
    len_x, len_y = arr.shape
    padding_row: np.ndarray = np.zeros((1, len_y+2), dtype=np.int32)
    padding_column: np.ndarray = np.zeros((len_x, 1), dtype=np.int32)
    arr = np.concatenate([padding_column, arr, padding_column], axis=1)
    arr = np.concatenate([padding_row, arr, padding_row], axis=0)
    return arr


def next_generation(arr: np.ndarray) -> np.ndarray:
    next_pattern_np: np.ndarray = np.zeros((arr.shape), dtype=np.int32)
    arr_padded: np.ndarray = pad_array(arr)
    row_idx: int
    row: str
    cell_idx: int
    cell: int
    status: int
    for row_idx, row in enumerate(arr):
        for cell_idx, cell in enumerate(row):
            neighbors: int = arr_padded[row_idx:row_idx+3,cell_idx:cell_idx+3].sum() - arr_padded[row_idx+1, cell_idx+1]
            if cell == 1:
                if neighbors < 2:
                    status = 0
                elif neighbors < 4:
                    status = cell
                else:
                    status = 0
            else:
                if neighbors == 3:
                    status = 1
                else:
                    status = cell
            next_pattern_np[row_idx, cell_idx] = status
    return next_pattern_np

def print_output(arr: np.ndarray) -> str:
    output: str = ''
    row: np.ndarray
    cell: int
    status: str
    for row in arr:
        for cell in row:
            if cell == 0:
                status = '.'
            else:
                status = 'O'
            output += status
        output += '\n'
    return output



def main(input_pattern):
	first_gen: np.ndarray = first_generation(input_pattern)
	next_gen: np.ndarray = next_generation(first_gen)
	output: str = print_output(next_gen)
	sys.stdout.write(output)  


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Game of Life Kata')
	parser.add_argument('--input-pattern', type=argparse.FileType('r'), default=sys.stdin)
	args = parser.parse_args()
	input_pattern = args.input_pattern
	main(input_pattern)
