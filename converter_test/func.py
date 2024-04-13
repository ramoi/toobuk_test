import re

def contest1(text, r) :
    regx = re.compile(r"(?P<YYYY>\d{4})(?P<MM>\d{2}).")
    replace = "\\g<YYYY>-\\g<MM>"

    return regx.sub(replace, text)
