def check_float_point (i, iii) :
    dft = len(i)
    dfr = dft - 1
    i.replace(',' and '.' and '.' and ',', '.')
    dfq = 0
    while True:
        if i[dfq] == '.':
            dft = dfq
        dfq += 1
        if dfq > dfr:
            break
    if iii == 1 :
        des_float(i, dft)
    if iii == 0 :
        bin_int_and_float (i, dft)

def des_input () :
    # 2
    diq = input('\nВведите :')
    diw = 1
    des_and_bin_float_check (diq, diw)

def bin_input () :
    #2
    biq = input('\nВведите :')
    biw = 0
    des_and_bin_float_check(biq, biw)

def des_int(i):
    dii = i
    if int(dii):
        dii = int(dii)
        l = []
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

def des_str():
    pass

def des_float(i, dft):
    dfd = i
    dfy = i
    dfy = float(dfy)
    dfc = i[: dft]
    dfc = float(dfc)
    i = i[: dft]
    des_int(i)
    dft += 1
    dfm = dfd[dft:]
    dfm = int(dfm)
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
    t = len(i)
    bit = t
    t -= 1
    biafq = t
    bn = t
    bi = 0
    bu = 0
    if biq != 0 :
        biafw = []
        biaf = int(biaf)
        biafq = len( biaf)
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


def des_and_bin_float_check (dabq, iii):
    #3
    i = dabq
    db = bool(False)
    dbb = bool(False)
    db = i.isdigit()
    df = i
    dg = df.replace(',' and '.' and ',' and '.', '', 1)
    dbb = dg.isdigit()
    if db == True and dbb == True:
        if iii == 1 :
            des_int(i)
        if iii == 0 :
            bin_int_and_float (i)
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
