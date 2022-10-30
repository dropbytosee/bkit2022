from processing.classes import music, orchestra, orchMusic
from processing.connections import one_to_many, many_to_many
from processing.processing import task1, task2, task3

# Окрестры
orchestras = [
    orchestra(1, 'Российский национальный оркестр'),
    orchestra(2, 'Ансамбль песни и пляски'),
    orchestra(3, 'Большой симфонический оркестр'),
    orchestra(4, 'Русская филармония'),
    orchestra(5, 'Виртуозы Москвы'),
    orchestra(6, 'Местные ребята')
]

#Музыкальные произведения
musics = [
    music(1, 'Глинка', 60, 1),
    music(2, 'Чайковский', 38, 2),
    music(3, 'Шопен', 12, 4),
    music(4, 'Скрябин', 20, 6),
    music(5, 'Бобер', 28, 3),
    music(6, 'Рахманинов', 17, 5),
    music(7, 'Мусоргский', 33, 6),
    music(8, 'Прокофьев', 18, 4),
    music(9, 'Серов', 10, 2),
    music(10, 'Бетховен', 57, 1),
    music(11, 'Моцерт', 37, 5),
    music(12, 'Бах', 22, 3),
    music(13, 'Варламов', 7, 3)
]


# Для связи многие-ко-многим
orchMusics = [
    orchMusic(1, 1),
    orchMusic(2, 1),
    orchMusic(3, 2),
    orchMusic(4, 2),
    orchMusic(5, 1),
    orchMusic(6, 3),
    orchMusic(7, 4),
    orchMusic(8, 4),
    orchMusic(9, 5),
    orchMusic(10, 5),
    orchMusic(11, 5),
    orchMusic(12, 6),
    orchMusic(13, 6),
    orchMusic(7, 1),
    orchMusic(8, 2),
    orchMusic(2, 3),
    orchMusic(3, 4),
    orchMusic(4, 5),
    orchMusic(5, 6)
]

# Установка связей
one_to_many = one_to_many(musics, orchestras)
many_to_many = many_to_many(musics, orchestras, orchMusics)


print(*one_to_many, sep='\n', end='\n\n')
print(*many_to_many, sep='\n', end='\n\n')


def main():
    print('Task 1', task1(one_to_many), sep='\n', end='\n\n')
    print('Task 2', task2(one_to_many), sep='\n', end='\n\n')
    print('Task 3', task3(many_to_many), sep='\n', end='\n\n')


if __name__ == '__main__':
    main()
