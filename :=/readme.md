# :=
파이썬 3.8.14부터 추가된 := 연산자(할당표현식, Assignment expression)를 알아보자.
https://docs.python.org/3/reference/expressions.html#operator-precedence

# 변수 할당시 None이 아닌 데이터를 남기는 방법
`print(age = 3)`은 에러가 발생합니다.
또한 변수 할당을 하면 그 자리는 None 상태, 즉 데이터가 없는 상태입니다. (Thonny Python으로 확인 가능)
age = 3이란 변수 할당도 하고, 그 자리에 데이터 값도 남기려면 다음처럼 해보세요
`print(age := 3)`

## 때때로 named expression(명명 표현식) walrus(바다코끼리)라고 불린다.
- 바다코끼리 표정
- 바다코끼리 연산자라고 꽤 한다.

## 상황. 변수를 아끼니 같은 함수 처리를 계속 해야될 때
- prob1.py, sol1.py

## 상황. input() 유효성 검사를 위해 while밖에 ''로 초기화 할 때
- prob2.py, sol2.py

## 상황. 변수 상황이 비어있을 때 대체 정보를 활용해야 할 경우
- prob3.py, sol3.py

## TMI : 연산자 우선순위가 최우선(3.8.14)에서 최후순(3.9)
파이썬 3.8.14와 3.9 문서의 Operator precedence를 확인해보면
처음 바다코끼리 연산자의 우선순위가 초기인 3.8 때와 지금의 우선순위가 다르다.
[3.8.14](https://docs.python.org/3.8/reference/expressions.html#operator-precedence)에는 Operator 처리 우선순위 1번에서
[3.9](https://docs.python.org/3.9/reference/expressions.html#operator-precedence)에서는 우선순위 마지막으로 이동되어있다.