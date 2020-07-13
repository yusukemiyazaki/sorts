
# https://en.wikipedia.org/wiki/Bubble_sort
# https://ja.wikipedia.org/wiki/%E3%83%90%E3%83%96%E3%83%AB%E3%82%BD%E3%83%BC%E3%83%88
def bubble_sort(collection):
	
	for i in range(len(collection) - 1):
		could_swap = False
		
		for j in range(len(collection) - 1 - i):
			if collection[j] > collection[j + 1]:
				could_swap = True
				collection[j], collection[j + 1] = collection[j + 1], collection[j]
		
		if not could_swap:
			break
	
	return collection

if __name__ == "__main__":
	assert bubble_sort([0, -8, 3, 3, 2]) == [-8, 0, 2, 3, 3]
	assert bubble_sort([8, 4, 6, 3, 7, 1]) == [1, 3, 4, 6, 7, 8]
			
	
	
	
	
