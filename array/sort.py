# ประกาศ Array ชื่อ "numbers" เก็บจำนวนเต็ม 5 ตัว
numbers = [50, 20, 30, 10, 40]

# เรียงลำดับ Array ด้วย Bubble Sort
n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# แสดง Array ที่เรียงลำดับแล้ว
print(numbers)
