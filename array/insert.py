def insert_item(arr, n, item, position):
    if position < 0 or position > n:
        print("Invalid position")
        return n

    arr.append(None)
    for i in range(n - 1, position - 1, -1):
        arr[i + 1] = arr[i]

    arr[position] = item
    n += 1
    return n
