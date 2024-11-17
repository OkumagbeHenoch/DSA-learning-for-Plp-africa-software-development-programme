# 1.
my_list = []
# 2.


my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print (my_list)

# 3.
my_list[2] = 15
print(my_list)

# 4.

updated_list = [50, 60, 70]
my_list.extend(updated_list)

print(my_list)

# 5.
del my_list[6]
print(my_list)


# 6
my_list.sort()
print (my_list)

# 7.
index = my_list.index(60)
print(index)