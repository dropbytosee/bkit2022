import unittest
from classes import music, orchestra, orchMusic
from connections import one_to_many, many_to_many
from processing import task1, task2, task3

class RK_test(unittest.TestCase):
    def setUp(self):
        orchestras = [
            orchestra(1, 'Российский национальный оркестр'),
            orchestra(2, 'Ансамбль песни и пляски'),
            orchestra(3, 'Большой симфонический оркестр'),
            orchestra(4, 'Русская филармония'),
            orchestra(5, 'Виртуозы Москвы'),
            orchestra(6, 'Местные ребята')
        ]
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
        self.one_to_many = one_to_many(musics, orchestras)
        self.many_to_many = many_to_many(musics, orchestras, orchMusics)

    def test_task1(self):
        expected_result = [('Рахманинов', 17, 'Виртуозы Москвы'),
                           ('Серов', 10, 'Ансамбль песни и пляски'), ('Варламов', 7, 'Большой симфонический оркестр')]
        result = task1(self.one_to_many)
        self.assertEqual(result, expected_result)

    def test_task2(self):
        expected_result = [('Российский национальный оркестр', (58.5, 2)), ('Виртуозы Москвы', (27.0, 2)),
                           ('Местные ребята', (26.5, 2)), ('Ансамбль песни и пляски', (24.0, 2)),
                           ('Русская филармония', (15.0, 2)), ('Большой симфонический оркестр', (10.666666666666666, 3))]
        result = task2(self.one_to_many)
        self.assertEqual(result, expected_result)

    def test_task3(self):
        expected_result = [('Российский национальный оркестр', ('Глинка', 'Чайковский', 'Бобер', 'Мусоргский')),
                           ('Русская филармония', ('Мусоргский', 'Прокофьев', 'Шопен'))]
        result = task3(self.many_to_many)
        self.assertEqual(result, expected_result)


def main():
    unittest.main()


if __name__ == '__main__':
    main()

