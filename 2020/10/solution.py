#!/usr/bin/env python3

import sys

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

	intlst = [int(x) for x in inlst]
	intlst.sort()
	intlst.append(max(intlst)+3)
	differences = count_differences(intlst)
	diff_counts = [0, 0, 0, 0]

	def inclst(lst, index):
		lst[index] += 1

	[inclst(diff_counts, x) for x in differences if x <= 3]
	output = diff_counts[1] * diff_counts[3]

	return output


def main():
	inlst = read_input_file()
	result = solve(inlst)
	print(result)

if __name__ == "__main__":
	main()
