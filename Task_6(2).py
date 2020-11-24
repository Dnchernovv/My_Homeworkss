indexes = (input('Введите индексы продуктов: ')).split()
products = []
prices = []
quantity = []
units = []
index_1 = indexes[0]
index_2 = indexes[1]
index_3 = indexes[2]
value_names = ['название','цена','количество','единицы измерения']
product_1_info = input('Введите значения для продукта 1: ').split()
products.append(product_1_info[0])
prices.append(product_1_info[1])
quantity.append(product_1_info[2])
units.append(product_1_info[3])
product_1 = dict(zip(value_names,product_1_info))
product_1_index = tuple((index_1,product_1))
product_2_info = input('Введите значения для продукта 2: ').split()
products.append(product_2_info[0])
prices.append(product_2_info[1])
quantity.append(product_2_info[2])
units.append(product_2_info[3])
product_2 = dict(zip(value_names,product_2_info))
product_2_index = tuple((index_2,product_2))
product_3_info = input('Введите значения для продукта 3: ').split()
products.append(product_3_info[0])
prices.append(product_3_info[1])
quantity.append(product_3_info[2])
units.append(product_3_info[3])
product_3 = dict(zip(value_names,product_3_info))
product_3_index = tuple((index_3,product_3))
goods = [product_1_index,product_2_index,product_3_index]
everything = [products,prices,quantity,units]
product_analytics = dict(zip(value_names,everything))
print(product_analytics, goods)