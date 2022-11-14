def 집에서먹기(func):
    def decorator():
        print(f'집에 있는지 확인한다')
        func()
        print(f'뒷정리를 한다.')
    return decorator


@집에서먹기
def 라면먹기():
    print(f'가이드만큼 물을 냄비에 넣는다.')
    print(f'물이 끓으면')
    print(f'가이드로 스프와 냄비를 넣고 끓인 뒤 먹는다.')


@집에서먹기
def 과자먹기():
    print(f'과자 봉지를 뜯고 먹는다.')


@집에서먹기
def 과일먹기():
    print(f'과일 껍질을 벗기고 먹는다.')


라면먹기(); print();
과자먹기(); print();
과일먹기()