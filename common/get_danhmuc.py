from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_db  # hàm connect_mysql bạn đã viết

def get_all_danhmuc():
    """
    Hàm lấy và in toàn bộ danh mục trong bảng danhmuc
    """
    try:
        connection = connect_db()
        if connection is None:
            print("❌ Không thể kết nối tới cơ sở dữ liệu.")
            return

        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM danhmuc"
        cursor.execute(sql)

        results = cursor.fetchall()

        if results:
            print("✅ Danh sách danh mục trong cơ sở dữ liệu:")
            print("──────────────────────────────────────────────")
            for dm in results:
                print(f"🆔 {dm['id_danhmuc']} | 📦 {dm['ten_danhmuc']} | 📝 {dm['mota']}")
            print("──────────────────────────────────────────────")
        else:
            print("⚠️ Không có danh mục nào trong cơ sở dữ liệu.")

    except Error as e:
        print("❌ Lỗi khi lấy danh sách danh mục:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
