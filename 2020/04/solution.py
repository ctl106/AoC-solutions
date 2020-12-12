#!/usr/bin/env python3

import sys


REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def seperate_passports(inlst):
	passports = []

	inlst.append("")
	passport = ""
	for line in inlst:
		if len(line) > 0:
			passport += " " + line
		elif len(passport) > 0:
			passports.append(passport)
			passport = ""

	return passports


def seperate_fields(passport):
	passfields = {entry.split(":")[0]:entry.split(":")[1] for entry in passport.split()}
	return passfields


def is_valid(passport):
	output = True
	for field in REQUIRED_FIELDS:
		if field not in passport.keys():
			output = False
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

	passports = seperate_passports(inlst)
	passfields = [seperate_fields(passport) for passport in passports]
	for passport in passfields:
		if is_valid(passport):
			output += 1

	return output


def main():
	inlst = read_input_file()
	result = solve(inlst)
	print(result)

if __name__ == "__main__":
	main()
