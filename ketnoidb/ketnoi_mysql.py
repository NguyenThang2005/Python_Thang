import mysql.connector
from mysql.connector import Error

def connect_db():
    """Hàm kết nối tới MySQL, trả về đối tượng connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',        # tên máy chủ (vd: '127.0.0.1')
            user='root',             # tên đăng nhập MySQL
            password='',             # mật khẩu (để trống nếu không đặt)
            database='qlthuocankhang'    # tên database bạn đang dùng
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi khi kết nối MySQL:", e)
        return None
