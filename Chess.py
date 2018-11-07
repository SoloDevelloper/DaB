def object_ferz():
    obj = input('   Enter ferz:  ')
    pol = input('   Enter hub:   ')
    objects = []
    obj = int(obj)
    obje = obj
    while True:
        objects.append(1)
        objects.append(1)
        obj -= 1
        if obj == 0:
            check(pol, obje, objects)

def check(pol, obje, objects):
    index = obje * 2 - 1
    variables = 0
    pol = int(pol)
    while True:
        variables += 1
        objects[index] += 1
        if objects[0] > pol:
            break
        index3 = 1
        while True:
            if index3 == 0:
                break
            if objects[index] > pol:
                objects[index - 1] += 1
                objects[index] = 1
            index3 = index - 1
            while True:
                if objects[index3] > pol:
                    objects[index3 - 1] += 1
                    objecrs[index3] = 1
                index3 -= 1
                if index3 == 0:
                    break
            print(variables)
            return
object_ferz()