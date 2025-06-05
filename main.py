from stats import get_book_wordcount
from stats import count_characters
from stats import get_sorted_dicts
import sys 
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
    
    print("----------- Word Count ----------")
    num_words = get_book_wordcount(book_text)
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    character_dict=count_characters(book_text)
    sorted_dicts = get_sorted_dicts(character_dict)
    for dict in sorted_dicts:
        if dict["char"].isalpha(): 
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")







def get_book_text (filepath):
    with open(filepath) as f:
        #do things with f here
        #print("inside get_book_text")
        book_text = f.read()
        return book_text



main()