import os
import re


def adjust_empty_lines(text):
    print('Ajustando linhas vazias...')
    result = []
    empty = 3
    for line in text:
        line = line.strip()
        line = re.sub(r'\s+', ' ', line)
        if not line:
            empty += 1
        else:
            empty = 0
        if empty <= 2:
            result.append(line + '\n')
    return result


def adjust_chapter(text, path):
    print('Ajustando capítulos...')
    text[0] = text[0].strip()
    main_title = 'Capítulo. ' + os.path.splitext(os.path.basename(path))[0] + '.\n'
    if not text[0] == main_title:
        text[0] = main_title
    return text


def adjust_items(text):
    print('Ajustando itens...')
    for i in range(len(text)):
        line = text[i]
        initial_space = line.find(' ')
        if initial_space > 0:
            initial_part = line[:initial_space]
            only_numbers_or_dots = True
            there_is_a_dot = False
            there_is_a_number = False
            for c in initial_part:
                if not c.isdigit() and c != '.':
                    only_numbers_or_dots = False
                elif c.isdigit():
                    there_is_a_number = True
                elif c == '.':
                    there_is_a_dot = True
            if only_numbers_or_dots and there_is_a_number and there_is_a_dot:
                text[i] = "Item. " + text[i]
    return text


def adjust_chars(text):
    print('Ajustando caracteres...')
    result = []
    for line in text:
        line = line.replace('“', '"')
        line = line.replace('”', '"')
        line = line.replace('’', "'")
        line = line.replace('‘', "'")
        line = line.replace('–', '-')
        line = line.replace('•', '*')
        line = line.replace('♦', '*')
        line = line.replace('…', '...')
        result.append(line)
    return result


def adjust_lost_numbers(text):

    def is_only_three_numbers(line):
        line = line.strip()
        result = False
        if len(line) > 0 and len(line) < 4:
            result = True
            for c in line:
                if not c.isdigit():
                    result = False
                    break
        return result

    print('Ajustando números perdidos...')
    result = []
    for line in text:
        if not is_only_three_numbers(line):
            result.append(line)
    return result


def adjust_only_dots(text):

    def is_only_dots(line):
        line = line.strip()
        for c in line:
            if not (c == " " or c == "."):
                return False
        return True

    print('Ajustando somente pontos...')
    result = []
    for line in text:
        if not is_only_dots(line):
            result.append(line)
    return result


def list_paths():
    return [p for p in os.listdir('.') if p[-4:] == '.txt']


def read_text(path):
    print('Lendo: ' + path)
    with open(path, 'r', encoding="utf-8") as file:
        return file.readlines()


def adjust_text(text, path):
    print('Ajustando: ' + path)
    text = adjust_empty_lines(text)
    text = adjust_chapter(text, path)
    text = adjust_chars(text)
    text = adjust_items(text)
    text = adjust_lost_numbers(text)
    return text


def save_text(text, path):
    print('Salvando: ' + path)
    with open(path, 'w', encoding="utf-8") as file:
        file.writelines(text)


if __name__ == '__main__':
    for path in list_paths():
        save_text(adjust_text(read_text(path), path), path)
