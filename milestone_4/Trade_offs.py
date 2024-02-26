from typing import List, Tuple

def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    all_pair_index = set()
    for a in li:
        for b in li:
            if a < b and a + b == target:
               all_pair_index.add((li.index(a), li.index(b)))
               
    return all_pair_index

print(find_sum(5, [1, 2, 3, 4, 5]))# in {(0, 3), (1, 2)}

    # time complexity is O(n^2)
    # space complexity - out-of-space algorithm O(n) 
    #                   (we create only set f tuples and we don't know its size in advance)


# Second VERSION of find_sum_fast

def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
	numbers = {}
	pair_index = ()
	all_pair_index = set()
	for i in range(len(li)):
		if target - li[i] in numbers:
			pair_index = (li.index(target - li[i]), i,)
			all_pair_index.add(pair_index)
		numbers[li[i]] = i
	return all_pair_index

print(find_sum_fast(5, [1, 2, 3, 4, 5]))# in {(0, 3), (1, 2)}

    # time complexity is O(n)
    # space complexity - out-of-space algorithm  O(n+n) -> O (n) 
    #                   (we create dict, set of tuples)