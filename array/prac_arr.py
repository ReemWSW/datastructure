# ฟังก์ชันสำหรับเพิ่มสินค้าในรายการช็อปปิ้งที่ตำแหน่งที่กำหนด
def add_item(shopping_list, n, item, position):
    # ตรวจสอบว่าตำแหน่งที่กำหนดอยู่นอกช่วงที่ยอมรับได้หรือไม่
    if position < 0 or position > n:
        # ถ้าตำแหน่งไม่ถูกต้อง ให้พิมพ์ข้อความแสดงข้อผิดพลาดและออกจากฟังก์ชัน
        return print("xxxxx ตำแหน่งไม่ถูกต้อง xxxxx")

    # เพิ่มค่า None ไปที่ท้ายรายการเพื่อให้มีพื้นที่สำหรับสินค้าที่จะเพิ่ม
    shopping_list.append(None)

    # เลื่อนรายการสินค้าไปทางขวาเพื่อสร้างพื้นที่ที่ตำแหน่งที่กำหนด
    for i in range(n - 1, position - 1, -1):
        shopping_list[i + 1] = shopping_list[i]

    # ใส่สินค้าที่ตำแหน่งที่กำหนด
    shopping_list[position] = item
    print("เพิ่มสินค้าเสร็จสิ้น")  # พิมพ์ข้อความแสดงความสำเร็จ


# ฟังก์ชันสำหรับลบสินค้าจากรายการช็อปปิ้งที่ตำแหน่งที่กำหนด
def remove_item(shopping_list, n, position):
    # ตรวจสอบว่าตำแหน่งที่กำหนดอยู่นอกช่วงที่ยอมรับได้หรือไม่
    if position < 0 or position >= n:
        # ถ้าตำแหน่งไม่ถูกต้อง ให้พิมพ์ข้อความแสดงข้อผิดพลาดและออกจากฟังก์ชัน
        return print("ตำแหน่งไม่ถูกต้อง")

    # เลื่อนรายการสินค้าไปทางซ้ายเพื่อเติมช่องว่างที่ตำแหน่งที่ลบ
    for i in range(position, n - 1):
        shopping_list[i] = shopping_list[i + 1]

    # ลบสินค้าชิ้นสุดท้ายออก (ซึ่งกลายเป็นข้อมูลซ้ำหลังจากการเลื่อน)
    shopping_list.pop(position)
    print("ลบสินค้าเสร็จสิ้น")  # พิมพ์ข้อความแสดงความสำเร็จ


# ฟังก์ชันสำหรับแสดงสินค้าทั้งหมดในรายการช็อปปิ้ง
def display_items(shopping_list, n):
    print("รายการสินค้า:")  # พิมพ์หัวข้อ
    # วนลูปผ่านรายการและพิมพ์สินค้าแต่ละรายการพร้อมกับดัชนี
    for i in range(n):
        print(f"{i}: {shopping_list[i]}")


# ฟังก์ชันหลักสำหรับรันโปรแกรมรายการช็อปปิ้ง
def main():
    shopping_list = []  # เริ่มต้นด้วยรายการช็อปปิ้งที่ว่างเปล่า

    # วนลูปเพื่อถามผู้ใช้เกี่ยวกับการดำเนินการซ้ำ ๆ
    while True:
        # แสดงเมนู
        print("\nเลือกการดำเนินการ:")
        print("1. เพิ่มสินค้า")
        print("2. ลบสินค้า")
        print("3. แสดงรายการสินค้า")
        print("4. ออกจากโปรแกรม")
        # รับตัวเลือกจากผู้ใช้
        choice = input("ป้อนตัวเลือกของคุณ (1/2/3/4): ")

        # ดำเนินการตามตัวเลือกของผู้ใช้
        if choice == "1":
            # เพิ่มสินค้าในรายการ
            item = input("ป้อนชื่อสินค้า: ")
            position = int(input("ป้อนตำแหน่งที่ต้องการเพิ่ม: "))
            add_item(shopping_list, len(shopping_list), item, position)
        elif choice == "2":
            # ลบสินค้าออกจากรายการ
            position = int(input("ป้อนตำแหน่งที่ต้องการลบ: "))
            remove_item(shopping_list, len(shopping_list), position)
        elif choice == "3":
            # แสดงรายการช็อปปิ้ง
            print("\nแสดงรายการสินค้า:")
            display_items(shopping_list, len(shopping_list))
        elif choice == "4":
            # ออกจากโปรแกรม
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง")


# เริ่มโปรแกรม
if __name__ == "__main__":
    main()
