# 기초 Thread 생성 예제
# Main(Parent) Thread vs Sub(Child) Thread

# Section 3
# Multithreading - Thread(1) - Basic
# Keyword - Threading basic

import logging
import threading
import time


# 스레드 실행 함수
def thread_func(name):
    logging.info('Sub-Thread %s: starting', name)
    time.sleep(3)
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
    x = threading.Thread(target=thread_func, args=('First',))

    logging.info('Main-Thread: before running thread')

    # 서브 스레드 시작
    x.start()

    # 주석 전후 결과 확인
    # 자식 스레드가 끝날 때까지 기다려준다.
    # x.join()

    logging.info('Main-Thread: wait for the thread to finish')

    logging.info('Main-Thread: all done')

    # 메인 스레드 (메인 영역)가 끝났다 하더라도, 자식 스레드는 작업을 마무리한다.
