from stats import get_characters_counts
from stats import get_num_words


def get_book_text(path_to_file) :
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents # list


###################

def main() :
    text = get_book_text("/Users/matthieubuy/bookbot/bookbot/books/frankenstein.txt")
    num_words = get_num_words(text) # type: ignore
    characters = get_characters_counts(text)
    print(f"{num_words} words found in the document")
    print(characters)

main()

