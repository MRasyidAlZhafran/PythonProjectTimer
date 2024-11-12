import time

timer = int(input("Masukkan waktunya (detik):"))

for a in range(timer, 0, -1):
    Detik = a % 60
    Menit = int(a / 60) % 60
    Jam = int(a / 3600)
    print(f"{Jam:02}:{Menit:02}:{Detik:02}")
    time.sleep(1)

print("Waktu Telah Habis!")