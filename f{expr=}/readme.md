## 친절하게 변수값을 보여주는 print()를 작성할 때...
```python
username = "Spencer"
print(f"username = {username}")
```
작성하는데 파이썬에서 지원하는 Formatting 기능을 더 잘 써봅시다. [Python 3.11.0 - 7. Input and Output](https://docs.python.org/3/tutorial/inputoutput.html?highlight=fancier%20output%20formatting#formatted-string-literals)


## f'{expr=}' 
참고 : sol1.py
포맷 표시 {}에 `expr =` 를 하면 값이 같이 나온다
```python
username = "Spencer"
print(f"username = {username}")
print(f"{username=}")
print(f"{username =}")
print(f"{username = }")
```
실행결과
```
username = Spencer
username = 'Spencer'
username='Spencer'
```

## 연산, 함수도 될까?
참고 : sol2.py sol3.py
```python
number = 10
mod = 2
print(f"number/mod = {number/mod}")
print(f"{number/mod = }")
```

```python
basket = "사과 바나나 오렌지 딸기케이크"
print(f"basket.split() = {basket.split()}")

# f"{expr=}""
basket = "사과 바나나 오렌지 딸기케이크"
print(f"{basket.split() = }")
```