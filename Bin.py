def check_float_point (i, dabe) :
    dft = len(i)
    dfr = dft - 1
    i.replace(',' and '.' and '.' and ',', '.')
    dfq = 0
    while True:
        if i[dfq] == '.':
            dft = dfq
        dfq += 1
        if dfq > dfr:
            if dabe == 1 :
                des_float()
def des_input () :
    diq = input('\nВведите :')
    diw = 1
    des_and_bin_float_check (diq, diw)

def bin_input () :
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

def des_float(i):
    check_float_point(i)
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

def bin_int(i):
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

def bin_float (i) :
    pass

def des_and_bin_float_check (dabq, dabw):
    i = dabq
    dabe = dabw
    db = bool(False)
    dbb = bool(False)
    db = i.isdigit()
    df = i
    dg = df.replace(',' and '.' and ',' and '.', '', 1)
    dbb = dg.isdigit()
    if db == True and dbb == True:
        if dabe == 1 :
            des_int(i)
        if dabe == 0 :
            bin_int (i)
    if db == False and dbb == True:
        if dabe == 1:
            des_float(i)
        if dabe == 0:
            bin_float(i)
    if db == False and dbb == False:
            des_str()

while True:
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
