# https://www.youtube.com/watch?v=kT_VabdscHk&index=4&list=PLeIMaH7i8JDj7DnmO7lll97P1yZjMCpgY
# Given n keys, count number of possible BSTs that can be formed.
# User Dynamic Programming 
# Solution:

def count_possible_bst(keys):
  # only one bst can be formed
  # if len(keys) <= 1 
	N = [1, 1]
	if len(keys) <= 1:
		return 1
  
	for i in range(2, len(keys)+1):
		N.append(0)
		for j in range(0, i):
			N[i] += N[j] * N[i-j-1]
   
	return N[len(keys)]

if __name__ == "__main__":
	keys = [1, 2, 3, 4]
	print(count_possible_bst(keys))


