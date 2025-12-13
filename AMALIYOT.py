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

# def palindrom(matn):
#     if matn == matn[::-1]:
#         return f"{matn.title()} - so'zi palindrom ✅"
#     return f"{matn.title()} - so'zi palindrom emas ❌"
#
# matn = input("Matinni kriting: ").lower()
# print(palindrom(matn))

## Masala 9: List comprehension bilan kvadratlar

# def kvadratlar(list1):
#     natija = []
#     for i in list1:
#         natija += [i**2]
#     print(f"Haqiqiy list: {list1}")
#     print(f"Kvadratga oshirilgan list: {natija}")
#
# kvadratlar([1,2,3,4,5,6,7,8,9,10])

## Masala 10: Ro'yxatni filterlash

# def musbat_son(*sonlar):
#     natija = []
#     for son in sonlar:
#         if son > 0:
#             natija.append(son)
#
#     print(f"Haqiqiy sonlar: {sonlar}")
#     print(f"Musbat sonlar: {natija}")
#
# musbat_son(1, 3, -2, 5, -1)

## Masala 11: Faktorial (iterativ)

# def faktorial(son):
#     natija = 1
#     for i in range(1, son + 1):
#         natija *= i
#     return f"{son}! = {natija}"
#
# print(faktorial(x := int(input("Sonni kriting: "))))

## Masala 12: Dictionary manipulation

# def dictionary(dict1,dict2):
#     return f"Natija: {dict1 +' '+ dict2}"
#
# print(dictionary(dict1='salom',dict2='nimagap'))

## Masala 13: Fibonacci ketma-ketligi (iterativ)
