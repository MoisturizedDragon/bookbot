def words_in_text(input):
    words = input.split()
    return len(words) 

def count_characters(input):
    lowercase_string = input.lower()
    character_dict = {}
    for character in lowercase_string:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 0 
    return character_dict

def pretty_print_dict(input):
    for key in input:
        value = input[key]
        print(f"The character {key} appeared {value} times.")
        
def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()

    print(f"There are {words_in_text(file_contents)} words in this document.") 
    pretty_print_dict(count_characters(file_contents))

main()
