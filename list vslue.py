# Write a function to find Duplicate values in the List.
list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
 
uniqueList = []
duplicateList = []
 
for i in list:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)
 
print(list)
print(duplicateList)