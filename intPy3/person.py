#!/usr/bin/python3
class Person:
	age = 0
	name = "noname"
	friends = []

	def __init__(self):
		self.friends = []

	def addFriend(self, friend):
		self.friends.append(friend)
		print(friend.name, "added to", self.name, "friend list")

	def string(self):
		string = "Name: " + self.name + "\tAge: " + str(self.age) + "\n"
		string += "Friends:\n"
		for friend in self.friends:
			string += "\t" + friend.friendlessString() + "\n"
		string += "favourite colour: " + self.colour + "\n"
		return string
	def friendlessString(self):
		string = "Name: " + self.name + "\tAge: " + str(self.age)
		return string
		
	

def Main():
	me = Person()
	me.age = 21
	me.name = "Carl"
	me.colour = "Blue"
	print(me.colour)

	friend = Person()
	friend.age = 21
	friend.name = "Brian"

	other_friend = Person()
	other_friend.name = "Henry"
	other_friend.age = 22
	print(me.string())
	empty = Person()

	people = { me, friend, other_friend, empty }

	for person in people:
		print(person.string())

	me.addFriend(friend)
	me.addFriend(other_friend)

	friend.addFriend(me)
	friend.addFriend(other_friend)

	other_friend.addFriend(friend)
	other_friend.addFriend(me)

	for person in people:
		print(person.string())


if __name__ == "__main__":
	Main()
