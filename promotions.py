def fidelity_promo(order): # 각각의 구체적인 전략이 함수로 구현되었다.
    """충성도 포인트가 1000점 이상인 고객에게 전체 5% 할인 적용"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    """20개 이상의 동일 상품을 구입하면 10% 할인 적용"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order):
    """10종류 이상의 상품을 구입하면 전체 7% 할인 적용"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0