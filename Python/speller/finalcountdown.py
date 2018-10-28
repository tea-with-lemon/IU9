from dict_from_text import create_dict
from dict_from_text import add_dict
from skaner import skaner

def proverka(text, *args):
    dictionary=create_dict(args[0])
    for dict_filename in args[1:]:
        add_dict(dictionary, dict_filename)
    for token in skaner(text):
        if token[2] not in dictionary:
            print('Слово', token[2],'написано неверно, строка -',token[0]+1,', столбец -', token[1]+1)
            
proverka("splin.txt", "test.txt")           

    