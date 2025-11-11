from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_db  # file chứa hàm connect_mysql()

def delete_danhmuc(id_danhmuc):
    """
    Hàm xóa 1 danh mục theo id_danhmuc
    """
    try:
        connection = connect_db()
        if connection is None:
            print("❌ Không thể kết nối tới cơ sở dữ liệu.")
            return

        cursor = connection.cursor()
        sql = "DELETE FROM danhmuc WHERE id_danhmuc = %s"
        data = (id_danhmuc,)

        cursor.execute(sql, data)
        connection.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã xóa danh mục có ID: {id_danhmuc}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID: {id_danhmuc}")

    except Error as e:
        print("❌ Lỗi khi xóa danh mục:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
