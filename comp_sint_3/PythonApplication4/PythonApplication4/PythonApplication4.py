import sys
import re

yaml_file = open('t3.txt', 'r', encoding='utf-8')

print("{")

def word_parser(s):
    words = []
    # Разбиваем строку на части: слова, двоеточия, и игнорируем пробелы и переносы строк
    parts = re.split(r'(s+|:)', s)
    word = ""
    has_two_points = False
    for part in parts:
        part = part.strip()
        
        if part == ':':
            words.append("\"" + word + "\"")
            word = ""
            words.append(":")
            has_two_points = True
        elif part:
                word += part
            # Если встречен перенос строки, обрабатываем накопленное слово
    if word != "":
        words.append("\"" + word + "\"")
    return words
      
#пробелы в оригинале
flag = 0
#наличие { в конце строки
a_flag = 0
first_ = 0
def toJson(str):
    global flag
    global a_flag
    global first_
    c = re.findall(r"\s\s+", str);
    c.append('')
    count_of_space = len(c[0])
    str = str.lstrip()
    # уменьшается количество пробелов = закрываются скобки
    if(count_of_space < flag):
        print("\n", (count_of_space*4 + 4)*' ', "},", end ='')
    else:
        if(a_flag == 0 and first_ == 1):
            print(",", end='', sep='')

    flag = count_of_space
    json_ = ""
    words_ = word_parser(str)
    a_flag=0
    #если после : нет слов - это начало нового блока
    if(words_[len(words_)-1] == ":"):
        words_.append("{")
        a_flag = 1
    if first_ == 1:
        print()
    if(first_ == 0):
        first_ = 1
    string_ = ' ' * (count_of_space * 4 + 4)
    print(string_, end='')
    for i in range(len(words_)) :
        print(words_[i] + " ", end='')


for line in yaml_file:

    toJson(line)

while(flag != 0):
    print("\n", (flag*4)*' ', "}", end='')
    flag -=2
print("\n}")