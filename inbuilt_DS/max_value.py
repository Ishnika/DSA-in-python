#calculate the maximum value in the list
def find_largest(numbers):
    max_num=numbers[0]
    for i in numbers:
        if i>max_num:
            max_num=i 
    return max_num
numbers=eval(input("Enter the list:"))
print(find_largest(numbers))
