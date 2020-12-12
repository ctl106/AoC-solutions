#!/usr/bin/env python3

import sys
from functools import reduce


sym = {
	"floor":	'.',
	"un_occ":	'L',
	"occ":		'#'
}


def count_char(lst, char):
	return reduce((lambda x, y: x+y.count(char)), lst, 0)


def print_floor(layout):
	for row in layout:
		for col in row:
			print(col, end=" ")
		print()


def pad_floor(layout):
	pad_layout = [sym["floor"]*(len(layout[0])+2)]
	pad_layout += [(sym["floor"]+row+sym["floor"]) for row in layout]
	pad_layout += [sym["floor"]*(len(layout[0])+2)]
	return pad_layout


def unpad_floor(layout):
	unpad_layout = [row[1:len(row)-1] for row in layout[1:len(layout)-1]]
	print_floor(unpad_layout)
	print()
	return unpad_layout


def count_first_occupied(layout, row, col):
	count = 0
	directions = [
		(0, 1),
		(0, -1),
		(1, 0),
		(-1, 0),
		(1, 1),
		(1, -1),
		(-1, 1),
		(-1, -1)
	]

	for d in directions:
		drow = row + d[0]
		dcol = col + d[1]
		char = sym["floor"]
		while (
			(char == sym["floor"]) and
			(drow >= 0) and
			(drow < len(layout)) and
			(dcol >= 0) and
			(dcol < len(layout[0]))
		):
			char = layout[drow][dcol]
			drow += d[0]
			dcol += d[1]

		if char == sym["occ"]:
			count += 1

	return count


def cycle(layout):
	pad_layout = pad_floor(layout)
	new_layout = []

	row = 1
	while row < (len(pad_layout)-1):
		col = 1
		new_row = ""
		while col < (len(pad_layout[row])-1):
			occupied = count_first_occupied(pad_layout, row, col)

			if (pad_layout[row][col] == sym["un_occ"]) and (occupied == 0):
				new_row += sym["occ"]
			elif (pad_layout[row][col] == sym["occ"]) and (occupied >= 5):
				new_row += sym["un_occ"]
			else:
				new_row += pad_layout[row][col]

			col += 1
		new_layout.append(new_row)
		row += 1

	return new_layout


def read_input_file():
	if len(sys.argv) <= 1:
		print("Please specify an input file.")
		exit(1)

	inname = sys.argv[1]
	inlst = []
	infile = open(inname, "r")
	for line in infile:
		inlst.append(line.strip())
	infile.close
	return inlst
	
		
def solve(inlst):
	output = 0

	cur = inlst.copy()
	prev = None
	while cur != prev:
		prev = cur
		cur = cycle(prev)

	output = count_char(cur, sym["occ"])
	return output


def main():
	inlst = read_input_file()
	result = solve(inlst)
	print(result)

if __name__ == "__main__":
	main()
