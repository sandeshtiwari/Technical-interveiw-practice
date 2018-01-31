# Function to check if string2 is an anagram of string1
def check_anagram(string1, string2):
    string1 = list(string1)
    # Sorting string1 to compare - O(n*log(n))
    string1.sort()
    return string1 == string2
