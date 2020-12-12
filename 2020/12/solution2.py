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


def rotate(point, direct, deg):
	if direct == ACTIONS["right"]:
		deg = 360 - deg
	rad = radians(deg)
	rpoint = atan2(point[1], point[0])

	new_rpoint = rpoint + rad
	scale = (point[0]**2 + point[1]**2)**(1/2)
	rise = round(sin(new_rpoint)*scale)
	run = round(cos(new_rpoint)*scale)
	new_point = type(point)((run, rise))
	return new_point


def split_actions(inlst):
	actions = [[x[0], int(x[1:])] for x in inlst]
	return actions


def navigate(actions):
	location = [0, 0]
	waypoint = [10, 1]	#always relative to location!

	for action in actions:
		if action[0] == ACTIONS["north"]:
			waypoint[1] += action[1]
		elif action[0] == ACTIONS["south"]:
			waypoint[1] -= action[1]
		elif action[0] == ACTIONS["east"]:
			waypoint[0] += action[1]
		elif action[0] == ACTIONS["west"]:
			waypoint[0] -= action[1]
		elif (action[0] == ACTIONS["left"]) or (action[0] == ACTIONS["right"]):
			waypoint = rotate(waypoint, action[0], action[1])
		elif action[0] == ACTIONS["forward"]:
			location[0] += (waypoint[0] * action[1])
			location[1] += (waypoint[1] * action[1])

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
