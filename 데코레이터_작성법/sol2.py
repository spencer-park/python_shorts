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