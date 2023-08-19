# %%
import multiprocessing

print(multiprocessing.cpu_count())

def square(x):
    return x * x

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pool = multiprocessing.Pool(processes=4) # 4 workers
    inputs = [0,1,2,3,4] # 5 proses
    outputs = pool.map(square, inputs) # map input ke function output
    print("Input: {}".format(inputs))
    print("Output: {}".format(outputs))

# %%
