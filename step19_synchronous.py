# Section 19
# Concurrency, CPU Bound vs I/O Bound - CPU Bound(1) - Synchronous
# Keyword - CPU Bound

# CPU Bound 예제
# 고속 계산에 특화

import time


# 실행 함수 1 (계산)
def cpu_bound(number):
    return sum(i * i for i in range(number))


# 실행 함수 2
def find_sums(numbers):
    result = list()
    for number in numbers:
        result.append(cpu_bound(number))

    return result


def main():
    numbers = [5_000_000 + x for x in range(100)]

    # 확인
    # print(numbers)

    # 실행 시간 측정
    start_time = time.time()

    # 실행
    total = find_sums(numbers)

    print()

    # 결과 출력
    print(f'Total list : {total}')
    print(f'Sum : {sum(total)}')

    # 실행 시간 종료
    duration = time.time() - start_time

    print()

    # 수행 시간
    print(f'Duration : {duration} seconds')


if __name__ == '__main__':
    main()
