import sys
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

from stats import get_num_words
from stats import get_num_character
from stats import sort_for_report

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        num_words = get_num_words(get_book_text(sys.argv[1]))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        num_character_dict = get_num_character(get_book_text(sys.argv[1]))
        sorted_dict = sort_for_report(num_character_dict)
        print("--------- Character Count -------")
        for char_dict in sorted_dict:
            char = char_dict["char"]
            if char.isalpha():
                print(f"{char}: {char_dict['count']}")
        print("============= END ===============")


main()
