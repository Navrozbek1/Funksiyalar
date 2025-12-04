# Funksiyaning sintaksisi:
# def funksiya_nomi(parametr1, parametr2, ...):
#     funksiya bajarilganda ishlaydigan qodi yozing
#     return qaytadigan qiymat

# def salomlashish(ism, familiya):
#     matn = f"Nimagapla {ism} {familiya} darsimizga hush kelibsan !"
#     return matn

# ism = input("Ismingizni kiriting: ").title()
# fam = input("Familiyangizni kiriting: ").title()

# print(salomlashish(ism, fam))

""" Bu yerda mukammal qanqulator def yordamida yaratilgan !"""

# def kankulator(x, y, belgi):
#     if belgi == '+':
#         return f"Yig'indi: {x + y} ✅"
#     elif belgi == '-':
#         return f"Ayirma: {x - y} ✅"
#     elif belgi == '*':
#         return f"Ko'paytma: {x * y} ✅"
#     elif belgi == '/':
#         return f"Bo'linma: {x / y} ✅"
#     elif belgi == '**':
#         return f"Daraja: {x ** y} ✅"
#     elif belgi == '//':
#         return f"Qoldiqsiz bo'lish: {x // y} ✅"
#     elif belgi == '√':
#         return f"Ildizi: {x ** (1/y)} ✅"
#     elif belgi == '%':
#         return f"Foyiz: {x * (y/100)} ✅"
#     elif belgi == '!':
#         faktorial = 1
#         for son in range(1, x + 1):
#             faktorial *= son
# 
#         faktorial1 = 1
#         for son in range(1, y + 1):
#             faktorial1 *= son
# 
#         return f"{x}! = {faktorial} \n{y}! = {faktorial1}"
# 
#     else:
#         return "Xato qiymat Bu belgi mavjud emas ❌"  # Agar kerak bolsa yana Qo'shimcha qoshishim mumkin
# 
# x = int(input("X:"))
# y = int(input("Y:"))
# belgi = input("Belgi:")
# 
# print(kankulator(x, y, belgi))
