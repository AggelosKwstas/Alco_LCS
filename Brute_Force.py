def Brute_Force(a, b):
    if not a or not b:
        return ""
    a_x, a_xs, b_y, b_ys = a[0], a[1:], b[0], b[1:]
    if a_x == b_y:
        return str(Brute_Force(a_xs, b_ys)) + a_x
    else:
        return max(Brute_Force(a, b_ys), Brute_Force(a_xs, b), key=len)
