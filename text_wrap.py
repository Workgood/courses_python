def wrap(text, maxlen):
    words = []
    ntext = ""
    c = 0
    for i in text.split():
        words.append(i)
    for word in words:
        c += len(word)
        if c >= maxlen:
            ntext += '\n'
            c = len(word)
        ntext += " "
        c += 1
        ntext += word
    ntext.split()
    return ntext
    


with open("text.txt") as f:
    print(wrap(f.read(),30))


'''
def spl(text, maxlen):
    ntext = ''
    c = 0
    for i in text.split():
        c += len(i)
        if c >= maxlen:
            ntext += '\n'
            c = len(i)
        elif ntext != '':
            ntext += ' '
            c += 1
        ntext += i
    return ntext


filename = input("Enter a filename: ")
maxlen = int(input("Enter a max length of the line: "))
with open(filename) as f:
    print(spl(f.read(), maxlen))

'''
