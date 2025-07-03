import sys
from stats import word_count, character_count, sort_character_counts

def get_book_text(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    word_c = word_count(get_book_text(file))
    chars_c = sort_character_counts(character_count(get_book_text(file)))
    print(f"""
          ============ BOOKBOT ============\n
          Analyzing book found at {file}...\n
          ----------- Word Count ----------\n
          Found {word_c} total words\n
          --------- Character Count -------
          """)
    for char in chars_c:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()