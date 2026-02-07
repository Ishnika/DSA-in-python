#compare two strings without using any built in function to compare
def are_equal_strings(s, t):
    if len(s)!=len(t):
        return False 
    else:
        flag=1
        for i,j in zip(s,t) :
            if i == j:
                continue
            else :
                flag=0
                break
        if flag==0:
            return False 
        else:
            return True
s=input("Enter the first string:")
t=input("Enter the second string:")
print(are_equal_strings(s, t))
