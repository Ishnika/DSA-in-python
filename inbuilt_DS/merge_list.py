#merge two sorted list and the final list should be sorted in non-descending order
def merge_two_sorted_lists(list1, list2):
    lst_final=list1+list2 
    lst_final.sort()
    return lst_final
list1=eval(input("Enter the 1st list:"))
list2=eval(input("Enter the 2nd list:"))
print(merge_two_sorted_lists(list1, list2))
