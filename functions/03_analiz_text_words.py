filename = input("Enter a filename: ")
with open(filename) as f:
    words = f.read().split()
d_words = {}
for word in words:
    try:
        d_words[word] += 1
    except KeyError:
        d_words[word] = 1
pairs = sorted(d_words.items(), key = lambda x: x[1], reverse =  True)
for p in pairs[:10]:
    print("{} - {} times".format(p[0],p[1]))

