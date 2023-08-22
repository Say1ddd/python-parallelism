#%%
import time # import library time

print("menghitung 0 sampai 200000000...")

def worker(num):
    awal = time.time()
    for _ in range(200000000):
        pass # menghitung 0 ke 200000000, untuk benchmark
    akhir = time.time()
    print(f"Worker {num} selesai, durasi: {akhir-awal} detik \nmenghitung..")
    return akhir-awal

def start():
    durasi = 0
    for i in range(3):
        durasi += worker(i)

total_durasi = start()
print(f"Total durasi: {total_durasi} detik") # print durasi proses dari awal hingga selesai

# %%
