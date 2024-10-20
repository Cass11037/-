import re
import sys

sys.stdin = open('t2.txt')

#������� ��� ���������� 3x^2 + 5
def transform(match):
    #re ���������� ������-������ ����� ���������� �����������, �������� � ���
    num = int(match.group(0))
    return str(3 * num ** 2 + 5)

def functionTransformer(message):
    #���������� ���������� ��������� ��� ������ ���� ����� �����
    #-? - ��� ������������� � ������������� �����, d+ - ��� ����� �����(��� ������ 1)
    return re.sub(r'-?\d+', transform, message)

for _ in range(5):
    text = input()
    print(f"Your text: " + text + " now is " + functionTransformer(text))