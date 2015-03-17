#!/usr/bin/python3
import math

class Vector2D:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Vector2D(self.x + other.x, self.y + other.y)

	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		return self

	def __sub__(self, other):
		return Vector2D(self.x - other.x, self.y - other.y)

	def __isub__(self, other):
		self.x -= other.x
		self.y -= other.y
		return self

	def __mul__(self, other):
		return Vector2D(self.x * other.x, self.y * other.y)

	def __imul__(self, other):
		self.x *= other.x
		self.y *= other.y
		return self

	def __div__(self, other):
		return Vector2D(self.x / other.x, self.y / other.y)

	def __idiv__(self, other):
		self.x /= other.x
		self.y /= other.y
		return self

	def get_length(self):
		return math.sqrt(self.y**2 + self.x**2)
	
	def get_angle_degree(self):
		return self.get_angle_radian() / (math.pi / 180)
	
	def get_angle_radian(self):
		return math.atan2(self.y, self.x)
	
	def normalise(self):
		length = self.get_length()
		if length != 0:
			return Vector2D(self.x/length, self.y/length)
		return Vector2D(self)

	def __str__(self):
		return "X: " + str(self.x) + ", Y: " + str(self.y)
def Main():
	vec = Vector2D(5, 6)
	vec2 = Vector2D(2, 3)
	print(vec)
	print(vec2)
	temp_method = vec.get_angle_degree
	vec = vec + vec2

	print(vec)
	print(vec2)

	#temp_method = vec.get_angle_degree

	vec += vec2

	print(vec)
	print(vec2)

	vec *= Vector2D(2,2)

	print(vec)
	print(vec2)


	print(vec.normalise())
	print(vec.get_angle_degree())

	print(temp_method())
if __name__ == "__main__":
	Main()
