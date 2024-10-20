import sys
import yaml

# Открываем файл
with open('t3.txt', 'r', encoding='utf-8') as yaml_file:
    # Загружаем содержимое yaml файла
    content = yaml.safe_load(yaml_file)

# Конвертируем данные в формат JSON
import json
# ensure_ascii - экранирует не ASCII-символы
json_output = json.dumps(content, ensure_ascii=False, indent=2)

# Печатаем результат
print(json_output)
