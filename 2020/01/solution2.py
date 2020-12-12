#!/usr/bin/env python3

import sys

def find_parts(inlst, parts, sum):
	outparts = []

	i = 0
	match = None
	while i < (len(inlst)-parts+1):
		subparts = []
		if parts > 1:
			subparts = find_parts(inlst[i+1:], parts-1, sum-inlst[i])
			if len(subparts)+1 == parts:
				match = inlst[i]
		else:
			if inlst[i] == sum:
				match = inlst[i]

		if match:
			outparts = [match] + subparts
			break
		i += 1

	return outparts


def solve(inlst, parts, sum):
	parts = find_parts(inlst, parts, sum)
	mult = 1
	for x in parts:
		mult *= x
	return mult


def main():
	sum = int(sys.argv[1])
	parts = int(sys.argv[2])
	inname = sys.argv[3]

	inlst = []
	infile = open(inname, "r")
	for line in infile:
		inlst.append(int(line.strip()))
	infile.close

	solution = solve(inlst, parts, sum)
	print(solution)

if __name__ == "__main__":
	main()
