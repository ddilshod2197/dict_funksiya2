def add_item(d, key, value):
    if key in d:
        return "Kalit mavjud"
    d[key] = value
    return d

items = {'apple': 5, 'banana': 3}
print(add_item(items, 'orange', 7))   # {'apple': 5, 'banana': 3, 'orange': 7}
print(add_item(items, 'apple', 10))   # Kalit mavjud
