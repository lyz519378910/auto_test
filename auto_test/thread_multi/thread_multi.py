import time
import threading

def movie():
    i = 1
    while 1:
        if i == 4:
            break
        print('i watch movie {}'.format(time.ctime()))
        i += 1
        time.sleep(1)

def music():
    i = 1
    while 1:
        if i == 4:
            break
        print('i listen music {}'.format(time.ctime()))
        i += 1
        time.sleep(1)

if __name__ == '__main__':
    # movie()
    # music()
    thread1 = threading.Thread(target=movie).start()
    #args=('mysunshine',) 元组类型
    thread2 = threading.Thread(target=music).start()
    thread_list = [thread1,thread2]
    # for thread_n in thread_list:
    #     #守护线程（以主线程为主，执行主线程）
    #     thread_n.setDaemon(True)
    #     thread_n.start()
    for thread_n in thread_list:
        # #线程阻塞
        # thread_n.join()
        thread_n.setDaemon(True)
        thread_n.start()


