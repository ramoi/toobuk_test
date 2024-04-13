import re
import pprint as pp

def dateformat(text, dic) :
    dateRe = re.compile(r'(?P<YYYY>\d{4})(?P<MM>\d{2}).')
    return dateRe.sub("\\g<YYYY>-\\g<MM>", text)

def pprint(dic) :
    p = pp.PrettyPrinter(indent=4)
    p.pprint(dic)