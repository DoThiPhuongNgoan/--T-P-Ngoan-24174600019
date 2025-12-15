

# --- 2. THỰC HIỆN YÊU CẦU DÙNG GROUPBY VÀ AGG ---

# Yêu cầu 1: Tính chi phí trung bình theo khoa.
print("## 1. Chi phí trung bình theo khoa")
df_chi_phi_khoa = df.groupby('Khoa').agg(
    Chi_phi_Trung_binh = ('Chi phí khám', 'mean')
).reset_index()
print(df_chi_phi_khoa)
print("\n" + "="*50 + "\n")

# Yêu cầu 2: Tính số lượt khám theo bệnh nhân (Sử dụng 'count' cho bất kỳ cột nào, ví dụ 'Khoa')
print("## 2. Số lượt khám theo bệnh nhân")
df_luot_kham_bn = df.groupby('Mã BN').agg(
    So_luot_kham = ('Khoa', 'count')
).reset_index()
print(df_luot_kham_bn)
print("\n" + "="*50 + "\n")


# Yêu cầu 3: Tính tỷ lệ BHYT trung bình (cho toàn bộ dữ liệu)
# Lưu ý: Yêu cầu này không cần GroupBy, nhưng có thể tính Trung bình BHYT theo Khoa để phân tích sâu hơn.
print("## 3. Tỷ lệ BHYT trung bình (Toàn cục)")
ty_le_bhyt_tb_toan_cuc = df['Tỷ lệ BHYT'].mean()
print(f"Tỷ lệ BHYT trung bình toàn cục: {ty_le_bhyt_tb_toan_cuc:.4f}")

# (Mở rộng) Tính tỷ lệ BHYT trung bình theo khoa
print("\n## 3. Mở rộng: Tỷ lệ BHYT trung bình theo khoa")
df_bhyt_khoa = df.groupby('Khoa').agg(
    Ty_le_BHYT_TB = ('Tỷ lệ BHYT', 'mean')
).reset_index()
print(df_bhyt_khoa)
print("\n" + "="*50 + "\n")


# Yêu cầu 4: Xác định khoa có chi phí cao nhất.
print("## 4. Khoa có chi phí khám trung bình cao nhất")
# Dựa trên kết quả từ Yêu cầu 1
khoa_chi_phi_max = df_chi_phi_khoa.loc[df_chi_phi_khoa['Chi_phi_Trung_binh'].idxmax()]
print(f"Khoa có chi phí trung bình cao nhất: {khoa_chi_phi_max['Khoa']}")
print(f"Chi phí trung bình: {khoa_chi_phi_max['Chi_phi_Trung_binh']:.0f} VND")
print("\n" + "="*50 + "\n")


# Yêu cầu 5: Phân tích liên hệ giữa tuổi và chi phí khám.
print("## 5. Phân tích liên hệ giữa tuổi và chi phí khám")
# Phương pháp 1: Tính hệ số tương quan (Correlation Coefficient)
correlation = df['Tuổi'].corr(df['Chi phí khám'])
print(f"Hệ số tương quan Pearson (Tuổi vs Chi phí khám): {correlation:.4f}")

# Phương pháp 2: Grouping theo nhóm tuổi (binning)
bins = [0, 18, 40, 60, 100]
labels = ['Thiếu nhi', 'Người trẻ (19-40)', 'Trung niên (41-60)', 'Người cao tuổi (61+)']
df['Nhom Tuoi'] = pd.cut(df['Tuổi'], bins=bins, labels=labels, right=True)

df_chi_phi_theo_tuoi = df.groupby('Nhom Tuoi', observed=True).agg(
    Chi_phi_Trung_binh = ('Chi phí khám', 'mean'),
    So_luot_kham = ('Khoa', 'count')
).reset_index()

print("\nChi phí trung bình theo nhóm tuổi:")
print(df_chi_phi_theo_tuoi)
print("\n" + "="*50 + "\n")