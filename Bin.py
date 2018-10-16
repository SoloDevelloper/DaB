def des_int():
    global i
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


def des_float():
    global i
    dft = len(i)
    dfr = dft - 1
    dfi = i.replace(',' and '.' and '.' and ',', '.')
    dfq = 0
    while True:
        if i[dfq] == '.':
            dft = dfq
        dfq += 1
        if dfq > dfr:
            break
    dfd = i
    dfy = i
    dfy = float(dfy)
    dfc = i[: dft]
    dfc = float(dfc)
    i = i[: dft]
    des_int()
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


def bin():
    i = input('\nВведите :')
    t = len(i)
    bh = t
    t -= 1
    bn = t
    bi = 0
    bu = 0
    while True:
        g = int(i[t])
        if g > 1:
            print('bin - 0 and 1')
        t -= 1
        bh -= 1
        if bh <= 0:
            break
    while True:
        bu = int(i[bi]) * 2 ** bn + bu
        bi += 1
        bn -= 1
        if bn < 0:
            break
    print(bu)


def des():
    global i
    i = input('\nВведите :')
    db = bool(False)
    dbb = bool(False)
    db = i.isdigit()
    df = i
    dg = df.replace(',' and '.' and ',' and '.', '', 1)
    dbb = dg.isdigit()
    if db == True and dbb == True:
        des_int()
    if db == False and dbb == True:
        des_float()
    if db == False and dbb == False:
        des_str()


while True:
    z = input('\nDes or bin? ')
    z = str(z)
    if z == 'd':
        des()
        z = 'con'
    if z == 'b':
        bin()
        z = 'con'
    if z == 'end':
        break
    if z == 'con':
        continue
    else:
        print('d or b!')
