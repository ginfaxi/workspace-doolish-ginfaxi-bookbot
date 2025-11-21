def get_num_words(text):
    text_list = text.split()
    words = len(text_list)
    return words

def get_num_characters(text):
    char_count = {}
    character_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    text_lower = text.lower()
    pure_text = [c for c in text_lower if not c.isspace()] # create list and omit whitespace
    
    # initialize dictionary without needing to type out everything
    for c in character_list:
        d = char_count["char"] = c
        char_count["num"] = 0

    # count characters
    for letter in pure_text:
        if letter in character_list:
            char_count["num"] += 1

    return char_count

def report_dictionaries(dictionaries):
    num = dictionaries.sort(reverse=True)
    return num

def create_dictionary_list(text):
    character_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "æ", "â", "ê", "ë", "ô"]
    dictionary_list = []
    text_lower = text.lower()
    pure_text = [c for c in text_lower if not c.isspace()] # create list and omit whitespace
    for c in character_list:
        d = {"char": c, "num": 0}
        dictionary_list.append(d)

    # count characters
    for letter in pure_text:
        for dict in dictionary_list:
            if dict["char"] == letter:
                dict["num"] += 1

    sorted_dictionaries = sort_dictionaries(dictionary_list)
    return sorted_dictionaries

def sort_dictionaries(dictionaries):
    dictionaries.sort(key=lambda d: d["num"], reverse=True)
    return dictionaries