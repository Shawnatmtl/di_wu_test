
""" 
Question A

Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. 
As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

"""

def ifOverlap(x1, x2, x3, x4):
	try:
		x = range(x1, x2)
		y = range(x3, x4)
		xs = set(x)
		if xs.intersection(y):
			return "Overlap!"
		else:
			return "Not overlap"
	except:
		print("Error")



print("Three possibilities, \n \
case A  X(1, 4) not overlap Y(5, 6) \n \
-------------------------------------------- \n \
    x1-----x2     x3-----x4")
print(ifOverlap(1,4,5,6))

print("case B X(1, 6) overlaps Y(2, 10) \n\
-------------------------------------------- \n \
    x1----x3======x2----x4")
print(ifOverlap(1,6,2,10))

print("case B X(x1, x2) inside Y(x3, x4) \n \
--------------------------------------------\n \
    x3-----x1======x2-----x4")
print(ifOverlap(1,10,2,6))