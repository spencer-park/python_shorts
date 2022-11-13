def step_case(stair: int):
    if stair < 1:
        return 0
    elif 1 <= stair < 4:
        """계단 3개를 오르는 방법의 수 =
        = ’이전 단계인 2까지 오르는 경우의 수’
        += ‘이전 단계인 1까지 오르는 경우의 수’
        += ‘한 번에 오르는 경우’
        """
        return 1 + sum([step_case(n) for n in range(1, stair)])
    else:
        """계단 4개를 오르는 방법의 수
        = ’이전 단계인 3까지 오르는 경우의 수’
        += ‘이전 단계인 2까지 오르는 경우의 수’
        += ‘이전 단계인 1까지 오르는 경우의 수’
        """
        return (
            step_case(stair - 3)
            + step_case(stair - 2)
            + step_case(stair - 1)
        )

print(f'{step_case(1) = }')
print(f'{step_case(2) = }')
print(f'{step_case(3) = }')
print(f'{step_case(4) = }')
print(f'{step_case(5) = }')
print(f'{step_case(6) = }')
print(f'{step_case(100) = }')