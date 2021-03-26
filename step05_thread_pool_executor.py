# Many Threads
# Futures : 3.2 버전 부터 지원
# ThreadPoolExecutor

# Section 5
# Multithreading - Thread(3) - ThreadPoolExecutor
# Keyword - Many Threads, concurrent.futures, (xxx)PoolExecutor

# 그룹스레드
# (1) Python 3.2 이상 표준 라이브러리 사용
# (2) concurrent.futures
# (3) with 사용으로 thread 를 생성, 소멸 라이프사이클 관리 용이
# (4) 디버깅하기가 난해함 (단점)
# (5) 대기중인 작업 -> Queue 에 담김 -> 완료 상태 조사 -> 결과 또는 예외 -> 단일화(캡슐화)

# ThreadPoolExecutor 는 Thread 를 조금 더 쉽게 사용할 수 있도록 도와주는 패키지 (내부적으로 큐 사용)
# 직접 Thread 를 디자인하는 것도 가능하다.

import logging
from concurrent.futures import ThreadPoolExecutor
import time


def task(name):
    logging.info('Sub-Thread: %s: starting', name)

    result = 0
    for i in range(10001):
        result += i

    logging.info('Sub-Thread: %s: finishing result: %d', name, result)

    return result


def main():
    logging_format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=logging_format, level=logging.INFO, datefmt='%H:%M:%S')
    
    logging.info('Main-Thread: before creating and running thread')
    
    # 실행 방법 1
    # max_workers: 작업의 개수가 넘어가면 직접 설정이 유리
    # executor = ThreadPoolExecutor(max_workers=3)
    # task1 = executor.submit(task, ('First',))
    # task2 = executor.submit(task, ('Second',))

    # return 값이 있을 경우 사용
    # print(f'task1 Result: {task1.result()}')
    # print(f'task2 Result: {task2.result()}')

    # 실행 방법 2
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = executor.map(task, ['First', 'Second', 'Third'])

        # 결과 확인
        print(list(tasks))


if __name__ == '__main__':
    main()
