#to remove duplicates from a list
def remove_duplicates(lst):
    lst1=[]
    for i in lst:
        if i in lst1:
            continue 
        else :
            lst1.append(i)
    return lst1 
lst=eval(input("Enter a list:"))
print(remove_duplicates(lst))
