# function to check if the given string is palindrome or not
def is_palindrome(string):
    if string == None:
        return False
    # reversing the string to compare
    return string == string[::-1]

# function to find the longest palindromic string
def question2(string):
    if string == None:
        return ""
    n = len(string)
    longest = 0
    left_index = 0
    right_index = 0
    for i in range(0, n):
        for j in range(i + 1, n + 1):
            check_str = string[i:j]
            if is_palindrome(check_str) and len(check_str) > longest:
                longest = len(check_str)
                left_index = i
                right_index = j
    longest_pal = string[left_index:right_index]
    return longest_pal

longest = question2("Some one call my dad in malayalam")
# malayalam
print (longest)
longest = question2(None)
# 
print (longest)
longest = question2("")
# 
print(longest)
