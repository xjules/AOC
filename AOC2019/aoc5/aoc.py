f = open('input.txt').readline()
arr = f.split(',')

# arr = '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'.split(',')
arr = [int(a) for a in arr]


def get_oppcode(val):
    return [int(d) for d in str(val)]


def compute(arr, input):
    index = 0
    output = -1
    while index < len(arr):
        operator = arr[index]
        im_mode_a = False
        im_mode_b = False
        # print('Doing {} index={}'.format(arr[index], index))
        if operator>99:
            l = get_oppcode(operator)
            operator = l[-1]
            try:
                im_mode_a = l[-3] == 1
            except:
                pass
            try:
                im_mode_b = l[-4] == 1
            except:
                pass
        a, b = 0, 0
        try:
            a = arr[index + 1] if im_mode_a else arr[arr[index + 1]]
            b = arr[index + 2] if im_mode_b else arr[arr[index + 2]]
        except:
            print('missing parameters for {}'.format(arr[index]))
        if operator == 99:
            return (output, arr)
        elif operator == 1:
            arr[arr[index + 3]] = a + b
            index += 4
        elif operator == 2:
            arr[arr[index + 3]] = a * b
            index += 4
        elif operator == 3:
            arr[arr[index+1]] = input
            index += 2
        elif operator == 4:
            output = a
            index += 2
        elif operator == 5:
            if a != 0:
                index = b
            else:
                index += 3
        elif operator == 6:
            if a == 0:
                index = b
            else:
                index += 3
        elif operator == 7:
            arr[arr[index + 3]] = int(a < b)
            index += 4
        elif operator == 8:
            arr[arr[index + 3]] = int(a == b)
            index += 4
            
        else:
            raise Exception('Something Went wrong {} modes A:{} B:{}'.format(arr[index], im_mode_a, im_mode_b))

output, b = compute(arr, 5)
print("SOLUTION:", output)