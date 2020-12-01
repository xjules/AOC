def read_lines_int(filename):
    with open(filename) as f:
        l = f.readlines()
        return [int(a) for a in l]
    return None
