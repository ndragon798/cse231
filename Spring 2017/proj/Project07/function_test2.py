from proj07 import num_in_common_between_lists

list1 = [0, 4, 6, 7, 9]
list2 = [0, 3, 6, 8, 9]

num_in_common = num_in_common_between_lists(list1, list2)
print("should be 3:",num_in_common)

list1 = [1, 4, 8]
list2 = [2, 3, 4, 6, 7]
num_in_common = num_in_common_between_lists(list1, list2)
print("should be 1:",num_in_common)