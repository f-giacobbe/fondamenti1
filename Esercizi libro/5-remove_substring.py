def remove_substring_v0(substring, string):

    if substring not in string:
        return string

    new_str = ""

    sub_len = len(substring)
    sub_index = string.index(substring)
    sub_last_index = (sub_index + sub_len)-1

    for letter_i in range(len(string)):
        if (letter_i == sub_index) and (sub_index <= sub_last_index):
            sub_index += 1
            continue
        else:
            new_str += string[letter_i]

    return new_str


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


print(remove_substring("cl", "bicycle"))