min_val = 109165
max_val = 576723

min_code = [1, 0, 9, 1, 6, 5]

def code_to_int(code):
    c = [str(i) for i in code]
    return int(''.join(c))

def int_to_code(val):
    return [int(d) for d in str(val)]

def are_only_two_same2(code):
    def match_digit(d, cd):
        cnt=0
        for a in cd:
            if d==a:
                cnt+=1
            else:
                return cnt
        return cnt
    i=0
    while i<len(code): 
        id = match_digit(code[i], code[i+1:])
        if id==1:
            return True
        else:
            i+=id+1
    return False

# code = [1,2,4,4,5,5,5]
# print(are_only_two_same(code))
# exit(1)

def are_two_same(code):
    for a, b  in zip(code[1:], code[:-1]):
        if a-b == 0:
            return True
    return False

def is_increasing(code):
    for a, b  in zip(code[1:], code[:-1]):
        if a-b < 0:
            return False
    return True

count = 0
for x in range(min_val, max_val+1):
    code = int_to_code(x)
    if are_only_two_same2(code) and is_increasing(code):
        count += 1
print(count)


