
# https://en.wikipedia.org/wiki/Bead_sort
# https://ja.wikipedia.org/wiki/%E3%83%93%E3%83%BC%E3%82%BA%E3%82%BD%E3%83%BC%E3%83%88
def bead_sort(sequence: list) -> list:
	
	if any(not isinstance(x, int) or x < 0 for x in sequence): 
		raise TypeError("Sequence must be a list of non-negative integers")
	
	for _ in range(len(sequence)):
		for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
			if rod_upper > rod_lower:
				sequence[i] -= rod_upper - rod_lower
				sequence[i + 1] += rod_upper - rod_lower
	
	return sequence

if __name__ == "__main__":
	assert bead_sort([7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7]
	assert bead_sort([8,4,6,3,7,1]) == [1,3,4,6,7,8]
			
	
	
	
	
