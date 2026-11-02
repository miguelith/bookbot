import sys

from stats import chars_dict_to_sorted_list, get_num_chars, get_num_words


def get_book_txt(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def print_report(book_path: str, num_words: int, char_nums_list: list[tuple[str, int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, num in char_nums_list:
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_contents = get_book_txt(book_path)
    num_words = get_num_words(book_contents)
    char_nums_list = chars_dict_to_sorted_list(get_num_chars(book_contents))
    print_report(book_path, num_words, char_nums_list)


main()
