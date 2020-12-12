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


def cycle(layout):
	pad_layout = pad_floor(layout)
	new_layout = []

	row = 1
	while row < (len(pad_layout)-1):
		col = 1
		new_row = ""#"."
		while col < (len(pad_layout[row])-1):
			square = [row[col-1:col+2] for row in pad_layout[row-1:row+2]]
			occupied = count_char(square, sym["occ"])

			if (pad_layout[row][col] == sym["un_occ"]) and (occupied == 0):
				new_row += sym["occ"]
			elif (pad_layout[row][col] == sym["occ"]) and (occupied > 4):
				new_row += sym["un_occ"]
			else:
				new_row += pad_layout[row][col]

			col += 1
		#new_row += "."
		new_layout.append(new_row)
		row += 1
			
	#new_layout = unpad_floor(new_layout)
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
