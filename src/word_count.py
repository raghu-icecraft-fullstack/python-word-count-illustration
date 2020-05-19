from input import read_file
from util import get_word_count, get_file_name
from output import print_output

def main():
    file_path = get_file_name()
    file_content = read_file(file_path)
    if file_content:
        word_count = get_word_count(file_content)
        print_output(word_count)

if __name__ == "__main__":
    main()