# ประกาศ Array ชื่อ "fruits" เก็บชื่อผลไม้ 5 ตัว
fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry"]

# ค้นหาว่ามี "Banana" อยู่ใน Array หรือไม่
found = False
for fruit in fruits:
    if fruit == "Banana":
        found = True
        break

# แสดงผลการค้นหา
if found:
    print('พบ "Banana" ใน Array')
else:
    print('ไม่พบ "Banana" ใน Array')
