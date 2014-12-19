import sys

answer_set = {0:1}
composition = (1, 3, 5)
def number_of_composition(n):
	if n < 0:
		return 0
	elif n in answer_set.keys():
		return answer_set[n]

	d = sum(number_of_composition(n-i) for i in composition)
	answer_set.update({n:d})
	return d

for i in range(1, int(sys.argv[1])+1):
	print i, ":", number_of_composition(i)
