'''
    Author: Gautam Gadipudi
'''
from lib.classes import WordCounter
from lib.util import get_file_name

def main():
    '''
        Driver(main) method
    '''
    try:
        file_path = get_file_name()
        word_counter = WordCounter(file_path)
        word_counter.print_count()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()