#!/usr/bin/env python3

import sys


def count_combos(intlst):
	output = 0
	
	branches_per = [0]*len(intlst)
	i = len(branches_per) - 1
	end = 4
	while i >= 0:
		if (len(intlst) - i) == 1:
			branches_per[i] = 1
		elif (len(intlst) - i) < 4:
			end = len(intlst) - i
		else:
			end = 4



		for j in intlst[i+1:i+end]:
			if j <= intlst[i] + 3:
				branches_per[i] += branches_per[intlst.index(j)]

		i -= 1

	output = branches_per[0]

	return output


def count_differences(intlst):
	output = []
	prev = 0
	i = 0
	while i < len(intlst):
		output.append(intlst[i] - prev)
		prev = intlst[i]
		i += 1
	return output


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

	intlst = [0] + [int(x) for x in inlst]
	intlst.sort()
	intlst.append(max(intlst)+3)
	output = count_combos(intlst)

	return output


def main():
	inlst = read_input_file()
	result = solve(inlst)
	print(result)

if __name__ == "__main__":
	main()
