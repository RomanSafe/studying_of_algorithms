import random

def edit_distance1(s1, s2):
    # recursion version
    m, n = len(s1), len(s2)
    d = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        d[i][0] = i
    for j in range(n + 1):
        d[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            d[i][j] = min(d[i][j - 1] + 1,
                       d[i - 1][j] + 1,
                       d[i - 1][j - 1] + (s1[i - 1] != s2[j - 1]))

    return d[m][n]


def edit_distance(s1, s2):
    # iteration version
    m, n = len(s1), len(s2)
    if m < n:
        return edit_distance(s2, s1)

    prev = list(range(n + 1))
    for i, ch1 in enumerate(s1, 1):
        curr = [i]
        for j, ch2 in enumerate(s2, 1):
            curr.append(min(curr[-1] + 1,
                            prev[j] + 1,
                            prev[j - 1] + (ch1 != ch2)))
        prev = curr
    return prev[n]

def test(n_iter=100):
    for i in range(n_iter):
        length = random.randint(0, 64)
        s = "".join(random.choice("01") for _ in range(length))

        assert edit_distance(s, '') == edit_distance('', s) == len(s)
        assert edit_distance(s, s) == 0

    assert edit_distance("ab", "ab") == 0
    assert edit_distance("short", "ports") == 3


def main():
    s1 = input()
    s2 = input()
    print(edit_distance(s1, s2))


if __name__ == '__main__':
    test()
