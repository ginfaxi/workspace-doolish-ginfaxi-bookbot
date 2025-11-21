import sys
from stats import *

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

def main():
    # check if valid argument for book path
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    txt = get_book_text(book_path)
    word_count = get_num_words(txt)
    character_count = get_num_characters(txt)
    character_count_report = create_dictionary_list(txt)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in character_count_report:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()
