from ketnoidb.ketnoi_mysql import get_connection

def get_all_danhmuc():
    """
    Lấy toàn bộ danh mục từ bảng 'danhmuc' và tự động in ra màn hình.
    """
    conn = get_connection()
    if not conn:
        print("❌ Không thể kết nối cơ sở dữ liệu.")
        return []

    try:
        with conn.cursor() as cursor:
            sql = "SELECT madm, tendm, mota FROM danhmuc ORDER BY madm ASC"
            cursor.execute(sql)
            danhmucs = cursor.fetchall()

            # ✅ In ra danh sách ngay trong hàm
            if danhmucs:
                print("\n📋 DANH SÁCH DANH MỤC:")
                for dm in danhmucs:
                    print(f" - Mã: {dm['madm']}, Tên: {dm['tendm']}, Mô tả: {dm.get('mota', '')}")
            else:
                print("⚠️ Không có danh mục nào trong cơ sở dữ liệu.")

            return danhmucs
    except Exception as e:
        print("❌ Lỗi khi lấy danh sách danh mục:", e)
        return []
    finally:
        conn.close()
