numbers = [1, 2, 3, 4, 5, 6]

# 특정 상황 : 반복해서 처리한 값들을 새로운 곳에 담는다
results1 = []
for n in numbers:
    results1.append(n * 2)
print(results1)

# 리스트 컴프리헨션
# 1. 리스트 안에 for 문을 : 이전까지 적는다.
# 2. 앞에 무엇을 남길지 적는다.
results2 = [n*2 for n in numbers]
print(results2)
print(results2 == results2)