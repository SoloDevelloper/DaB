lan = '1'
def errors(err, lan):
    if err == 0:
        print('    bin - 0 and 1')
    if err == 2:
        print('    Enter symbol!')
    if err == 1:
        print('    d or b!')
    call(lan)
def language(lan):
    lanq = 1
    if lan == 'ang':
        lan = input('    Language:')
        lanq = 0
    if lan == 'rus':
        if lanq == 1:
            lan = input('    Язык:')
    if lan == 'ang':
        lan = 'ang'
        call(lan)
    if lan == 'rus':
        lan = 'rus'
        call(lan)
    if lan == 'ukr':
        lan = 'ukr'
        call(lan)
    if lan == 'cze':
        lan = 'cze'
        call(lan)

def help_inter(lan):
    if lan == 'ang':
        print('    Comand: \end, \\back\n    Des - decimal. Enter: d.\n    Bin - binar. Enter: b')
    if lan == 'rus':
        print('    Команды: \end, \\back\n    Des - десятичная система счисления. Ввод: d.\n', end='')
        print('Bin - двоичная система счисления. Ввод: b')
    if lan == 'ukr':
        print('    Команди: \end, \\back\n    Des - десяткова система числення. Ввід: d.\n', end='')
        print('Bin - двійкова система числення')
    if lan == 'cze':
        print('    Týmy: \end, \\back\n    Des - desítkové číslo systému. Zadejte: d.\n', end='')
        print('Bin - systém binárních čísel. Zadejte: b')

def str_funk(i, diw, lan):
    if diw == 0:
        bin_str(i, lan)
    if diw == 1:
        dec_str(i, lan)

def bin_check_str(i, diw, lan):
    while True:
        if i[0] == '1':
            dec_and_bin_float_check(i, diw, lan)
            break
        if i[0] == '0':
            str_funk(i, diw, lan)
            break
        else:
            errors(0, lan)
            call(lan)

def check_float_point(i, iii, lan):
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
        dec_float(i, dft, lan)
    if iii == 0:
        i = i.replace('.', '')
        bin_int_and_float(i, lan, dft)

def dec_input(lan):
    # 2
    global z
    if lan == 'ang':
        biq = input('    Enter :')
    if lan == 'rus':
        biq = input('    Введите :')
    if biq == '\help':
        help_inter(lan)
    if biq == '\\back':
        return
    if biq == '\\end':
        z = 'end'
        return z
    if biq == '':
        errors(2, lan)
        return
    if biq == '\language':
        language(lan)
    diw = 1
    dec_and_bin_float_check(biq, diw, lan)

def bin_input(lan):
    # 2
    if lan == 'ang':
        biq = input('    Enter :')
    if lan == 'rus':
        biq = input('    Введите :')
    if biq == '':
        errors(2, lan)
        return
    if biq == '\language':
        language(lan)
    biw = 0
    bin_check_str(biq, biw, lan)

def dec_int(i, lan, dfq=0):
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
    print('    ', end='')
    while True:
        print(dip[Dio], end='')
        Dio += 1
        if Dio > dim:
            break
    if dfq == 0:
        call(lan)

def dec_str(i, lan):
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
        'A': '01000001',
        'B': '01000010',
        'C': '01000011',
        'D': '01000100',
        'E': '01000101',
        'F': '01000110',
        'G': '01000111',
        'H': '01001000',
        'I': '01001001',
        'J': '01001010',
        'K': '01001011',
        'L': '01001100',
        'M': '01001101',
        'N': '01001110',
        'O': '01001111',
        'P': '01010000',
        'Q': '01010001',
        'R': '01010010',
        'S': '01010011',
        'T': '01010100',
        'U': '01010101',
        'V': '01010110',
        'W': '01010111',
        'X': '01011000',
        'Y': '01011001',
        'Z': '01011010',
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
        '~': '01111110',
    }
    dsw = len(i) - 1
    dse = 0
    print('    ', end='')
    while True:
        dsr = i[dse]
        if lan == 'ang':
            print(dsq.get(dsr, 'ThisSimbolNotFound'), end='')
        dse += 1
        if dse > dsw:
            break
    call(lan)

