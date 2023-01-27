def LCS(a, b):
    m = len(a)
    n = len(b)

    c = list()
    for i in range(m + 1):
        c.append([None] * (n + 1))

    for i in range(m + 1):
        c[i][0] = 0

    for j in range(n + 1):
        c[0][j] = 0

    for i in range(m + 1):

        for j in range(n + 1):

            if i == 0 or j == 0:
                c[i][j] = 0

            elif a[i - 1] == b[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1

            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

    return c


def LCS_sub_sequence(a, b):
    i = len(a)
    j = len(b)
    c = LCS(a, b)
    finalString = ""
    max = c[i][j]

    while i >= 1 and j >= 1:

        if a[i - 1] == b[j - 1]:  # Αν το Γράμμα στη συγκεκριμένη θέση είναι το ίδιο και για τις δύο ακολουθίες

            finalString = a[i - 1] + finalString
            i = i - 1
            j = j - 1

        elif c[i - 1][j] > c[i][j - 1]:  # Αν δεν είναι ίδιο ελέγχει τις θέσεις πάνω και αριστερά
            i = i - 1

        else:
            j = j - 1

    return max, finalString
