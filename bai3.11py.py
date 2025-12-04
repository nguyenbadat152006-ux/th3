def benefit(t, n, k):
    if t < 0 or n <= 0 or k <= 0:
        print("Lỗi: Dữ liệu nhập không hợp lệ!")
        return
    S = n * (1 + t / 100) ** k
    print(f"Số tiền nhận được sau {k} tháng là: {S:.2f} đồng")
try:
    t = float(input("Nhập lãi suất hàng tháng (t %): "))
    n = float(input("Nhập số vốn ban đầu (n): "))
    k = int(input("Nhập số tháng gửi (k): "))
    benefit(t, n, k)
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ!")
