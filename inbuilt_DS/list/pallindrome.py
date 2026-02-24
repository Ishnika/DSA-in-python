#check if the list is a pallindrome or not 
def is_palindrome(lst):
    if lst==lst[::-1]:
        return True 
    else:
        return False 
lst=eval(input("Enter the list:"))
print(is_palindrome(lst))
