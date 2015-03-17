#!/usr/bin/python3
def getInteger(prompt):
	return int(input(prompt))
def Main():
	print("started")
	output = getInteger("Please enter an integer: ")
	output2 = getInteger("Please enter another integer: ")
	print(output)

if __name__ == "__main__":
	Main()
	


