## 파이썬 빌트인 함수 어디까지 알아봤니
다 알아야 개발자라고 할 수 있는 건 아니지만,
알면 더 좋은 개발자가 될 수도? 라고 생각하며..
개발 공부는 안하고 언어 공부만 하는 느낌으로 파이썬 자체를 알아보는 시간을 가져보자.

### 빌트인 함수라고 되어 있으나 함수만 소개된 건 또 아니다.
아이러니하게도 파이썬 문서에서 빌트인 **함수**를 보면 함수만 설명이 되어있는 건 아니다.
- [https://docs.python.org/3/library/functions.html#built-in-functions](https://docs.python.org/3/library/functions.html#built-in-functions)

막상 들어가보면 함수가 아닌 경우가 2가지가 있는데
하나는 `class` 또 다른 하나는 `decorator`가 있다.
`class`는 대체로 기본 자료형인 `bool`, `float`과 같은 것들인데, 생성자도 함수이긴 하니 여기에 포함한 듯 하다.

다만 헷갈리는 것은 `decorator`인데 예로 `classmethod`와 `staticmethod`를 들어가보면 `@classmethod`, `@staticmethod`설명이 나온다. decorator도 함수를 감싸는, wrapper을 위한 함수이기 때문에 빌트인 함수로 표현한 것 같다. 

다만 다른 빌트인 함수와 기능의 성격이 크게 달라서, 'decorator를 빌트인 함수로 굳이 넣어야했는가?'에 대해 호불호가 나뉘는 듯하다. 특히 사용법에서 의견이 갈리는 듯한데, 1번의 class의 생성자 함수나 다른 sum, len같은 함수는 다른 모듈을 참조하지 않고 바로 사용하는 `함수(인자)`방식으로 `빌트인 함수 호출 방식`을 따르고 있으나, `@classmethod`나 `@staticmethod`는 주로 `class`의 `method` 선언 시에 붙이는 보조역할로 사용되고 있다.

### 빌트인 함수는 내장 함수?
많은 책이 Built-in-function을 내장 함수라고 번역하여 사용하고 있다.
import 과정을 필요로 하지 않는 함수들, 언제 어디서나 **항상** 사용 가능한 파이썬 내부에 구축된 함수(기능)으로 볼 수 있다.

여기에 **왜(why)?** 빌트인 함수로 구현하였는가?를 생각해보며 아래 콘텐츠를 따라가보자.
1. 필요해서
1. 자주 사용해서
1. 유용해서

---

# 어찌됐든 빌트인 함수 알아보기

## abs(x)
### 1. 간단소개
- Python의 `abs()`함수는 인자로 받은 수의 절대값을 반환합니다. 
- 양수/음수 모두 양수 값을 반환합니다.

### 2. 내장함수 추가배경
- `abs()`함수는 Python 초기 버전부터 함게 내장된 함수입니다. 즉, 파이썬의 탄생과 함께한 고참입니다.
- 수학 연산에서 자주 사용되는 함수이며, 수의 절대값을 얻는데 사용됩니다.

### 3. 매개변수
`abs(x)`
- `x`
    - 절대값 계산을 위한 숫자 하나. 즉 매개변수 하나가 필요합니다.
    - 인자로는 정수(int), 부동소수점(float), 복소수(complex)가 가능합니다.

### 4. 예제코드

#### 예시 : 정수의 abs()사용
```python
x = -10
print(abs(x))
# Output: 10
```

#### 예시 : 부동소수점의 abs()사용
```python
y = -7.3
print(abs(y))
# Output: 7.3
```

#### 예시 : 복소수의 abs()사용
```python
z = 3 + 4j
print(abs(z))
# Output: 5.0
```

### 5. 관련함수
유사한 모듈의 함수로 `math.fabs()`도 있습니다. 이 함수도 절대값을 반환하지만 부동소수점에서만 작동합니다.


---

## aiter(async_iterable)
### 1. 간단소개
- aiter()함수는 비동기 이터러블 객체(asynchronous iterable object.)에 대한 비동기 이터레이터 객체(asynchronous iterator object)를 반환합니다.
- 위를 통해 비동기 방식으로 반복 가능한 비동기 객체를 반복할 수 있습니다.
- 어렵다! 비동기는 뭐고, 또 Iterable, Iterator는 무슨 말이지.

### 2. 내장함수 추가배경
- Python 3.5부터 사용할 수 있습니다. 
- 비동기 I/O연산(입출력 연산)을 작성하기 위한 환경(infra, infrastructure) 제공하는 내장된 asyncio 모듈의 일부입니다.

### 3. 매개변수
**aiter(async_iterable)**
- `async_iterable`
    - 비동기 반복가능(Iterable) 객체 하나를 인자로 받습니다.
    - 비동기 이터러블은 파이썬에서 정의한 **비동기 이터레이션 프로토콜**을 지원하는 객체입니다. 
    - 이 프로토콜에는 호출 시 **비동기 반복자(Iterator) 개체**를 반환하는 `__aiter__()` 메서드가 필요합니다.

### 4. 예제코드

#### 예시 : 이터러블과 함께 aiter()를 사용
```python
import asyncio

async def my_coroutine():
    async for i in aiter(my_async_iterable):
        print(i)

async def my_async_iterable():
    yield 1
    yield 2
    yield 3

asyncio.run(my_coroutine())
```

### 5. 관련지식
- 비동기식 반복 가능 객체를 생성하려면 비동기 생성기 함수를 정의해야 합니다. 
- 이것은 하나 이상의 `yield` 문을 포함하고 `async` 키워드로 장식된 함수입니다. 
- 이 함수는 호출 시 비동기 iterable로 사용할 수 있는 비동기 제너레이터(generator) 객체를 반환합니다.


### 6. 관련함수
- `anext()` : `aiter()`에 의해 반환된 비동기 반복자 개체에서 다음값을 검색하는데 사용됩니다.

### 7. 내용보완
#### 비동기

#### 반복자(Iterator), 반복가능(Iterable)

#### 코루틴(coroutine)

#### yield

#### 제너레이터(generator)


---

## all(iterable)
### 1. 간단소개
- `all()`함수는 
    - True 반환 : iterable의 모든 요소가 참, 또는 iterable이 비어 있으면 
    - False 반환 : True가 아닌 상황. 즉, 하나의 요소라도 False인 경우

### 2. 내장함수 추가배경
- Python 2.5부터 사용할 수 있습니다. 
- 주로 iterable 데이터의 모든 요소가 참(True)인지 테스트할 때 사용합니다.

### 3. 매개변수
**all(iterable)** 
- iterable
    - 테스트할 iterable(반복가능)단일 인자 하나를 받습니다.
    - 필수 매개변수
    - 단일 인자를 받아 테스트 한다는 것은 역으로 '1depth만 검사한다'는 의미이기도 합니다. `all([True, [True, False], True]) # True`

### 4. 예제코드

#### 예시 :이터러블 각 유형에 all()를 사용
- iterable의 모든 요소가 참인지 테스트하는 예제
- 리스트, 튜플, set(집합), 딕셔너리(dict) 모두 iterable합니다.
    - 쉽게 iterable을 판단하는 방법 >>> for문이 가능한가?
- False를 포함하고 있으면 False를 반환합니다.
- 0을 가진 경우 False를 반환합니다. 이는 falsy(False로 처리되는 데이터)에 관하여 알아야 합니다.

```python
# Test if all elements in a list are true
lst = [True, True, False, True]
print(all(lst)) # False

# Test if all elements in a tuple are true
tup = (1, 2, 3, 4)
print(all(tup)) # True

# Test if all elements in a set are true
s = {0, 1, 2, 3, 4}
print(all(s)) # False

# Test if all elements in a dictionary are true
d = {'a': True, 'b': True, 'c': False}
print(all(d.values())) # False
```

### 5. 관련지식
- 빈 iterable 데이터는 테스트할 요소가 없습니다.
- 이 경우 all() 함수는 기본적으로 True를 반환하도록 설계되어있습니다.

### 6. 관련함수
- all() 함수는 and 연산과 처리방식이 같습니다. 모든 요소가 True여야 True를 반환합니다.
- 반대로 or 연산과 같은 처리를 하는 any() 함수가 있는데, 하나라도 True면 True를 반환합니다.
    - all(), and : 하나라도 False라면 False
    - any(), or : 하나라도 True라면 True



---

## awaitable anext(async_iterator), awaitable anext(async_iterator, default)
### 1. 간단소개
- 다른 빌트인 함수인 next()의 비동기 버전
- 비동기 이터레이터에서 다음 항목을 검색합니다.
- next()와 다르게 anext()는 코루틴(coroutine)이라서 다음 값이 검색되는 걸 대기(await)해야 합니다.

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**awaitable anext(async_iterator), awaitable anext(async_iterator, default)** 
- async_iterator
    - 다음 항목을 검색할 비동기 반복자(async_iterator) 객체입니다.
- default
    - Optional
    - 반복자가 소진된 경우(=받아올 다음 항목값이 없을 경우에) 반환할 기본값을 정합니다.
    - default 값을 정해주지 않으면 `StopAsyncIteration` 예외가 발생합니다.


### 4. 예제코드

#### 예시 : 비동기 생성 함수 작성
- 예제에서 my_async_generator() 함수는 3개의 값(항목)을 생성하는 비동기 생성기로 정의됩니다.
- main() 함수는 비동기 for 루프를 사용하여 생성기가 반환한 항목을 반복합니다.
```python
async def my_async_generator():
    yield 1
    yield 2
    yield 3

async def main():
    async for item in my_async_generator():
        print(item)

asyncio.run(main())

```

#### 예시 : +anext() 사용
- 위 예제에서 anext()를 사용해보는 예제입니다.
- 비동기 이터레이터에서 항목을 수동으로 검색하려면 다음처럼 사용합니다.
- `my_async_iterator()` 함수는 3개의 값(항목)을 생성하는 비동기 반복자 함수로 정의했습니다.
- main()함수는 anext()함수를 사용하여 반복자에서 각 항목을 수동으로 검색하고 이를 출력(print)합니다.
```python
async def my_async_iterator():
    for i in range(3):
        yield i

async def main():
    async_iterator = my_async_iterator().__aiter__()
    try:
        while True:
            item = await anext(async_iterator)
            print(item)
    except StopAsyncIteration:
        pass

asyncio.run(main())
```

#### 예시 : default를 사용하는 코드 포함
- 내용

```python
import asyncio

async def async_generator():
    for i in range(3):
        yield i

async def main():
    async_iterator = async_generator().__aiter__()
    print(await anext(async_iterator))  # prints 0
    print(await anext(async_iterator))  # prints 1
    print(await anext(async_iterator))  # prints 2
    try:
        print(await anext(async_iterator))  # raises StopAsyncIteration
    except StopAsyncIteration:
        print("Iterator is exhausted")

    default_value = "Iterator is exhausted"
    async_iterator = async_generator().__aiter__()
    print(await anext(async_iterator, default_value))  # prints 0
    print(await anext(async_iterator, default_value))  # prints 1
    print(await anext(async_iterator, default_value))  # prints 2
    print(await anext(async_iterator, default_value))  # prints "Iterator is exhausted"
```

### 5. 관련지식
- `anext()`를 사용하기 위해서는 
    - 비동기 제너레이터, 비동기 이터레이터, 코루틴 등 파이썬 비동기 프로그래밍 개념과 이에 대한 기본적인 이해가 필요합니다.
    - `async for` 반복문이라는 비동기 반복자 순회 문법이 있습니다.

---

## any(iterable)
### 1. 간단소개
- 인자로 받은 iterable에 적어도 요소 하나가 True이면 True를 반환
- iterable이 비어 있으면 False를 반환합니다.

### 2. 내장함수 추가배경
- Python 2.5부터 사용 가능한 함수
- 조건문에서 리스트(또는 다른 반복가능 객체) 요소 중 적어도 하나가 True인지(또는 True로 평가되는 값인지) 확인하는 데 사용합니다.

### 3. 매개변수
**any(iterable)** 
- iterable
    - 리스트, 튜플, Set와 같은 반복 가능한 단일 객체 하나를 인자로 받습니다.
    - all과 마찬가지로 depth 1만 검사합니다.

### 4. 예제코드

#### 예시 :설명
- 내용

```python
# Example 1: Using any() with a list
my_list = [False, True, False]
result = any(my_list)
print(result)  # Output: True

# Example 2: Using any() with a tuple
my_tuple = (0, "", None)
result = any(my_tuple)
print(result)  # Output: False

# Example 3: Using any() with a set
my_set = {"", 1, 0}
result = any(my_set)
print(result)  # Output: True

# Example 4: Using any() with an empty iterable
empty_list = []
result = any(empty_list)
print(result)  # Output: False
```

### 5. 관련지식
- bool 값
    - Python에서 True 및 False는 진리 값을 나타내는 데 사용되는 부울 값입니다. 부울 값은 비교 연산자와 논리 연산자에 의해 반환됩니다.
- 반복가능(Iterable) 객체
    - Iterable은 한 번에 하나의 요소를 반환할 수 있는 Python 객체입니다
    - List, Tuple, Set, String 등
    - for가 가능한가? 여부로 구분해봅시다.
- True/False로 처리되는 과정. falsy
    - 파이썬에선 모든 데이터가 bool()함수를 통해 True/False로 변환 가능.
    - 대체로 데이터를 True로 처리합니다. 그 외의 상황인 False는 경우가 적습니다.
    - 대표적 예로는 False, None, 0, ""(빈 문자열), 빈 컨테이너(list, tuple 등)
    - False로 처리되는(falsy)만 알면, 나머지는 모두 True로 처리됩니다.

### 6. 관련함수
- all()
    - all() 함수는 iterable 모든 요소가 True인 경우에만 True를 반환
- filter()
    - filter() 함수는 특정 조건을 만족하는 iterable에서 요소를 필터링하는 함수
    - 조건을 만족하는 요소만 포함하는 새로운 iterable을 반환합니다.
    - 조건을 하나라도 만족하는 데이터만 뽑는다면 filter와 any를 같이 사용해볼 수 있습니다.

---

## ascii(object)
### 1. 간단소개
- ascii()함수는 객체의 출력가능한(printable) 표현이 포함된 문자열을 반환합니다. 
- 여기서 나오는 문자열 표현은 파이썬 코드에서 리터럴(literal, 데이터 그 자체)로 사용할 수 있는 ASCII 문자열 형식입니다.
    - 리터럴에 대해 이해하려면 메모리와 인스턴스에 대한 개념을 알아야 합니다.
    - 리터럴 데이터는 사용한다는 것은, 새롭게 값을 만드는 것이 아닌 기본적으로 있는 데이터를 빌려 사용하는 것을 의미합니다. (말이 좀 어렵죠?)
- ASCII가 아닌 문자는 이스케이프(\\) 시퀀스로 대체됩니다.

### 2. 내장함수 추가배경
- Python 2.0에 도입
- 사람이 읽을 수 있는 형식으로 객체를 표현하고자 만든 유틸리티 함수입니다.
    - 현재 프로그래머들이 직접적으로 쓸 일은 임베디드 개발자 이 외에는 흔치 않다.

### 3. 매개변수
**ascii(object)** 
- object
    - ASCII 문자열로 표현할 객체입니다.

### 4. 예제코드

#### 예시 : 문자열에 ascii() 사용
```python
>>> ascii('hello')
"'hello'"
```

#### 예시 : Using ascii() on a list
```python
>>> my_list = [1, 'hello', 'world', 'こんにちは', '안녕하세요']
>>> ascii(my_list)
'[1, 'hello', 'world', '\\u3053\\u3093\\u306b\\u3061\\u306f', '\\uc548\\ub155\\ud558\\uc138\\uc694']'
```

#### 예시 : ASCII가 아닌 문자에 ascii() 사용
```python
>>> ascii('안녕하세요')
"'\\uc548\\ub155\\ud558\\uc138\\uc694'"
```

### 5. 관련지식
- `ascii()`과 `repr()`는 함수 구현 목적은 비슷하지만 접근 방식과 출력 결과가 완전히 다릅니다.
- `ascii()`는 파이썬 코드에서 리터럴로 사용할 수 있는 문자열을 생성합니다.
- 반면 `repr()`은 인터프리터가 재구성할 수 있는 형식으로 객체를 나타내는 문자열을 생성하기 위한 것입니다.

### 6. 관련함수
- `ascii()`와 관련된 다른 내장 함수로는 `chr()`, `ord()`, `repr()` 등이 있습니다.

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

---

## 함수명
### 1. 간단소개
- 내용

### 2. 내장함수 추가배경
- 내용

### 3. 매개변수
**함수명** 
- 매개변수
    - 내용

### 4. 예제코드

#### 예시 :설명
- 내용

```python

```

### 5. 관련지식
- 내용

### 6. 관련함수
- 내용

