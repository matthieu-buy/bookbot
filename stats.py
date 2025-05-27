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




