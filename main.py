from stats import word_count, character_count

def get_book_text(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()

def main():
    file = "books/frankenstein.txt"
    word_c = word_count(get_book_text(file))
    chars_c = character_count(get_book_text(file))
    print(word_c, "words found in the document")
    print(chars_c)

main()