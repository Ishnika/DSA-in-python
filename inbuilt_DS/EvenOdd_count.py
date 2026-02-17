#to count and return the number of even and odd numebers in a list
def count_even_odd(lst):
    count_odd=0
    count_even=0
    for i in lst:
        if i%2==0:
            count_even+=1 
        else:
            count_odd+=1 
    return (count_even,count_odd)
lst=eval(input("Enter the list:"))
print(count_even_odd(lst))
