#%%
import time # import library time

def worker(num):
    '''worker function'''
    for i in range(20000000): number=0 # menghitung ke 20000000, untuk benchmark
    print("Selesai")
    return

def mulai():
    for i in range(3):
        worker(i)

awal = time.time()
mulai()
akhir = time.time()
durasi = akhir-awal
print(durasi) # print durasi proses dari awal hingga selesai
# %%
