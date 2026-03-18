
# def searchValue(target):
#     for i in range(len(mylist)):
#         if mylist[i] == target:
#             return i
#         return -1
    
# mylist = [4,2,7,8,5,4,1]
# target = 9
# res = searchValue(target)
# print("The target is at index:", res)

def searchValue(mylist):
    sum =0
    for i in range(len(mylist)):
        sum = sum + mylist[i]
    return sum
    
mylist = [4,2,7,8,5,4,1]
res = searchValue(mylist)
print("The sum of the list is:", res)