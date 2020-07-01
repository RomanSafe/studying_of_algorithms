def packing(pw, choice):
    amount = 0
    while pw > 0 and len(choice) >= 1:
        temp = choice.pop(0)
        if temp[1] <= pw:
            pw -= temp[1]
            amount += round(temp[0], 3)
        else:
            amount += (temp[0] / temp[1]) * pw
            pw = 0
    return amount


if __name__ == '__main__':
    things = []
    n, W = map(int, input().split())
    for _i in range(n):
        c, w = map(int, input().split())
        things.append([c, w])
    things.sort(reverse=True, key=lambda thing: thing[0] / thing[1])
    print(packing(W, things))
