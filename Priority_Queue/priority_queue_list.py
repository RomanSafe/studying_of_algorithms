list = []

def insert(value):
    if len(list) > 0:
        for item in list:
            if item >= value:
                list.insert(list.index(item), value)
                break
            continue
        else:
            list.append(value)
    else:
        list.append(value)

def extract_max():
    print(list)
    print(list.pop())


if __name__ == '__main__':
    with open("input.txt") as text:
        for line in text:
            operation = line.rstrip()
            if operation.startswith("Insert"):
                a, b = operation.split(' ')
                insert(int(b))
            else:
                extract_max()
    # for _a in range(int(input())):
    #     operation = input()
    #     if operation.startswith("Insert"):
    #         a, b = operation.split(' ')
    #         insert(b)
    #     else:
    #         extract_max()
