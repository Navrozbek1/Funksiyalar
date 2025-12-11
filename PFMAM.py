""" PFMAM = Python'da Funksiyalar mavzusidan Algoritmik masalalar """

# 3QkNoQ

""" ✅✅✅✅✅✅✅✅✅✅✅ 1 - modul ✅✅✅✅✅✅✅✅✅✅✅ """

##   1.Sonning kvadratini hisoblash

# def kvadrat(son):
#     """Berilgan sonning kvadratini qaytaradi."""
#     if son == 0:
#         return 0
#     return f"{son}² = {son * son}"
#
# print(kvadrat(x := int(input("Sonni kriting: "))))

##   2.Matnni takrorlash

# def takrorlash(matn, son):
#     if son != 0:
#         return f"{matn * son}"
#     return f"Xato qiymat qayta kritng🛑"
#
# matn = input("Matini krting: ")
# son = int(input("Soni krting: "))
# print(takrorlash(matn, son))

##   3.Juft yoki toq ekanligini aniqlash

# def juft_toq(son):
#     if son % 2 == 0:
#         return True
#     return False
#
# print(juft_toq(x := int(input("Sonni kriting: "))))

##   4.Ikkita sonning yig'indisi

# def qoshish(x, y):
#     if True:
#         return f"Yig'indi: {x + y}"
#
# x = int(input("X Sonni kriting: "))
# y = int(input("Y Sonni kriting: "))
# print(qoshish(x, y))

##   5.Matn uzunligini aniqlash

# def uzunlik(matn):
#    return f"Bu {matn} uzunligi = {len(matn)} ga teng✅"
#
# print(uzunlik(x := input("Matinni kriting: ")))

##   6.Musbat yoki manfiy son

# def son_turi(son):
#     if son == 0:
#         return "Nol"
#     elif son > 0:
#         return "Musbat"
#     return "Manfiy"
#
# print(son_turi(x := int(input("Matinni kriting: "))))

##   7.Sonning modulini hisoblash

# def abs_qiymat(son):
#     if son == 0:
#         return "Xato qiymat"
#     elif son > 0:
#         return son
#     return son * -1
#
# print(abs_qiymat(son := int(input("Sonni kriting: "))))

##   8.Matnni teskari qilish

# def teskari(matn):
#     if len(matn) > 0:
#         return matn[::-1]
#     return "Qayta kriting"
#
# print(teskari(son := input("Sonni kriting: ")))

""" ✅✅✅✅✅✅✅✅✅✅✅ 2 - modul ✅✅✅✅✅✅✅✅✅✅✅ """

##    1.Faktorial hisoblash

# def faktorial(x):
#     faktorial = 1
#     for son in range(1, x + 1):
#         faktorial *= son
#
#     return f"{x}! = {faktorial}"
#
# x = int(input("Sonni kriting: "))
# print(faktorial(x))

##    2.Sonlar ro'yxatidagi juft sonlar yig'indisi

# def juft_yigindi(list1):
#     yigindi = 0
#     for i in list1:
#         if i % 2 == 0:
#             yigindi += i
#     return f"Yig'indi: {yigindi}"
#
# x = [1, 2, 3, 4, 5, 6, 7]
# print(juft_yigindi(x))

##    3.Matndagi unli harflar son

# def unli(matn):
#     unlilar = ['a','e','o','u',"o'",'i']
#     unli_lar = ''
#     for i in matn:
#         if i in unlilar:
#             unli_lar += i
#     return f"Bu matnda unli harflar: {len(unli_lar)} ta!"
#
# matn = input("Matn kiriting: ").lower()
# print(unli(matn))

##    4.Sonning darajasini hisoblash

# def daraja(x, y):
#     if x > 0 or y > 0:
#         return (f"Natija:{x} = {x**y}")
#
# x = int(input('Sonni kriting: '))
# y = int(input('Darajasini kriting: '))
# print(daraja(x, y))

##    5.Ro'yxatdagi eng katta element

# def eng_katta_son(list1):
#     katta = list1[0]
#     for i in list1:
#         if i > katta:
#             katta = i
#     return f"Ro'yxatdagi eng katta element: {katta}"
#
# print(eng_katta_son([12, 45, 78, 23, 56, 89, 90, 11]))

##    6.Matnni katta harfga aylantirish
