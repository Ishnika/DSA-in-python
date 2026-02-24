"""You are given a sorted array of characters letters, sorted in non-decreasing order, and a character target. 
There are at least two different characters in letters. Your task is to return the smallest character in letters 
that is lexicographically greater than target. If such a character does not exist, return the first character in 
letters"""
def next_greatest_letter(letters, target):
    flag=letters[0]
    for i in letters:
        if ord(target)<ord(i):
            flag=i
            break
    return flag
letters=eval(input("Enter the list of letters:"))
target=input("Enter the target letter:")
print(next_greatest_letter(letters, target))
