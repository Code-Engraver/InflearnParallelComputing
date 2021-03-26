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
import time


# 스레드 실행 함수
def thread_func(name, d):
    logging.info('Sub-Thread %s: starting', name)

    for i in d:
        print(i)

    logging.info('Sub-Thread %s: finishing', name)


# 메인 영역
if __name__ == '__main__':
    # Logging format 설정
    # 해당 파일의 logging 의 기능은 간단히 설명하면 print 함수를 이용하여 출력할 내용을
    # 일정 형태에 맞춰서 출력을 해주는 것이다.
    # 물론 그 외 파일로 저장하는 기능 등 다양한 기능을 가지고 있다.
    # Thread 는 디버깅이 어렵기 때문에 로깅을 잘 찍어줘야 한다.
    logging_format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=logging_format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.info('Main-Thread: before creating thread')

    # 함수 인자 확인
    # Daemon : Default False
    x = threading.Thread(target=thread_func, args=('First', range(20000)), daemon=True)
    y = threading.Thread(target=thread_func, args=('Two', range(10000)), daemon=True)

    logging.info('Main-Thread: before running thread')

    # 서브 스레드 시작
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

    # 메인 스레드 (메인 영역)가 끝났다 하더라도, 자식 스레드는 작업을 마무리한다.
