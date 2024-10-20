import sys


yaml_file = open('t3.txt', 'r', encoding='utf-8')

print("{")

def wordOarser(str):
    words = []
    word = ""
    #флаг-проверка на наличие двоеточия
    has_two_points = False
    for i in range(len(str)):
        #если еще не было двоеточия
        if(has_two_points == False):
            if(str[i] == ':') :
                if(word != ""):
                    words.append("\"" + word + "\"")
                word = ""
                words.append(":")
                has_two_points = True
            if(str[i] != ':' and str[i] != " " and str[i] != "\n"):
                word += str[i]
            if str[i] == " " or str[i] == "\n":
                if(word != ""):
                    words.append(word)
                word = ""
        #было двоеточие. дальше нет смыслап делить строку на слова
        else :
            if(str[i] != ':' and str[i] != "\n"):
                word += str[i]
            if str[i] == "\n":
                if(word != ""):
                    while(word[0] == ' ') :
                        word = word[1:]
                    words.append("\"" + word + "\"")
                word = ""
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
    count_of_space = 0;
    while str[0] == ' ':
        count_of_space +=1
        str = str[1:]
    # уменьшается количество пробелов = закрываются скобки
    if(count_of_space < flag):
        print("\n", (count_of_space*4)*' ', "    ", "},", end ='')
    else:
        if(a_flag == 0 and first_ == 1):
            print(",", end='', sep='')
    if(first_ == 0):
        first_ = 1
    flag = count_of_space
    json_ = ""
    words_ = wordOarser(str)
    a_flag=0
    #если после : нет слов - это начало нового блока
    if(words_[len(words_)-1] == ":"):
        words_.append("{")
        a_flag = 1
    print()
    string_ = ' ' * (count_of_space * 4) +  "    "
    print(string_, end='')
    for i in range(len(words_)) :
        print(words_[i] + " ", end='')


for line in yaml_file:

    toJson(line)

while(flag != 0):
    print("\n", (flag*4)*' ', "}", end='')
    flag -=2
print("\n}")