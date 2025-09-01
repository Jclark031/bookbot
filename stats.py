def get_num_words(text: str):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

def count_characters(text: str):
    char_counts = {}
    lower = text.lower()
    for char in lower:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(dictionary_item):
    return dictionary_item["num"]

def char_sort(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list