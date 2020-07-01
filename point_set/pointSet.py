def pointset(sections):
    solution = []
    while len(sections) > 0:
        solution.append(sections.pop(0)[0])
        # print(solution)
        # print(sections)
        while len(sections) > 0:
            if solution[-1] <= sections[0][1] and solution[-1] >= sections[0][0]:
                sections.remove(sections[0])
            else:
                break
    # print(len(solution))
    for _i in solution:
        print(i, end=' ')


if __name__ == '__main__':
    sections = []
    # sections = [[1, 3], [2, 5], [4, 7], [5, 7]]
    for _i in range(int(input())):
        b, e = map(int, input().split())
        sections.append([b, e])
    sections.sort(reverse=True)
    pointset(sections)

