import sys
from stats import count_words
from stats import character_counter
from stats import dict_sorter

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

bookpath = str(sys.argv[1])


def get_book_text(bookpath):
    with open(bookpath) as f:
        file_contents = f.read()
        return str(file_contents)


def main():
    book_text = get_book_text(bookpath)
    word_count = count_words(book_text)
    letter_count = character_counter(book_text)
    sorted_letter_count = dict_sorter(letter_count)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_letter_count:
        for char, count in char_dict.items():
            print(f"{char}: {count}")


main()