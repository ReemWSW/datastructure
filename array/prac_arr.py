def add_item(shopping_list, n, item, position):
    if position < 0 or position > n:
        return print("xxxxx ตำแหน่งไม่ถูกต้อง xxxxx")

    shopping_list.append(None)
    for i in range(n - 1, position - 1, -1):
        shopping_list[i + 1] = shopping_list[i]

    shopping_list[position] = item
    print('เพิ่มสินค้าเสร็จสิ้น')


def remove_item(shopping_list, n, position):
    if position < 0 or position >= n:
        return print("ตำแหน่งไม่ถูกต้อง")

    for i in range(position, n - 1):
        shopping_list[i] = shopping_list[i + 1]
    shopping_list.pop(position)
    print('ลบสินค้าเสร็จสิ้น')


def display_items(shopping_list, n):
    print("รายการสินค้า:")
    for i in range(n):
        print(f"{i}: {shopping_list[i]}")


def main():
    shopping_list = []

    while True:
        print("\nเลือกการดำเนินการ:")
        print("1. เพิ่มสินค้า")
        print("2. ลบสินค้า")
        print("3. แสดงรายการสินค้า")
        print("4. ออกจากโปรแกรม")
        choice = input("ป้อนตัวเลือกของคุณ (1/2/3/4): ")

        if choice == "1":
            item = input("ป้อนชื่อสินค้า: ")
            position = int(input("ป้อนตำแหน่งที่ต้องการเพิ่ม: "))
            add_item(shopping_list, len(shopping_list), item, position)
        elif choice == "2":
            position = int(input("ป้อนตำแหน่งที่ต้องการลบ: "))
            remove_item(shopping_list, len(shopping_list), position)
        elif choice == "3":
            print("\nแสดงรายการสินค้า:")
            display_items(shopping_list, len(shopping_list))
        elif choice == "4":
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง")


if __name__ == "__main__":
    main()
