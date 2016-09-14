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
    for line in ntext.split("\n"):
        print(line.strip())
    return ""
    
maxlen = int(input("Enter a max length of the line: "))


with open("text.txt") as f:
    print(wrap(f.read(),maxlen))


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

'''





