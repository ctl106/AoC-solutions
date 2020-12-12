#!/usr/bin/env python3

import sys


class env:
	def __init__(self, addr=0, acc=0, run=True, loop=True):
		self.addr = addr
		self.acc = acc
		self.run = run
		self.loop = loop
		self.trace = []


def exec_acc(myenv, command, argument):
	output = 0
	myenv.acc += argument
	return output


def exec_jmp(myenv, command, argument):
	output = 0
	jaddr = myenv.addr + argument
	if (not myenv.loop) and (jaddr in myenv.trace):
		myenv.run = False
		output = -1
	else:
		myenv.addr = jaddr - 1	# -1 to account for normal inc of addr

	return output


def exec_nop(myenv, command, argument):
	output = 0
	return output


commands = {
	"acc": exec_acc,
	"jmp": exec_jmp,
	"nop": exec_nop
}


def execute(myenv, command, argument):
	output = None
	if command in commands:
		output = commands[command](myenv, command, argument)
	else:
		# raise some sort of error?
		pass
	return output


def interp(myenv, inlst):
	if not myenv:
		myenv = env()

	while myenv.run and (myenv.addr >= 0) and (myenv.addr < len(inlst)):
		myenv.trace.append(myenv.addr)
		execute(
			myenv,
			inlst[myenv.addr].split()[0],
			int(inlst[myenv.addr].split()[1])
		)
		myenv.addr += 1


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

	myenv = env(loop = False)
	interp(myenv, inlst)
	output = myenv.acc

	return output


def main():
	inlst = read_input_file()
	result = solve(inlst)
	print(result)

if __name__ == "__main__":
	main()
