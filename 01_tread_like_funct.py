from threading import Thread

def worker(arg):
    print(arg)

if __name__ == '__main__':
    
    for i in range(5):
        th = Thread(target=worker, args=(f'count th- {i}',))
        th.start()

        #hbhbh jnjn
