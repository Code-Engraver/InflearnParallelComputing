# Section 1 : Multithreading - Difference between Process and Thread
# Keyword - Process, Thread

# 운영체제에 포함되어 있는 Process 와 Thread 를 이해하는 것은 매우 중요하다.
# Multi Thread 나 Multi Process 는 숙련도에 따라서 성능의 차이가 난다. (오히려 느릴 수 있다)
# 대용량 처리를 해야하는 상황에서 잘 사용하게 되면 효율을 극대화할 수 있다.

# (1) Process
#   - 운영체제 -> 할당 받는 자원 단위(실행 중인 프로그램)
#   - CPU 동작 시간, 주소공간(독립적) => Chrome, Explorer 를 동시에 열어도 독립적으로 실행됨
#   - Code, Data, Stack, Heap 영역이 독립적 => 많은 프로그램을 띄우게 되면 독립적인 공간이 많이 잡기 때문에 느려짐.
#   - 최소 1개의 메인 스레드 보유
#   - 파이프, 파일, 소켓 등을 사용해서 프로세스간 통신 (Cost 높음) -> Context Switching

# (2) Thread
#   - process 내에 실행 흐름 단위
#   - process 자원 사용
#   - Stack 만 별도로 할당. 나머지는 공유(Code, Data, Heap)
#   - 메모리 공유(변수 공유)
#   - 한 thread 의 결과가 다른 thread 에 영향 끼침
#   - 동기화 문제는 정말 주의(디버깅 어려움)

# (3) Multi Thread
#   - 한 개의 단일 어플리케이션(응용 프로그램) -> 여러 thread 로 구성 후 작업 처리
#   - 시스템 자원 소모 감소 (process 를 띄우는 것보다는 감소. 효율성), 처리량 증가(Cost 감소)
#   - 통신 부담 감소, 디버깅 어려움, 단일 process 에는 효과 미약, 자원 공유 문제(교착 상태), process 에 영향을 줌.

# (4) Multi Process
#   - 한 개의 단일 어플리케이션(응용프로그램) -> 여러 process 로 구성 후 작업 처리
#   - 한 개의 process 문제 발생은 확산 없음 (process Kill)
#   - 캐시 체인지, Cost 비용 매우 높음(오버헤드), 복잡한 통신 방식 사용
