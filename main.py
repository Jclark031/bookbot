from stats import get_num_words, count_characters, char_sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)    
    else:    
        path = sys.argv[1]
        text = get_book_text(path)
        num_words = get_num_words(text)
        chars_dict = count_characters(text)
        char_sorted = char_sort(chars_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in char_sorted:
            if not item["char"].isalpha():
                continue
            print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()