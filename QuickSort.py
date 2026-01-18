def soma(array):
    count = 0
    for i in array:
        count += i
    return count

def sum_recursive(array, i):
    if i >= len(array):
        return 0
    return array[i] + sum_recursive(array, i + 1)

def sum_recursive_2(array):
    if len(array) <= 0:
        return 0
    return array.pop() + sum_recursive_2(array)

def calc_len(array):
    if len(array) <= 0:
        return 0
    return 1 + calc_len(array[:-1])

def find_max(array):
    biggest = array[0]
    for i in array:
        if i > biggest:
            biggest = i
    return biggest

def find_max_recursivo(array, biggest):
    if len(array) <= 0:
        return biggest
    actual = array.pop()

    if actual > biggest:
        biggest = actual

    return find_max_recursivo(array, biggest)

def find_max_recursivo_2(array):
    if array is None:
        return 0

    if len(array) == 1:
        return array[0]

    max_resto = find_max_recursivo_2(array[1:])

    return array[0] if array[0] > max_resto else max_resto

arrei = [2, 8, 1, 4, 7, 3, 9, 2, 5, 12, 3]

print(find_max_recursivo_2(arrei))