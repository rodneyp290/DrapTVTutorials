#!/usr/bin/python3
# import vector2d 
# below means you don't have to specify the package as you would if you useed the above
# wildcard (*) can be used to import  everything instead of something specific
from vector2d import Vector2D 

def Main():
	# if using "import vector2d"
	# vec1 = vector2d.Vector2D(5, 6)
	vec1 = Vector2D(5, 6)
	vec2 = Vector2D(1, 1)

	print(vec1)
	print(vec2)

if __name__ == "__main__":
	Main()
