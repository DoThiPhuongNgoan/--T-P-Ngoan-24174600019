import pandas as pd
import numpy as np

# --- 1. TẠO DỮ LIỆU GIẢ LẬP (MOCK DATA) ---
# Giả định dữ liệu bệnh viện gồm các cột cần thiết:
# 'Mã BN': ID bệnh nhân
# 'Khoa': Khoa khám bệnh (Nội, Ngoại, Nhi,...)
# 'Chi phí khám': Tổng chi phí dịch vụ
# 'Tỷ lệ BHYT': Phần trăm chi phí được BHYT chi trả (từ 0 đến 1)
# 'Tuổi': Tuổi của bệnh nhân
# 'Ngày khám': Giả lập cho việc đếm số lượt khám

data = {
    'Mã BN': [101, 102, 103, 101, 104, 105, 106, 103, 107, 108, 109, 110, 102, 101, 111],
    'Khoa': ['Nội', 'Ngoại', 'Nhi', 'Nội', 'Ngoại', 'Tim Mạch', 'Nhi', 'Nhi', 'Nội', 'Ngoại', 'Tim Mạch', 'Nội', 'Ngoại', 'Nội', 'Tim Mạch'],
    'Chi phí khám': [500000, 850000, 300000, 550000, 900000, 1200000, 350000, 320000, 600000, 800000, 1300000, 520000, 880000, 480000, 1250000],
    'Tỷ lệ BHYT': [0.5, 0.8, 0.2, 0.5, 0.8, 0.9, 0.2, 0.2, 0.5, 0.8, 0.9, 0.5, 0.8, 0.5, 0.9],
    'Tuổi': [45, 30, 5, 45, 55, 65, 8, 5, 70, 40, 62, 50, 30, 45, 68]
}

df = pd.DataFrame(data)
# Thêm cột 'Tổng chi phí thực' để phục vụ việc phân tích nâng cao (tổng chi phí khám cho từng bệnh nhân)
df['Tổng chi phí thực'] = df['Chi phí khám'] * (1 - df['Tỷ lệ BHYT'])

print("--- Dữ liệu gốc (5 dòng đầu) ---")
print(df.head())
print("\n" + "="*50 + "\n")
