#calculate the sum of the elements of a list
def sum_list(numbers):
    
    sum=0
    for i in numbers:
        sum+=i 
    return sum
numbers=eval(input("Enter a list:"))
print(sum_list(numbers))
