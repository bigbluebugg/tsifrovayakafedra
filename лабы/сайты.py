users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dict_users = {
    "Общее количество" : 0,
    "Уникальные посещения" : 0
}
dict_users.update({"Общее количество": len(users)})
l = []
for i in users:
    if i not in l:
        l.append(i)
dict_users.update({"Уникальные посещения": len(l)})
print(dict_users)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
