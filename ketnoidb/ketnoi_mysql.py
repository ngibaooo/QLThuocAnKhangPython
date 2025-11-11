import pymysql

def get_connection():
    try:
        connection = pymysql.connect(
            host='localhost',       # Địa chỉ server MySQL
            user='root',            # Tên đăng nhập
            password='',            # Mật khẩu (để trống nếu chưa đặt)
            database='qlthuocankhang',# Tên CSDL bạn muốn kết nối
            charset='utf8mb4',      # Hỗ trợ tiếng Việt
            cursorclass=pymysql.cursors.DictCursor  # Trả kết quả dạng dictionary
        )
        print("✅ Kết nối MySQL thành công!")
        return connection
    except Exception as e:
        print("❌ Kết nối thất bại:", e)
        return None
