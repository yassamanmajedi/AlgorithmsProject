def counting_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
    for q in range(0, len(arr)):
        count_arr[arr[q] - min_element] += 1
    for q in range(1, len(count_arr)):
        count_arr[q] += count_arr[q - 1]
    for q in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[q] - min_element] - 1] = arr[q]
        count_arr[arr[q] - min_element] -= 1
    for q in range(0, len(arr)):
        arr[q] = output_arr[q]

    return arr