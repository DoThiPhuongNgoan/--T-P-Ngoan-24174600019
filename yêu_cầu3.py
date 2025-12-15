# Sử dụng groupby và agg() để tổng hợp đa chỉ số
bang_tong_hop_khoa = df.groupby('Khoa').agg(
    SoBenhNhan=('BenhNhanID', 'nunique'), # Đếm số bệnh nhân duy nhất
    SoLuotKham=('BenhNhanID', 'count'),   # Đếm tổng số lượt khám
    ChiPhiTB_Khoa=('ChiPhiKham', 'mean'), # Trung bình chi phí
    TongChiPhi=('ChiPhiKham', 'sum'),     # Tổng chi phí
    TyLeBHYT_TB=('CoBHYT', 'mean'),       # Tỷ lệ BHYT (dạng 0-1)
    TuoiTB_Khoa=('Tuoi', 'mean')          # Tuổi trung bình
).reset_index()

# Định dạng lại tỷ lệ BHYT thành phần trăm
bang_tong_hop_khoa['TyLeBHYT_TB'] = (bang_tong_hop_khoa['TyLeBHYT_TB'] * 100).round(2).astype(str) + '%'

print("\n=======================================================")
print("      BẢNG TỔNG HỢP PHÂN TÍCH THEO KHOA (Dùng agg())")
print("=======================================================")
print(bang_tong_hop_khoa)
print("=======================================================")