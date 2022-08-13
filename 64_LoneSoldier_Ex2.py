'''
Given a non-empty list of integers, 
every element appears twice except for one. 
Find that single one.
'''

# Odd number is 4
int_list = [1, 9, 2, 1, 3, 3, 4, 2, 9]
seen_list = set()
dups_list = []
unique = []
for i in int_list:
    if i in seen_list:
        dups_list.append(i)
    else:
        seen_list.add(i)

for i in int_list:
    if i not in dups_list:
        unique.append(i)


print(seen_list)
print(dups_list)
print(unique)

