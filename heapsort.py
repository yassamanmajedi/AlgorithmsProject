from heapq import heappop, heappush
def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)
    ordered = []
    while heap:
        ordered.append(heappop(heap))
    return ordered