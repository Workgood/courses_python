filename = input("Enter a filename: ")
with open(filename) as f:
    text = f.read()
def count_char(char,text):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count
for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(char,text) / len(text)
    print("{0}-{1}%".format(char,round(perc,2)))
