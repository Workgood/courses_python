def greet_lang(lang):
    if lang == "en":
       greet = "Hello world!"#variable which contains language of the greeting
    elif lang == "be":
        greet ="Прывітанне свет!"
    elif lang == "ru":
        greet ="Привет мир!"
    elif lang == "de":
        greet ="Hallo Welt!"
    elif lang == "ua":
        greet ="Привіт світ!"
    elif lang == "fr":
        greet ="Bonjour tout le monde !"
    else: 
        greet = "Undefined language!"
    return greet


usr_input = input("Enter a language of greeting(en, be, ru, de, ua, fr):")
print(greet_lang(usr_input))
    
