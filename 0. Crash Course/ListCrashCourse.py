my_list = []  # Initializes an empty list.
my_list.append(1)
print(my_list) # [1]
for i in range(0,6):
    my_list.append(i) # Each append takes O(1) time. Just like a stack.
print(my_list) # [1,0,1,2,3,4, 5]
print(len(my_list)) # 7

# You can pop from the end of the list in O(1) time.
last_element = my_list.pop()
print(last_element) # 5
print(my_list) # [1,0,1,2,3,4]

# You can also pop from the front, but be careful this is O(n) time worst case!
first_element = my_list.pop(0)

string_numbers = [str(x) for x in my_list]
print(string_numbers) # ["0", "1", "2", "3", "4"]

even_numbers = [x for x in my_list if (x % 2) == 0]
print(even_numbers) # [0, 2, 4]
print(my_list)

names = ["Sam", "Bob", "Ann"]
ages = [10, 8, 13]

# zip combines two parallel lists into a list of tuples.
names_and_ages = zip(names, ages)
print(list(names_and_ages)) # [("Sam", 10), ("Bob", 8), ("Ann", 13)]

row= 10
col = 5
matrix = [[0 for i in range(0, row)] for j in range(0,col)]
print(matrix)