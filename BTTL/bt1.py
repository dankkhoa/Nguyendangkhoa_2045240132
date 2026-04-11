import math
from decimal import Decimal

#Bai2
s="Hello World"
print(s[2:5])

#Bai1
a=int(input("Nhập giá trị a: "))
b=int(input("Nhập gias trị b: "))
tong=a+b
hieu=a-b
tich=a*b
thuong=a/b
print(f"Tổng:{tong} , Hiệu: {hieu}, Tích:{tich}, Thương:{thuong} ")


#Bai3
s=" Hello World "
s=s.strip()
print("Chuỗi sau khi xoá khoảng trắng:",s)
print("Chữ hoa:",s.upper())
print("Chữ thường",s.lower())
s=s.replace('H','J')
print("Sau khi thay H thành J: ",s)

# Bài 4: In "Hello World!" nếu a > b
def bai4():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    if a > b:
        print("Hello World!")
bai4()

# Bài 5: In "Yes" nếu a == b, ngược lại "No"
def bai5():
    a = bool(input("Nhập a: "))
    b = bool(input("Nhập b: "))
    if a == b:
        print("Yes")
    else:
        print("No")

bai5()

# Bài 6: In 1 nếu a==b, 2 nếu a>b, 3 nếu ngược lại
def bai6():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    if a == b:
        print(1)
    elif a > b:
        print(2)
    else:
        print(3)
bai6()

# Bài 7
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
d = float(input("Nhập d: "))
if a == b == d:
    print("Hello World!")

# Bài 8: Kiểm tra một trong hai cặp bằng nhau


a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
d = float(input("Nhập d: "))
if a == b or c == d:
    print("Hello World!")

# Bài 9: Viết câu lệnh if else trên một dòng
print("A") if a > b else print("B")

# Bài 10: Sử dụng câu lệnh điều kiện 3 ngôi lồng nhau
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print("A") if a > b else print("=") if a == b else print("B")

# Bài 11: Lọc các phần tử chẵn từ mảng a sang mảng b
n = int(input("Nhập số phần tử n: "))
a = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(value)
b = [x for x in a if x % 2 == 0]
print("Mảng a:", a)
print("Mảng b (các số chẵn):", b)

# Bài 12: Tính tổng các số chia hết cho 3 hoặc 5 trong khoảng 0-999
total = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print("Tổng các số là bội của 3 hoặc 5 từ 0 đến 999:", total)

# Bài 13 Hàm trộn hai mảng, cộng các phần tử tương ứng
def merge_arrays(arr1, arr2):
    result = []
    min_len = min(len(arr1), len(arr2))
    for i in range(min_len):
        result.append(arr1[i] + arr2[i])
    if len(arr1) > min_len:
        result.extend(arr1[min_len:])
    elif len(arr2) > min_len:
        result.extend(arr2[min_len:])
    return result
a = [3, 9, 1, 4]
b = [2, 7, 4, 3, 2, 8]
result = merge_arrays(a, b)
print("Mảng a:", a)
print("Mảng b:", b)
print("Mảng kết quả:", result)

import random

# a. Tạo mảng 2 chiều ngẫu nhiên
def tao_ma_tran(m, n):
    a = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.randint(1, 10))  # số ngẫu nhiên từ 1-10
        a.append(row)
    return a

# Hàm in ma trận
def in_ma_tran(a):
    for row in a:
        print(row)

# b. Xuất dòng k
def xuat_dong(a, k):
    print("Dòng", k, ":", a[k])

# c. Xuất cột k
def xuat_cot(a, k):
    print("Cột", k, ":")
    for i in range(len(a)):
        print(a[i][k], end=" ")
    print()

# d. Tìm dòng có tổng lớn nhất nhưng ≤ 45
def dong_tong_max_45(a):
    max_sum = -1
    index = -1
    for i in range(len(a)):
        s = sum(a[i])
        if s <= 45 and s > max_sum:
            max_sum = s
            index = i
    return index, max_sum

