def find_lowest(vector):
    lowest_index = 0

    for i in range(0, len(vector)):
        if vector[i] < vector[lowest_index]:
            lowest_index = i
    return lowest_index

def sort(vector):
    sorted_vector = []

    for i in range(0, len(vector)):
        lowest_index = find_lowest(vector)
        sorted_vector.append(vector.pop(lowest_index))

    return sorted_vector

vetor = [8, 2, 4, 1, 6, 4, 0, 12, 49, 21, -10]

sorted = sort(vetor)