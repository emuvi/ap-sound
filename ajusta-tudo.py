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
            for c in initial_part:
                if not c.isdigit() and c != '.':
                    only_numbers_or_dots = False
                    break
            if only_numbers_or_dots:
                text[i] = "Item. " + text[i]
    return text


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
    text = adjust_items(text)
    return text


def save_text(text, path):
    print('Salvando: ' + path)
    with open(path, 'w', encoding="utf-8") as file:
        file.writelines(text)


if __name__ == '__main__':
    for path in list_paths():
        save_text(adjust_text(read_text(path), path), path)
