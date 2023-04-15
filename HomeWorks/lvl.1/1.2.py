# Задача 1.2.

# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут


import random
from datetime import timedelta


my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]


song_1,song_2,song_3 = random.sample(my_favorite_songs,3)
three_song_time = round(song_1[1] + song_2[1] + song_3[1], 2)
total_time = timedelta()
m, s = str(three_song_time).split(".")
total_time += timedelta(minutes=int(m), seconds=int(s))
print(f'Три песни звучат {total_time} минут')



# Пункт B.
# Есть словарь песен
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.


my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}


songs_time = random.sample(list(my_favorite_songs_dict.values()), 3)
total_time1 = timedelta()
for _ in songs_time:
    m, s = str(_).split(".")
    total_time1 += timedelta(minutes=int(m), seconds=int(s))
    print(f'Три песни звучат {total_time1} минут')


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime