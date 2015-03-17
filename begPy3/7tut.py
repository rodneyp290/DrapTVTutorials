#!/usr/bin/python3
def Main():
	f = open("myFile.txt", "r")
	for line in f:
		print(line.strip("\r\n"))
	f.close()
	with open("myFile.txt", "w") as f:
		for i in range(4):
			f.write(input("Please enter a word: ") + "\r\n")

if __name__ == "__main__":
	Main()
