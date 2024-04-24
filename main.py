# 3, 7, 9, 11, 15, 16, 18, 21, 22
import random

# 3
# sonlar = (1, 15, 8, 9)
#
# for i in sonlar:
#     if i % 3 == 0:
#         print(i)


# 7

a = 1
b = 7

# a, b = b, a

# a = a + b  # a = 8 b = 7
# b = a - b  # a = 8 b = 1
# a = a - b  # a = 7 b = 1

c = a  # c = 1 a = 1 b = 7
a = b  # c = 1 a = 7 b = 7
b = c  # c = 1 a = 7 b = 1

# print(a, b)

# 9
# son = 0
# for x in range(5):
#     print(son + 1)

# 11
# sonlar = (5, 8, 12, 3)
# for i in range(1, len(sonlar) + 1):  # -1, -2, -3, -4
#     print(sonlar[-i])


# 15
# sonlar = [4, 36, 13, 61, 72]
# for i in sonlar:
#     if i == 13:
#         continue
#     print(i)


# 16
# set1 = {'olma', 'anor', 'shaftoli'}
# set2 = {'olma', 'behi', 'shaftoli'}
#
# print(set1.intersection(set2))

# n1 = 3
# n2 = -4
# n3 = 10
# musbat = 0
# manfiy = 0
# if n1 < 0:
#     musbat = musbat + 1
# else:
#     manfiy = manfiy + 1
# if n2 < 0:
#     musbat = musbat + 1
# else:
#     manfiy = manfiy + 1
# if n3<0:
#     musbat = musbat + 1
# else:
#     manfiy = manfiy + 1
# print(f'{musbat} musbat son bor ekan va {manfiy} manfiy son bor ekan')

# 18
# son = int(input("2 xonali son kiriting: "))  # 75 -> 57
#
# on = son // 10  # on = 7
# bir = son % 10  # bir = 5
#
#
# teskari = bir * 10 + on
# print(teskari)

# 21

# sonlar = [3, 6, 8, 2, 1, 13]
# natija = []
#
# for son in sonlar:
#     if son % 2 == 1:
#         natija.insert(0, son)
#     else:
#         natija.append(son)
#
# print(natija)

# 22
# def toq_juft(sonlar: list) -> list:
#     for son in sonlar:
#         if son % 2 == 1:
#             sonlar.remove(son)
#             sonlar.insert(0, son + 1)
#     return sonlar
#
#
# print(toq_juft([1, 5, 8, 10, 3]))

#
# son = int(input("Son kiriting: "))
#
# while son % 2 == 0:
#     print("Kiritilgan son juft!")
#     son = int(input("Qayta kiriting: "))

# import random
#
# a = random.randrange(1, 10)
# b = random.randrange(1, 10)
#
# c = int(input(f"{a} + {b} = "))
# while c == a + b:
#     print("Javob to'g'ri")
#     a = random.randrange(1, 10)
#     b = random.randrange(1, 10)
#
#     c = int(input(f"{a} + {b} = "))
# else:
#     print("Noto'g'ri javob kiritldi")

# son = 1
# while son:
#     print(son, end=" ")
#     son += 1
#
# son = 1
# while son <= 100:
#     print(son)
#     son += 1

# qadam = 5
#
# while qadam > 0:
#     son = int(input("Son kiriting: "))
#     if son < 0:
#         print("Manfiiy son kiritdingiz!")
#         break
#     qadam -= 1
# else:
#     print("Imkoniyatingiz tugadi")


# son = abs(int(input("Son kiriting: ")))

# xona = 0
# while son >= 1:
#     son //= 10
#     xona += 1
#
# print(xona)
# Foydalanuvchi tasodifiy sonni topguncha ishlaydigan while loop tuzing.

# son = random.randrange(1, 10)
# son2 = int(input("Son kiriting: "))
# while son != son2:
#     son2 = int(input("Son kiriting: "))
# else:
#     print("Sonni to'g'ri topdingiz")

# son1 = 3.14
# son2 = 1.24
# son3 = 1023.1293
#
# son4 = float(input("4-sonni kiriting: "))
# son5 = float(input("5-sonni kiriting: "))


# print(son1, son2, son3, son4, son5)


# men_talabaman = True
# vazifa_qilmadim = True
# kompyuterlar_ochiq = False
#
# pas = input("Passportingiz bormi: ")
# if pas == "Ha":
#     pas = True
# elif pas == "Yo'q":
#     pas = False
# else:
#     print("Ha yoki yo'q degan javob berishingiz mumkin xolos!")
#     pas = None
#
# print(pas)

# son = 365
# son = str(son)
# print(son)
# print(type(son))

# num = str()
# print(type(num), num)

# a = 10
# b = 6
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# Sonni bo'lib butun qismini olish
#
# a = 77
# b = 10
#
# print(a / b)  # 14 = 2 * 5 + 4
# print(a // b)
# print(a % b)

# print(5 ** 3)

