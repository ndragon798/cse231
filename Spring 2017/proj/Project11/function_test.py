import proj11

fp = open('test1.txt')
M = proj11.Matrix()
M.read_file(fp)
print("Testing __str__ by calling __str__ through print():")
print(M)
print("Testing adjacent method:")
set_of_adjacent_rooms = M.adjacent(2)
print("rooms adjacent to room 2:",set_of_adjacent_rooms)
print("Testing rooms method:")
number_of_rooms = M.rooms()
print("number of rooms:",number_of_rooms)
