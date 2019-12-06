l = open('input.txt').readline()
val = [int(a) for a in l.split(',')]

def afunc(noun, verb, oppcode):
    ptr = 0
    oppcode[1] = noun
    oppcode[2] = verb
    while True:
        if oppcode[ptr]==1:
            a = oppcode[ptr+1]
            b = oppcode[ptr+2]
            c = oppcode[ptr+3]
            oppcode[c] = oppcode[a] + oppcode[b]
        elif oppcode[ptr]==2:
            a = oppcode[ptr+1]
            b = oppcode[ptr+2]
            c = oppcode[ptr+3]
            oppcode[c] = oppcode[a] * oppcode[b]
        elif oppcode[ptr]==99:
            break
        else:
            break
        ptr+=4
        if ptr>len(oppcode):
            break
    return oppcode[0]


for a in [95]:
    for b in [7]:
        oppcode = val.copy()
        print('noun={} verb={} output={}'.format(a, b, afunc(a, b, oppcode)))
        print(a*100+b)
