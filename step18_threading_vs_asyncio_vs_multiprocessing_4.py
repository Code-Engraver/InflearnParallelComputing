# Section 18
# Concurrency, CPU Bound vs I/O Bound - I/O Bound(2) - threading vs asyncio vs multiprocessing
# Keyword - I/O Bound, requests

import asyncio
import aiohttp
import time

# I/O Bound Asyncio 예제
# threading 보다 높은 코드 복잡도 (호출되는 순서가 보장되지 않고, 함수가 비동기적으로 실행되는지도 확인)
# Async, await 적절히 코딩

# requests 는 동기식이기 때문에 사용 불가
# aiohttp 사용


# 실행함수1(다운로드)
async def request_site(session, url):
    # 세션 확인
    print(session)
    print(session.headers)
    async with session.get(url) as response:
        print('Read Contents {0}, from {1}'.format(response.content_length, url))


# 실행함수2(요청)
async def request_all_sites(urls):
    async with aiohttp.ClientSession() as session:
        # 작업 목록
        tasks = list()
        for url in urls:
            # 테스크 목록 생성
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)

        # 테스크 확인
        # print(*tasks)
        # print(tasks)

        await asyncio.gather(*tasks, return_exceptions=True)


def main():
    # 테스트 URLS
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://realpython.com"
    ] * 5

    # 실행 시간 측정
    start_time = time.time()

    # 실행
    # 3.8+ 에서는 run 으로 실행했을 때 예외가 발생함.
    # asyncio.run(request_all_sites(urls))
    asyncio.get_event_loop().run_until_complete(request_all_sites(urls))

    # 실행 시간 종료
    duration = time.time() - start_time

    print()
    # 결과 출력
    print(f'Downloaded {len(urls)} sites in {duration} seconds')


if __name__ == '__main__':
    main()
