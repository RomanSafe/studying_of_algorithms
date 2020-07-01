list = []

def siftup(i):
    while i > 0 and list[(i - 1) // 2] < list[i]:
        t = list[(i - 1) // 2]
        list[(i - 1) // 2] = list[i]
        list[i] = t
        i = (i - 1) // 2


def insert(value):
    list.append(value)
    siftup(list.index(value, -1))


def siftdown(i):
    while 2 * i + 1 <= len(list) - 1:
        max = i
        if list[2 * i + 1] > list[max]:
            max = 2 * i + 1
        if (2 * i + 2 <= len(list) - 1) and list[2 * i + 2] > list[max]:
            max = 2 * i + 2
        if max == i:
            break
        t = list[i]
        list[i] = list[max]
        list[max] = t
        i = max

def extract_max():
    print(list[0])
    if len(list) == 1:
        return
    list[0] = list.pop()
    siftdown(0)


if __name__ == '__main__':
    for _a in range(int(input())):
        operation = input()
        if operation.startswith("Insert"):
            a, b = operation.split(' ')
            insert(b)
        else:
            extract_max()
