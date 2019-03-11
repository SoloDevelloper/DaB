def start():
    data = open('data.txt')
    file = data.read()
    q = 0
    country = input()
    counrty = list(country)
    next(file, q, country)

def next(file, q, country):
    while True:
        if file[q] == country[0]:
            nextw(file, q, country)
        q += 1
def nextw(file, q, country):
    qw = []
    while True:
        if file[q] == '' or file[q] == ',':
            thenext(qw, file, country)
        qw.append(file[q])
        q += 1

def thenext(qw, file, country, q):
    if qw == country:
        return nneexxtt(file, q)
    next (file, q, country)

def nneexxtt(file, q):
    while True:
        if file[q].isdigit == True:
            capital(file, q)
        if file[q].isalpha == True:
            countryside(file, q)
        q += 1

start()