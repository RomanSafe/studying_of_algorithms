def general():
    def rec_analysing(array):
        from math import log
        print(array)
        n = int(10e100)
        d = array[2]
        log_ab = log(array[0], array[1])
        if d == log_ab:
            return n**d * log(n)
        elif d > log_ab:
            return n**d
        else:
            return n**log_ab


    with open("AOR_input.txt") as reading_input:
        array = [tuple(map(int, line.split())) for line in reading_input.readlines()]
    for line in sorted(array, key=rec_analysing):
        a, b, d = line[0], line[1], line[2]
        print("{}T(n/{}) + O(n**{})".format(a, b, d))






if __name__ == '__main__':
    general()
