import sys


def p(*args):
    text = ""
    for i in args:
        text += str(i)
    print(text)
    sys.stdout.flush()