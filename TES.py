import matplotlib.pyplot as plt

# ==========================================
# DATA YANG SUDAH DIBERSIHKAN UNTUK GRAFIK
# ==========================================
kota = ["Makassar", "Parepare", "Palopo"]
pendapatan_kota = [2598000000, 1520000000, 1324500000]

segmen = ["Mobil", "Motor"]
pendapatan_segmen = [4710000000, 1272500000]

tanggal = ["02", "03", "05", "07", "10", "12", "15", "18", "21", "25"]
tren_pendapatan = [840000000, 292500000, 540000000, 280000000, 840000000, 270000000, 1240000000, 192000000, 1250000000, 238000000]


harga_kendaraan = [280, 19.5, 270, 35, 420, 27, 310, 32, 250, 34] # dalam juta Rupiah
jumlah_terjual = [3, 15, 2, 8, 2, 10, 4, 6, 5, 7]


# ==========================================
# GRAFIK 1: Bar Chart Pendapatan per Kota
# ==========================================
plt.figure(figsize=(6, 4))
plt.bar(kota, pendapatan_kota, color=["blue", "orange", "green"])
plt.title("Total Pendapatan per Kota")
plt.ylabel("Pendapatan (Rupiah)")
plt.xlabel("Kota")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()


# ==========================================
# GRAFIK 2: Pie Chart Proporsi Pendapatan
# ==========================================
print('\n')
plt.figure(figsize=(5, 5))
plt.pie(pendapatan_segmen, labels=segmen, autopct="%1.1f%%", startangle=90, colors=["skyblue", "lightcoral"])
plt.title("Proporsi Pendapatan Mobil vs Motor")
plt.show()


# ==========================================
# GRAFIK 3: Line Chart Tren Pendapatan
# ==========================================
print('\n')
plt.figure(figsize=(7, 4))
plt.plot(tanggal, tren_pendapatan, marker="o", color="red", linewidth=2)
plt.title("Tren Pendapatan Berdasarkan Tanggal (Januari 2025)")
plt.ylabel("Pendapatan (Rupiah)")
plt.xlabel("Tanggal")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()


# ==========================================
# GRAFIK 4: Scatter Plot Hubungan Harga & Terjual
# ==========================================
print('\n')
plt.figure(figsize=(6, 4))
plt.scatter(harga_kendaraan, jumlah_terjual, color="purple", s=100, alpha=0.8)
plt.title("Hubungan Harga Kendaraan vs Jumlah Terjual")
plt.xlabel("Harga Kendaraan (Dalam Juta Rupiah)")
plt.ylabel("Jumlah Terjual (Unit)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

print('\n')
print("Grafik telah berhasil dibuat dan ditampilkan.")
print ('BFF')