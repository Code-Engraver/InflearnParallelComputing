from multiprocessing import Process, current_process, Value, Array
import os


# 프로세스 메모리 공유 예제(공유o)
# 실행함수
# !!! 강의 코드에 문제가 있는 것으로 보여 커뮤니티에 문의한 상태.
# !!! 해결 시 코드 정리 예정. Lock 을 이용한 코드는 기대한 결과 값이 나옴.
# def generate_update_number(v: int):
#     for _ in range(5000):
#         v.value += 1
#     print(current_process().name, 'data', v.value)
def generate_update_number(v: int):
    with v.get_lock():
        for _ in range(5000):
            v.value += 1
    print(current_process().name, 'data', v.value)


def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f'Parent process ID: {parent_process_id}')

    # 프로세스 리스트 선언
    processes = list()

    # 프로세스 메모리 공유 변수
    # from multiprocess import shared_memory 사용 가능(파이썬 3.8 이상)
    # from multiprocess import Manager 사용 가능
    # share_numbers = Array('i', range(50))  # 타입, 초기 값
    share_value = Value('i', 0)

    for _ in range(1, 10):
        # 생성
        p = Process(target=generate_update_number, args=(share_value,))
        # 배열에 담기
        processes.append(p)
        # 실행
        p.start()

    # Join
    for p in processes:
        p.join()

    # 최종 프로세스 부모 변수 확인
    print('Final Data in parent process', share_value.value)


if __name__ == '__main__':
    main()
