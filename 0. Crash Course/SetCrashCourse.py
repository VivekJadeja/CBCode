even_num_set = set()
even_num_set.add(2) # O(1)
even_num_set.add(4) # O(1)
odd_num_set = set()
odd_num_set.add(1) # O(1)
odd_num_set.add(3) # O(1)

3 in even_num_set # False in O(1) time.
2 in even_num_set # True in O(1) time.

# We can do set union as well in O(m+n) time.
union_num_set = even_num_set.union(odd_num_set) # (1,2,3,4)

# We can also do set intersection as well in O(m+n) time.
intersect_num_set = even_num_set.intersection(odd_num_set) # an empty set

# new set with elements in union_nums but not in even_num_set
difference_set = union_num_set.difference(even_num_set) # (1,3)
print(difference_set)
difference_set = even_num_set.difference(odd_num_set) # (1,3)
print(difference_set)
