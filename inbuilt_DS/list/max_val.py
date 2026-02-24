#find the maximum value of the list without using built in function
def find_max_element(lst):
    max_lst=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>max_lst:
            max_lst=lst[i]
        else:
            continue 
    return max_lst
lst=eval(input("Enter the list:"))
print(find_max_element(lst))
