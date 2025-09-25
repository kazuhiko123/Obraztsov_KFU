#получаем строку
vegetables_input= input('Введите овощи через запятую: ')

#приводим к нижнему регистру
vegetables_input_low_reg = vegetables_input.lower()
#print(vegetables_input_low_reg)

#разделяем по солвам строку и игнорируем запятыеБ добавляем в массив отдельные слова
list_of_vegetables =[veg.strip() for veg in vegetables_input_low_reg.split(',')]
print(list_of_vegetables)

#считаем уникальные буквы
uniq_letters=set()
for veg in list_of_vegetables:
    uniq_letters.update(set(veg))
letters ={x: vegetables_input.count(x) for x in uniq_letters}

#находим овощ с максимальным колличеством букв o
max_o_vegetable =''
max_o_count=0
for veg in list_of_vegetables:
    o_count=veg.count('o')
    if o_count > max_o_count:
        max_o_count = o_count
        max_o_vegetable = veg
#print(max_o_vegetable)

#создаём словарь
vowels = 'aueyio'
dict_veg_count_vowels={}
for veg in list_of_vegetables:
    counter_vowels =0
    for letter in veg:
        if letter in vowels:
            counter_vowels += 1
    dict_veg_count_vowels.update({veg: counter_vowels})
#print(dict_veg_count_vowels)

#найдём овощь с наибольшим числом гласных
max_vowels_veg=max(dict_veg_cout_vowels, key=dict_veg_count_vowels.get)
print(max_vowels_veg)
#max_value_veg=''
#max_value=0
#for key, value if dict_veg_count_vowels.items()
   # if max_value<value:
  #      max_value=value
 #       max_value_veg=key
#print(max_value_veg)

#сформируем список овощей, длинна которых больше средней длинны по всем овощам
lis_wtthout_space = vegetabels_input.replace(' ', '')
list_wtthout_space_commo = list_wtthout_space.replace(',','')
list_word = list_wtthout_space.split(',')


 #кортеж с обратным порядком ввода
reverse_veg = tuple(reversed(vegetables_list)
print(reverse_veg)
                    
 #встречаюстя ли овощи на букву с или к

# спросить n и вывесть овощи колличество букв которых больше n
n = int(input('введите число n: ')
count_letters=0
veg_list_more_n = set()
for i in list_of_vegetables:
        if len(i)>n:
            print(i)
