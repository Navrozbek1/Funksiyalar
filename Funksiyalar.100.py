"""  Funksiyalar va Shart operatorlari mavzusidan 100 masala! """

""" 1. 📆 Yil kabisa yilmi? """

# def kabisa_yili(yil):
#     if yil % 4 == 0 or yil % 400 == 0 or yil % 100 != 0:
#         return f'Bu yil kabisa yilli ✅'
#     return "Bu kabisa yili emas!"
#
# yil= int(input("Hozirgi yilni kiriting: "))
# print(kabisa_yili(yil))

""" 2. 💡 Elektr energiyasini tejash """

# def energiya_tejash(jihozlar, vaqt):
#     if jihozlar < 5 and vaqt < 8:
#         return "Tejamkor"
#     elif jihozlar < 5 and vaqt >= 8:
#         return "O'rtacha iste'mol"
#     elif jihozlar >= 5 and vaqt < 8:
#         return "Ko'p iste'mol"
#     return "Haddan tashqari iste'mol"

# jihozlar = int(input("Uyda nechta jihoz bor? "))
# vaqt = int(input("Kuniga necha soat ishlatiladi? "))
# print(energiya_tejash(jihozlar, vaqt))

""" 3. ☕ Qahva iliqmi, issiqmi yoki sovuqmi?" """

# def qahva_holati(temperatura):
#     if temperatura > 60:
#         return "Ogoh bo‘ling! Juda issiq!"
#     elif 30 <= temperatura <= 60:
#         return "Ideal!"
#     else:
#         return "Sovib qolgan!"

# temp = float(input("Qahva haroratini kiriting (°C): "))
# print(qahva_holati(temp))

"""4. 🔋 Telefon quvvati haqida ogohlantirish. """

# def telefon_zaryadi(zaryad):
#     if zaryad < 10:
#         return "Zaryadlash zarur!"
#     elif 10 <= zaryad < 50:
#         return "Yana biroz ishlatish mumkin."
#     return "Zaryad yetarli."

# zaryad_foizi = int(input("Telefon zaryadini kiriting (%): "))
# print(telefon_zaryadi(zaryad_foysi))

""" 5. 📱 Raqam tekshiruvi — Sizning operatoringiz kim? """

# def operator_aniqlash(raqam):
#     if raqam.startswith(('+99820', '+99890', '+99891')):
#         return "Beeline"
#     elif raqam.startswith(('+99850', '+99893', '+99894')):
#         return "Ucell"
#     elif raqam.startswith(('+99887', '+99888', '+99897')):
#         return "Mobiuz"
#     elif raqam.startswith(('+99877', '+99899')):
#         return "Uzmobile"
#     elif raqam.startswith('+99898'):
#         return "Perfectum"
#     elif raqam.startswith('+99833'):
#         return "Humans"
#     return "Noma’lum operator"

# telefon_raqam = input("Telefon raqamingizni kiriting (+998...): ")
# print(operator_aniqlash(telefon_raqam))

""" 6. 📧 Email to‘g‘riligini tekshirish """

# def email_togriligi(email):
#     if "@" in email:
#         return "Email to'g'ri kiritilgan ✅"
#     return "Email noto'g'ri kiritilgan ❌"

# email_manzil = input("Email manzilingizni kiriting: ")
# print(email_togriligi(email_manzil))

""" 7. 🏫 Baholash tizimi" """

# def baholash_tizimi(ball):
#     if ball < 56:
#         return "Qoniqarsiz"
#     elif 56 <= ball < 70:
#         return "Qoniqarli"
#     elif 71 <= ball < 85:
#         return "Yaxshi"
#     return "A’lo"

# ball = int(input("O'quvchi ballini kiriting: "))
# print(baholash_tizimi(ball))

"""  8. 🎫 Kino chiptasi narxi (yoshga qarab) """

# def kino_chiptasi_narxi(yosh):
#     if yosh < 7:
#         return "Kino chiptasi narxi: Bepul"
#     elif 7 <= yosh <= 18:
#         return "Kino chiptasi narxi: 5000 so‘m"
#     elif 19 <= yosh <= 59:
#         return "Kino chiptasi narxi: 10000 so‘m"
#     return "Kino chiptasi narxi: 7000 so‘m"

# yosh = int(input("Yoshingizni kiriting: "))
# print(kino_chiptasi_narxi(yosh))

""" 9. 💬 Satr bo‘sh joy bilan tugaydimi? """

# def satr_bosh_joy(satr):
#     if satr.endswith(" "):
#         return True
#     return False

# print(satr_bosh_joy(satr := input("Satrni kiriting: ")))

"""" 10. 🏦 Karta raqami uzunligi to‘g‘rimi? """

# def karta_raqami(raqam):
#     if raqam.isdigit() and len(raqam) == 16:
#         return True
#     return False

