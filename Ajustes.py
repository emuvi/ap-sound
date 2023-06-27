import os


def list_paths():
    return [p for p in os.listdir('.') if p[-4:] == '.txt']


def read_text(path):
    with open(path, 'r') as file:
        return file.readlines()


def save_text(path, text):
    with open(path, 'w') as file:
        file.writelines(text)
    

def proc_text(text):
    return [line.replace('\n', '') for line in text]


if __name__ == '__main__':
    for path in list_paths():
