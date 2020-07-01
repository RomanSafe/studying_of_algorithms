def addents(cn):
    list_of_addents = []
    addent = 1
    while cn > 0:
        temp = cn - addent
        if temp <= addent:
            list_of_addents.append(cn)
            break
        else:
            cn -= addent
            list_of_addents.append(addent)
            addent += 1
    print(len(list_of_addents))
    for a in list_of_addents:
        print(a, end=" ")


if __name__ == '__main__':
    n = int(input())
    addents(n)
