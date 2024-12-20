evector = [2, 7, 11, 17]
target = 9
map = {}

def indextarget(examplevector):
    for i in range(len(examplevector)):
        diff = target - examplevector[i]
        if diff in map:
            return [map[diff], i]
            map[examplevector[i]] = i

    return []

indextarget(evector)