#linear search 
def linear_search(arr, target):
    for i in range(0,len(arr)):
        if arr[i] == target:
            return i
    return -1
lst=eval(input("Enter the list:"))
target=int(input("Enter the target value:"))
print(linear_search(lst , target))
