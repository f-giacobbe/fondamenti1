my_text = "This is an example of a text containing a url http://www.mywebsite.net which will hopefully be extracted"


def url_extract(text):
    url = ""

    if "http://" not in text:
        return None
    
    url_start_index = text.index("http://")
    blank_after_url_index = (text[url_start_index:].index(" ") + url_start_index)

    for i in range(len(text)):
        if url_start_index <= i <= blank_after_url_index:
            url += text[i]

    return url


print(url_extract(my_text))