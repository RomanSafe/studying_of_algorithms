from rcviz import CallGraph, viz
from IPython.display import Image

cg = CallGraph(filename="fib1.png")
@viz(cg)
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)

if __name__ == '__main__':
    print(fib1(5))
    cg.render()
