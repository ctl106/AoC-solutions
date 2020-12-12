#!/usr/bin/env python3

import sys
from functools import reduce


def split_groups(inlst):
	groups = []
	tmp = []

	for line in inlst:
		if len(line) > 0:
			tmp.append(line)
		else:
			groups.append(tmp)
			tmp = []

	if len(tmp) > 0:
		groups.append(tmp)

	return groups


def add_unique(str1, str2):
	out = str1 + "".join([char for char in str2 if char not in str1])
	return out


def combine_group(group):
	out = reduce(add_unique, group)
	return out


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

	answers = [combine_group(group) for group in split_groups(inlst)]
	output = reduce((lambda x, y: x + len(y)), answers, 0)

	return output


def main():
	inlst = read_input_file()
	result = solve(inlst)
	print(result)

if __name__ == "__main__":
	main()
