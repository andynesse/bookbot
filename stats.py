def word_count(txt):
    return len(txt.split())

def character_count(txt):
    txt.strip()
    txt = txt.lower()
    chars_counts = {}
    for char in txt:
        if not char in chars_counts:
            chars_counts[char] = 0
        chars_counts[char] += 1
    return chars_counts

def sort_character_counts(char_counts):
    char_c_list = []
    for key in char_counts.keys():
        char_c_list.append({
            "char": key,
            "num": char_counts[key]
        })
    char_c_list.sort(reverse=True, key=lambda items: items["num"])
    return char_c_list
    