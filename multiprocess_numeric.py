import multiprocessing # import library multiprocessing
import time # import library time

# function yang akan dijalankan sebagai 'proses'
def worker(num):
    awal = time.time()
    for __ in range(200000000): # menghitung ke 200000000, untuk benchmark
        pass
    akhir = time.time()
    print(f"Worker {num} selesai, durasi: {akhir-awal} detik") # print durasi lama proses
    return akhir-awal

def start():
    print("menghitung 0 sampai 200000000...")
    with multiprocessing.Pool() as pool:
        durasi = max(pool.map(worker, range(3)))
    return durasi

if __name__ == "__main__":
    durasi_final = start()
    print(f"Total waktu digunakan: {durasi_final} detik")
