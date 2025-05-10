def remove_substring(substring, string):

    if substring not in string:
        return string
    
    new_str = ""

    sub_len = len(substring)
    sub_start_index = string.index(substring)
    sub_final_index = (sub_start_index + sub_len)-1

    for i in range(len(string)):
        if not sub_start_index <= i <= sub_final_index:
            new_str += string[i]

    return new_str


def remove_all_substrings(substring, string):
    
    new_str = string

    while substring in new_str:
        new_str = remove_substring(substring, new_str)

    return new_str


print(remove_all_substrings("an", "banana"))