from queue import Queue
import pymysql


class ConnPool:
    def __init__(self, size, *args, **kwargs):
        if not isinstance(size, int) or size < 1:
            size = 8
        self._pool = Queue(size)
        for i in range(size):
            self._pool.put(pymysql.connect(*args, **kwargs))

    def get_conn(self):
        return self._pool.get()

    def return_conn(self, conn):
        self._pool.put(conn)


pool = ConnPool(4, user='root', password='123456', host='10.11.16.213', port=3306, database='xiao')
conn = pool.get_conn()