import numpy as np
l = open('input.txt').readlines()
a = l[0].strip().split(',')
b = l[1].strip().split(',')
d = {}
print(a)
print(b)

def get_dir(a):
    if a[0]=='U':
        return (0, 1)
    if a[0]=='D':
        return (0, -1)
    if a[0]=='L':
        return (-1, 0)
    if a[0]=='R':
        return (1, 0)

def get_change(a):
    dir = get_dir(a)
    return np.array(int(a[1:])) * dir

def updafe_dict(d, pos, wid):
    if pos[0]==pos[1]==0:
        return d
    pos_str = '{},{}'.format(pos[0], pos[1])
    if pos_str in d:
        d[pos_str].add(wid)
    else:
        d[pos_str] = {wid}
    return d

def updade_steps(sd, pos, steps):
    if pos[0]==pos[1]==0:
        return sd
    pos_str = '{},{}'.format(pos[0], pos[1])
    if not pos_str in sd:
        sd[pos_str] = steps
    return sd
   

def project_wire(px, py, a, d, wid):
    pos = np.array([px, py])
    for cmd in a:
        tmp = pos + get_change(cmd)
        if tmp[0] < pos[0]:
            for ix in range(tmp[0], pos[0]+1):
                d = updafe_dict(d, (ix, pos[1]), wid)
        else:
            for ix in range(pos[0], tmp[0]+1):
                d = updafe_dict(d, (ix, pos[1]), wid)
        if tmp[1] < pos[1]:
            for ix in range(tmp[1], pos[1]+1):
                d = updafe_dict(d, (pos[0], ix), wid)
        else:
            for ix in range(pos[1], tmp[1]+1):
                d = updafe_dict(d, (pos[0], ix), wid)
        pos = tmp
    return d

def project_wire_steps(px, py, a, d, wid, steps):
    pos = np.array([px, py])
    stc = 0
    for cmd in a:
        tmp = pos + get_change(cmd)
        if pos[0]!=tmp[0]:
            sgn = -1 if tmp[0]<pos[0] else 1
            for ix in range(pos[0], tmp[0] + sgn, sgn):
                d = updafe_dict(d, (ix, pos[1]), wid)
                steps = updade_steps(steps, (ix, pos[1]), stc)
                stc+=1
        if pos[1]!=tmp[1]:
            sgn = -1 if tmp[1]<pos[1] else 1
            for ix in range(pos[1], tmp[1] + sgn, sgn):
                d = updafe_dict(d, (pos[0], ix), wid)
                steps = updade_steps(steps, (pos[0], ix), stc)
                stc+=1
        stc-=1
        pos = tmp
    return (steps, d)



def get_dst(val, pos2):
    pos = [int(p) for p in val.split(',')]
    dst = np.abs(pos[0] - pos2[0]) + np.abs(pos[1] - pos2[1])
    return dst

step_a = {}
step_b = {}
(steps_a, d) = project_wire_steps(0, 0, a, d, 0, step_a)
(steps_b, d) = project_wire_steps(0, 0, b, d, 1, step_b)

k = []
for val in d:
    if len(d[val])>1:
        k.append(val)

print(k)

steps_comb = []
for key in k:
    steps_comb.append(step_a[key] + step_b[key])
    print('k={}, steps_a={} steps_b={}'.format(key, step_a[key], step_b[key]))
print(sorted(steps_comb))