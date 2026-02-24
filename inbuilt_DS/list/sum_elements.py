#find the sum of all the elements in the list
def sum_of_elements(lst):
    sum_lst=0
    for i in lst:
        sum_lst+=i
    return sum_lst
lst=eval(input("Enter the list:"))
print(sum_of_elements(lst))
