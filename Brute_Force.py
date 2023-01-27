def Brute_Force(a, b):
    if not a or not b:
        return ""
    x, xs, y, ys = a[0], a[1:], b[0], b[1:]
    if x == y:
        return str(Brute_Force(xs, ys)) + x
    else:
        return max(Brute_Force(a, ys), Brute_Force(xs, b), key=len)
