import heapq
list = []

if __name__ == '__main__':
    with open("input.txt") as text:
        for line in text:
            operation = line.rstrip()
            if operation.startswith("Insert"):
                a, b = operation.split(' ')
                heapq.heappush(list, -(int(b)))
            else:
                print(-(heapq.heappop(list)))
