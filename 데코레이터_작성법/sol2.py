def 집에서먹는다(func):
    def wrapper(args):
        print('집에 있는지 확인한다')
        result = func(args)
        print('먹는다')
        return result
    return wrapper


@집에서먹는다
def 라면끓이기(item):
    print(f'{item} 가이드만큼 물을 냄비에 넣는다.')
    print(f'물이 끓으면')
    print(f'{item} 가이드로 스프와 냄비를 넣고 끓인다.')
    return "끓이기 성공"


print(라면끓이기('신라면'))