# print(karta_raqami(raqam := input("Karta raqamini kiriting: ")))

"""" 11. 🛒 Onlayn savdo uchun chegirma hisoblash """

# def chegirma_hisoblash(narx):
#     if narx < 50000:
#         return f"Chegirma yo'q. To'lov summasi: {narx} so'm"
#     elif 50000 <= narx < 100000:
#         chegirma = narx * 0.05
#     elif 100000 <= narx < 200000:
#         chegirma = narx * 0.10
#     else:
#         chegirma = narx * 0.15
#     jami_tolov = narx - chegirma
#     return f"Chegirma: {chegirma} so'm. To'lov summasi: {jami_tolov} so'm"

# narx = float(input("Mahsulot narxini kiriting (so'm): "))
# print(chegirma_hisoblash(narx))

"""" 12. 🚕 Yo‘lkira haqini hisoblash """

# def yolkira_hisoblash(masofa):
#     if masofa <= 5:
#         return 7000
#     elif 6 <= masofa <= 15:
#         ortiqcha_km = masofa - 5
#         return 7000 + (ortiqcha_km * 1000)
#     else:
#         ortiqcha_km_15dan = masofa - 15
#         return 7000 + (10 * 1000) + (ortiqcha_km_15dan * 2000)

# masofa = float(input("Bosib o'tilgan masofani kiriting (km): "))
# print(f"Yo‘lkira: {yolkira_hisoblash(masofa)} so‘m")

"""" 13. 🧠 Aqliy test bahosi """

# def aqiliy_test(togri, notogri):
#     if togri == 0 and notogri == 0:
#         return "Baholanmadi"
#     ball = (togri * 2) - (notogri * 1)
#     return f"O'quvchining umumiy bahosi: {ball} ball"

# togri_javoblar = int(input("To'g'ri javoblar soni: "))
# notogri_javoblar = int(input("Noto'g'ri javoblar soni: "))
# print(aqiliy_test(togri_javoblar, notogri_javoblar))

""" 14. 🕒 Ish vaqti aniqlovchi """

# def ish_vaqti(soat, minut):
#     total_minutes = soat * 60 + minut
#     if 9 * 60 <= total_minutes <= 18 * 60:
#         return "Ish vaqti"
#     elif 18 * 60 < total_minutes <= 23 * 60 + 59:
#         return "Dam olish vaqti"
#     else:
#         return "Uyqu vaqti"

# soat = int(input("Soatni kiriting (0-23): "))
# minut = int(input("Minutni kiriting (0-59): "))
# print(ish_vaqti(soat, minut))

""" 15. 💼 Rezyume baholovchi """

# def rezyume_baholash(tajriba_yili, loyiha_soni):
#     if tajriba_yili < 3:
#         return "Boshlovchi"
#     elif 3 <= tajriba_yili <= 5:
#         return "O‘rta daraja"
#     elif tajriba_yili > 5 and loyiha_soni >= 1:
#         return "Tajribalilar"
#     return "Tajriba yetarli emas"

# tajriba_yili = int(input("Tajriba yilingizni kiriting: "))
# loyiha_soni = int(input("Loyihalar sonini kiriting: "))
# print(rezyume_baholash(tajriba_yili, loyiha_soni))  

""" 16. 🩺 Tana harorati bo‘yicha sog‘liq bahosi """

# def sogliq_bahosi(harorat):
#     if harorat < 36:
#         return "Past harorat"
#     elif 36 <= harorat <= 37:
#         return "Normal"
#     elif 37 < harorat <= 38:
#         return "Yengil isitma"
#     return "Yuqumli kasallik ehtimoli bor"

# harorat = float(input("Tana haroratini kiriting (°C): "))
# print(sogliq_bahosi(harorat))


""" 17. 🧾 Buyurtmani tekshirish """

# def buyurtma_tekshirish(taom1, taom2):
#     if (taom1 == "lavash" and taom2 == "cola") or (taom1 == "cola" and taom2 == "lavash"):
#         return "Combo: chegirma!"
#     elif taom1 == "lavash" or taom1 == "cola" or taom2 == "lavash" or taom2 == "cola":
#         return "Yaxshi tanlov!"
#     return "Oddiy buyurtma."

# taom1 = input("Birinchi taomni kiriting: ")
# taom2 = input("Ikkinchi taomni kiriting: ")
# print(buyurtma_tekshirish(taom1, taom2))

""" 18. 💳 Bank kartasi turi aniqlovchi """

# def karta_turi(raqam):
#     if raqam.startswith('8600'):
#         return "UzCard"
#     elif raqam.startswith('9860'):
#         return "Humo"
#     elif raqam.startswith('4000'):
#         return "Visa"
#     return "Noma’lum karta"

# raqam = input("Bank kartasi raqamini kiriting: ")
# print(karta_turi(raqam))

""" 19. 🧍‍♂️ Yoshga qarab maqom """

