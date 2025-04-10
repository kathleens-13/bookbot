def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

from stats import get_num_words
from stats import get_num_character

def main():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    num_character_dict = get_num_character(get_book_text("books/frankenstein.txt"))
    print(num_character_dict)


main()
