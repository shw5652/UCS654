import os, sys, time, sysconfig, threading, multiprocessing
import numpy as np

def mat():
    return np.random.rand(1000, 1000)


def task(line):
    print(line)
    conMat = mat()
    results = []
    for _ in range(100):
        ranMat = mat()
        resMat = np.matmul(ranMat, conMat)
        results.append(resMat)
    
    print(line)
    return

# main
startTime = time.time()
activeThreads=threading.activeCount()
print('Active threads : ', activeThreads)
line = 'Program to multiply two matrix'
print('Program Started')
print('Thread1 Starts')
t1=threading.Thread(target=task, args=(line,))
t1.start()
print('Thread2 Starts')
t2=threading.Thread(target=task, args=(line,))
t2.start()
print('Thread3 Starts')
t3=threading.Thread(target=task, args=(line,))
t3.start()
print('Thread4 Starts')
t4=threading.Thread(target=task, args=(line,))
t4.start()
print('Thread5 Starts')
t5=threading.Thread(target=task, args=(line,))
t5.start()
print('Thread6 Starts')
t6=threading.Thread(target=task, args=(line,))
t6.start()
print('Thread7 Starts')
t7=threading.Thread(target=task, args=(line,))
t7.start()

while True:
    if threading.activeCount()==activeThreads:
        break
    else :
        print('Thread is still running (remaining %d)...' % (threading.activeCount()-activeThreads))
        time.sleep(1)

print('Thread Ends')
print('Program Finished')
print('Total time %f sec ' % (round(time.time()-startTime, 4)))