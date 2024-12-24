def words_in_text(input):
    words = input.split()
    return len(words) 
    
def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()

    print(f"There are {words_in_text(file_contents)} words in this document.") 

main()
