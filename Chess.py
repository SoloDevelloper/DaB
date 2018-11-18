def object_ferz():
    obj = input('   Enter ferz:  ')
    pol = input('   Enter hub:   ')
    obj = int(obj)
    pol = int(pol)
    create_objects(pol, obj)

def create_objects(pol, obj):
    objects = []
    while True:
        objects.append(1)
        objects.append(1)
        obj -= 1
        target = len(objects) - 1
        if obj == 0:
            operations(objects, pol, target)

def operations(objects, pol, target):
    while True:
        if objects[0] > pol:
            print(variable)
            return
        objects[target] = objects[target] + 1
        steps = target
        operation_2(steps, objects, target, pol)

def operation_2(steps, objects, target, pol):
    while True:
        checkpoint = objects[steps]
        if checkpoint > pol:
            objects[steps] = 1
            objects[steps - 1] += 1
            steps = target
            continue
        steps -= 1
        if steps < 0:
            operations(objects, pol, target)

object_ferz()