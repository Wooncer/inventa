import random
from collections import OrderedDict

def shuffle_dict(d):
    keys = list(d.keys())
    random.shuffle(keys)
    return OrderedDict([(k, d[k]) for k in keys])

all_positions = {
    '01. КБТ Отдельностоящая': 68,
    '02. КБТ Встраиваемая': 61,
    '03. Аксессуары к КБТ': 5,
    '04. МБТ Дом': 126,
    '05. МБТ Красота': 218,
    '06. МБТ Кухня': 131,
    '07. Посуда': 192,
    '08.Товары для дома и порядка ( аксессуары для БТ,фильтрация воды)': 128,
    '09.Бытовая химия': 47,
    '10. Климат': 50,
    '11. МБТ Напитки': 102,
    '12. Умная Техника для Дома': 28,
    '13. Освещение': 84,
    '14. Метеостанции': 5,
    '01. Компьютеры': 3,
    '02. Ноутбуки': 19,
    'Аксессуары для ноутбуков': 40,
    '01. Планшеты': 22,
    '02. Cмартфоны': 68,
    '03. Сотовые телефоны': 39,
    '04. Электронные книги': 6,
    '05. Умные часы и браслеты': 40,
    '04. Аксессуары для мобильных устройств': 464,
    '05. Фототехника и аксессуары': 13,
    '06. Флэш память': 121,
    '07. Мониторы': 23,
    '01. Телевизоры': 52,
    '02. Web камеры, Модули WiFi, 3D очки, Клавиатуры Smart TV': 13,
    '03. Видеоплееры, Приставки для цифрового ТВ, Комплекты спутникового ТВ': 18,
    '04. ТВ Антенны и антенные кабели, Кронштейны, подвесы и столы': 64,
    '05. Кабели и переходники HDMI и SCART': 22,
    '06. Переключатели, разветвители, конвертеры': 2,
    '09. Интертеймент': 65,
    '10. Аудио': 398,
    '11. Печатная техника и расходные материалы': 134,
    '12. Оргтехника': 12,
    '13. Источники питания': 177,
    '14. Комплектующие': 321,
    '15. Клавиатуры, мыши, web-камеры': 272,
    '16. Чехлы и сумки': 420,
    '17. Расходные материалы': 15,
    '18. Носители информации': 19,
    '20. Автотовары': 77,
    '21. Сетевое оборудование': 92,
    '22. Пассивное коммутационное оборудование': 177,
    '25. Программное обеспечение': 11,
    '26. Инструмент': 136,
    '44. Товары для дома (Сантехника, Текстиль, Бытовая химия)': 4
}

vlad = 0
vlad_pull = []
danil = 1
danil_pull = []
igor = 2
igor_pull = []
zamir = 3
zamir_pull = []
mihuil = 4
mihuil_pull = []

for k, v in shuffle_dict(all_positions).items():
    if vlad < danil and vlad < igor and vlad < zamir and vlad < mihuil:
        vlad += v
        vlad_pull.append(k)
    elif danil < vlad and danil < igor and danil < zamir and danil < mihuil:
        danil += v
        danil_pull.append(k)
    elif igor < vlad and igor < danil and igor < zamir and igor < mihuil:
        igor += v
        igor_pull.append(k)
    elif zamir<vlad and zamir<danil and zamir<igor and zamir<mihuil:
        zamir += v
        zamir_pull.append(k)
    else:
        mihuil += v
        mihuil_pull.append(k)

print(vlad, vlad_pull)
print(danil, danil_pull)
print(igor, igor_pull)
print(zamir, zamir_pull)
print(mihuil, mihuil_pull)

f = open('test.txt', 'w')

f.write(f'Житников: {vlad} строк. Позиции: {vlad_pull}')
f.close()