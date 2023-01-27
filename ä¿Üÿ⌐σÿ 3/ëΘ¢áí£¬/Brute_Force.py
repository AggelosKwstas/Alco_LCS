def Brute_Force(xstr, ystr):
    if not xstr or not ystr:
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return str(Brute_Force(xs, ys)) + x
    else:
        return max(Brute_Force(xstr, ys), Brute_Force(xs, ystr), key=len)
