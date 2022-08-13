'''
Given a non-empty list of integers, 
every element appears twice except for one. 
Find that single one.
'''

def return_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    return list(set1.intersection(set2))

def return_lone(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    dups = return_intersection(list1, list2)
    lone_list = []

    for i in list1:
        iIsDuplicate = False
        for j in list2:
            if i is j:
                jIsDuplicate = True
                lone_list.remove(j)
                break
                

        if i is j:
            iIsDuplicate = True
            lone_list.remove(i)
            break
            
            
        
    # lone_list = [value for value in list1 if value is not in list2]

    return lone_list
    

list1 = [2, 1, 4, 3, 6, 5, 7, 8]
list2 = [1, 2, 3, 4, 7, 5, 8]
new_list = return_intersection(list1, list2)

return_lone(list1, list2)


print(new_list)
print(return_lone(list1, list2))