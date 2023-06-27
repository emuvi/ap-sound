import os


def adjust_empty_lines(text):
    print('Ajustando linhas vazias...')
    result = []
    empty = 3
    for line in text:
        line = line.strip()
        if not line:
            empty += 1
        else:
            empty = 0
        if empty <= 2:
            result.append(line + '\n')
    return result


def adjust_chapter(text):
    print('Ajustando capítulos...')
    text[0] = text[0].strip()
    if not text[0].startswith('Capítulo. '):
        text[0] = 'Capítulo. ' + text[0]
    if not text[0].endswith('.'):
        text[0] = text[0] + '.'
    text[0] = text[0] + '\n'
    return text


def list_paths():
    return [p for p in os.listdir('.') if p[-4:] == '.txt']


def read_text(path):
    print('Lendo: ' + path)
    with open(path, 'r', encoding="utf-8") as file:
        return file.readlines()


def adjust_text(text):
    print('Ajustando: ' + path)
    text = adjust_empty_lines(text)
    text = adjust_chapter(text)
    return text


def save_text(path, text):
    print('Salvando: ' + path)
    with open(path, 'w', encoding="utf-8") as file:
        file.writelines(text)


if __name__ == '__main__':
    for path in list_paths():
        save_text(path, adjust_text(read_text(path)))
