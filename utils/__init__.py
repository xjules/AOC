def read_lines_int(filename):
    with open(filename) as f:
        l = f.readlines()
        return [int(a) for a in l]
    return None


def read_lines_str(filename, ch=None):
    with open(filename) as f:
        l = f.readlines()
        if bool(ch):
            return [a.split(ch) for a in l]
        return l
    return None


def read_lines_str_stripped(filename):
    with open(filename) as f:
        l = f.readlines()
        return [line.strip() for line in l]
    return None
