swapActive = True
list = [10, 30, 3, 9, 21, 11 ,8]
print("Unsorted List: ",list)
#
#
#
while swapActive == True:
    swapActive = False
    for i in range(0, (len(list)-1)):
        if list [i] > list [i+1]:
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
            swapActive = True

print("Sorted List: ",list)