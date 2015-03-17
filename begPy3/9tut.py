#!/usr/bin/python
import math

def Main():
	try:
		radius = float(input("Please enter the radius: "))
		area = math.pi * radius**2
		print("Area =", area)
	except:
		print("You did not enter a number")

if __name__ == "__main__":
	Main()
