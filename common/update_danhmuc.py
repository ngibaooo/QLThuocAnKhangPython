from ketnoidb.ketnoi_mysql import get_connection


def update_danhmuc(madm, tendm=None, mota=None):
    conn = get_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            # Xây dựng câu lệnh động tùy dữ liệu nào được truyền vào
            sql = "UPDATE danhmuc SET "
            values = []
            updates = []

            if tendm is not None:
                updates.append("tendm = %s")
                values.append(tendm)
            if mota is not None:
                updates.append("mota = %s")
                values.append(mota)

            # Nếu không có gì để cập nhật thì dừng
            if not updates:
                print("⚠️ Không có dữ liệu cần cập nhật.")
                return False

            sql += ", ".join(updates) + " WHERE madm = %s"
            values.append(madm)

            cursor.execute(sql, tuple(values))
            conn.commit()

            if cursor.rowcount > 0:
                print(f"✅ Đã cập nhật danh mục có mã {madm} thành công!")
                return True
            else:
                print(f"⚠️ Không tìm thấy danh mục có mã {madm}.")
                return False
    except Exception as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)
        return False
    finally:
        conn.close()