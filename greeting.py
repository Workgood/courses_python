def eng():
    return "Hello world!"

def bel():
    return "Прывітанне свет!"

def rus():
    return "Привет мир!"

def ua():
    return "Привіт світ!"

def de():
    return "Hallo Welt!"

def fra():
    return "Bonjour tout le monde !"


def greet_lang(lang):
    if lang == "en":
       return eng()
    elif lang == "be":
        return bel()
    elif lang == "ru":
        return rus()
    elif lang == "de":
        return de()
    elif lang == "ua":
        return ua()
    elif lang == "fr":
        return fra()
    else: 
        return "Undefined language!" 


usr_input = input("Enter a language of greeting(en, be, ru, de, ua, fr):")
print(greet_lang(usr_input))
    
