import re
test = 'urg(a="a", b=72., c="uuuuu"), int, reg(regx="(\\d{4})", replace="\\group(date)"), uu(u="a")'
test1 = "int"

# C = re.compile(r'(?P<name>\w+)(\()')
# C = re.compile(r'(?P<key>\w+)(?:\((?P<args>(\w+)=((".+?")|[0-9.]+))+\))?')
C = re.compile(r'(?P<key>\w+)(?:\((?P<args>(\w+)=((".+?")|[0-9.]+))+\))?')
m = C.match(test)

# A = re.compile(r'(?P<key>\w+)=(?:\(?P<value>((\w+)=((".+?")|[0-9.]+))+\))?')
A = re.compile(r'(?P<key>(\w+)=(?P<value>(\".+?\")|[0-9.]+))')

print(m)
if m :
    print('match')
else :
    print('not match')

list = C.finditer(test)
print(list)
for i in list :
    print(i.group())
    # print(i.group("key") )

    args = i.group("args")
    print(args)
    if not args is None:
        l = A.finditer(args)
        print('afaskfja;sfkjasfj;lkaj====' + str( [ll.group() for ll in l ]) )