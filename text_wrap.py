import sys

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

filename = input("Enter filename: ").strip()
maxlen = int(input("Enter a max length of the line: "))
if (maxlen < 0):
    logAndExit("The length of the line is too short: {}".format(maxlen), 1)

try:
    with open(filename) as f:
        print(wrap(f.read(), maxlen))
except FileNotFoundError:
    logAndExit("The length of the line is too short: {}".format(maxlen), 1)

