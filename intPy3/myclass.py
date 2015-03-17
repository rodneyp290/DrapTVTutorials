#!/usr/bin/python3
class MyClass:
	number = 0
	name = "noname"

def Main():
	me = MyClass()
	me.number = 6
	me.name = "Carl"

	friend = MyClass()
	friend.number = 7
	friend.name = "Brian"

	empty = MyClass()

	print("Name: " + me.name + ", Favourite Number: " + str(me.number))
	print("Name: " + friend.name + ", Favourite Number: " + str(friend.number))
	print("Name: " + empty.name + ", Favourite Number: " + str(empty.number))


if __name__ == "__main__":
	Main()
