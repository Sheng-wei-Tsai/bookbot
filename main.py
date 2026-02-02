import sys
from stats import get_num_words



def main():
    if(len(sys.argv) != 2):
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    total_word_counts = get_num_words(text)
    print(f"Found {total_word_counts} total words")

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
        sys.exit(1)


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
        print(f"{char}: {count}")
    print("--- End report ---")





if __name__ == "__main__":
    main()



