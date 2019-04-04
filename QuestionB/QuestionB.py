"""

Question B

The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. 
As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

"""

"""
idea
the version may be 1.0.01,1.0.a1,1.abc.1
spilit from left to right one by one , each spilit we do comparison, then iterate the comparsion 

"""


def versions(version1, version2):
	global string1
	global string2
	string1 = version1
	string2 = version2
	return versionCompare( version1, version2)

def versionCompare( version1, version2):

	if version1 == version2:
		return "{} is euqal to {}".format(string1, string2)

	digit1 = version1.find('.')
	digit2 = version2.find('.')

	part1 = version1[0:digit1] if digit1 != -1 else version1
	part2 = version2[0:digit2] if digit2 != -1 else version2

	if int(part1) == int(part2):
		rest1 = version1[len(part1)+1:] if version1[len(part1)+1:] != '' else '0'
		rest2 = version2[len(part2)+1:] if version2[len(part2)+1:] != '' else '0'
		return versionCompare(rest1,rest2)
	else:
		if int(part1) > int(part2):
			return "{} is greater than {}".format(string1, string2)
		else:
			return "{} is less than {}".format(string1, string2)
