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
no_cards = []
for card in user2:
    if not card in user1:
        no_cards += [card,]
print(no_cards)