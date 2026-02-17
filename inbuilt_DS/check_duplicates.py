#return true if no duplicates and false if duplicates occur 
def check_unique(lst):
    flag=1
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]==lst[j]:
                flag=0
                break
    if flag:
        return True 
    else:
        return False 
lst=eval(input("Enter the list:"))
print(check_unique(lst))
