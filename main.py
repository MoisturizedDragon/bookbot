def words_in_text(input):
    words = input.split()
    return len(words) 

def count_characters(input):
    lowercase_string = input.lower()
    character_dict = {}
    for character in lowercase_string:
        if character in character_dict and character.isalpha():
            character_dict[character] += 1
        elif character not in character_dict and character.isalpha():
            character_dict[character] = 1 
    return character_dict

def print_report(file_path, input):
    print(f"--- Begin report of {file_path} ---")
    print(f"There are {words_in_text(input)} words in this text.\n")
    char_dict = count_characters(input)
    sorted_char_list = sorted(char_dict.items(), reverse=True, key=lambda item: item[1])
    for char, count in sorted_char_list:
        print(f"The '{char}' character was found {count} times.")
    print("--- End report ---")
        
def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()

    print_report(file_path, file_contents)

main()
