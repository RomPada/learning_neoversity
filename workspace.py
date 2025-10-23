def format_string(string, length):
    l = len(string)
    if l >= length:
        return(string)
    else:
        gap = (length - len(string)) // 2
        string_gap = " " * gap
        string = string_gap + string
        return(string)


        