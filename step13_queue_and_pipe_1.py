# Section 13
# Parallelism with Multiprocessing - Multiprocessing(5) - Queue, Pipe
# Keyword - Queue, Pipe, Communications between processes

# 프로세스 통신 구현 Queue
from multiprocessing import Process, Queue, current_process
import time
import os


# 실행 함수
def worker(identifier, base_num, q):
    process_id = os.getpid()
    process_name = current_process().name

    # 누적
    sub_total = 0

    # 계산
    for _ in range(base_num):
        sub_total += 1

    # Produce
    q.put(sub_total)

    # 정보 출력
    print(f'Process ID: {process_id}, Process Name: {process_name} ID: {identifier}')
    print(f'Result: {sub_total}')


def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f'Parent Process ID: {parent_process_id}')

    # 프로세스 리스트 선언
    processes = list()

    # 시작 시간
    start_time = time.time()

    # Queue 선언
    queue = Queue()

    for i in range(5):
        # 생성
        t = Process(name=str(i), target=worker, args=(i, 100000000, queue))

        # 배열에 담기
        processes.append(t)

        # 시작
        t.start()

    # Join
    for process in processes:
        process.join()

    # 순수 계산 시간
    print('*** %s seconds ***' % (time.time() - start_time))

    # 종료 플래그
    queue.put('exit')

    total = 0

    # 대기
    while True:
        tmp = queue.get()
        if tmp == 'exit':
            break
        else:
            total += tmp

    print()

    print('Main-Processing Total Count={}'.format(total))
    print('Main-Processing Done!')


if __name__ == '__main__':
    main()
