import re
import sys

sys.stdin = open('t2.txt')

#‘ункци€ дл€ вычислени€ 3x^2 + 5
def transform(match):
    #re возвращает объект-группу когда по€вл€етс€ соотвествие, работаем с ним
    num = int(match.group(0))
    return str(3 * num ** 2 + 5)

def functionTransformer(message):
    #»спользуем регул€рное выражение дл€ поиска всех целых чисел
    #-? - дл€ отрицательных и положительных чисел, d+ - все цифры числа(как миниум 1)
    return re.sub(r'-?\d+', transform, message)

for _ in range(5):
    text = input()
    print(f"Your text: " + text + " now is " + functionTransformer(text))