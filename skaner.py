def skaner(file):
    file=open(file)
    text=file.read().lower()
    file.close()
    count_str=0
    count_pos=0
    word=""
    token=()
    result = []
    for c in text[1:]:
        if c == '\n':
            if word != "":
                token=(count_str,count_pos-len(word),word)
                result.append(token)
                word = ""            
            count_str += 1
            count_pos = 0
        elif c.isalpha():
            count_pos += 1
            word += c
        else:
            if word != "":
                token=(count_str,count_pos-len(word),word)
                result.append(token)
                word = ""            
            count_pos += 1
    return result
            
    
