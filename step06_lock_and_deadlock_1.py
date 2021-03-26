# Section 6
# Multithreading - Thread(4) - Lock, DeadLock
# Keyword - Lock, DeadLock, Race Conditions(경쟁 상태), Thread synchronization(스레드 동기화)

# 용어 설명
# (1) 세마포어(Semaphore)
#     프로세스간 공유 된 자원에 접근 시 문제 발생 가능성이 존재하기에 한 개의 프로세스만 접근 처리 고안 (경쟁 상태 예방)
#     이해 예제: 화장실이 3개 존재하고, 대기자는 50명이 존재한다. 화장실 Key 를 3개 이용하여 50명이 이용하는 방법
# (2) 뮤텍스(Mutex)
#     공유된 자원의 데이터를 여러 스레드가 접근하는 것을 막는 것(경쟁 상태 예방)
#     이해 예제: 화장실이 1개 존재하고, 대기자는 3명이 존재한다. 화장실 Key 를 1개 이용하여 3명이 이용하는 방법
# (3) Lock: 상호 배제를 위한 잠금(Lock)처리 (데이터 경쟁) => 화장실 Key 를 이용하는 행위로 생각
# (4) 데드락(Deadlock)
#     프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황(교착 상태)
#     교착 상태란?
#     A 와 B 작업이 있을 때, A가 HDD 를 사용하고 있고, B가 Printer 를 사용하고 있다.
#     이 상태에서 A는 Printer 에 접근하려 하고, B는 HDD 에 접근하려 할 때
#     서로의 자원을 반환하지 못한 채 상대의 자원을 접근하려 하기 때문에 무한 대기 상태에 빠지게 된다.
# (5) Thread synchronization(스레드 동기화)를 통해서 안정적으로 동작하게 처리한다.(동기화 메소드, 동기화 블록)
# (6) Semaphore 와 Mutex 차이점은?
#     세마포어와 뮤텍스 개체는 모두 병렬 프로그래밍 환경에서 상호배제를 위해 사용
#     뮤텍스 개체는 단일 스레드가 리소스 또는 중요 섹션을 소비 허용
#     세마포어는 리소스에 대한 제한된 수의 동사 액세스를 허용
#     Semaphore 는 Mutex 가 될 수 있지만, Mutex 는 Semaphore 가 될 수 없다.

import logging
from concurrent.futures import ThreadPoolExecutor
import time


# 기억할 사항
# Stack 만 별도로 할당. 나머지는 공유(Code, Data, Heap)
# Stack 을 별도로 할당해야 하는 이유는 스레드 별로 함수를 호출할 경우 함수가 끝난 후에 되돌아갈 인자 값이라던지
# 함수 내에서 스레드 별로 변수를 선언해서 계산할 경우에 필요하기 때문이다.
# 클래스를 선언한 코드가 Code 영역으로 공유가 되야 실행 가능
class FakeDataStore:
    # 공유 변수 (value)
    def __init__(self):
        # 이 부분은 Data 와 Heap 영역에서 공유
        self.value = 0

    # 변수 업데이트 함수
    def update(self, name):
        logging.info('Thread: %s: starting update', name)

        # 뮤텍스 & Lock 등 동기화(Thread synchronization 필요한 부분)
        # 기대하는 값은 3이 되어야 하지만 스레드 동기화가 이루어 지지 않아 원하는 값을 얻지 못한다.
        # 공유 변수 value 를 Stack 영역에 저장하고, 값을 증가시킨 뒤 업데이트를 시키기 이전에
        # 다른 스레드에서 공유 변수 value 에 접근하여 값을 가져가기 때문이다.
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy

        logging.info('Thread: %s: finishing update', name)


if __name__ == '__main__':
    logging_format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=logging_format, level=logging.INFO, datefmt='%H:%M:%S')

    # 클래스 인스턴스화
    store = FakeDataStore()

    logging.info('Testing update. Starting value is %d', store.value)

    # With Context 시작
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First', 'Second', 'Third']:
            executor.submit(store.update, n)

    logging.info('Testing update. Ending value is %d', store.value)
