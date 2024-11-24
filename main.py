def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    total_word_counts = count_words(text)
    # print(f"The Frankenstein book contain {total_word_counts} words!")
    
    get_count_characters = count_characters(text)
    sorted_char_counts = sort_characters(get_count_characters)
    # print(sorted_char_counts)
    print_report(book_path, total_word_counts, sorted_char_counts)



def get_book_text(path):
    try: 
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file at path '{path}' was not found.")
    
def count_words(text):
    words = text.split()
    total_word_counts = len(words)
    return total_word_counts

def count_characters(text):
    char_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_characters(get_count_characters):
    # Convert the dictionary to a list of tuples and sort it
    sorted_chars = sorted(get_count_characters.items(), key=lambda item: item[1], reverse=True)
    return sorted_chars

def print_report(book_path, total_word_counts, sorted_char_counts):
    print(f"--- Begin report of {book_path} ---")
    print(f"{total_word_counts} words found in the document\n")
    
    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
    
    
    

    
if __name__ == "__main__":
    main()



    