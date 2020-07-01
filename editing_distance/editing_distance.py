def editing_distasce(str1, str2):
    def check_of_diff(letter1, letter2):
        if letter1 == letter2:
            return 0
        return 1

    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1
    dist = [[i for i in range(len_str1)], [0] * len_str1]
    for j in range(1, len_str2):
        dist[1] = [0] * len_str1
        dist[1][0] = j
        for i in range(1, len_str1):
            difference = check_of_diff(str1[i - 1], str2[j - 1])
            dist[1][i] = min(dist[0][i] + 1, dist[1][i - 1] + 1, dist[0][i - 1] + difference)
        dist[0] = dist[1]
    return dist[1][-1]


def general():
    from sys import stdin
    reading = stdin
    string1 = reading.readline().rstrip()
    string2 = reading.readline().rstrip()
    print(editing_distasce(string1, string2))


if __name__ == '__main__':
    general()
