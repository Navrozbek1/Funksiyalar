""" PFMAM = Python'da Funksiyalar mavzusidan Algoritmik masalalar """

## 1-modul

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

## 2-modul

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

