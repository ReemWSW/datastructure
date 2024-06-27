def delete_item(arr, n, position):
    if position < 0 or position >= n:
        print("Invalid position")
        return n

    for i in range(position, n - 1):
        arr[i] = arr[i + 1]

    arr.pop()
    n -= 1
    return n
