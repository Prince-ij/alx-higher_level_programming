#!/usr/bin/python3
import marshal
if __name__ = "__main__":
    with open('hidden_4.pyc', 'rb') as file:
        file_content = file.read()
        code_object = marshal.loads(file_content[8:])

    names = code_object.co_names
    names = sorted(name for name in names if not name.startswith('__'))
    for name in names:
        print(name)

