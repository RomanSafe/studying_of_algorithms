def input_generator():
    with open("input2.txt") as f:
        f2 = open("input.txt", 'a')
        for line in f:
            f2.write("Insert " + line)
            f2.write("ExtractMax\n")


if __name__ == '__main__':
    input_generator()
