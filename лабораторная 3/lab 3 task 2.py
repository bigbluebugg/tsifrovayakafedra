# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, sep=","):
    first_group = participants_first_group.split(sep)
    second_group = participants_second_group.split(sep)
    common_participants = list(set(first_group) & set(second_group))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))