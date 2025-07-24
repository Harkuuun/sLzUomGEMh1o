def sum_negatives_between_max_min(A):
    if not A:
        return 0
    
    # Находим максимальный и минимальный элементы
    max_val = max(A)
    min_val = min(A)
    
    # Находим индексы первого максимума и последнего минимума
    max_idx = A.index(max_val)
    min_idx = len(A) - 1 - A[::-1].index(min_val)
    
    # Определяем границы для суммирования
    start, end = (max_idx, min_idx) if max_idx < min_idx else (min_idx, max_idx)
    
    # Суммируем отрицательные элементы между максимальным и минимальным
    return sum(x for x in A[start+1:end] if x < 0)

# Ввод чисел от пользователя
A = list(map(int, input("Введите числа через пробел: ").split()))
result = sum_negatives_between_max_min(A)
print(f"Сумма отрицательных элементов между максимальным и минимальным: {result}")