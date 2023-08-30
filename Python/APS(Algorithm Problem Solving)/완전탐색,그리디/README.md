# 반복(Iteration)과 재귀(Recursion)

 - 반복과 재귀는 유사한 작업을 수행
 - 반복은 수행하는 작업이 완료될 때 까지 계속 반복 (for, while 구조)
 - 재귀는 주어진 문제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용하는 방법
   - 하나의 큰 문제를 해결하기 위해 더 작은 문제로 쪼개고 결과를 결합

## 반복

 - 반복되는 명령문을 실행하기 전 조건 검사에 사용할 변수의 초기값 설정
 - 조건검사
 - 반복할 명령문 실행
 - 업데이트
 - 반복을 이용한 선택정렬

    ```python
        def SelectionSort(A):
            n = len(A)
            for i in range(0, n-1):
                minI = i
                for j in range(i+1, n):
                    if A[j] < A[minI]:
                        minI = j
                A[minI], A[i] = A[i], A[minI]
    ```

## 재귀 함수(Recursie Function)

 - 함수 내부에서 직접 혹은 간접적으로 자기 자신을 호출
 - 일반적으로 재귀적 정의를 이용해 재귀 함수를 구현한다.
 - 기본 부분(basis part)와 유도 부분(inductive part)로 구성된다.
 - 재귀적 프로그램을 작성하는 것은 반복 구조에 비해 간결하고 이해하기 쉽다.
 - 함수 호출은 프로그램 메모리 구조에서 스택을 사용한다. 반복적 스택의 사용을 의미하며 메모리 및 속도에서 성능저하가 발생한다.


 차이점 | 재귀 | 반복
 ---------|----------|---------
 종료 | 재귀 함수 호출이 종료되는 베이스 | 반복문의 종료 조건
 수행 시간 | (상대적) 느림 | 빠름
 메모리 공간 | (상대적) 많이 사용 | 적게 사용
 소스 코드 길이 | 짧고 간결 | 길다
 소스 코드 형태 | 선택 구조(if...else) | 반복 구조(for, while)
 무한 반복시 | 스택 오버플로우 | CPU를 반복해서 점유

## 순열(Permutation)

 - 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것
 - 서로 다룬 n개 중 r개를 택하는 순열은 아래와 같이 표현한다.
 - nPr => nPr = n * (n-1) * (n-2) * ... * (n-r+1)
 - nPn = n! Factorial 이라 부른다.


 N | 순열의 수 | Million/sec | Billion/sec | Trillion/sec 
---------|----------|---------|---------|---------
 10 | 3628800 | . | . | .
 11 | 39916800 | seconds | . | .
 12 | 478001600 | minutes | . | .
 13 | 6227020800 | hours | seconds | .
 14 | 87178291200 | Day | Minute | .
 15 | 1307674368000 | weeks | Minutes | .
 16 | 20922789888000 | Months | Hours | Seconds
 17 | 355687428096000 | Years | Days | Minutes
 18 | 6402373705728000 | . | Months | Hours
 19 | 121645100408832000 | . | Years | Days
 20 | 2432902008176640000 | . | . | Month

 - 재귀 호출을 통한 순열 생성
```python
    def perm(i, k):
        if i == k:
            print(array)
        else:
            for j : i -> k-1:
                p[i] <-> p[j]
                perm(i+1, k)
                p[i] <-> p[j]
```

## 부분 집합 생성 방법

 - 바이너리 카운팅을 통한 부분집합 생성 코드

```python
    arr = [3, 6, 7, 1, 5, 4]
    n = len(arr)

    for i in range(0, (1<<n)): # 1 << n 부분집합의 개수
        for j in range(0, n):
            if i & (1 << j):
                print("%d"%arr[j], end="")
        print()
```

## 조합

 - 서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것을 조합(combination)이라고 부른다.
 - 재귀 호출을 이용한 조합 생성 알고리즘

```python
    an[] : n개의 원소를 가지고 있는 배열
    tr[] : r개의 크기의 배열, 조합이 임시 저장될 배열

    def comb(n, r):
        if ( r == 0 ):
            print(arr)
        elif n < r:
            return
        else:
            tr[r-1] = an[n-1]
            comb(n-1, r-1)
            comb(n-1, r)
```

 - n개에서 r개를 고르는 조합 (재귀)

```python
    def nCr(n, r, s): # n개에서 r개를 고르는 조합, s 선택할 수 있는 구간의 시작
        if r == 0:
            print(*comb)
        else:
            for i in range(s, n-r+1):
                comb[r-1] = A[i]
                nCr(n, r-1, i+1)
```