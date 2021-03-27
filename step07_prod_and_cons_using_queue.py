# Section 7
# Multithreading - Thread(5) - Prod vs Cons Using Queue
# Keyword - 생산자 소비자 패턴(Producer/Consumer Pattern)

# Producer-Consumer Pattern
# (1) 멀티 스레드나 멀티 프로세싱 디자인 패턴의 정석
# (2) 서버측 프로그래밍의 핵심
# (3) 주로 허리역할 (중요)
# (4) 주로 데이터를 생산하는 쪽과 데이터를 소비하는 쪽으로 나누어져 있고,
#     이는 큐를 통해서 통신하게 된다.

# Python Event 객체
# (1) Flag 초기값(0)
# (2) Set() -> 1, Clear() -> 0, Wait(1 -> 리턴, 0 -> 대기), isSet() -> 한 플래그 상태

import concurrent.futures
import logging
import queue
import random
import threading
import time


# 생산자
def producer(q, e):
    """
        네트워크 대기 상태라 가정(서버)
        크롤링 혹은 데이터 정제 등 작업
    """
    while not e.is_set():
        message = random.randint(1, 11)
        logging.info('Producer got message: %s', message)
        q.put(message)

    logging.info('Producer received event Exiting')


# 소비자
def consumer(q, e):
    """
        응답 받고 소비하는 것으로 가정 or DB 저장
    """
    while not e.is_set() or not q.empty():
        message = q.get()
        logging.info('Consumer storing message: %s (size=%d)', message, q.qsize())

    logging.info('Consumer received event Exiting')


if __name__ == '__main__':
    logging_format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=logging_format, level=logging.INFO, datefmt='%H:%M:%S')

    # 사이즈 중요
    # 생산자가 생산한 것을 큐에 담고, 소비자는 큐에서 꺼내 소비한다.
    # 사이즈가 중요한 이유는 서비스하고자 하는 환경에 맞춰 사이즈를 정해줘야
    # 무한대로 작업량이 담기거나 병목 현상이 일어났을 때 문제가 발생하지 않는다.
    pipeline = queue.Queue(maxsize=10)

    # 이벤트 플래그 초기 값 0 (특정 속성 값)
    event = threading.Event()

    # with Context 시작
    # 스레드가 각각 생산자와 소비자 역할을 하고, 큐를 이용하여 데이터를 주고 받는다.
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
    
        # 실행 시간 조정
        time.sleep(0.1)

        logging.info('Main : about to set event')

        # 프로그램 종료
        event.set()
