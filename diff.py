def diff(f_line,s_line):
    f_set = set(f_line)
    s_set = set(s_line)
    return f_set ^ s_set


uf_line = input("Enter some letters: ")
us_line = input("One more line: ")

print("Letters in first and second lines but not at both : ", diff(uf_line,us_line))           
