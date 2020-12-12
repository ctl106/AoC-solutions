#!/usr/bin/env python3

import sys


def is_num_valid(num_list, x):
	output = False

	num_reduced = [n for n in num_list if n < x]
	num_reduced.sort()

	i = 0
	dif = None
	while (num_reduced[i] < (x/2)) and not output:
		dif = x - num_reduced[i]
		if dif in num_reduced:
			output = True
		i += 1

	return output


def	validate(inlst, check_length):
	output = 0
	ints = [int(line) for line in inlst]
	check = ints[:check_length]
	i = check_length
	while (i < len(ints)) and not output:
		if is_num_valid(check, ints[i]):
			i += 1
			check = ints[(i-check_length):i]
		else:
			output = ints[i]
	return output


def find_addends(inlst, invalid):
	ints = [int(line) for line in inlst]
	addends = []
	i = 0
	while (i < len(ints)) and (not len(addends)):
		test_addends = []
		j = i

		while (ints[j] != invalid) and (sum(test_addends) < invalid):
			test_addends.append(ints[j])
			j += 1

		if sum(test_addends) == invalid:
			addends = test_addends.copy()

		i += 1
	return addends


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
	check_length = 25
	if len(sys.argv) > 2:
		check_length = int(sys.argv[2])

	invalid = validate(inlst, check_length)
	addends = find_addends(inlst, invalid)
	addends.sort()
	output = addends[0] + addends[-1]

	return output


def main():
	inlst = read_input_file()
	result = solve(inlst)
	print(result)

if __name__ == "__main__":
	main()
