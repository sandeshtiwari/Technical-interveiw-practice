'''
Given two strings s and t, determine whether some anagram of t is a substring
of s. For example: if s = "udacity" and t = "ad", then the function returns
True. Your function definition should look like: question1(s, t) and return
a boolean True or False.
'''
# Function to check all the possible substrings of the original_string
def question1(original_string, check_string):
    check_string_len = len(check_string)
    original_string_len = len(original_string)
    # making a list of the check_string
    sorted_check_string = list(check_string)
    # Using Quick sort to sort the string - O(n*log(n))
    sorted_check_string.sort()
    for i in range(original_string_len - check_string_len + 1):
        if check_anagram(original_string[i: i+check_string_len], sorted_check_string):
            return True
    return False

# Function to check if string2 is an anagram of string1
def check_anagram(string1, string2):
    string1 = list(string1)
    # Sorting string1 to compare - O(n*log(n))
    string1.sort()
    return string1 == string2
x = question1("udacity", "wxyzabc")
# x = False
print (x)
y = question1("udacity", "da")
# y = True
print (y)
z = question1("udacity", "")
# z = True
print (z)
