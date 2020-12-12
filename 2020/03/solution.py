#!/usr/bin/env python3

import sys


KEY = {"end": "!", "tree": "#", "empty": "."}


def read_input_file():
	inname = sys.argv[1]
	inlst = []
	infile = open(inname, "r")
	for line in infile:
		inlst.append(line.strip())
	infile.close
	return inlst


def contents(loc, mymap):
	output = None
	if loc[1] >= len(mymap):
		output = KEY["end"]
	else:
		output = mymap[loc[1]][loc[0]%len(mymap[0])]
	return output


def traverse(loc, x, y, mymap):
	loc[0] += x
	loc[1] += y
	return contents(loc, mymap)
	
		
def solve(inlst):
	total = 0

	loc = [0, 0]
	content = contents(loc, inlst)
	while content != KEY["end"]:
		if content == KEY["tree"]:
			total += 1
		content = traverse(loc, 3, 1, inlst)

	return total


def main():
	inlst = read_input_file()
	total = solve(inlst)
	print(total)

if __name__ == "__main__":
	main()
