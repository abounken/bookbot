from stats import get_word_count
from stats import get_text_count

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        fileContents = f.read()
    return fileContents

def main():
  book = (get_book_text('./books/frankenstein.txt'))
  print(f'{get_word_count(book)} words found in the document')
  print(f'{get_text_count(book)}')

main()