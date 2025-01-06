def skipFunc1(text, r) :
    return text == '\xa0'

def isSpace(text, r) :
    return text.isspace()

def skipJan(text, r) :
    return text[4:6] == "01";
