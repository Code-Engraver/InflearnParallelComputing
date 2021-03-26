# Section 2
# Multithreading - Python's GIL
# Keyword - CPython, 메모리 관리, GIL 사용 이유

# GIL(Global Interpreter Lock)
# (1) Cpython -> Python(bytecode) 실행 시 여러 thread 사용할 경우
#       단일 thread 만이 Python object 에 접근하게 제한하는 mutex
# (2) Cpython 메모리 관리가 취약 때문 (즉, Thread-safe)
# (3) 단일 스레드로 충분히 빠르다.
# (4) 프로세스가 사용 가능하기 때문에 GIL 은 문제가 없다. (Numpy/Scipy 등)
#       GIL 외부 영역에서 효율적인 코딩
# (5) 병렬 처리는 Multiprocessing, asyncio 사용 가능. (선택지 다양함)
# (6) thread 동시성 완벽 처리를 위해 -> Jython, IronPython, Stackless Python 등이 존재

# 오랜 기간동안 Cpython 을 개발하다 보니, 여러 thread 를 사용할 경우
# Thread-safe 하지 못하고, 단일 thread 로 충분히 빠르다고 판단하여
# 단일 thread 만이 Python object 에 접근하도록 제한한 것.
# 그러나 이는 다른 선택지가 많기 때문에 제약이 되진 않는다.
