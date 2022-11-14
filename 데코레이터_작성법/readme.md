## 원리 자체는 쉬운 데코레이터(decorator)
이미 만들어진 함수에 앞/뒤 작업이 필요하다면 다음처럼 할 수도 있습니다.
```python
def 이미만든함수():
    return value


def 이미만든함수의앞뒤로처리할함수():
    # 실행 전 수행코드...
    result = 이미만든함수()
    # 실행 후 수행코드...
    return result


이미만든함수의앞뒤로처리할함수()
```
이와 같은 경우에 사용할 수 있는 문법에 데코레이터입니다.
함수를 통해 또 다른 함수를 만드는 것이 반복되다보면 `이미만든함수의앞뒤로처리할함수()`같이 이름이 복잡해지거나 점점 길어집니다. 대부분 `이미만든함수()`가 가장 좋은 이름일 확률도 높죠. 그대로 쓰고 싶지만, 이미 썼으니 다른 이름으로 함수 이름을 지어야하는 상황이 됩니다.

'그럼 함수를 수정하면 되지않나?'라고 생각할 수 있어요. 맞습니다.
다만 그러지 못하는 상황이 있습니다.
"기존 함수가 제 역할의 기능을 유지하고 과한 범위를 요구하여 원자성이 깨지게 될 상황"


## 이미 만들어진 함수에 덧붙이려면(X) 기존 함수들의 공통 코드를 모으려면(O)
데코레이터의 실행 과정을 보면 '함수를 인자로 받아 기능을 덧씌운다'로 진행되지만
코드를 작성하는 우리가 '처음부터 데코레이터 사용하겠다'는 접근으로 가선 안됩니다.

충분한 경험없이 데코레이터를 활용하겠단 생각부터 시작할 경우 
생각이 얽메여 코드 설계가 점점 이상해지다가 실패한 데코레이터가 나오게 되며 가독성도 굉장히 좋지 않게 됩니다.
따라서 프로그램 완성 이후 '최적화'의 과정 또는 '추상화'가 그려졌을 때 데코레이터 사용을 고려해보세요.

## 데코레이터 기본 작성법
인자와 반환값까지 고려한 데코레이터 기본 문법 구조는 다음과 같습니다.
내부에 있는 `def decorator()`는 이름이 바뀌어도 상관 없으나 wrapper`로 쓰는 것을 많이 봐왔습니다.
- 원래 매개변수라고 해야되나, 타입을 '함수'로 받으니 설명을 위해 임시로 '매개함수'란 표현을 쓰겠습니다.

```python
def 데코레이터함수(매개함수명):
    def decorator(매개함수에서받는인자)
        매개함수_실행_전_코드
        매개함수명()
        매개함수_실행_후_코드
        return 반환할_값
    return 매개함수명
```


## 예제 1 - 인자와 반환값이 없는 상황에서의 데코레이터 사용
그럼 데코레이터가 사용된 상황 예제를 비교하고 실행해보세요.
```python
def 집에서라면먹기():
    print(f'집에 있는지 확인한다')
    print(f'가이드만큼 물을 냄비에 넣는다.')
    print(f'물이 끓으면')
    print(f'가이드로 스프와 냄비를 넣고 끓인 뒤 먹는다.')
    print(f'뒷정리를 한다.')


def 집에서과자먹기():
    print(f'집에 있는지 확인한다')
    print(f'과자 봉지를 뜯고 먹는다.')
    print(f'뒷정리를 한다.')


def 집에서과일먹기():
    print(f'집에 있는지 확인한다')
    print(f'과일 껍질을 벗기고 먹는다.')
    print(f'뒷정리를 한다.')


집에서라면먹기(); print();
집에서과자먹기(); print();
집에서과일먹기()
```

```python
def 집에있는지확인(func):
    def decorator():
        print(f'집에 있는지 확인한다')
        func()
        print(f'뒷정리를 한다.')
    return decorator


@집에있는지확인
def 라면먹기():
    print(f'가이드만큼 물을 냄비에 넣는다.')
    print(f'물이 끓으면')
    print(f'가이드로 스프와 냄비를 넣고 끓인 뒤 먹는다.')


@집에있는지확인
def 과자먹기():
    print(f'과자 봉지를 뜯고 먹는다.')


