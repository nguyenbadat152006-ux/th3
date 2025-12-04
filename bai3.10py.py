
import math 
def Tinh(R):
    if R <= 0:
        print("Lỗi: Bán kính phải là số dương!")
    else:
        chu_vi = 2 * math.pi * R
        dien_tich = math.pi * R ** 2
        print(f"Chu vi hình tròn: {chu_vi:.2f}")
        print(f"Diện tích hình tròn: {dien_tich:.2f}")

try:
    R = float(input("Nhập bán kính R: "))
    Tinh(R)
except ValueError:
    print("Lỗi: Vui lòng nhập một số hợp lệ!")
