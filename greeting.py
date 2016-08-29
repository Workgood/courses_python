langs = {'en':"Hello world!",'be':"Прывітанне свет!",'ru':"Привет мир!",'de':"Hallo Welt!",'fr':"Bonjour tout le monde!",'ua':"Привіт Світ"}

def greet_lang(lang):
    if lang == "en":
       return langs['en']
    elif lang == "be":
        return langs['be']
    elif lang == "ru":
        return langs['ru']
    elif lang == "de":
        return langs['de']
    elif lang == "ua":
        return langs['ua']
    elif lang == "fr":
        return langs['fr']
    else: 
        return "Undefined language!" 


usr_input = input("Enter a language of greeting(en, be, ru, de, ua, fr):")
print(greet_lang(usr_input))
    
