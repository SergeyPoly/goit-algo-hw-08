import heapq

def merge_k_lists(lists):
    # Використовуємо оператор * для розпакування списків та одночасної їх передачі в аргументи методу heapq.merge
    return list(heapq.merge(*lists))


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
