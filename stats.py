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
