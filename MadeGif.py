import json
import os
import pymorphy2
from nltk.corpus import stopwords
from tqdm import tqdm
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import csv

'''Код создает гиф изображение по анализу данных, а так же записывает в файл test.CSV полученные данные.'''

def made_gif():
    '''Создает список для хранения кадров. в первый кадр добавляет остальные кадры и сохраняет гифку'''
    frames = [Image.open(f'fig{i}.png') for i in range(1, 6)]
    frames[0].save(
        'result.gif',
        save_all=True,
        append_images=frames[1:],
        optimize=False,
        duration=400,
        loop=0)

def norm_form_words(text):
    '''Заменение на нормолизованную форму каждого слова в списке'''
    morph = pymorphy2.MorphAnalyzer(lang='ru')
    text = ' '.join([morph.parse(word)[0].normal_form for word in text.split()])
    return text

def dellit_stopwords(text, stopwords):
    '''Удаление стоп слов с помощью nltk, нужно просписать стрроку перед вызовом функции:
    stopwords = stopwords.words('russian'), которая скачивает стоп-слова в stopwords'''
    text_result = [i for i in text.split() if i not in stopwords]
    return text_result

def stopwords_creat():
    return stopwords.words('russian')


def dellit_symbols(text):
    '''Приведение к нижнему регистру и удаление специальных символов'''
    text_lower = text.lower()
    text_result = ''
    for ch in text_lower:
        if 'а' <= ch <= 'я' or ch == ' ':
            text_result += ch
    return text_result

def reading_json(path1):
    '''Функция считывает из файла json текс и возвращает его'''
    f = open(path1, 'r', encoding='utf8')
    text = json.load(f)
    f.close()
    return text['text']

def generator_json():
    '''Генератор, который считывает один файлик и выдает текс с именем папаки, в которой читал'''
    for name_path in os.listdir('lenta_news_2020'):
        path = 'lenta_news_2020' + '\\' + name_path
        for file_in_path in os.listdir(path):
            path_in_path = path+'\\'+file_in_path
            text = reading_json(path_in_path)
            yield text, name_path

def dir_plus_dir(first_dir, second_dir):
    for key, vol in second_dir.items():
        if key in first_dir:
            first_dir[key] += vol
        else:
            first_dir[key] = vol
    return first_dir

def words_cloud(dir_dirs_words):
    '''Создание картинки wordcloud'''
    counter = 1
    for key, dir_ in dir_dirs_words.items():
        wordcloud = WordCloud(background_color='White').generate_from_frequencies(dir_)
        plt.axis('off')
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.savefig(f'fig{counter}.png', dpi = 1000)
        counter += 1

def converting_dir_to_csv(dir_mounth):
    '''Конвертирует словарь в более удбный вид для записи в CSV-файл'''
    list_dirs = []
    for mounth, dir_words in dir_mounth.items():
        for word, count in dir_words.items():
            list_dirs.append({'mounth' : mounth, 'word' : word, 'count' : count})
    return list_dirs

def append_in_dir(text):
    '''Функция собирает словарь из текста по количеству слов'''
    dir_result = {}
    for word in text:
        if word in dir_result:
            dir_result[word] += 1
        else:
            dir_result[word] = 1
    return dir_result

def saving_cleared_text(text, mounth, iteration):
    '''Записывает text в файл '(номер итерации).txt' в папке mounth'''
    name_txt = str(iteration)+'.txt'
    f = open(f'lenta_news_2020_cleared\\{mounth}\\{name_txt}', 'w', encoding='utf8')
    f.write(text)
    f.close()

if __name__ == '__main__':
    #Считывать каждый файл, удалять из него спец символы, нормализовыват каждое слово и удалять стоп-слова, после заносить полученный текст в список подсчета слов
    g = generator_json()
    stopwords = stopwords.words('russian')
    stopwords.append('это')
    stopwords.append('который')
    dir_mounth = {}
    iteration = 0
    for text_in_file, name in tqdm(g):
        mounth = list(name)[6]
        iteration += 1

        text = dellit_symbols(text_in_file)
        text = norm_form_words(text)
        text = dellit_stopwords(text,stopwords)

        dir_result = append_in_dir(text)

        if mounth in dir_mounth:
            dir_mounth[mounth] = dir_plus_dir(dir_mounth[mounth], dir_result)
        else:
            dir_mounth[mounth] = dir_result

        text = ' '.join(text)
        saving_cleared_text(text, mounth, iteration)

    list_dirs = converting_dir_to_csv(dir_mounth)

    made_gif()