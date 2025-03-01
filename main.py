import sys
from stats import get_word_count
from stats import get_text_count
from stats import sort_text_count

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        fileContents = f.read()
    return fileContents

def main():
  if len(sys.argv) <= 1:
    print("Usage: python script.py <book_location>")
    sys.exit(1)
  book_location =  sys.argv[1]#'books/frankenstein.txt'
  book = (get_book_text(book_location))
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_location}")
  print("----------- Word Count ----------")
  print(f'Found {get_word_count(book)} total words')
  print("--------- Character Count -------")
  char_counts = get_text_count(book)
  for char, count in char_counts:
    if char.isalpha():
       print(f"{char}: {count}")


main()