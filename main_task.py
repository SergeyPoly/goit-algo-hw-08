import heapq

def min_connection_cost(cables):
    if not cables or len(cables) == 1:
        return 0

    # Створюємо мінімальну купу
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        # Дістаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Обраховуємо вартість з'єднання двох кабелів
        cost = first + second
        total_cost += cost

        # Додаємо новий об'єднаний кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost


cables = [4, 3, 1, 6]
result = min_connection_cost(cables)
print(f"Мінімальна вартість об'єднання кабелів: {result}")