@집에있는지확인
def 과일먹기():
    print(f'과일 껍질을 벗기고 먹는다.')


라면먹기(); print();
과자먹기(); print();
과일먹기()
```

## 예제 2 - 인자와 반환 값이 있는 상황에서의 데코레이터 사용
참고 : prob2.py sol2.py
```python
def 집에서라면끓이기(item):
    print(f'집에 있는지 확인한다')
    print(f'{item} 가이드만큼 물을 냄비에 넣는다.')
    print(f'물이 끓으면')
    print(f'{item} 가이드로 스프와 냄비를 넣고 끓인다.')
    return f'끓인 {item}'


def 집에서과자뜯기(item):
    print(f'집에 있는지 확인한다')
    print(f'{item} 과자 봉지를 뜯는다.')
    return f'개봉한 {item}'


def 집에서과일준비(item):
    print(f'집에 있는지 확인한다')
    print(f'과일 {item} 껍질을 벗긴다.')
    return f'껍질벗긴 {item}'


print(f'{집에서라면끓이기("신라면") = }'); print();
print(f'{집에서라면끓이기("진라면") = }'); print();
print(f'{집에서라면끓이기("삼양라면") = }')
```

```python
def 집에서준비(func):
    def decorator(item):
        print(f'집에 있는지 확인한다')
        return func(item)
    return decorator


@집에서준비
def 라면끓이기(item: str):
    print(f'{item} 가이드만큼 물을 냄비에 넣는다.')
    print(f'물이 끓으면')
    print(f'{item} 가이드로 스프와 냄비를 넣고 끓인다.')
    return f'끓인 {item}'


@집에서준비
def 과자뜯기(item: str):
    print(f'집에 있는지 확인한다')
    print(f'{item} 과자 봉지를 뜯는다.')
    return f'개봉한 {item}'


@집에서준비
def 과일준비(item: str):
    print(f'집에 있는지 확인한다')
    print(f'과일 {item} 껍질을 벗긴다.')
    return f'껍질벗긴 {item}'


print(f'{라면끓이기("신라면") = }'); print();
print(f'{라면끓이기("진라면") = }'); print();
print(f'{라면끓이기("삼양라면") = }')
```


## 프레임워크에서의 데코레이터 사용
이미 데코레이터가 준비되어 있다면? 
"너는 이것만 작성해줘! 나머지는 내가 알아서 준비해둘게"

웹 프레임워크에서 이 상황을 쉽게 볼 수 있습니다. 예시로 flask의 `route`를 사용 예제를 보겠습니다.
```python
@app.route('요청URL_path')
def 응답값계산함수():
    return "응답할_값"
```
1. 웹 페이지 요청과 이에 맞는 응답을 보내주는 처리를 하려면 
1. 라우터, URL허용 등 무슨무슨 일을 해야하는데...
1. 이거 수행하는 코드는 내가 준비해둘테니까
1. 너는 어떤 URL로 요청 받았을 때, 어떤 응답 보내줄 건지만 생각해놓고 있다가
1. 아래처럼만 작성해주면 그 외에 필요한 세팅은 돌아가도록 내가 코드 짜놓을게

추가로 `route`함수를 확인해보면 다음처럼 구현되어있다.
데코레이터를 배운 우리들이라면 위에서 작성된 `응답값계산함수`가 아래 코드 에서 `def decorator(f: F) -> F:`의 매개변수 f에 들어간다는 걸 알 수 있다.
```python
def route(self, rule: str, **options: t.Any) -> t.Callable[[F], F]:
    """Decorate a view function to register it with the given URL
    rule and options. Calls :meth:`add_url_rule`, which has more
    details about the implementation.

    .. code-block:: python

        @app.route("/")
        def index():
            return "Hello, World!"

    See :ref:`url-route-registrations`.

    The endpoint name for the route defaults to the name of the view
    function if the ``endpoint`` parameter isn't passed.

    The ``methods`` parameter defaults to ``["GET"]``. ``HEAD`` and
    ``OPTIONS`` are added automatically.

    :param rule: The URL rule string.
    :param options: Extra options passed to the
        :class:`~werkzeug.routing.Rule` object.
    """

    def decorator(f: F) -> F:
        endpoint = options.pop("endpoint", None)
        self.add_url_rule(rule, endpoint, f, **options)
        return f

    return decorator
```