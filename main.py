with open("books/frankenstein.txt") as f:
    file_contents = f.read()
# prints entire novel
def word_count(words):
    words_list = words.split()
    word_count = len(words_list)
    return word_count
#returns word count
word_count(file_contents)

def character_count(count):
    characters = {}
    for char in count:
        char =char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters
char_counts = character_count(file_contents)
# creates a dictionary of each individual character

def sort_on(characters):
    return characters["num"]

sorted_chars = []
for char, count in char_counts.items():
    char_dict = {"name": char, "num": count}
    sorted_chars.append(char_dict)
sorted_chars.sort(reverse=True, key=sort_on)
word_count_variable = word_count(file_contents)
print( "--- Begin report of books/frankenstein.txt ---")
print(f"{word_count_variable} words found in the document\n")

for char_dict in sorted_chars:
    if char_dict['name'].isalpha():
        print(f"The '{char_dict['name']}' character was found {char_dict['num']} times")

print ("--- End report ---")
