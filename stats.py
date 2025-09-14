def get_num_words(book_string):
    book_list = book_string.split()
    return len(book_list)

def get_num_chars(book_string):
    characters = {}
    char_list = []
    for word in book_string:
        for char in word:
            char = char.lower()
            if char not in characters:
                characters[char] = 1
            else:
                characters[char] += 1

    for character in characters:
        char_dict = {}
        char_dict["char"] = character
        char_dict["num"] = characters[character]
        char_list.append(char_dict)

    char_list.sort(reverse=True, key=sort_char_counts_on)
    return char_list


def sort_char_counts_on(char_dict):
    return char_dict["num"]
