from ketnoidb.ketnoi_mysql import get_connection


def insert_danhmuc(tendm, mota=None):
    conn = get_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO danhmuc (tendm, mota) VALUES (%s, %s)"
            cursor.execute(sql, (tendm, mota))
            conn.commit()
            print("✅ Thêm danh mục thành công!")
            return True
    except Exception as e:
        print("❌ Lỗi khi thêm danh mục:", e)
        return False
    finally:
        conn.close()