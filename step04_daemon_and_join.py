# Daemon Thread 개념
# Join 개념

# Section 4
# Multithreading - Thread(2) - Daemon, Join
# Keyword - DaemonThread, Join

# DaemonThread(데몬스레드)
# (1) 백그라운드에 실행
# (2) 메인스레드 종료 시 즉시 종료 (핵심)
# (3) 주로 백그라운드 무한 대기 이벤트 발생 실행하는 부분 담당 -> JVM(가비지 컬렉션), 자동 저장 기능
# (4) 일반 스레드는 작업 종료 시까지 실행되는 것과 차이가 있음

import logging
import threading


# 스레드 실행 함수
def thread_func(name, d):
    logging.info('Sub-Thread %s: starting', name)

    for i in d:
        print(i)

    logging.info('Sub-Thread %s: finishing', name)


# 메인 영역
if __name__ == '__main__':
    logging_format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=logging_format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.info('Main-Thread: before creating thread')

    # Daemon : Default False
    x = threading.Thread(target=thread_func, args=('First', range(20000)), daemon=True)
    y = threading.Thread(target=thread_func, args=('Two', range(10000)), daemon=True)

    logging.info('Main-Thread: before running thread')

    x.start()
    y.start()

    # DaemonThread 확인
    # print(x.isDaemon())

    # 데몬스레드일 때도 join을 사용하면 스레드가 끝나길 기다린다.
    # 데몬스레드를 할 때는 join 을 같이 사용하지 않는다.
    # x.join()
    # y.join()

    logging.info('Main-Thread: wait for the thread to finish')

    logging.info('Main-Thread: all done')
