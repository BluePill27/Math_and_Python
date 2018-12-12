import numpy
import scipy
import re
from scipy.spatial import distance

dict_words = {}#словарь слово : индекс
word_index = 0# индекс слова
sentence_count = 0# счетчик предложений

file = open("C:\\Users\\andre\\Desktop\\sentences.txt", 'r')
for line in file:
    sentence_count += 1
    line = re.split('[^a-z]', line.lower())# разделение по не буквам с переводом
    while line.count('') != 0:# удаление пустых слов в соотв с их кол-вом
        line.remove('')
    for word in line:# запись новых слов в словарь
        if word not in dict_words.keys():
            dict_words[word] = word_index
            word_index += 1
file.close()

matrix = numpy.zeros((sentence_count, len(dict_words)))# создание матрицы из 0
sentence_count = -1

file = open("C:\\Users\\andre\\Desktop\\sentences.txt", 'r')
for line in file:
    sentence_count += 1
    line = re.split('[^a-z]', line.lower())
    while line.count('') != 0:
        line.remove('')
    for word in line:# заполнение элементов матрицы вместо 0 сколько раз слово с таким индексом встретилось в предложении
        matrix[int(sentence_count), int(dict_words[word])] += 1
file.close()

cosine = {}# значение функции : номер строки нумеруемой с 0
for sentence in range(1, sentence_count+1):
    cosine[scipy.spatial.distance.cosine(matrix[0], matrix[sentence])] = sentence

file = open("C:\\Users\\andre\\Desktop\\sentences-1.txt", 'w')# дальше запись строк для которых функция макс
file.write(str(cosine[sorted(cosine.keys())[0]]) + ' ' + str(cosine[sorted(cosine.keys())[1]]))
file.close()