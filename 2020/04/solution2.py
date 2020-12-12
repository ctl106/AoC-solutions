#!/usr/bin/env python3

import sys
import re


REQUIRED_FIELDS = {
	"byr": "^19[2-9]\d|200[0-2]$",
	"iyr": "^201\d|2020$",
	"eyr": "^202\d|2030$",
	"hgt": "^1[5-8]\dcm|19[0-3]cm|59in|6\din|7[0-6]in$",
	"hcl": "^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$",
	"ecl": "^amb|blu|brn|gry|grn|hzl|oth$",
	"pid": "^\d\d\d\d\d\d\d\d\d$"
}


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
	for field in REQUIRED_FIELDS.keys():
		if (
			(field not in passport.keys()) or
			not re.match(REQUIRED_FIELDS[field], passport[field])
		):
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
