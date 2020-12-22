def get_count(input_str):
    num_vowels = 0
    i = 0
    vowels = ["a","e","i","o","u"]
    len_input_str = len(input_str)
    while i < len_input_str:
        validation = input_str[i] in vowels
        if validation == True:
            num_vowels = num_vowels + 1
            i = i + 1
        else:
            i = i + 1       
        
    return num_vowels
