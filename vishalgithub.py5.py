nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
length = len(nested_list)
print("Length of nested_list:", length)
list1 = [10, 20, 30]
list2 = [40, 50, 60]
concatenated = list1 + list2
print("Concatenated list:", concatenated)
item = 20
print(f"Is {item} in list1?", item in list1)
print("Iterating over list2:")
for element in list2:
    print(element, end=" ")
print()
print("First element of list1:", list1[0])
print("Last element of list2:", list2[-1])
print("Slicing list1 from index 1 to 3:", list1[1:3])
print("Slicing nested_list first two sublists:", nested_list[:2])
print("Accessing element 5 inside nested_list:", nested_list[1][1])  # second list, second element
