import sys
import argparse

def logAndExit(msg, err_code):
    print(msg)
    sys.exit(err_code)

def wrap(text, maxlen):
    result = ''
    len_string = 0
    for word in text.strip().split():
        len_word = len(word)
        # if line is too long, go to the next
        if len_string + len_word >= maxlen:
            result += '\n'
            len_string = 0
        # else and is not at the beginning, add a space
        elif len_string != 0:
            result += ' '
        result += word
        len_string += len_word + 1
    return result

#filename = input("Enter filename: ").strip()
parser = argparse.ArgumentParser('Enter Max length of the line and filename:')
parser.add_argument('maxlen', type = int, help = 'Max length of the line')
parser.add_argument('filename', type = str, help = 'Filename')
maxlen = parser.parse_args()
filename = parser.parse_args()

if (maxlen.maxlen < 0):
    logAndExit("The length of the line is too short: {}".format(maxlen.maxlen), 1)

try:
    with open(filename.filename) as f:
        print(wrap(f.read(), maxlen.maxlen))
except FileNotFoundError:
    logAndExit("Can't find file: {}".format(filename.filename), 1)

