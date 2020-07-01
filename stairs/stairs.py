import sys

def steps_counting(amount_of_steps, weights_of_steps):
    _sum, previous_sum, earlier_previous_sum = 0, 0, 0
    for position in range(amount_of_steps):
        if position == 0:
            _sum = weights_of_steps[0]
        elif position == 1:
            previous_sum = _sum
            _sum = max(previous_sum + weights_of_steps[position], weights_of_steps[position])
        else:
            earlier_previous_sum = previous_sum
            previous_sum = _sum
            _sum = max(earlier_previous_sum, previous_sum) + weights_of_steps[position]
    return _sum


def preparation():
    amount_of_steps = int(input())
    reading = (map(int, line.split()) for line in sys.stdin)
    weights_of_steps = tuple(next(reading))
    assert len(weights_of_steps) == amount_of_steps
    print(steps_counting(amount_of_steps, weights_of_steps))


if __name__ == '__main__':
    preparation()
