
import re

def create_dict (file):
    return set(re.findall("[а-я]+", open(file).read().lower()))

def add_dict (dic, file):
    return dic.update(create_dict(file))


