def reverse(str):
    new_str = ""

    for i in range(1, len(str)+1):
        new_str += str[-i]

    return new_str


def isPalindrome(str):
    str = str.lower()   #it also works with uppercase letters
    if reverse(str) == str:
        return True
    else:
        return False
    

print(isPalindrome("Abba"))