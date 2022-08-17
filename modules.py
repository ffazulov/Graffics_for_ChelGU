import os
from tqdm import tqdm
import re
import matplotlib.pyplot as plt
'''Считываю файл txt, анализирую данные по заданому слову и составляю график'''

def reading_txt(name_txt):
    f = open(name_txt, 'r', encoding='utf8')
    text = f.read()
    f.close()
    return text

def generator_txt():
    '''Генератор, который считывает один файлик и выдает текс и имя папаки, в которой читал'''
    for name_path in os.listdir('lenta_news_2020_cleared'):
        path = 'lenta_news_2020_cleared' + '\\' + name_path
        for file_in_path in os.listdir(path):
            path_in_path = path+'\\'+file_in_path
            text = reading_txt(path_in_path)
            yield text, name_path

def dir_plus_dir(first_dir, second_dir):
    for key, vol in second_dir.items():
        if key in first_dir:
            first_dir[key] += vol
        else:
            first_dir[key] = vol
    return first_dir

def add_in_dir(word, dir_user, res):
    '''Добавления элемента word в словарь. Параметр res обозначает '''
    if word in dir_user:
        dir_user[word] += res
    else:
        dir_user[word] = res

#----------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    word_user = input('Введите слова или словосочетания через запятую: ').lower().split(', ')

    g = generator_txt()
    dir_words = {word : {} for word in word_user}
    for text_in_file, name in tqdm(g):
        for word, dir_counts in dir_words.items():

            teg = f'\\b{word}\\b'

            mounth = name


            res = len(re.findall(teg, text_in_file))
            if mounth in dir_counts:
                dir_counts[mounth] += res
            else:
                dir_counts[mounth] = res

    for word, dir_counts in dir_words.items():
        list_mounth = ['Январь','февраль','март','апрель','июнь']

        lst_count_word = [dir_counts[munth] for munth in dir_counts]
        print(list_mounth,lst_count_word)
        plt.plot(list_mounth, lst_count_word)
    plt.title(word_user)
    plt.xlabel('Месяца')
    plt.ylabel('Количество')
    plt.legend(word_user)
    plt.show()

