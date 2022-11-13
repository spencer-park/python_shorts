## f-string으로 ascii, repr 출력하기
모든 문자는 컴퓨터에 문자번호로 매칭되어있고
클래스를 이미 아신다면 str와 repr의 차이는 아실 것 같습니다.
- 클래스의 `__str__`과 `__repr__`의 차이 알아보기

## 아스키, 확장 아스키까진 아는데 이모티콘도 아스키로 변환되나?
128자를 다루는 아스키 테이블, 256자를 다루는 확장 아스키.
그런데 그 밖의 문자도 아스키 코드로 변환되는 것에 의아하신 분들이 계실 것 같습니다.

이는 RFC 5137 ASCII Escaping of Unicode Characters. Ascii Safe Escaped Version으로 치환됩니다. 이것 때문에 변환은 되는거죠.

# f-string으로 ascii, repr확인하려면
파이썬의 `ascii`, `repr` 함수를 지원하지만
f-string을 활용한 포맷팅 방식으로도 할 수 있습니다. 
[7.1.1. Formatted String Literals](https://docs.python.org/3/tutorial/inputoutput.html?highlight=fancier%20output%20formatting#formatted-string-literals)
```python
text = "😇"
print(text)
print(ascii(text))
print(repr(text))

# f'{expr!s}' f'{expr!r}' f'{expr!a}'
print(f"{text!s}")  # print(f"{text}")
print(f"{text!a}")
print(f"{text!r}")
```
print가 __repr__이 아닌 __str__의 반환값을 확인하는 함수입니다. 즉 `!s`는 default입니다.