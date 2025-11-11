import tkinter as tk
from tkinter import ttk, messagebox
from zoneinfo._common import load_data

from common.delete_danhmuc import delete_danhmuc
from common.insertdanhmuc import insert_danhmuc
from common.update_danhmuc import update_danhmuc
from ketnoidb.ketnoi_mysql import get_connection


def on_row_select(event):
    selected = tree.selection()
    if selected:
        madm, tendm, mota = tree.item(selected[0])['values']
        entry_tendm.delete(0, tk.END)
        entry_tendm.insert(0, tendm)
        entry_mota.delete(0, tk.END)
        entry_mota.insert(0, mota)
def load_data():
    for row in tree.get_children():
        tree.delete(row)
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM danhmuc ORDER BY madm ASC")
            rows = cursor.fetchall()
            for row in rows:
                tree.insert("", "end", values=(row['madm'], row['tendm'], row['mota']))
        conn.close()
def insert_danhmuc():
    tendm = entry_tendm.get().strip()
    mota = entry_mota.get().strip()
    if tendm == "":
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên danh mục!")
        return
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO danhmuc (tendm, mota) VALUES (%s, %s)", (tendm, mota))
            conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Thêm danh mục thành công!")
        load_data()
        entry_tendm.delete(0, tk.END)
        entry_mota.delete(0, tk.END)


def delete_danhmuc():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục để xóa!")
        return
    madm = tree.item(selected[0])['values'][0]
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM danhmuc WHERE madm = %s", (madm,))
            conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Đã xóa danh mục!")
        load_data()


def update_danhmuc():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục để sửa!")
        return
    madm = tree.item(selected[0])['values'][0]
    tendm = entry_tendm.get().strip()
    mota = entry_mota.get().strip()
    if tendm == "":
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên danh mục!")
        return
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE danhmuc SET tendm=%s, mota=%s WHERE madm=%s", (tendm, mota, madm))
            conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Cập nhật danh mục thành công!")
        load_data()
import pymysql
# ------------------ GIAO DIỆN CHÍNH ------------------
root = tk.Tk()
root.title("Quản lý Danh Mục")
root.geometry("600x400")
root.resizable(False, False)

# Tiêu đề
tk.Label(root, text="QUẢN LÝ DANH MỤC", font=("Arial", 16, "bold"), fg="blue").pack(pady=10)

# Form nhập
frame_form = tk.Frame(root)
frame_form.pack(pady=5)

tk.Label(frame_form, text="Tên danh mục:").grid(row=0, column=0, padx=5, pady=5)
entry_tendm = tk.Entry(frame_form, width=30)
entry_tendm.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Mô tả:").grid(row=1, column=0, padx=5, pady=5)
entry_mota = tk.Entry(frame_form, width=30)
entry_mota.grid(row=1, column=1, padx=5, pady=5)

# Nút thao tác
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

tk.Button(frame_buttons, text="Thêm", command=insert_danhmuc, bg="#4CAF50", fg="white", width=10).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Sửa", command=update_danhmuc, bg="#FFC107", fg="black", width=10).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Xóa", command=delete_danhmuc, bg="#F44336", fg="white", width=10).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Làm mới", command=load_data, bg="#2196F3", fg="white", width=10).grid(row=0, column=3, padx=5)

# Bảng hiển thị
columns = ("madm", "tendm", "mota")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
tree.heading("madm", text="Mã DM")
tree.heading("tendm", text="Tên danh mục")
tree.heading("mota", text="Mô tả")
tree.pack(pady=10, fill="x", padx=10)

tree.bind("<<TreeviewSelect>>", on_row_select)

# Nạp dữ liệu khi mở app
load_data()

root.mainloop()