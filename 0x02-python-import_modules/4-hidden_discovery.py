#!/usr/bin/python3
if __name__ == "__main__":
    import pyc_dis
    code = pyc_dis.get_code_object_from_pyc('hidden_4.pyc')
    for name in sorted(code.co_names):
        if not name.startswith('__'):
            print(name)