def bin_str(i, lan):
    bsfe = []
    bsfr = 0
    bsfy = 1
    bsfq = len(i)
    bsfw = bsfq / 8
    print('    ', end='')
    while True:
        if bsfy > bsfw:
            break
        bsfe.append(i[bsfr])
        bsfr += 1
        bsfu = bsfy * 8
        if bsfr >= bsfu:
            ASCII = bsfe
            if ASCII == ['0','0','1','0','0','0','0','0']:
                print(' ', end='')
            if ASCII == ['0','0','1','0','0','0','0','1']:
                print('!', end='')
            if ASCII == ['0','0','1','0','0','0','1','0']:
                print('"', end='')
            if ASCII == ['0','0','1','0','0','0','1','1']:
                print('#', end='')
            if ASCII == ['0','0','1','0','0','1','0','0']:
                print('$', end='')
            if ASCII == ['0','0','1','0','0','1','0','1']:
                print('%', end='')
            if ASCII == ['0','0','1','0','0','1','1','0']:
                print('&', end='')
            if ASCII == ['0','0','1','0','0','1','1','1']:
                print("'", end='')
            if ASCII == ['0','0','1','0','1','0','0','0']:
                print('(', end='')
            if ASCII == ['0','0','1','0','1','0','0','1']:
                print(')', end='')
            if ASCII == ['0','0','1','0','1','0','1','0']:
                print('*', end='')
            if ASCII == ['0','0','1','0','1','0','1','1']:
                print('+', end='')
            if ASCII == ['0','0','1','0','1','1','0','0']:
                print(',', end='')
            if ASCII == ['0','0','1','0','1','1','0','1']:
                print('-', end='')
            if ASCII == ['0','0','1','0','1','1','1','0']:
                print('.', end='')
            if ASCII == ['0','0','1','0','1','1','1','1']:
                print('/', end='')
            if ASCII == ['0','0','1','1','0','0','0','0']:
                print('0', end='')
            if ASCII == ['0','0','1','1','0','0','0','1']:
                print('1', end='')
            if ASCII == ['0','0','1','1','0','0','1','0']:
                print('2', end='')
            if ASCII == ['0','0','1','1','0','0','1','1']:
                print('3', end='')
            if ASCII == ['0','0','1','1','0','1','0','0']:
                print('4', end='')
            if ASCII == ['0','0','1','1','0','1','0','1']:
                print('5', end='')
            if ASCII == ['0','0','1','1','0','1','1','0']:
                print('6', end='')
            if ASCII == ['0','0','1','1','0','1','1','1']:
                print('7', end='')
            if ASCII == ['0','0','1','1','1','0','0','0']:
                print('8', end='')
            if ASCII == ['0','0','1','1','1','0','0','1']:
                print('9', end='')
            if ASCII == ['0','0','1','1','1','0','1','0']:
                print(':', end='')
            if ASCII == ['0','0','1','1','1','0','1','1']:
                print(';', end='')
            if ASCII == ['0','0','1','1','1','1','0','0']:
                print('<', end='')
            if ASCII == ['0','0','1','1','1','1','0','1']:
                print('=', end='')
            if ASCII == ['0','0','1','1','1','1','1','0']:
                print('>', end='')
            if ASCII == ['0','0','1','1','1','1','1','1']:
                print('?', end='')
            if ASCII == ['0','1','0','0','0','0','0','0']:
                print('@', end='')
            if ASCII == ['0','1','0','0','0','0','0','1']:
                print('A', end='')
            if ASCII == ['0','1','0','0','0','0','1','0']:
                print('B', end='')
            if ASCII == ['0','1','0','0','0','0','1','1']:
                print('C', end='')
            if ASCII == ['0','1','0','0','0','1','0','0']:
                print('D', end='')
            if ASCII == ['0','1','0','0','0','1','0','1']:
                print('E', end='')
            if ASCII == ['0','1','0','0','0','1','1','0']:
                print('F', end='')
            if ASCII == ['0','1','0','0','0','1','1','1']:
                print('G', end='')
            if ASCII == ['0','1','0','0','1','0','0','0']:
                print('H', end='')
            if ASCII == ['0','1','0','0','1','0','0','1']:
                print('I', end='')
            if ASCII == ['0','1','0','0','1','0','1','0']:
                print('J', end='')
            if ASCII == ['0','1','0','0','1','0','1','1']:
                print('K', end='')
            if ASCII == ['0','1','0','0','1','1','0','0']:
                print('L', end='')
            if ASCII == ['0','1','0','0','1','1','0','1']:
                print('M', end='')
            if ASCII == ['0','1','0','0','1','1','1','0']:
                print('N', end='')
            if ASCII == ['0','1','0','0','1','1','1','1']:
                print('O', end='')
            if ASCII == ['0','1','0','1','0','0','0','0']:
                print('P', end='')
            if ASCII == ['0','1','0','1','0','0','0','0']:
                print('Q', end='')
            if ASCII == ['0','1','0','1','0','0','1','0']:
                print('R', end='')
            if ASCII == ['0','1','0','1','0','0','1','1']:
                print('S', end='')
            if ASCII == ['0','1','0','1','0','1','0','0']:
                print('T', end='')
            if ASCII == ['0','1','0','1','0','1','0','1']:
                print('U', end='')
            if ASCII == ['0','1','0','1','0','1','1','0']:
                print('V', end='')
            if ASCII == ['0','1','0','1','0','1','1','1']:
                print('W', end='')
            if ASCII == ['0','1','0','1','1','0','0','0']:
                print('X', end='')
            if ASCII == ['0','1','0','1','1','0','0','1']:
                print('Y', end='')
            if ASCII == ['0','1','0','1','1','0','1','0']:
                print('Z', end='')
            if ASCII == ['0','1','0','1','1','0','1','1']:
                print('[', end='')
            if ASCII == ['0','1','0','1','1','1','0','0']:
                print('\\', end='')
            if ASCII == ['0','1','0','1','1','1','0','1']:
                print(']', end='')
            if ASCII == ['0','1','0','1','1','1','1','0']:
                print('^', end='')
            if ASCII == ['0','1','0','1','1','1','1','1']:
                print('_', end='')
            if ASCII == ['0','1','1','0','0','0','0','0']:
                print('`', end='')
            if ASCII == ['0','1','1','0','0','0','0','1']:
                print('a', end='')
            if ASCII == ['0','1','1','0','0','0','1','0']:
                print('b', end='')
            if ASCII == ['0','1','1','0','0','0','1','1']:
                print('c', end='')
            if ASCII == ['0','1','1','0','0','1','0','0']:
                print('d', end='')
            if ASCII == ['0','1','1','0','0','1','0','1']:
                print('e', end='')
            if ASCII == ['0','1','1','0','0','1','1','0']:
                print('f', end='')
            if ASCII == ['0','1','1','0','0','1','1','1']:
                print('g', end='')
            if ASCII == ['0','1','1','0','1','0','0','0']:
                print('h', end='')
            if ASCII == ['0','1','1','0','1','0','0','1']:
                print('i', end='')
            if ASCII == ['0','1','1','0','1','0','1','0']:
                print('j', end='')
            if ASCII == ['0','1','1','0','1','0','1','1']:
                print('k', end='')
            if ASCII == ['0','1','1','0','1','1','0','0']:
                print('l', end='')
            if ASCII == ['0','1','1','0','1','1','0','1']:
                print('m', end='')
            if ASCII == ['0','1','1','0','1','1','1','0']:
                print('n', end='')
            if ASCII == ['0','1','1','0','1','1','1','1']:
                print('o', end='')
            if ASCII == ['0','1','1','1','0','0','0','0']:
                print('p', end='')
            if ASCII == ['0','1','1','1','0','0','0','1']:
                print('q', end='')
            if ASCII == ['0','1','1','1','0','0','1','0']:
                print('r', end='')
            if ASCII == ['0','1','1','1','0','0','1','1']:
                print('s', end='')
            if ASCII == ['0','1','1','1','0','1','0','0']:
                print('t', end='')
            if ASCII == ['0','1','1','1','0','1','0','1']:
                print('u', end='')
            if ASCII == ['0','1','1','1','0','1','1','0']:
                print('v', end='')
            if ASCII == ['0','1','1','1','0','1','1','1']:
                print('w', end='')
            if ASCII == ['0','1','1','1','1','0','0','0']:
                print('x', end='')
            if ASCII == ['0','1','1','1','1','0','0','1']:
                print('y', end='')
            if ASCII == ['0','1','1','1','1','0','1','0']:
                print('z', end='')
            if ASCII == ['0','1','1','1','1','0','1','1']:
                print('{', end='')
            if ASCII == ['0','1','1','1','1','1','0','0']:
                print('|', end='')
            if ASCII == ['0','1','1','1','1','1','0','1']:
                print('}', end='')
            if ASCII == ['0','1','1','1','1','1','1','0']:
                print('~', end='')
            bsfy += 1
            bsfe = []
    call(lan)

