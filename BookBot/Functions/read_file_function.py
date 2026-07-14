import sys

from stats import count_words, letter_stats, chars_dict_to_sorted_list 

def print_report(filepath, num_words, sorted_stats):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------------ Character Count ----------")
    for kp in sorted_stats:
        if kp[0].isalpha():
            print(f"{kp[0]}: {kp[1]}")
    print("============= END ===============")

def get_book_text(filepath:str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <file_to_path>")
        sys.exit(1)
    filepath = sys.argv[1] 
    file_content = get_book_text(filepath)
    num_words = count_words(file_content)
    stats = letter_stats(file_content)
    sorted_stats = chars_dict_to_sorted_list (stats)
    # print(stats)
    # print(file_content)
    # print(sorted_stats)
    print_report(filepath, num_words, sorted_stats)


main()
"""
import sys

def get_book_text(filepath:str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    filepath = sys.argv[1]
    result = get_book_text(filepath)
    print(result)

main()
"""