import logging


class MyThread(Thread):
    pass

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(massage)s')