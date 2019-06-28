import math


def addVectors(vector1,vector2):
	'''simple vector addition'''
	x = vector1[0] + vector2[0]
	y = vector1[1] + vector2[1]
	return (x, y)


def subtractVectors(vector1,vector2):
	'''simple vector addition'''
	x = vector1[0] - vector2[0]
	y = vector1[1] - vector2[1]
	return (x, y)

def convertVector(vector):
	'''convert from angel vector to normal vector(first number is length, second is angel)'''
	x = vector[0] * math.cos(vector[1])
	y = vector[0] * math.sin(vector[1])
	return (x,y)

def NtimesVector(vector, n):
	x = vector[0] * n
	y = vector[1] * n
	return (x,y)

def VectorLength(vector):
	return math.sqrt((vector[0]**2) + (vector[1]**2))

def unitVector(vector):
	length = VectorLength(vector)
	x = vector[0] / length
	y = vector[1] / length
	return (x,y)


def dot(vector1, vector2):
	return (vector1[0] * vector2[0]) + (vector1[1] * vector2[1])


def det(vector1, vector2):
	return (vector1[0] * vector2[1]) - (vector1[1] * vector2[0]) 

def hat(vector):
	x = -vector[1]
	y = vector[0]
	return (x,y)

def isParal(vector1, vector2):
	if det(vector1, vector2) == 0:
		return True
	else:
		return False

def isOrtogonal(vector1, vector2):
	if dot(vector1, vector2) == 0:
		return True
	else:
		return False

def findAngle(vector1, vector2):
	v = math.acos(dot(vector1, vector2) / (VectorLength(vector1) * VectorLength(vector2)))
	return math.degrees(v)  

def proj(vector1, vector2):
	a = dot(vector1, vector2)
	n = (a /  ((vector2[0]**2) + (vector2[1]**2)))
	return NtimesVector(vector2, n)

def projLength(vector1, vector2):
	return (abs(dot(vector1, vector2)) / VectorLength(vector2))


def paraAreal(vector1, vector2):
	return abs(det(vector1, vector2))

def trekantAreal(vector1, vector2):
	return .5 * paraAreal(vector1, vector2)


