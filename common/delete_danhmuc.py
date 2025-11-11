from ketnoidb.ketnoi_mysql import get_connection


def delete_danhmuc(madm):
    conn = get_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM danhmuc WHERE madm = %s"
            cursor.execute(sql, (madm,))
            conn.commit()

            if cursor.rowcount > 0:
                print(f"✅ Đã xóa danh mục có mã {madm} thành công!")
                return True
            else:
                print(f"⚠️ Không tìm thấy danh mục có mã {madm}.")
                return False
    except Exception as e:
        print("❌ Lỗi khi xóa danh mục:", e)
        return False
    finally:
        conn.close()