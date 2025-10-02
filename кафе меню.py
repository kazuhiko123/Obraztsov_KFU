
'''меню кафе'''
from random import choice

menu ={
    'coffe': 120,
    'tea': 80,
    'sandwich': 200,
    'cake': 150,
    'juice': 100
}

def all_menu_alph():
    name_sorted_menu = (sorted(menu.items(), key = lambda item: item[0]))
    for dish, price in name_sorted_menu:
        return (f'{dish}: {price} руб.')

def all_menu_price():
    price_sorted_menu =sorted(menu.items(), key = lambda item: item[1])
    for dish, price in price_sorted_menu:
        print(f'{dish}: {price}руб.')


def avg_price():
    sum_all = sum(menu.values())
    avg = sum_all / len(menu)
    return   (f'{avg}руб.')

def add_new_dish():
    name = input('Введите название блюда: ').strip()
    price = int(input('Введите стоимость блюда: '))
    menu.update({name: price})
    return 'Блюдо добавлено'

def delete_dish():
    dish = input('Введите название блюда: ').strip()
    delete = lambda x: menu.pop(dish)  if dish in menu else print('Блюдо не найдено')
    return ('блюдо удалено')

def show_low_price_dishes():
    n =int(input('Введите число: '))
    cheap_dishes = dict(filter(lambda item: item[1]<n, menu.items()))
    return cheap_dishes

def cheapest_and_mostexpensive():
    cheapest =min(menu.items(), key = lambda item: item[1])
    most_expensive = max(menu.items(), key = lambda item: item[1])
    cheapest_dish, cheapest_price = cheapest
    expensive_dish, expensive_price =most_expensive
    print(f'самое дешевое блюдо: {cheapest_dish} - {cheapest_price} руб.')
    print(f'Самое дорогое блюдо: {expensive_dish} - {expensive_price} руб.')
    return cheapest, most_expensive

def only_drinks_sorted(menu):
    drinks =['coffe', 'tea', 'juice']
    sorted_drinks = sorted(
        filter(lambda item: item[0] in drinks, menu.items()),
        key =lambda item: item[1]
    )
    print('список  напитков')
    for i, (drinks, price) in enumerate(sorted_drinks, 1):
        print(f'{i}. {drinks} - {price} руб.')

    return dict(sorted_drinks)


def new_order(menu):
    from functools import reduce
    order_dict = {

    }
    order = input("Введите список блюд через запятую: ")

    if not order:
        return 'Вы ничего не заказали'

    dishes_list = order.replace(' ','').split(',')
    print(dishes_list)
    dishes_clear = list(map(lambda order: order.strip(), dishes_list))


    order_dict.update({dish: menu[dish] for dish in list(filter(lambda dish: dish in menu, dishes_list))})

    notfound_dishes = [dish for dish in dishes_clear if dish not in menu]
    if notfound_dishes:
        return f'не найдено блюдо: {','.join(notfound_dishes)}'

    order_sum = reduce(lambda x, y: x + y, order_dict.values())

    num_order = enumerate(order_dict.items(), 1)
    if order_dict:
        pretty_str = list(map(
            lambda item: f'{item[0]}. {item[1][0].capitalize()} = {item[1][1]} руб.',
            enumerate(order_dict.items(), 1)
        ))
        print(list(pretty_str))
        for line in pretty_str:
            print(line)
    else:
        return 'заказ пуст'

    discount_add =[order_sum>500]
    if all(discount_add):
        new_order_sum = order_sum - order_sum*0.1
        return f'У вас скидка! Итого: {new_order_sum}'
    else:
        return f'Итого: {order_sum} руб.'

while __name__ =="__main__":
    choice = int(input("Выберите действие(1-9): "))
    print('1. Сортировка меню по алфавиту')
    print('2. Сортировка меню по стоимости')
    print('3. Средняя стоимость по меню')
    print('4. Добавить новое блюдо')
    print('5. Удалить блюдо')
    print('6. Показать блюда дешевле N')
    print('7. Показать самое дешевое и самое дорогое блюдо')
    print('8. Показать меню напитков')
    print('9. Сделать заказ')
    if choice ==1:
        all_menu_alph()
    if choice ==2:
        all_menu_price()
    if choice ==3:
        avg_price()
    if choice ==4:
        add_new_dish()
    if choice ==5:
        delete_dish()
    if choice ==6:
        show_low_price_dishes()
    if choice ==7:
        cheapest_and_mostexpensive()
    if choice ==8:
        only_drinks_sorted(menu)
    if choice ==9:
        new_order(menu)
