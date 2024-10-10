def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1  
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            upper_bound = arr[mid]  
            high = mid - 1
        else:
            return (iterations, arr[mid])

    # Якщо не знайдено, повертаємо кількість ітерацій та верхню межу
    return (iterations, upper_bound)
#-------------------------------------------

arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]

x = 4.0
result = binary_search(arr, x)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")


x = 2.2
result = binary_search(arr, x)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")
