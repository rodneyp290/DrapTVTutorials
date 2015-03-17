#!/usr/bin/python3
def Main():
	for step in range(5):
		print(step)
	words = ["cat", "bat", "hat", "rat", "sat"]
	for word in words:
		print(word)
	services = { "ssh":22, "http":80, "telnet":23 }
	for key in services:
		print(key, ":", services[key])
	num = 0
	while num <= 0:
		num = int(input("Please enter a positive number:"))
	while True:
		print("HAHAHAHAHAHAHAAAAAAAA!")

if __name__ == "__main__":
	Main()
