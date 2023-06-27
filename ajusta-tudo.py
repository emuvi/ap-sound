import os


def adjust_empty_lines(text):
    print('Ajustando linhas vazias...')
    result = []
    empty = 0
    for line in text:
        line = line.strip()
        if line == '':
            empty += 1
        else:
            empty = 0
        if empty < 2:
            result.append(line + '\n')
    return result


def list_paths():
    return [p for p in os.listdir('.') if p[-4:] == '.txt']


def read_text(path):
    print('Lendo: ' + path)
    with open(path, 'r', encoding="utf-8") as file:
        return file.readlines()


def adjust_text(text):
    print('Ajustando: ' + path)
    text = adjust_empty_lines(text)
    return text


def save_text(path, text):
    print('Salvando: ' + path)
    with open(path, 'w', encoding="utf-8") as file:
        file.writelines(text)


if __name__ == '__main__':
    for path in list_paths():
        save_text(path, adjust_text(read_text(path)))
