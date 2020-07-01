from collections import deque


def merge_sort(array, left_ind, right_ind):
    def merge(array1, array2):
        temp_store = deque()
        array1_pointer = 0
        array1_end = len(array1) - 1
        array2_pointer = 0
        array2_end = len(array2) - 1
        while array1_pointer <= array1_end and array2_pointer <= array2_end:
            if array1[array1_pointer] < array2[array2_pointer]:
                temp_store.append(array1[array1_pointer])
                array1_pointer += 1
            else:
                temp_store.append(array2[array2_pointer])
                array2_pointer += 1
        while array1_pointer <= array1_end:
            temp_store.append(array1[array1_pointer])
            array1_pointer += 1
        while array2_pointer <= array2_end:
            temp_store.append(array2[array2_pointer])
            array2_pointer += 1
        return list(temp_store)

    if left_ind < right_ind:
        middle = int((left_ind + right_ind) / 2)
        return merge(merge_sort(array, left_ind, middle), merge_sort(array, middle + 1, right_ind))
    else:
        return [array[left_ind]]


if __name__ == '__main__':
    array = [5, 2, 4, 6, 1, 3, 2, 6]
    print(merge_sort(array, 0, len(array) - 1))
