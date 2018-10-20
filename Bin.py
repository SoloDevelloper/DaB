def str(i, diw):
    if diw == 0:
        bin_str(i)
    if diw == 1:
        des_str(i)

def des_and_bin_check_str(i, diw):
    if i[0] == 1:
        des_and_bin_float_check(i, diw)
    if i[0] == 0:
        str()

def check_float_point(i, iii):
    # 4
    dft = len(i)
    dfr = dft - 1
    dfq = 0
    while True:
        if i[dfq] == '.':
            dft = dfq
        dfq += 1
        if dfq > dfr:
            break
    if iii == 1:
        des_float(i, dft)
    if iii == 0:
        i = i.replace('.', '')
        bin_int_and_float(i, dft)

def des_input():
    # 2
    diq = input('\nВведите :')
    diw = 1
    des_and_bin_check_str(diq, diw)

def bin_input():
    # 2
    biq = input('\nВведите :')
    biw = 0
    des_and_bin_check_str(biq, biw)

def des_int(i):
    # 4
    dii = i
    l = []
    if int(dii):
        dii = int(dii)
    while True:
        n = int(dii % 2)
        dii = int(dii / 2)
        l.append(n)
        if dii < 1:
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
    while True:
        print(dip[Dio], end='')
        Dio += 1
        if Dio > dim:
            break

def des_str(i):
    dsq = {
        ' ': '00100000',
        '!': '00100001',
        '"': '00100010',
        '#': '00100011',
        '$': '00100100',
        '%': '00100101',
        '&': '00100110',
        "'": '00100111',
        '(': '00101000',
        ')': '00101001',
        '*': '00101010',
        '+': '00101011',
        ',': '00101100',
        '-': '00101101',
        '.': '00101110',
        '/': '00101111',
        '0': '00110000',
        '1': '00110001',
        '2': '00110010',
        '3': '00110011',
        '4': '00110100',
        '5': '00110101',
        '6': '00110110',
        '7': '00110111',
        '8': '00111000',
        '9': '00111001',
        ':': '00111010',
        ';': '00111011',
        '<': '00111100',
        '=': '00111101',
        '>': '00111110',
        '?': '00111111',
        '@': '01000000',
        '[': '01011011',
        '\\': '01011100',
        ']': '01011101',
        '^': '01011110',
        '_': '01011111',
        '`': '01100000',
        'a': '01100001',
        'b': '01100010',
        'c': '01100011',
        'd': '01100100',
        'e': '01100101',
        'f': '01100110',
        'g': '01100111',
        'h': '01101000',
        'i': '01101001',
        'j': '01101010',
        'k': '01101011',
        'l': '01101100',
        'm': '01101101',
        'n': '01101110',
        'o': '01101111',
        'p': '01110000',
        'q': '01110001',
        'r': '01110010',
        's': '01110011',
        't': '01110100',
        'u': '01110101',
        'v': '01110110',
        'w': '01110111',
        'x': '01111000',
        'y': '01111001',
        'z': '01111010',
        '{': '01111011',
        '|': '01111100',
        '}': '01111101',
        '~': '01111110'
    }
    dsw = len(i) - 1
    dse = 0
    while True:
        dsr = dsq[dse]
        print(dsr)
        dse += 1
        if dse > dsw:
            break

