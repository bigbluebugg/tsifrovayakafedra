list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count_players = len(list_players)
half_players = count_players // 2
names_team1 = list_players[:half_players]
names_team2 = list_players[half_players:]
print(names_team1)
print(names_team2)