from stats import get_characters_counts
from stats import get_num_words
from stats import order_list_of_characters
import sys



def get_book_text(path_to_file :str) :
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents # list


def print_report(book_path :str, num_words :int, characters_list :list) :
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("----------- Character Count ----------")
    for item in characters_list : #item is a dictionnary
        if item["char"].isalpha() :
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


###################

def main() :
    if len(sys.argv) < 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else :
        # book_path = "books/frankenstein.txt"
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        chars_dict = get_characters_counts(text)
        chars_sorted_list = order_list_of_characters(chars_dict)
        print_report(book_path, num_words, chars_sorted_list)



main()

