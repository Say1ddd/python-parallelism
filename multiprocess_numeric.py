#%%
import multiprocessing # import library multiprocessing
import time #import library time

awal = time.time()

# function yang akan dijalankan sebagai 'proses'
def worker(num):
    """worker function"""
    nama_proses = multiprocessing.current_process().name
    print ('%s: Worker%s, MULAI!' %(nama_proses,num))
    for i in range(20000000): number=0 # menghitung ke 20000000, untuk benchmarking
    print (nama_proses," SELESAI!")
    akhir=time.time()
    print (akhir-awal) # print durasi lama proses
    return

def go():
    if __name__ == '__main__': # insert proses di Windows -- tidak diperlukan di Linux
        for i in range(3): # eksekusi 3 proses
            arguments_tuple=(i,) # (num,) -- argument passed ke dalam proses function dalam bentuk tuple
            p = multiprocessing.Process(target=worker,args=arguments_tuple) # define proses
            p.start() # memulai proses
            p.join()

go()
# %%
