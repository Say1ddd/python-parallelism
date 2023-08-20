# %%
import multiprocessing # import multiprocessing library

def worker(num):
    '''proses yang akan dibuat di Pool'''
    return num*2 # mengkalikan angka dengan 2

if __name__ == '__main__': # insert proses di Windows -- tidak diperlukan di Linux
    angka = [1,2,3,4,5,6,7,8,9] # list untuk reiterate dan mengkalikan dengan 2
    p = multiprocessing.Pool(2) # membuat 2 prosesor pool
    value = p.map(func=worker,iterable=angka) # mengirim angka ke pool proses
    p.close() # mematikan pool proses 
    print(value) # print value baru

# %%
