def get_num_words(book_contents: str) -> int:
    return len(book_contents.split())


def get_num_chars(book_contents: str) -> dict[str, int]:
    num_chars = {}

    for char in book_contents:
        char_lower = char.lower()
        if char_lower not in num_chars:
            num_chars[char_lower] = 1
        else:
            num_chars[char_lower] += 1

    return num_chars


def sort_on(num_char: tuple[str, int]) -> int:
    return num_char[1]


def chars_dict_to_sorted_list(num_chars: dict[str, int]) -> list[tuple[str, int]]:
    num_chars_sorted = []
    for char, num in num_chars.items():
        num_chars_sorted.append((char, num))
    return sorted(num_chars_sorted, reverse=True, key=sort_on)
