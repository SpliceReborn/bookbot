def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_lower = text.lower()
    num_words = get_num_words(text)
    char_count = get_char_count(text_lower)
    char_list = get_char_list(text_lower)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for char in char_list:
        print(f"The '{char}' character was found {char_count[char]} times")
    print("--- End report ---")

def get_char_list(text):
    myList = []
    for char in text:
        if char.isalpha() and char not in myList:
            myList.append(char)
    myList.sort()
    return myList

def get_char_count(text):
    myDict = dict()
    for char in text:
        if char in myDict:
            myDict[char] += 1
        else:
            myDict[char] = 1    
    return myDict

def get_num_words(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

