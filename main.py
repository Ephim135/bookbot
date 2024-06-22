def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_characters(text)

    filtered_char_dict = filter_isalpha(char_dict)
    filtered_char_dict.sort(reverse=True, key=sort_on)
    print(filtered_char_dict)
    report(book_path, num_words, filtered_char_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_characters(text):
    character_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def report(book_path, num_words, filtered_char_dict):
    heading = f'--- Begin report of {book_path} ---\n{num_words} words found in the document\n\n'
    main = ''
    for obj in filtered_char_dict:
        main += f"The '{obj['letter']}' character was found {obj['amount']} times\n"

    end = "--- End Report ---"
    print(heading + main + end)
    #why do i get a white space in front of the line ' The 'e' character was found 46043 times' in tha output from this print statement

def filter_isalpha(char_dict):
    characters_array = []
    for key in char_dict:
        if key.isalpha():
            temp_dict = {'letter': key, 'amount': char_dict[key]}
            characters_array.append(temp_dict)
    return characters_array

def sort_on(dict):
    return dict["amount"]

main()