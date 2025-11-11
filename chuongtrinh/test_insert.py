from common.insert_danhmuc import insert_danhmuc
while True:

    ten_danhmuc=input("Nhập vào tên danh mục")
    mota=input("Nhập vào mô tả")
    insert_danhmuc(ten_danhmuc, mota)
    con=input("TIẾP TỤC y, THOÁT THÌ NHẤN KÍ TỰ BẤT KỲ")
    if con!="y":
        break;

