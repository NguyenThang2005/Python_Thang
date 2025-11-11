# --- Giao diện chính ---
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
from common import get_danhmuc
from common.delete_danhmuc import delete_danhmuc
from common.insert_danhmuc import insert_danhmuc
from common.update_danhmuc import update_danhmuc
from ketnoidb.ketnoi_mysql import connect_db


def show_danhmuc():
    for row in tree.get_children():
        tree.delete(row)
    conn = connect_db()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM danhmuc")
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=(row["id_danhmuc"], row["ten_danhmuc"], row["mota"]))
        conn.close()
root = tk.Tk()
root.title("Quản lý Danh mục - Python Tkinter + MySQL")
root.geometry("650x400")
# --- Thêm danh mục ---
def insert_danhmuc():
    ten = entry_ten.get()
    mota = entry_mota.get()

    if ten == "":
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên danh mục!")
        return

    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO danhmuc (ten_danhmuc, mota) VALUES (%s, %s)"
        cursor.execute(sql, (ten, mota))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Đã thêm danh mục!")
        show_danhmuc()
        entry_ten.delete(0, tk.END)
        entry_mota.delete(0, tk.END)
# --- Xóa danh mục ---
def delete_danhmuc():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chọn dòng", "Vui lòng chọn danh mục để xóa!")
        return

    id_dm = tree.item(selected[0])["values"][0]
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM danhmuc WHERE id_danhmuc = %s", (id_dm,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Xóa thành công", "Đã xóa danh mục!")
        show_danhmuc()

# --- Cập nhật danh mục ---
def update_danhmuc():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chọn dòng", "Vui lòng chọn danh mục để cập nhật!")
        return

    id_dm = tree.item(selected[0])["values"][0]
    ten = entry_ten.get()
    mota = entry_mota.get()

    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        sql = "UPDATE danhmuc SET ten_danhmuc=%s, mota=%s WHERE id_danhmuc=%s"
        cursor.execute(sql, (ten, mota, id_dm))
        conn.commit()
        conn.close()
        messagebox.showinfo("Cập nhật", "Đã cập nhật danh mục!")
        show_danhmuc()

# --- Khi chọn 1 dòng trong bảng ---
def on_tree_select(event):
    selected = tree.selection()
    if selected:
        item = tree.item(selected[0])
        entry_ten.delete(0, tk.END)
        entry_mota.delete(0, tk.END)
        entry_ten.insert(0, item["values"][1])
        entry_mota.insert(0, item["values"][2])
# Form nhập
frame_form = tk.Frame(root)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Tên danh mục:").grid(row=0, column=0, padx=5, pady=5)
entry_ten = tk.Entry(frame_form, width=30)
entry_ten.grid(row=0, column=1, padx=5)

tk.Label(frame_form, text="Mô tả:").grid(row=1, column=0, padx=5, pady=5)
entry_mota = tk.Entry(frame_form, width=30)
entry_mota.grid(row=1, column=1, padx=5)

# Nút chức năng
frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="➕ Thêm", width=10, command=insert_danhmuc).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="📝 Sửa", width=10, command=update_danhmuc).grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="❌ Xóa", width=10, command=delete_danhmuc).grid(row=0, column=2, padx=5)
tk.Button(frame_btn, text="🔄 Làm mới", width=10, command=get_danhmuc).grid(row=0, column=3, padx=5)

# Bảng Treeview hiển thị danh mục
columns = ("id_danhmuc", "ten_danhmuc", "mota")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
tree.heading("id_danhmuc", text="ID")
tree.heading("ten_danhmuc", text="Tên danh mục")
tree.heading("mota", text="Mô tả")
tree.pack(fill="both", expand=True, padx=10, pady=10)

tree.bind("<<TreeviewSelect>>",on_tree_select )
# Hiển thị dữ liệu ban đầu
show_danhmuc()

root.mainloop()