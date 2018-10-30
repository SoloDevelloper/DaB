
def inp_s(z):
    i = input('\n    Enter:')
    inte_s(i, z)

def inte_s(i, z):
    l = []
    i = int(i)
    z = int(z)
    while True:
        n = int(i % z)
        i = int(i / z)
        n = str(n)
        if n == '10':
            n = 'a'
        if n == '11':
            n = 'b'
        if n == '12':
            n = 'c'
        if n == '13':
            n = 'd'
        if n == '14':
            n = 'e'
        if n == '15':
            n = 'f'
        if n == '16':
            n = 'g'
        if n == '17':
            n = 'h'
        if n == '18':
            n = 'i'
        if n == '19':
            n = 'j'
        if n == '20':
            n = 'k'
        if n == '21':
            n = 'l'
        if n == '22':
            n = 'm'
        if n == '23':
            n = 'n'
        if n == '24':
            n = 'o'
        if n == '25':
            n = 'p'
        if n == '26':
            n = 'q'
        if n == '27':
            n = 'r'
        if n == '28':
            n = 's'
        if n == '29':
            n = 't'
        if n == '30':
            n = 'u'
        if n == '31':
            n = 'v'
        if n == '32':
            n = 'w'
        if n == '33':
            n = 'x'
        if n == '34':
            n = 'y'
        if n == '35':
            n = 'z'
        if n == '36':
            n = 'A'
        if n == '37':
            n = 'B'
        if n == '38':
            n = 'C'
        if n == '39':
            n = 'D'
        if n == '40':
            n = 'E'
        if n == '41':
            n = 'F'
        if n == '42':
            n = 'G'
        if n == '43':
            n = 'H'
        if n == '44':
            n = 'I'
        if n == '45':
            n = 'J'
        if n == '46':
            n = 'K'
        if n == '47':
            n = 'L'
        if n == '48':
            n = 'M'
        if n == '49':
            n = 'N'
        if n == '50':
            n = 'O'
        if n == '51':
            n = 'P'
        if n == '52':
            n = 'Q'
        if n == '53':
            n = 'R'
        if n == '54':
            n = 'S'
        if n == '55':
            n = 'T'
        if n == '56':
            n = 'U'
        if n == '57':
            n = 'V'
        if n == '58':
            n = 'W'
        if n == '59':
            n = 'X'
        if n == '60':
            n = 'Y'
        if n == '61':
            n = 'Z'
        l.append(n)
        if i < 1:
            break
    r = len(l)
    r -= 1
    dsl = []
    while True:
        dsl.append(l[r])
        r -= 1
        if r < 0:
            break
    dip = dsl
    Dio = 0
    dim = len(dip)
    dim -= 1
    print('    ', end='')
    while True:
        print(dip[Dio], end='')
        Dio += 1
        if Dio > dim:
            break

def call():
        while True :
            z = input('\n   Enter:   ')
            inp_s(z)
call()

