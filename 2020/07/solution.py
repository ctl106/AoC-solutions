#!/usr/bin/env python3

import sys


class bag:
	def __init__(self, color, condict):
		self.color = color
		self.contain = condict

	def __iter__(self):
		self._i = 0
		self._keys = list(self.contain.keys())
		return self

	def __next__(self):
		output = None
		if self._i < len(self._keys):
			output = self._keys[self._i]
			self._i += 1
		else:
			raise StopIteration
		return output


	def keys(self):
		return self.contain.keys()


def make_rule(line):
	def rem_last_word(line):
		return " ".join(line.split()[:-1])

	splitline = line.split(" contain ")
	container = rem_last_word(splitline[0])

	contents = {}
	for b in splitline[1].split(", "):
		if b != "no other bags.":
			bsplit = b.split()[:-1]
			contents[" ".join(bsplit[1:])] = int(bsplit[0])

	bagrule = bag(container, contents)
	return bagrule


def compile_rules(inlst):
	return [make_rule(line) for line in inlst]


def find_containers(rules, color):
	output = []
	for rule in rules:
		if color in rule:
			output.append(rule.color)
	return output


def find_containers_r(rules, mycolor):
	output = []

	search = [mycolor]
	searched = []
	while(True):
		temp = []
		for color in search:
			temp += find_containers(rules, color)

		if len(temp) == 0:
			break

		[output.append(color) for color in temp if color not in output]

		searched += search
		search = []
		[search.append(color) for color in output if color not in searched]

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

	mycolor = "shiny gold"
	rules = compile_rules(inlst)
	containers = find_containers_r(rules, mycolor)
	output = len(containers)

	return output


def main():
	inlst = read_input_file()
	result = solve(inlst)
	print(result)

if __name__ == "__main__":
	main()
