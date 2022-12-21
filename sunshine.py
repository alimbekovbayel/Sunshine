# zadanya 2
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.
# class Furniture:
#     def __init__(self, name, squre):
#         self.name = name
#         self.squre = squre
#
#     def __str__(self):
#                  return f'Мебель: {self.name} Занятая площадь:{self.squre} квадратных метра.'
#
# class House:
#     def __init__(self, house_type, squre):
#         self.house_type = house_type
#         self.squre = squre
#         self.free_squre = squre
#         self.furniture_list = []
#
#     def __str__(self):
#                  return f'Тип дома {self.house_type} площадь {self.squre} остаточная площадь {self.free_squre} список мебели {self.furniture_list}'
#
#     def add_furniture(self,furniture):
#         self.furniture_list.append(furniture.name)
#         self.free_squre-=furniture.squre
#
#
#
# bedroom = Furniture('bedroom',4)
# wardrobe = Furniture('wardrobe',2)
# table = Furniture('table',1.5)
#
# print (bedroom)
# print (wardrobe)
# print (table)
#
#
# my_house = House ('private house', 440)
#
# my_house.add_furniture(bedroom)
# my_house.add_furniture(wardrobe)
# my_house.add_furniture(table)
#
# print (my_house)






#zadanya3
# # 3
# Students room:
# Реализуйте студенческую комнату с помощью ООП:
# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

# class Student():
#
#     def __init__(self, name: str, age: int, lessons: str):
#         self.name = name
#         self.age = age
#         self.lesson = lessons
#
#     def __repr__(self):
#         return f'<name : {self.name}, age: {self.age}, major; {self.lesson}>'
#
#
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# print(Johnny)





#zadanya 1
# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.
#
# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.

# class Soldier:
#
#     soldier = 'Ryan'
#
# class Guns(Soldier):
#
#     def __init__(self):
#         self.weopon = 'AK 47'
#         self.s_weopon = 'pistol'
#         self.ammo_1 = 30
#         self.ammo_2 = 7
#
# class Act_of_Shooting(Guns):
#
#     def shoot_AK47(self):
#         times = int(input('Сколько раз выстрельнуть из АК 47?'))
#         for bullet in range(times):
#             print('тиги-тигитиш')
#             self.ammo_1 -= 1
#             while self.ammo_1 == 0:
#                 print('Нету патронов, нужно перезаридить АК 47!')
#                 self.reload_AK47()
#
#     def shoot_pistol(self):
#         times = int(input('Сколько раз выстрельнуть из пистолета?'))
#         for bullet in range(times):
#             print('тиги-тигитиш')
#             self.ammo_2 -= 1
#             while self.ammo_2 == 0:
#                 print('Нету патронов, нужно перезаридить пистолет!')
#                 self.reload_pistol()
#
#     def reload_AK47(self):
#         print('Перезарижаю АК47!!!')
#         self.ammo_1 = 30
#
#     def reload_pistol(self):
#         print('Перезарижаю пистолет!!!')
#         self.ammo_2 = 7
#
# trial = Act_of_Shooting()
# trial.shoot_AK47()
# trial.shoot_pistol()





#zadanya 5
from random import shuffle

# class Card:
#     suits = ["червы", "бубны", "трефы", "пики"]
#     ranks = ["narf", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#
#     def __init__(self, suit=0, rank=0):
#         self.suit = suit
#         self.rank = rank
#     def __str__(self):
#         return (self.ranks[self.rank] + " из " + self.suits[self.suit])
#
#     def __cmp__(self, other):
#         # check the suits
#         if self.suit > other.suit: return 1
#         if self.suit < other.suit: return -1
#         # suits are the same... check ranks
#         if self.rank > other.rank: return 1
#         if self.rank < other.rank: return -1
#         # ranks are the same... it's a tie
#         return 0
# class Deck:
#     def __init__(self):
#         self.cards = []
#         for suit in range(4):
#             for rank in range(1, 14):
#                 self.cards.append(Card(suit, rank))
#
#     def print_deck(self):
#         for card in self.cards:
#             print(card)
#
#     def __str__(self):
#         s = ""
#         for i in range(len(self.cards)):
#             s = s + "" * i + str(self.cards[i]) + "\n"
#         return s
#
#     def shuffle(self):
#         import random
#         num_cards = len(self.cards)
#         for i in range(num_cards):
#             j = random.randrange(i, num_cards)
#             self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
#
#     def remove(self, card):
#         if card in self.cards:
#             self.cards.remove(card)
#             return True
#         else:
#             return False
#
#     def pop(self):
#         return self.cards.pop()
#
#     def is_empty(self):
#         return (len(self.cards) == 0)
#
# deck=Deck()
# print(deck)
# deck.shuffle()
# deck.print_deck()


#zadanya 4
# def dollarize(value):
#
#     value = str(value).split('.')
#     money = ''
#     count = 1
#
#     for digit in value[0][::-1]:
#         if count != 3:
#             money += digit
#             count += 1
#         else:
#             money += f'{digit},'
#             count = 1
#
#     if len(value) == 1:
#         money = ('$' + money[::-1]).replace('$-','-$')
#     else:
#         money = ('$' + money[::-1] + '.' + value[1]).replace('$-','-$')
#     return money
#
# print(dollarize(int(input("Ведите сумму: "))))
# from decimal import Decimal
#
# def moneyfmt(value, places=2, curr='', sep=',', dp='.',
#              pos='', neg='-', trailneggg=''):
#
#     q = Decimal(10) ** -places
#     sign, digits, exp = value.quantize(q).as_tuple()
#     result = []
#     digits = list(map(str, digits))
#     build, nex = result.append, digits.pop
#     if sign:
#         build(trailneggg)
#     for i in range(places):
#         build(nex() if digits else '0')
#     if places:
#         build(dp)
#     if not digits:
#         build('0')
#     i = 0
#     while digits:
#         build(nex())
#         i += 1
#         if i == 3 and digits:
#             i = 0
#             build(sep)
#     build(curr)
#     build(neg if sign else pos)
#     return ''.join(reversed(result))
#
# d = Decimal(12345678.021)
#
# print(moneyfmt(d, curr='$'))
# print(moneyfmt(d, places=0, sep='.', dp='', neg='', trailneggg='-'))
# print(moneyfmt(d, curr='$', neg='(', trailneggg=')'))
# print(moneyfmt(Decimal(1234567.021), sep=' '))
# print(moneyfmt(Decimal('-0.03'), neg='<', trailneggg='>'))






