def get_word_count(book_output):
    word_count = book_output.split()
    return len(word_count)

def get_text_count(book_output):
    characters = {}
    for char in book_output.lower():
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return sort_text_count(characters)

def sort_text_count(characters):
    char_list = list(characters.items())
    sorted_chars = sorted(char_list, key=lambda item: item[1], reverse=True)
    return sorted_chars