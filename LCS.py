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

    return c  # compute each sub-problem's results memorization table


def LCS_sub_sequence(a, b):
    m = len(a)
    n = len(b)
    L = LCS(a, b)  # get array using LCS method
    index = L[m][n]
    lcs_output_length = index
    lcs_output = [""] * (index + 1)
    lcs_output[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:  # get final sequence
        if a[i - 1] == b[j - 1]:
            lcs_output[index - 1] = a[i - 1]
            i = i - 1
            j = j - 1
            index = index - 1
        elif L[i - 1][j] > L[i][j - 1]:
            i = i - 1
        else:
            j = j - 1

    return lcs_output_length, "".join(lcs_output)
