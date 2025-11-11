from common.update_danhmuc import update_danhmuc
while True:
    madm = input ("Nhap vao ma danh muc: ")
    ten=input("Nhập vào tên danh mục: ")
    mota=input("Nhập vào mô tả: ")
    update_danhmuc(madm, ten, mota)
    con=input("TIẾP TỤC: y, THOÁT: kí tự bất kì")
    if con!="y":
        break
