#!/usr/bin/env python3

import sys


# policy follows format:
# {`character`: (min, max)}


def is_valid(policy, txt):
	valid = False
	count = 0
	for char in policy:
		if (txt[policy[char][0]-1] == char) and (txt[policy[char][1]-1] != char):
			valid = True
		elif (txt[policy[char][0]-1] != char) and (txt[policy[char][1]-1] == char):
			valid = True
			
	return valid


def make_policy(txt):
	txtsplit = txt.split()
	rng = txtsplit[0].split("-")
	output = {}
	output[txtsplit[1]] = (int(rng[0]), int(rng[1]))
	return output
		

def solve(inlst):
	total = 0
	for line in inlst:
		linesplit = line.split(":")
		policy = make_policy(linesplit[0].strip())
		if is_valid(policy, linesplit[1].strip()):
			total += 1

	return total


def main():
	inname = sys.argv[1]

	inlst = []
	infile = open(inname, "r")
	for line in infile:
		inlst.append(line.strip())
	infile.close

	total = solve(inlst)
	print(total)

if __name__ == "__main__":
	main()
