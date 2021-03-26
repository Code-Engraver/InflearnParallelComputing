import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading


class FakeDataStore:
    def __init__(self):
        self.value = 0
        # Lock 을 얻는 방법
        self._lock = threading.Lock()

    def update(self, name):
        logging.info('Thread: %s: starting update', name)

        # # Lock 획득 (방법 1)
        # self._lock.acquire()
        # logging.info('Thread %s has lock', name)
        # local_copy = self.value
        # local_copy += 1
        # time.sleep(0.1)
        # self.value = local_copy
        # logging.info('Thread %s about to release lock', name)
        # # Lock 반환
        # self._lock.release()

        # Lock 획득 (방법 2)
        with self._lock:
            logging.info('Thread %s has lock', name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.info('Thread %s about to release lock', name)

        logging.info('Thread: %s: finishing update', name)


if __name__ == '__main__':
    logging_format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=logging_format, level=logging.INFO, datefmt='%H:%M:%S')

    # 클래스 인스턴스화
    store = FakeDataStore()

    logging.info('Testing update. Starting value is %d', store.value)

    # With Context 시작
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First', 'Second', 'Third', 'Four']:
            executor.submit(store.update, n)

    logging.info('Testing update. Ending value is %d', store.value)
