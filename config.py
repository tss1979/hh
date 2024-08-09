from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):
    '''Функция составляет словарь с параметрами сонфигурации'''
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} is not found in {filename} file')
    return db

