user1 = [
    '피카츄', '라이츄', 
    '파이리', '꼬부기',
]

user2 = [
    '피카츄', '라이츄', 
    '파이리', '꼬부기',
    '버터플', '야도란'
]

# user1이 없는 user2의 카드
set_user1 = set(user1)
set_user2 = set(user2)
print(set_user2 - set_user1)
print(set_user2.difference(set_user1))