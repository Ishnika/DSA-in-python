#rotate the list (A rotation shifts elements from the end of the list to the front.)
def rotate_list(lst, k):
    if len(lst)<2:
        return lst
    else:
        while(k>0):
            ind=lst[len(lst)-1]
            lst.pop()
            lst.insert(0,ind)
            k-=1 
        return lst 
lst=eval(input("Enter the list:"))
k=int(input("Enter the number of shifts:"))
print(rotate_list(lst, k))
