#!/usr/bin/env python3

import sys
from math import atan2, sin, cos, radians


ACTIONS = {
	"north":	"N",
	"south":	"S",
	"east":		"E",
	"west":		"W",
	"left":		"L",
	"right":	"R",
	"forward":	"F"
}


def rotate(bearing, direct, deg):
	if direct == ACTIONS["right"]:
		deg = 360 - deg
	rad = radians(deg)
	rbearing = atan2(bearing[1], bearing[0])

	new_rbearing = rbearing + rad
	rise = round(sin(new_rbearing))
	run = round(cos(new_rbearing))
	new_bearing = (run, rise)
	#print(bearing, "->", deg, "->", new_bearing)
	return new_bearing


def split_actions(inlst):
	actions = [[x[0], int(x[1:])] for x in inlst]
	return actions


def navigate(actions):
	location = [0, 0]
	bearing = (1, 0)

	for action in actions:
		if action[0] == ACTIONS["north"]:
			location[1] += action[1]
		elif action[0] == ACTIONS["south"]:
			location[1] -= action[1]
		elif action[0] == ACTIONS["east"]:
			location[0] += action[1]
		elif action[0] == ACTIONS["west"]:
			location[0] -= action[1]
		elif (action[0] == ACTIONS["left"]) or (action[0] == ACTIONS["right"]):
			bearing = rotate(bearing, action[0], action[1])
		elif action[0] == ACTIONS["forward"]:
			location[0] += (bearing[0] * action[1])
			location[1] += (bearing[1] * action[1])
		#print(location)

	return location


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

	actions = split_actions(inlst)
	dest = navigate(actions)
	output = abs(dest[0]) + abs(dest[1])

	return output


def main():
	inlst = read_input_file()
	result = solve(inlst)
	print(result)

if __name__ == "__main__":
	main()
