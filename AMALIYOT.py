"""  AMALIYOT — 25 ta amaliy masala """

## Masala 1: Salomlashish funksiyasi

# def salomlash(ism):
#     return f"Assalomu alaykum, {ism}"
#
# ism = input("Ismingizni kiriting: ").title()
# print(salomlash(ism))

## Masala 2: Katta sonni topish

# def katta(x, y):
#     if x > y:
#         return f"{x}-Katta"
#     return f"{y}-Katta"
# x = int(input("X: "))
# y = int(input("Y: "))
# print(katta(x, y))

## Masala 3: Teskari matn

# def matn(matn1):
#     if len(matn1) > 0:
#         return matn1[::-1]
#     return "Qayta kirting"
#
# x = input("Mattinni krting: ")
# print(matn(x))


## Masala 4: Ro'yxat yig'indisi

# def sonlar_yigindisi(royhat):
#     yigindi = 0
#     for i in royhat:
#         yigindi += i
#     return yigindi
#
# royhat = [1,2,3,4,5,6,7,8,9,10]
# print(sonlar_yigindisi(royhat))

## Masala 5: Katta harfga o'girish

# def katta_harflar(matn):
#     return f"(: {matn}".title()
#
# x = input("Matinni krting: ")
# print(katta_harflar(x))

## Masala 6: Tubmi yoki yo'qmi

# def tub_sonlar(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return "Bu tub son emas !"
#     return f"{x} - Tub son !"
#
# x = int(input("Sonni kirting: "))
# print(tub_sonlar(x))

## Masala 7: Takrorlanuvchi harflar

# def count_chars(text):
#     x = {}
#     for i in text:
#         if i in x:
#             x[i] += 1
#         else:
#             x[i] = 1
#     return x
# x = input("Matn kriting: ")
# print(count_chars(x))

## Masala 8: Palindrom tekshiruvi 