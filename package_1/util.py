'''
    Author: Gautam Gadipudi
'''
from sys import argv


def get_file_name() -> str:
    '''
        Get name of file from command line argument or as user input
    '''
    file_name = ''
    if len(argv) == 2:
        file_name = argv[1]
    else:
        file_name = input("Please enter the file path: ")
    return file_name 


def read_file(file: str) -> list:
    '''
        Read file and return it's content.
    '''
    try:
        with open(file, "r", encoding="utf-8") as f:
            result = f.read()
            return result
    except IOError as e:
        print(f"Unable to read file {file}")
    finally:
        f.close()