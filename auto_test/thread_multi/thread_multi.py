import time
import threading

def movie(name):
    i = 1
    while 1:
        if i == 4:
            break
        print('i watch movie {},{}'.format(name,time.ctime()))
        i += 1
        time.sleep(1)

def music(name):
    i = 1
    while 1:
        if i == 4:
            break
        print('i listen music {},{}'.format(name,time.ctime()))
        i += 1
        time.sleep(1)

if __name__ == '__main__':
    # movie('Tom&jerry')
    # music('mysunshine')
    # thread1 =
    threading.Thread(target=movie,args=('Tom&jerry',)).start()
    #args=('mysunshine',) 元组类型
    threading.Thread(target=music, args=('mysunshine',)).start()
    # thread_list = [thread1,thread2]
    # for thread_n in thread_list:
    #     #守护线程（以主线程为主，执行主线程）
    #     thread_n.setDaemon(True)
    #     thread_n.start()
    # for thread_n in thread_list:
    #     #线程阻塞
    #     thread_n.join()
