langs = {'en':"Hello world!",'be':"Прывітанне свет!",'ru':"Привет мир!",'de':"Hallo Welt!",'fr':"Bonjour tout le monde!",'ua':"Привіт Світ"}

def greet_lang(lang):
    if lang in langs:
       return langs[lang]
    else: 
        return "Undefined language!" 


usr_input = input("Enter a language of greeting(en, be, ru, de, ua, fr):")
print(greet_lang(usr_input))
    