# e. Tìm cột có tích nhỏ nhất
def cot_tich_min(a):
    n = len(a[0])
    min_tich = float('inf')
    index = -1
    for j in range(n):
        tich = 1
        for i in range(len(a)):
            tich *= a[i][j]
        if tich < min_tich:
            min_tich = tich
            index = j
    return index, min_tich

# f. Xuất phần tử dòng chẵn, cột lẻ
def dong_chan_cot_le(a):
    print("Phần tử dòng chẵn, cột lẻ:")
    for i in range(0, len(a), 2):  # dòng chẵn
        for j in range(1, len(a[0]), 2):  # cột lẻ
            print(a[i][j], end=" ")
    print()

# g. TBC phần tử chẵn thuộc dòng lẻ
def tbc_chan_dong_le(a):
    tong = 0
    dem = 0
    for i in range(1, len(a), 2):  # dòng lẻ
        for j in range(len(a[0])):
            if a[i][j] % 2 == 0:
                tong += a[i][j]
                dem += 1
    return tong/dem if dem != 0 else 0

# h. TBC các phần tử biên
def tbc_bien(a):
    m = len(a)
    n = len(a[0])
    tong = 0
    dem = 0

    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                tong += a[i][j]
                dem += 1
    return tong / dem


m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

a = tao_ma_tran(m, n)

print("\nMa trận:")
in_ma_tran(a)

k = int(input("\nNhập k: "))

xuat_dong(a, k)
xuat_cot(a, k)

idx, s = dong_tong_max_45(a)
print("Dòng có tổng lớn nhất ≤ 45:", idx, "Tổng =", s)

idx, t = cot_tich_min(a)
print("Cột có tích nhỏ nhất:", idx, "Tích =", t)

dong_chan_cot_le(a)

print("TBC phần tử chẵn dòng lẻ:", tbc_chan_dong_le(a))
print("TBC phần tử biên:", tbc_bien(a))

from datetime import datetime


class SinhVien:
    def __init__(self, ma, ten, nam_sinh, dtb):
        self.ma = ma
        self.ten = ten
        self.nam_sinh = nam_sinh
        self.dtb = dtb

def nhap_ds(n):
    ds = []
    for i in range(n):
        print(f"\nNhập sinh viên {i+1}:")
        ma = input("Mã SV: ")
        ten = input("Tên: ")
        nam_sinh = int(input("Năm sinh: "))
        dtb = float(input("Điểm TB: "))
        ds.append(SinhVien(ma, ten, nam_sinh, dtb))
    return ds


# c. Đếm SV đủ điều kiện lên lớp
def dem_len_lop(ds):
    return sum(1 for sv in ds if sv.dtb >= 5)


# d. Xuất SV >= 20 tuổi
def sv_du_20_tuoi(ds):
    nam_ht = datetime.now().year
    print("\nSinh viên >= 20 tuổi:")
    for sv in ds:
        if nam_ht - sv.nam_sinh >= 20:
            print(sv.ma, sv.ten, sv.nam_sinh, sv.dtb)


# e. Đếm SV hệ ĐH (có "DH" ở vị trí 2,3)
def dem_he_dh(ds):
    return sum(1 for sv in ds if len(sv.ma) >= 4 and sv.ma[2:4] == "DH")


# f. Đếm SV tên Lan
def dem_ten_lan(ds):
    return sum(1 for sv in ds if sv.ten.split()[-1] == "Lan")


# g. Đếm SV họ Phan
def dem_ho_phan(ds):
    return sum(1 for sv in ds if sv.ten.split()[0] == "Phan")


def main():
    n = int(input("Nhập số sinh viên: "))
    ds = nhap_ds(n)

    print("\n--- KẾT QUẢ ---")
    print("Số SV đủ điều kiện lên lớp:", dem_len_lop(ds))

    sv_du_20_tuoi(ds)

    print("Số SV hệ đại học:", dem_he_dh(ds))
    print("Số SV tên Lan:", dem_ten_lan(ds))
    print("Số SV họ Phan:", dem_ho_phan(ds))


if __name__ == "__main__":
    main()

