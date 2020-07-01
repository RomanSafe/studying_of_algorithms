from collections import deque

def array_invertion(main_deck, mdeck_len):
    # if mdeck_len % 2 != 0:
    #     mdeck_len += 1
    #     main_deck.appendleft(0)
    inv_amount = 0
    len_objects_in_main_deck = deque(1 for _ in range(mdeck_len))

    def merge(len_left_part, len_right_part):
        nonlocal inv_amount, main_deck, mdeck_len, len_objects_in_main_deck
        len_left_part = len_left_part
        len_right_part = len_right_part
        temp_left_part = deque()
        for _ in range(len_left_part):
            temp_left_part.append(main_deck.popleft())
            # mdeck_len -= 1
        if mdeck_len % 2 != 0 and len(len_objects_in_main_deck) == (mdeck_len - 1) / 2:
            len_right_part += len_objects_in_main_deck.popleft()
        if len(len_objects_in_main_deck) == 1:
            len_right_part += len_objects_in_main_deck.popleft()
        len_objects_in_main_deck.append(0)
        while len_left_part and len_right_part:
            if temp_left_part[0] > main_deck[0]:
                inv_amount += 1
                main_deck.append(main_deck.popleft())
                len_right_part -= 1
                len_objects_in_main_deck.append(len_objects_in_main_deck.pop() + 1)
            else:
                main_deck.append(temp_left_part.popleft())
                len_left_part -= 1
                len_objects_in_main_deck.append(len_objects_in_main_deck.pop() + 1)
        if len_left_part:
            main_deck.extend(temp_left_part)
            len_objects_in_main_deck.append(len_objects_in_main_deck.pop() + len_left_part)
            return
        len_objects_in_main_deck.append(len_objects_in_main_deck.pop() + len_right_part)
        while len_right_part:
            main_deck.append(main_deck.popleft())
            len_right_part -= 1
        return

    while len_objects_in_main_deck[0] != mdeck_len:
        merge(len_objects_in_main_deck.popleft(), len_objects_in_main_deck.popleft())
    return inv_amount


def general():
    array_len = int(input())
    array = deque(map(int, input().split(" ")))
    assert len(array) == array_len
    print(array_invertion(array, array_len))


def test():
    # assert array_invertion(deque([2, 3, 9, 2, 9]), 5) == 2
    assert array_invertion(deque([0, 1, 2, 50, 75, 99, 100]), 7) == 0
    assert array_invertion(deque([0, 100, 2, 50, 75, 99, 10]), 7) == 9
    assert array_invertion(deque([7, 6, 5, 4, 3, 2, 1]), 7) == 28
    assert array_invertion(deque([1, 2, 3, 5, 4]), 5) == 1
    assert array_invertion(deque([1, 3, 4, 5, 6, 2]), 6) == 4
    #
    #
    # from random import randint
    # from timing import timed
    #
    # for attempt in range(10):
    #     n = randint(1, 10**5)
    #     search_where = deque(randint(1, 10**9) for _ in range(n))
    #     assert len(search_where) == n
    #     assert array_invertion(search_where, n) == 0
    #     search_where.sort()
    #     assert array_invertion(search_where, n) > 1
    #
    #     t = timed(array_invertion, search_where, n)
    #     assert t < 3


if __name__ == '__main__':
    # general()
    test()
