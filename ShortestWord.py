def find_short(s):
    i = 0
    len_word_s = 100000000
    list_s = s.split(" ")
    len_list_s = len(list_s)
    while i < len_list_s:
        if len_word_s > len(list_s[i]):
            len_word_s = len(list_s[i])
            print(len_word_s)
            i = i + 1
        else:
            i = i + 1
    return len_word_s
