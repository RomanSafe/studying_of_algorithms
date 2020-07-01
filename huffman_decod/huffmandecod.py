def huffmandecod(d, bicode):
    word = str()
    while len(bicode) > 0:
        for b in iter(d):
            if bicode.startswith(d[b]):
                word += b
                bicode = bicode[len(d[b]):]
                break
    print(word)


if __name__ == '__main__':
    n, length = map(int, input().split(' '))
    _list = []
    for _a in range(n):
        _list.append(input().split(': '))
    code = input()
    huffmandecod(dict(_list), code)
