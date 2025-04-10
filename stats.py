def get_num_words(book_as_string):
    list_words = book_as_string.split()
    total_words = len(list_words)
    return total_words

def get_num_character(book_as_string):
    char_dict = {}
    char_make_lower = book_as_string.lower()
    char_all_lower_list = list(char_make_lower)
    for char in char_all_lower_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

