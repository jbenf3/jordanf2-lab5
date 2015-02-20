"""This file implements several buggy functions such that you can practice your pdb skills on them."""

import sys



def main():
	"""main currently does nothing. Implement calls to the buggy functions for debugging purposes."""
	pass


def mean(it):
	"""This function takes an iterable containing numbers and computes the mean of those numbers. It currently does not work correctly. Where is the bug?"""
	sum = 0
	for num in it:
		sum += num
	sum = sum / len(it)
	return sum


def find_range(list):
	"""This function finds the range spanned by a list and returns a tuple containing the low and high values. It currently doesn't work correctly. """
	sorted(list)
	high = list[len(list)-1]
	low = list[0]
	return low,high


def concat_and_diff(list1,list2):
	"""This function concatenates two lists and produces a list of differences. It currently doesn't work correctly."""
	l = []
	l.extend(list1)
	l.extend(list2)
	diff = []
	print l
	for i in range(len(l)):
		diff.append(l[i] - l[i-1] )
	print diff

def is_prime():
	"""This function checks whether a command line argument is a prime number. It currently doesn't work correctly."""

	p = sys.argv[0]
	for i in range(p):
		if p % i == 0:
			return False
	return True	

main()
