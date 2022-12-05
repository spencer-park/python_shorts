basket = "사과 바나나 오렌지 딸기케이크"  # input() 예시
basket_info = {
    'items' : basket.split(),
    'len' : len(basket.split()),
    'first_item' : basket.split()[0],
    'last_item' : basket.split()[-1],
}
print(basket_info)