# ฟังก์ชันสำหรับค้นหาสิ่งของในอาร์เรย์
def search_array(arr, element):
    # วนลูปผ่านแต่ละองค์ประกอบในอาร์เรย์
    for ele in arr:
        # ถ้าองค์ประกอบในอาร์เรย์ตรงกับสิ่งที่เราต้องการค้นหา
        if ele == element:
            # พิมพ์ข้อความแสดงว่าพบสิ่งของที่ค้นหาแล้ว
            print(f"หาเจอนะ อันนี้ไง {element}")
            return  # ออกจากฟังก์ชันเมื่อพบสิ่งของ

    # ถ้าไม่พบสิ่งของที่ต้องการค้นหาในอาร์เรย์
    print("ไม่เจออ่ะ")


# รายการผลไม้
fruit = ["banana", "apple", "orange"]
# เรียกใช้ฟังก์ชันค้นหาภายในรายการผลไม้
search_array(fruit, "bananaa")  # ค้นหา "bananaa" ในรายการผลไม้
