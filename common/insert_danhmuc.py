from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_db  # kết nối MySQL bạn đã viết sẵn

def insert_danhmuc(ten_danhmuc, mota):
    try:
        # Gọi hàm kết nối
        connection = connect_db()
        if connection is None:
            print("❌ Không thể kết nối tới cơ sở dữ liệu.")
            return

        cursor = connection.cursor()
        sql = "INSERT INTO danhmuc (ten_danhmuc, mota) VALUES (%s, %s)"
        data = (ten_danhmuc, mota)

        cursor.execute(sql, data)
        connection.commit()

        print(f"✅ Đã thêm danh mục: {ten_danhmuc}")

    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