def dec_float(i, dft, lan):
        # 5
        dfy = i
        dfy = float(dfy)
        dfc = i[: dft]
        dfc = float(dfc)
        i = i[: dft]
        dec_int(i, lan, 1)
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

def bin_int_and_float(i, lan, biq = 0):
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
        if g != 0:
            if g != 1:
                errors(0, lan)
                return
        if g != 1:
            if g != 0:
                errors(0, lan)
                return
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
    print('    ', end='')
    print(bu)
    call(lan)


def dec_and_bin_float_check(dabq, iii, lan):
    # 3
    i = dabq
    db = i.isdigit()
    df = i
    dg = df.replace('.', '', 1)
    dbb = dg.isdigit()
    if db == True and dbb == True:
        if iii == 1:
            dec_int(i, lan)
        if iii == 0:
            bin_int_and_float(i, lan)
    if db == False and dbb == True:
            check_float_point(i, iii, lan)
    if db == False and dbb == False:
            if iii == 0:
                errors(0, lan)
                return
            dec_str(i, lan)
def call(lan):
    # 1
    if lan == '1':
        lan = 'ang'
    while True:
        global z
        if lan == 'ang':
            z = input('\n   Dec(d) or bin(b)? ')
        if lan == 'rus':
            z = input('\n   Десятеричная(d) или двоичная(b)? ')
        if z == '\language':
            language(lan)
        if z == '\help':
            help_inter(lan)
            z = 'con'
        if z == 'd':
            dec_input(lan)
            if z == 'end':
                break
            z = 'con'
        if z == 'b':
            bin_input(lan)
            z = 'con'
        if z == '\end':
            break
        if z == 'con':
            continue
        else:
                errors(1, lan)

call(lan)
