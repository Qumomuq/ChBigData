import sys


def mylogger(text: str):
    if text.lower().startswith('error'):
        print(text, file=sys.stderr)
    else:
        print(text)  # default value for 'file' argument in 'print' function is file=sys.stdout.
