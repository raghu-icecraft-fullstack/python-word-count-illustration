from sys import argv


def __get_words__(content: str) -> list:
    return content.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+\"“()\n", "").split()


def get_word_count(content: str) -> dict:
    words = __get_words__(content)
    word_count_dic = {}
    for word in words:
        if word in word_count_dic:
            word_count_dic[word] += 1
        else:
            word_count_dic[word] = 1
    return word_count_dic


def get_file_name() -> str:
    file_name = ''
    if len(argv) == 2:
        file_name = argv[1]
    else:
        file_name = input("Please enter the file path: ")
    return file_name
