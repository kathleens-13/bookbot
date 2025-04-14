def get_num_words(book_as_string):
    list_words = book_as_string.split()
    total_words = len(list_words)
    return total_words

# get_num_character changes book_as_string into dictionary Letter : count
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

def sort_for_report(char_dict):
    #first change char_dict into dictionary w/two key-value pairs
    result_list=[]
    for character, count in char_dict.items():
        #create new dictionary for each character with 'char' and 'count' keys
        new_char_dict = {"char": character, "count": count}
        result_list.append(new_char_dict)
    #create function to tell sort which key to use
    def sort_using(dict_item):
        return dict_item["count"]
    #sort the list in place
    result_list.sort(reverse=True, key=sort_using)
    return result_list