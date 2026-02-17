#reverse a list without using slicing 
def reverse_list(lst):
    lst1=[]
    for i in range(len(lst)-1,-1,-1):
        lst1.append(lst[i])
    return lst1
lst=eval(input("Enter the list:"))
print(reverse_list(lst))