def bin_str(i):
    bst = len(i)
    bsq = len(i) - 1
    bsw = []
    bsr = bst / 8
    while True:
        if ASCII == '00100000':
            print(' ')
        if ASCII == '00100001':
            print('!')
        if ASCII == '00100010':
            print('"')
        if ASCII == '00100011':
            print('#')
        if ASCII == '00100100':
            print('$')
        if ASCII == '00100101':
            print('%')
        if ASCII == '00100110':
            print('&')
        if ASCII == '00100111':
            print("'")
        if ASCII == '00101000':
            print('(')
        if ASCII == '00101001':
            print(')')
        if ASCII == '00101010':
            print('*')
        if ASCII == '00101011':
            print('+')
        if ASCII == '00101100':
            print(',')
        if ASCII == '00101101':
            print('-')
        if ASCII == '00101110':
            print('.')
        if ASCII == '00101111':
            print('/')
        if ASCII == '00110000':
            print('0')
        if ASCII == '00110001':
            print('1')
        if ASCII == '00110010':
            print('2')
        if ASCII == '00110011':
            print('3')
        if ASCII == '00110100':
            print('4')
        if ASCII == '00110101':
            print('5')
        if ASCII == '00110110':
            print('6')
        if ASCII == '00110111':
            print('7')
        if ASCII == '00111000':
            print('8')
        if ASCII == '00111001':
            print('9')
        if ASCII == '00111010':
            print(':')
        if ASCII == '00111011':
            print(';')
        if ASCII == '00111100':
            print('<')
        if ASCII == '00111101':
            print('=')
        if ASCII == '00111110':
            print('>')
        if ASCII == '00111111':
            print('?')
        if ASCII == '01000000':
            print('@')
        if ASCII == '01000001':
            print('A')
        if ASCII == '01000010':
            print('B')
        if ASCII == '01000011':
            print('C')
        if ASCII == '01000100':
            print('D')
        if ASCII == '01000101':
            print('E')
        if ASCII == '01000110':
            print('F')
        if ASCII == '01000111':
            print('G')
        if ASCII == '01001000':
            print('H')
        if ASCII == '01001001':
            print('I')
        if ASCII == '01001010':
            print('J')
        if ASCII == '01001011':
            print('K')
        if ASCII == '01001100':
            print('L')
        if ASCII == '01001101':
            print('M')
        if ASCII == '01001110':
            print('N')
        if ASCII == '01001111':
            print('O')
        if ASCII == '01010000':
            print('P')
        if ASCII == '01010001':
            print('Q')
        if ASCII == '01010010':
            print('R')
        if ASCII == '01010011':
            print('S')
        if ASCII == '01010100':
            print('T')
        if ASCII == '01010101':
            print('U')
        if ASCII == '01010110':
            print('V')
        if ASCII == '01010111':
            print('W')
        if ASCII == '01011000':
            print('X')
        if ASCII == '01011001':
            print('Y')
        if ASCII == '01011010':
            print('Z')
        if ASCII == '01011011':
            print('[')
        if ASCII == '01011100':
            print('\\')
        if ASCII == '01011101':
            print(']')
        if ASCII == '01011110':
            print('^')
        if ASCII == '01011111':
            print('_')
        if ASCII == '01100000':
            print('`')
        if ASCII == '01100001':
            print('a')
        if ASCII == '01100010':
            print('b')
        if ASCII == '01100011':
            print('c')
        if ASCII == '01100100':
            print('d')
        if ASCII == '01100101':
            print('e')
        if ASCII == '01100110':
            print('f')
        if ASCII == '01100111':
            print('g')
        if ASCII == '01101000':
            print('h')
        if ASCII == '01101001':
            print('i')
        if ASCII == '01101010':
            print('j')
        if ASCII == '01101011':
            print('k')
        if ASCII == '01101100':
            print('l')
        if ASCII == '01101101':
            print('m')
        if ASCII == '01101110':
            print('n')
        if ASCII == '01101111':
            print('o')
        if ASCII == '01110000':
            print('p')
        if ASCII == '01110001':
            print('q')
        if ASCII == '01110010':
            print('r')
        if ASCII == '01110011':
            print('s')
        if ASCII == '01110100':
            print('t')
        if ASCII == '01110101':
            print('u')
        if ASCII == '01110110':
            print('v')
        if ASCII == '01110111':
            print('w')
        if ASCII == '01111000':
            print('x')
        if ASCII == '01111001':
            print('y')
        if ASCII == '01111010':
            print('z')
        if ASCII == '01111011':
            print('{')
        if ASCII == '01111100':
            print('|')
        if ASCII == '01111101':
            print('}')
        if ASCII == '01111110':
            print('~')

def des_float(i, dft):
    # 5
    dfy = i
    dfy = float(dfy)
    dfc = i[: dft]
    dfc = float(dfc)
    i = i[: dft]
    des_int(i)
    dft += 1
    dfo = dfy - dfc
    dfa = []
    while True:
        dfo = dfo * 2
        if dfo < 1:
            dfa.append(0)
        if dfo >= 1:
            dfa.append(1)
            dfo -= 1
        if len(dfa) == 10:
            break
    dfz = len(dfa)
    dfz -= 1
    dfv = 0
    print('00101110', end='')
    while True:
        dfx = dfa[dfv]
        dfv += 1
        dfz -= 1
        print(dfx, end='')
        if dfz < 0:
            break

def bin_int_and_float(i, biq = 0):
    # 5,3
    t = len(i)
    bit = t
    t -= 1
    biafq = t
    bn = t
    bi = 0
    bu = 0
    if biq != 0:
        biq -= 1
        biafw = i[:biq]
        biafq = len(biafw)
    while True:
        g = int(i[bn])
        if g > 1:
            print('bin - 0 and 1')
        bn -= 1
        if bn <= 0:
            break
    while True:
        bu = int(i[bi]) * 2 ** biafq + bu
        biafq -= 1
        bi += 1
        bit -= 1
        if bit <= 0:
            break
    print(bu)


def des_and_bin_float_check(dabq, iii):
    # 3
    i = dabq
    db = i.isdigit()
    df = i
    dg = df.replace('.', '', 1)
    dbb = dg.isdigit()
    if db == True and dbb == True:
        if iii == 1:
            des_int(i)
        if iii == 0:
            bin_int_and_float(i)
    if db == False and dbb == True:
            check_float_point(i, iii)
    if db == False and dbb == False:
            des_str()

while True:
    # 1
    z = input('\nDes or bin? ')
    z = str(z)
    if z == 'd':
        des_input()
        z = 'con'
    if z == 'b':
        bin_input()
        z = 'con'
    if z == 'end':
        break
    if z == 'con':
        continue
    else:
        print('d or b!')