# a = 4
# b = 7
#
# S = a * b
# P = 2 * (a + b)
#
# print("S =", S)
# print("P =", P)
#
#
# print("S =", a * b)
# print("P =", 2 * (a + b))

import math

#
# print(math.pow(10, 2))
# print(math.factorial(5))
# print(math.ceil(124.00000000000001))
# print(math.floor(124.999999))
# print(math.pi)
#
# print(math.sin(90 / 57.6))
#
# import random
#
# print(random.randrange(1, 10))
# print(random.randint(1, 10))
# print(random.random())
# print(random.uniform(1, 10))

# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))

# orta = (a + b) / 2
# print(a, "va", b, "ning o'rta arifmetigi:", orta)


# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
#
# c = math.sqrt(a**2 + b**2)
# c1 = math.pow(a**2 + b**2, 1/2)
# c2 = (a**2 + b**2)**(1/2)
#
# print(c, c1, c2)

# 1
# while True:
#     print("Codial")


# 2    81 = 3 * 3 * 3 * 3   8 = 2 * 2 * 2
# son = 81
#
# while son >= 1:
#     if son == 1:
#         print(f"3 ning darajasi")
#         break
#     son /= 3
# else:
#     print(f"3 ning darajasi emas")

# 4  n = 10   10 * 8 * 6 * 4 * 2   11 * 9 * 7 * 5 * 3 * 1
# n = int(input("Son kiriting: "))
# a = 1
# while n > 1:
#     a *= n
#     n -= 2
# print(a)

# 5
# a = int(input("son kiriting: "))
# son = a
# count = 0
# while son >= 1:  # a = 7   son = 7
#     if a % son == 0:
#         count += 1
#     if count > 2:
#         print(f"{a} - tub son emas")
#         break
#     son -= 1
# else:
#     print(f"{a} - tub son")

# 6
# sonlar = [2, 3, 1, 12, 19, 3, 12]
# summa = 0
# sanoq = 0
#
# while sanoq < len(sonlar):
#     summa += sonlar[sanoq]
#     sanoq += 1
#
# print(summa / sanoq)
#
# # 7
#
# k = int(input("k = "))
# n = int(input("n = "))
#
# while n > 0:
#     print(k)
#     n -= 1
#
# # 8
#
# n = int(input("son kiriting: "))
# son = n
# S = 0
#
# while n <= 2 * son:
#     S += n ** 2
#     n += 1
#
# print(S)

# 12
# son = int(input("Son kiriting: "))
#
# chap = son // 100  # 537 -> 5
# ong = son % 100  # 537 -> 37
#
# son = ong * 10 + chap
# print(son)

# 13
# import random
#
# son = random.randint(10, 99)
#
# yigindi = son // 10 + son % 10
# print("Son =", son, "\nYigindi =", yigindi)

# 14
# son = int(input("Son kiriting: "))
#
# bir = son % 10  # 396 -> 6
# on = son // 10 % 10  # 396 -> 9
# yuz = son // 100  # 396 -> 3
#
# teskari_son = bir * 100 + on * 10 + yuz
# print(teskari_son)

# nom = "Codial zamonaviy kasblar akademiyasi - 3 yoshda"
# ism = "Nurmuhammad"

# print(ism[5])
# print(nom[7:16])
# print(nom[:16])
# print(nom[17:])
# print(nom[-6:])
# print(nom[-1])

# matn = "TESKARI yozish uchun"
#
# print(matn[::-1])
# print(matn.upper())
# print(matn.lower())

# matn = "bahor Keldi"
# print(matn.capitalize())
#
# ismlar = "SHukurjon XojiAkbar asadbek aDHamjon nurmuhammadjon"
# print(ismlar.title())
# # print(ismlar.capitalize())
#
# text = "kichik KATTA"
# print(text.swapcase())
#
# print("Sal456om".swapcase())

matn = "Nurmuhammad yaxshi bola, Nurmuhammad vazifalarni o'z vaqtida bajaradi!"

# print(matn.index('bola'))
# print(matn.find('c'))
#
# print(matn.count("Nurmuhammad"))
# print(len(matn))
print(matn.replace("Nurmuhammad", "Shukurjon"))

matn = "Nurmuhammad yaxshi bola, Nurmuhammad vazifalarni o'z vaqtida bajaradi! Nurmuhammad"

# print(matn.find("Nurmuhammad", 30, -1))
# print(matn.count("u", 20, 30))
# print(matn.replace("Nurmuhammad", "Xojiakbar", 10))

# text = "     salom        backend kursidagilar     "
# print(text.strip())

ism = "Adhamjon"
familiya = "Sobiraliyev"
yosh = 17
telefon = "+998 94 510 50 10"

# print("Mening ismim:", ism, "\nMening familiyam:", familiya, "\nMening yoshim:", yosh, "da")
print(f"Mening ismim {ism}. Mening familiyam {familiya}. Mening yoshim {yosh}da")






