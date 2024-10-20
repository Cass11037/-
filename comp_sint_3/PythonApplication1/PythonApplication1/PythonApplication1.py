import sys
import re
sys.stdin = open('t1.txt')
eyes = [':', ';', 'X', ';', '8', '=']
nose = ['-', '<', '-{', '<{']
mouth = ['(', ')', 'O', '|', '\\', '/', 'P']

def makeSmileFace(isu):
    return eyes[isu%5] + nose[isu%4] + mouth[isu%7]

def countAmmount (patt, str):
    return len(re.findall(patt, str))

patt =  r";<{\\"
print('Your smile face: ' + patt)
for _ in range(5):
    string = input()
    print('This line: ', 
          string , 
          ' has ' , 
          countAmmount(patt, string) , 
          ' smile face(s)')
    
