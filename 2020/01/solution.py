#!/usr/bin/env python3

import sys

def discard(big, small, entry):
	return

def addbig(big, small, entry):
	big.append(entry)
	return

def addsmall(big, small, entry):
	small.append(entry)
	return

actions = {"discard": discard, "addbig": addbig, "addsmall": addsmall}

def filter(big, small, max, inlst):
	half = 0
	for entry in inlst:
		if entry > max:
			actions["discard"](big, small, entry)
		elif entry > max/2:
			actions["addbig"](big, small, entry)
		elif entry < max/2:
			actions["addsmall"](big, small, entry)
		else:
			half += 1
	
	if half >= 2:
		big.append(max/2)
		small.append(max/2)

def find_parts(inlst, sum):
	big = []
	small = []
  
	filter(big, small, sum, inlst)

	big_half = None
	small_half = None

def find_parts(inlst, sum):
	big = []
	small = []

	filter(big, small, sum, inlst)

	big_half = None
	small_half = None

def find_parts(inlst, sum):
	big = []
	small = []

	filter(big, small, sum, inlst)

	big_half = None
	small_half = None

	for b in big:
		for s in small:
			if b+s == sum:
				big_half = b
				small_half = s
				break

		if big_half and small_half:
			break

	return (big_half, small_half)

def solve(inlst, sum):
	halves = find_parts(inlst, sum)
	mult = halves[0] * halves[1]
	return mult

def main():
	sum = int(sys.argv[1])
	inname = sys.argv[2]

	inlst = []
	infile = open(inname, "r")
	for line in infile:
		inlst.append(int(line.strip()))
	infile.close

	solution = solve(inlst, sum)
	print(solution)

if __name__ == "__main__":
	main()
