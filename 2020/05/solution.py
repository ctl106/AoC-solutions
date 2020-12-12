#!/usr/bin/env python3

import sys
import re


BOARDING_ROW = "^[FB]{7}"
BOARDING_COL = "[LR]{3}$"
BOARDING_WHOLE = BOARDING_ROW + BOARDING_COL


def is_valid(boardingpass):
	valid = False
	if re.search(BOARDING_WHOLE, boardingpass):
		valid = True
	return valid


def decode_rowcol(boardingpass):
	def bin_decode(code, low, high):
		return int(code.replace(low, "0").replace(high, "1"), 2)

	row = bin_decode(re.search(BOARDING_ROW, boardingpass).group(), "F", "B")
	col = bin_decode(re.search(BOARDING_COL, boardingpass).group(), "L", "R")

	return (row, col)


def calc_seatid(seat):
	return seat[0]*8 + seat[1]


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
	output = max([calc_seatid(decode_rowcol(line)) for line in inlst if is_valid(line)])			

	return output


def main():
	inlst = read_input_file()
	result = solve(inlst)
	print(result)

if __name__ == "__main__":
	main()
