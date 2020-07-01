def huffman(string):
    tree = []
    _dict = dict()
    _sum = 0

    def getposition(rate):
        for i in tree:
            if rate <= i[1]:
                return tree.index(i)
            continue
        return len(tree)

    def struct_of_tree():
        for a in string:
            frequence = string.count(a)
            if a not in _dict:
                tree.append([a, frequence, None])
                _dict[a] = None
            else:
                continue
        tree.sort(key=lambda node: node[1])
        while len(tree) >= 3:
            l_child = tree.pop(0)
            r_child = tree.pop(0)
            new_frequence = l_child[1] + r_child[1]
            parent_pos = getposition(new_frequence)
            tree.insert(parent_pos, [l_child[0] + r_child[0], new_frequence, None, l_child, r_child])


    def unpuck_of_tree():
        for node in tree:
            if len(node) <= 4:
                continue
            l_child = node.pop(3)
            r_child = node.pop(3)
            parent_position = tree.index(node)
            l_child.append(parent_position)
            r_child.append(parent_position)
            tree.extend([l_child, r_child])


    def code_assigning():
        for i in range(0, len(tree)):
            if i % 2 != 0:
                tree[i][2] = format(1, 'b')
            else:
                tree[i][2] = format(0, 'b')
            if tree[i][0] in _dict:
                _dict[tree[i][0]] = i


    def codecollecting(index):
        bincode = tree[index][2]
        if len(tree) <= 2:
            return bincode
        while index > 1:
            index = tree[index][3]
            bincode = tree[index][2] + bincode
        return bincode

    if len(string) == 1:
        _dict[string] = format(0, 'b')
    else:
        struct_of_tree()
        unpuck_of_tree()
        code_assigning()
        for i in iter(_dict):
            code = codecollecting(_dict[i])
            _dict[i] = code

    for i in string:
        _sum += len(_dict[i])
    print(len(_dict), _sum)
    for i in iter(_dict):
        print("{}: {}".format(i, _dict[i]))
    for i in string:
        print(_dict[i], end='')


if __name__ == '__main__':
    s = input()
    huffman(s)