# def yoshga_qarab_maqom(yosh):
#     if yosh < 6:
#         return "Go‘dak"
#     elif 6 <= yosh <= 12:
#         return "Bola"
#     elif 13 <= yosh <= 17:
#         return "O‘smir"
#     elif 18 <= yosh <= 25:
#         return "Yosh"
#     elif 26 <= yosh <= 59:
#         return "Katta yoshli"
#     return "Qariya"

# yosh = int(input("Yoshingizni kiriting: "))
# print(yoshga_qarab_maqom(yosh))

""" 20. 🏦 Depozit foizi hisoblash """

# def depozit_foizi(muddat):
#     if muddat == 3:
#         return "Depozit foizi: 5%"
#     elif muddat == 6:
#         return "Depozit foizi: 10%"
#     elif muddat == 12:
#         return "Depozit foizi: 20%"
#     return "Noto‘g‘ri tanlov"

# muddat = int(input("Depozit muddatini oyda kiriting: "))
# print(depozit_foizi(muddat))

""" 21. 📦 Yetkazib berish narxi hisoblash """

# def yetkazib_berish_narxi(ogirlik):
#     if ogirlik < 1:
#         return "Yetkazib berish narxi: 5000 so‘m"
#     elif 1 <= ogirlik < 3:
#         return "Yetkazib berish narxi: 8000 so‘m"
#     elif 3 <= ogirlik < 5:
#         return "Yetkazib berish narxi: 12000 so‘m"
#     return "Yetkazib berish narxi: 20000 so‘m"

# ogirlik = float(input("Mahsulot og‘irligini kiriting (kg): "))
# print(yetkazib_berish_narxi(ogirlik))

""" 22. 🎫 Kinoga kirish narxi """

# def kino_kirish_narxi(yosh, talaba):
#     if yosh < 7:
#         return "Kirish narxi: Bepul"
#     elif 7 <= yosh < 18:
#         return "Kirish narxi: 10000 so‘m"
#     elif talaba:
#         return "Kirish narxi: 12000 so‘m"
#     return "Kirish narxi: 15000 so‘m"

# yosh = int(input("Yoshingizni kiriting: "))
# talaba_input = input("Siz talaba misiz? (ha/yo'q): ").strip().lower()
# talaba = talaba_input == 'ha'
# print(kino_kirish_narxi(yosh, talaba))

""" 23. 🎓 Stipendiya aniqlovchi """

# def stipendiya_aniqlovchi(baholar):
#     if baholar.count(5) == 5:
#         return "Stipendiya: 1 000 000 so‘m"
#     elif baholar.count(4) == 1:
#         return "Stipendiya: 800 000 so‘m"
#     elif baholar.count(4) == 2:
#         return "Stipendiya: 600 000 so‘m"
#     return "Stipendiya yo‘q"        

# baholar = []
# for i in range(5):
#     baho = int(input(f"{i+1}-fan bahosini kiriting (1-5): "))
#     baholar.append(baho)
# print(stipendiya_aniqlovchi(baholar))   

""" 24. 📱 Uyali aloqa operatorini aniqlovchi dastur! """

# def operator_aniqlash(raqam):
#     if raqam.startswith(('+99890', '+99891')):
#         return "Beeline"
#     elif raqam.startswith(('+99893', '+99894')):
#         return "Ucell"
#     elif raqam.startswith(('+99888', '+99897')):
#         return "MobiUz"
#     elif raqam.startswith(('+99877', '+99895', '+99899')):
#         return "Uzmobile"
#     elif raqam.startswith('+99833'):
#         return "Humans"
#     elif raqam.startswith('+99898'):
#         return "Perfectum mobile"
#     return "Noma’lum operator"

# telefon_raqam = input("Telefon raqamingizni kiriting (+998...): ")
# print(operator_aniqlash(telefon_raqam))

""" 25. 🍕 Pitsa narxini hisoblash """

# def pizza_narxi(turi, pishloq, ichimlik):
#     if turi == "kichik":
#         narx = 30000
#     elif turi == "o'rta":
#         narx = 45000
#     elif turi == "katta":
#         narx = 60000
#     else:
#         return "Noto'g'ri pitsa turi"

#     if pishloq:
#         narx += 5000
#     if ichimlik:
#         narx += 10000

#     return f"Pitsa narxi: {narx} so'm"

# turi = input("Pitsa turini kiriting (kichik/o'rta/katta): ").strip().lower()
# pishloq_input = input("Qo'shimcha pishloq qo'shasizmi? (ha/yo'q): ").strip().lower()
# pishloq = pishloq_input == 'ha'
# ichimlik_input = input("Ichimlik qo'shasizmi? (ha/yo'q): ").strip().lower()
# ichimlik = ichimlik_input == 'ha'
# print(pizza_narxi(turi, pishloq, ichimlik))
