from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_db  # file chứa hàm connect_mysql()

def update_danhmuc(id_danhmuc, ten_moi, mota_moi, trangthai=1):
    """
    Hàm cập nhật thông tin danh mục theo id_danhmuc
    Tham số:
        id_danhmuc: ID danh mục cần sửa
        ten_moi: tên danh mục mới
        mota_moi: mô tả mới
        trangthai: 1 = hoạt động, 0 = ẩn (mặc định = 1)
    """
    try:
        connection = connect_db()
        if connection is None:
            print("❌ Không thể kết nối tới cơ sở dữ liệu.")
            return

        cursor = connection.cursor()
        sql = """
            UPDATE danhmuc
            SET ten_danhmuc = %s,
                mota = %s,
                trangthai = %s
            WHERE id_danhmuc = %s
        """
        data = (ten_moi, mota_moi, trangthai, id_danhmuc)

        cursor.execute(sql, data)
        connection.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã cập nhật danh mục có ID: {id_danhmuc}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID: {id_danhmuc}")

    except Error as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
