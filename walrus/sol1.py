basket = "사과 바나나 오렌지 딸기케이크"  # input() 예시
basket_info = {
    'items' : (items := basket.split()),
    'len' : len(items),
    'first_item' : items[0],
    'last_item' : items[-1],
}
print(basket_info)
print(items)