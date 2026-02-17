#to return the maximum difference of two consecutive numbers 
import math
def max_consecutive_difference(lst):
    if len(lst)<2:
        return 0
    else:
        max_diff=abs(lst[0]-lst[1])
        for i in range(1,len(lst)-1):
            if abs(lst[i]-lst[i+1])>max_diff:
                max_diff=abs(lst[i]-lst[i+1])
        return max_diff
lst=eval(input("Enter the list:"))       
print(max_consecutive_difference(lst))
        
