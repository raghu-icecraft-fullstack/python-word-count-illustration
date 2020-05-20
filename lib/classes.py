'''
    Author: Gautam Gadipudi
'''
from lib.util import read_file

class WordCounter:
    __slots__ = ["file", "counter"]

    def __init__(self, file: str):
        '''
            Constructor
        '''
        # set the file property
        self.file = file

        # set the counter property
        self.counter = self.__get_word_count__()

    def __get_words__(self, content: str) -> list:
        '''
            Get words from a content.

            1. Replace special characters
            2. Split the content using whitespace
        '''
        return content\
                    .replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+\"“()\n", "")\
                    .split()

    def __get_word_count__(self) -> dict:
        '''
            Get a dictionary with key as word and value as count of that word.

            If word present in dictionary, increment counter by 1 (+= 1)
            Else set value for the new key (new word) to 1 (= 1)

            return 
        '''
        # read file and get it's content
        content = read_file(self.file)

        # get all words as a list
        words = self.__get_words__(content)

        # declare an empty dictionary
        word_count_dic = {}

        # for each word set/increment it's occurance count.
        for word in words:
            if word in word_count_dic:
                word_count_dic[word] += 1
            else:
                word_count_dic[word] = 1

        return word_count_dic

    def get_file(self) -> str:
        '''
            Get the value of file (which is file_path)
        '''
        return self.file

    def get_counter(self) -> dict:
        '''
            Get the value of counter.
        '''
        return self.counter

    def print_count(self):
        '''
            Print each word and its count on each line.
        '''
        for word in self.counter:
            print(f"{word}: {self.counter[word]}")