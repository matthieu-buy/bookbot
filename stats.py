def get_num_words(file_contents : list) :
    file_content_words = file_contents.split() # type: ignore
    
    return len(file_content_words) # integer


def get_characters_counts(file : str) :
    char_count = {}
    for char in file.lower() :
        if char in char_count :
            char_count[char] += 1
        else :
            char_count[char] = 1
    
    return char_count #dictionnary


def sort_on(dictionnary) :
    return dictionnary["num"]


def order_list_of_characters(dictionnary : dict) :
    list_char = []
    for char in dictionnary :
        char_dict = {"char": char, "num": dictionnary[char]}
        list_char.append(char_dict)
    list_char.sort(reverse=True, key=sort_on) # type: ignore
    return list_char


