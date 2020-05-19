def print_output(word_count_dic: dict):
    for word in word_count_dic:
        print(f"{word}: {word_count_dic[word]}")