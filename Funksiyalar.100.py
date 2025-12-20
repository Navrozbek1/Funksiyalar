"""  Funksiyalar va Shart operatorlari mavzusidan 100 masala! """   # clck.ru/3PfMfM

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

""" 26. 🧾 To‘lov turi bo‘yicha chegirma """

# def chegirma_hisoblash(narx, tolov_turi):
#     if tolov_turi == "naqd":
#         chegirma = 0
#     elif tolov_turi == "plastik":
#         chegirma = narx * 0.05
#     elif tolov_turi == "onlayn":
#         chegirma = narx * 0.10
#     else:
#         return "Noto‘g‘ri to‘lov turi"

#     jami_tolov = narx - chegirma
#     return f"Chegirma: {chegirma} so‘m. To‘lov summasi: {jami_tolov} so‘m"

""" 27. 🏥 Tibbiy tekshiruv bahosi """

# def tibbiy_tekshiruv(qon_bosimi, yurak_urishi):
#     if qon_bosimi != "normal":
#         return "Qon bosimi muammosi"
#     elif yurak_urishi == "yuqori":
#         return "Tachikardiya"
#     return "Sog‘lom"

# qon_bosimi = input("Qon bosimingiz normalmi? (normal/boshqa): ").strip().lower()
# yurak_urishi = input("Yurak urishingiz yuqorimi? (yuqori/normal): ").strip().lower()
# print(tibbiy_tekshiruv(qon_bosimi, yurak_urishi))

""" 28. 🏖️ Dam olish uchun tavsiya """

# def dam_olish_tavsiya(fasli):
#     if fasli == "bahor":
#         return "Samarqandga borishni tavsiya qilamiz!"
#     elif fasli == "yoz":
#         return "Chorvoqga borishni tavsiya qilamiz!"
#     elif fasli == "kuz":
#         return "Xivaga borishni tavsiya qilamiz!"
#     elif fasli == "qish":
#         return "Beldersoyga borishni tavsiya qilamiz!"
#     return "Noma’lum fasl"

# fasli = input("Yil faslini kiriting (bahor/yoz/kuz/qish): ").strip().lower()
# print(dam_olish_tavsiya(fasli))

""" 29. 🚗 Yoqilg‘i sarfi aniqlovchi """

# def yoqilg_i_sarfi(avtomobil_turi, yol_sharoiti):
#     if avtomobil_turi == "yengil" and yol_sharoiti == "shahar":
#         return "Yoqilg‘i sarfi: 10l/100km"
#     elif avtomobil_turi == "yengil" and yol_sharoiti == "trassa":
#         return "Yoqilg‘i sarfi: 7l/100km"
#     elif avtomobil_turi == "yuk" and yol_sharoiti == "shahar":
#         return "Yoqilg‘i sarfi: 20l/100km"
#     elif avtomobil_turi == "yuk" and yol_sharoiti == "trassa":
#         return "Yoqilg‘i sarfi: 15l/100km"
#     return "Noma’lum avtomobil turi yoki yo‘l sharoiti"

# avtomobil_turi = input("Avtomobil turini kiriting (yengil/yuk): ").strip().lower()
# yol_sharoiti = input("Yo‘l sharoitini kiriting (shahar/trassa): ").strip().lower()
# print(yoqilg_i_sarfi(avtomobil_turi, yol_sharoiti))

""" 30. 🧮 To‘lov miqdori solishtiruvchi """

# def tolov_miqdori(tolov1, tolov2, tolov3):
#     eng_katta = max(tolov1, tolov2, tolov3)
#     eng_kichik = min(tolov1, tolov2, tolov3)
#     return f"Eng katta to'lov: {eng_katta} so'm, Eng kichik to'lov: {eng_kichik} so'm"

# tolov1 = float(input("Birinchi to'lov miqdorini kiriting (so'm): "))
# tolov2 = float(input("Ikkinchi to'lov miqdorini kiriting (so'm): "))
# tolov3 = float(input("Uchinchi to'lov miqdorini kiriting (so'm): "))
# print(tolov_miqdori(tolov1, tolov2, tolov3))

"""  🔢 31. Elektr energiyasi to‘lovi hisoblash """

# def elektr(istemol):
#     if istemol <= 100:
#         narx = istemol * 350
#     elif 101 <= istemol <= 200:
#         narx = (100 * 350) + ((istemol - 100) * 450)
#     else:
#         narx = (100 * 350) + (100 * 450) + ((istemol - 200) * 600)
#     return f"Umumiy to'lov: {narx} so'm"

# istemol = int(input("Iste'mol qilingan elektr energiyasi miqdorini kiriting (kVt/soat): "))
# print(elektr(istemol))

""" 🧒 32. Bolaning bo‘yi va vazni asosida sog‘lomlik tekshiruvi """

# def soglomlik_tekshiruvi(boy, vazn):
#     if 100 <= boy <= 130 and 20 <= vazn <= 40:
#         return "Sog‘lom"
#     return "Tekshiruv kerak"

# boy = int(input("Bolaning bo'yini kiriting (sm): "))
# vazn = float(input("Bolaning vaznini kiriting (kg): "))
# print(soglomlik_tekshiruvi(boy, vazn))

""" 📦 33. Internet paketi narxi aniqlovchi """

# def internet_paketi_narxi(hajm):
#     if hajm == 1:
#         return "Internet paketi narxi: 9000 so‘m"
#     elif hajm == 5:
#         return "Internet paketi narxi: 25000 so‘m"
#     elif hajm == 10:
#         return "Internet paketi narxi: 45000 so‘m"
#     elif hajm == 30:
#         return "Internet paketi narxi: 90000 so‘m"
#     return "Noma’lum internet paketi hajmi"

# hajm = int(input("Internet paketi hajmini kiriting (GB): "))
# print(internet_paketi_narxi(hajm))

""" 🏅 34. Sport musobaqasi g‘olibini aniqlash """

# def musobaqa_golibi(ball1, ball2, ball3):
#     if ball1 > ball2 and ball1 > ball3:
#         return "1-sportchi g'olib!"
#     elif ball2 > ball1 and ball2 > ball3:
#         return "2-sportchi g'olib!"
#     elif ball3 > ball1 and ball3 > ball2:
#         return "3-sportchi g'olib!"
#     return "Durrang!"

# ball1 = float(input("1-sportchi ballini kiriting: "))
# ball2 = float(input("2-sportchi ballini kiriting: "))
# ball3 = float(input("3-sportchi ballini kiriting: "))
# print(musobaqa_golibi(ball1, ball2, ball3))

""" 🏡 35. Ipoteka kreditiga yaroqlilik """

# def yaroqlilik(ishlaydi, oylik):
#     if ishlaydi and oylik > 5000000:
#         return "Yaroqli"
#     return "Yaroqsiz"

# ishlaydi_input = input("Siz ishlaysizmi? (ha/yo'q): ").strip().lower()
# ishlaydi = ishlaydi_input == 'ha'
# oylik = float(input("Oylik daromadingizni kiriting (so'm): "))
# print(yaroqlilik(ishlaydi, oylik))

""" 🎮 36. Kompyuter o‘yinini ishga tushirish """

# def oyin(ram, video_karta):
#     if ram >= 8 and video_karta:
#         return "O‘yin ishlaydi"
#     return "Tizim talabiga javob bermaydi"

# ram = int(input("Kompyuter RAM miqdorini kiriting (GB): "))
# video_karta_input = input("Video karta mavjudmi? (ha/yo'q): ").strip().lower()
# video_karta = video_karta_input == 'ha'
# print(oyin(ram, video_karta))

""" 🎓 37. Talabaning bahosini aniqlash """

# def talaba_bahosi(baho1, baho2, baho3):
#     baholar = [baho1, baho2, baho3]
#     if baholar.count(5) == 3:
#         return "A’lochi"
#     elif baholar.count(4) == 1:
#         return "Yaxshi"
#     return "O‘rtacha"

# baho1 = int(input("1-fan bahosini kiriting (1-5): "))
# baho2 = int(input("2-fan bahosini kiriting (1-5): "))
# baho3 = int(input("3-fan bahosini kiriting (1-5): "))
# print(talaba_bahosi(baho1, baho2, baho3))

""" 🛍️ 38. Savdo chegirmasi hisoblash """

# def chegirma_hisoblash(summa):
#     if summa < 100000:
#         chegirma = 0
#     elif 100000 <= summa <= 200000:
#         chegirma = summa * 0.05
#     else:
#         chegirma = summa * 0.10
#     jami_tolov = summa - chegirma
#     return f"Chegirma: {chegirma} so‘m. To‘lov summasi: {jami_tolov} so‘m"

# summa = float(input("Xarid summasini kiriting (so'm): "))
# print(chegirma_hisoblash(summa))

""" 🚕 39. Taksi narxini hisoblash """

# def taksi_narxi(masofa, dam_olish):
#     asosiy_narx = masofa * 3000
#     if dam_olish == 'ha':
#         asosiy_narx *= 1.20
#     return f"Taksi narxi: {asosiy_narx} so‘m"

# masofa = float(input("Bosib o'tilgan masofani kiriting (km): "))
# dam_olish_input = input("Bugun dam olish kunimi? (ha/yo'q): ").strip().lower()
# print(taksi_narxi(masofa, dam_olish_input))

""" 💳 40. Bank hisob raqamini tasdiqlash """

# def hisob_raqami_tasdiqlash(raqam):
#     if raqam.isdigit() and len(raqam) == 16:
#         return "Yaroqli"
#     return "Xato"
# raqam = input("Bank hisob raqamingizni kiriting: ")
# print(hisob_raqami_tasdiqlash(raqam))

""" 🔧 41. Ish haqi darajasi aniqlash """


# def ish_haqi_darajasi(lavozim):
#     if lavozim == "Direktor":
#         return "A"
#     elif lavozim == "Menejer":
#         return "B"
#     elif lavozim == "Ishchi":
#         return "C"
#     return "Noma’lum"

# lavozim = input("Lavozimingizni kiriting (Direktor/Menejer/Ishchi): ")
# print(ish_haqi_darajasi(lavozim))

""" 🏠 42. Uy narxi aniqlovchi """

# def uy_narxi(hudud, xona_soni):
#     if hudud == "Shahar" and xona_soni == 3:
#         return "Uy narxi: 450 mln so‘m"
#     elif hudud == "Shahar" and xona_soni == 2:
#         return "Uy narxi: 300 mln so‘m"
#     elif hudud == "Qishloq":
#         return "Uy narxi: 150 mln so‘m"
#     return "Noma’lum hudud yoki xona soni"

# hudud = input("Uy hududini kiriting (Shahar/Qishloq): ").strip()
# xona_soni = int(input("Xonalar sonini kiriting: "))
# print(uy_narxi(hudud, xona_soni))

""" 🧼 43. Kir yuvish rejimi tanlash """

# def kir_yuvish_rejimi(matot_turi, ifloslik_darajasi):
#     if matot_turi == "Paxta" and ifloslik_daraj
#         return "Rejim 1"
#     elif matot_turi == "Sintetik" and ifloslik_darajasi == "Og‘ir":
#         return "Rejim 3"
#     return "Rejim 2"

# matot_turi = input("Matoning turini kiriting (Paxta/Sintetik): ").strip()
# ifloslik_darajasi = input("Ifloslik darajasini kiriting (Yengil/Og‘ir): ").strip()
# print(kir_yuvish_rejimi(matot_turi, ifloslik_darajasi))

""" 📚 44. Kitob janrini aniqlovchi """

# def kitob_janri(nom):
#     if "sir" in nom or "jinoyat" in nom:
#         return "Detektiv"
#     elif "sevgi" in nom or "romantika" in nom:
#         return "Romantik"
#     elif "kosmos" in nom or "kelajak" in nom:
#         return "Fantastik"
#     return "Boshqa"

# nom = input("Kitob nomini kiriting: ").strip().lower()
# print(kitob_janri(nom))

""" 🎭 45. Konsert chiptasi narxi """

# def chipta_narxi(turi, yosh):
#     if turi == "VIP" and yosh > 60:
#         return "Chiptaning narxi: 50 000 so‘m"
#     elif turi == "Oddiy" and yosh < 18:
#         return "Chiptaning narxi: 20 000 so‘m"
#     return "Chiptaning narxi: 30 000 so‘m"

# turi = input("Chiptaning turini kiriting (VIP/Oddiy): ").strip()
# yosh = int(input("Yoshingizni kiriting: "))
# print(chipta_narxi(turi, yosh))

""" 🏪 46. Do'kon ish vaqti tekshiruvi" """

# def dokon(kun, soat):
#     if kun in ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma"] and 9 <= soat < 18:
#         return "Ochiq"
#     elif kun in ["Shanba", "Yakshanba"] and 10 <= soat < 16:
#         return "Ochiq"
#     return "Yopiq"

# kun = input("Haftaning kunini kiriting: ").strip()
# soat = int(input("Soatni kiriting (0-23): "))
# print(dokon(kun, soat))

""" 🌱 47. O'simlik parvarishi tavsiyasi """

# def osimlik_parvarishi(turi, fasl):
#     if turi == "Gul" and fasl == "Bahor":
#         return "Haftada 3 marta sug'oring"
#     elif turi == "Daraxt" and fasl == "Yoz":
#         return "Har kuni sug'oring"
#     elif turi == "Gul" and fasl == "Qish":
#         return "Haftada 1 marta sug'oring"
#     return "Haftada 2 marta sug'oring"

# turi = input("O'simlik turini kiriting (Gul/Daraxt): ").strip()
# fasl = input("Faslni kiriting (Bahor/Yoz/Kuz/Qish): ").strip()
# print(osimlik_parvarishi(turi, fasl))

""" 💰 48. Bank kreditini olish imkoniyati """

# def kredit(yosh, oylik, tarix):
#     if 21 < yosh < 65:
#         if oylik > 3_000_000 and tarix == 'yaxshi':
#             return "Kredit beriladi"
#         elif oylik > 3_000_000 and tarix == "Qoniqarli":
#             return "Qo'shimcha hujjat kerak"
#     return "Kredit berilmaydi"

# yosh = int(input("Yoshingizni kiriting: "))
# oylik = float(input("Oylik daromadingizni kiriting (so'm): "))
# tarix = input("Kredit tarixingizni kiriting (Yaxshi/Qoniqarli/Boshqa): ").strip().lower()
# print(kredit(yosh, oylik, tarix))

""" 🎭 49. Teatr tomoshasi uchun joy tavsiyasi """

# def teatr_joy_tavsiyasi(budjet, vip, yaxshi_korish):
#     if budjet > 100000 and vip:
#         return "Birinchi qator VIP"
#     elif budjet > 100000 and not vip:
#         return "Birinchi qator oddiy"
#     elif budjet <= 100000 and yaxshi_korish:
#         return "O'rta qatorlar"
#     return "Orqa qatorlar"

# budjet = float(input("Budjetingizni kiriting (so'm): "))
# vip_input = input("VIP o'rindiq kerakmi? (ha/yo'q): ").strip().lower()
# vip = vip_input == 'ha'
# yaxshi_korish_input = input("Yaxshi ko'rish kerakmi? (ha/yo'q): ").strip().lower()
# yaxshi_korish = yaxshi_korish_input == 'ha'
# print(teatr_joy_tavsiyasi(budjet, vip, yaxshi_korish))

""" 📱 50. Telefon xotirasi tekshiruvi """

# def a_zoligi_narxi(turi, yosh):
#     if turi == "A" and yosh < 18:
#         return "Narxi: 100 000 so‘m"
#     elif turi == "A" and yosh >= 18:
#         return "Narxi: 150 000 so‘m"
#     elif turi == "B" and yosh < 18:
#         return "Narxi: 80 000 so‘m"
#     elif turi == "B" and yosh >= 18:
#         return "Narxi: 120 000 so‘m"
#     return "Noma’lum tur"

# turi = input("A yoki B turini kiriting: ").strip().upper()
# yosh = int(input("Yoshingizni kiriting: "))
# print(a_zoligi_narxi(turi, yosh))

""" 🌡️ 51. Havoning holati bo'yicha kiyim tavsiyasi """

# def kiyim_tavsiyasi(harorat, yomgir_ehtimol):
#     if harorat < 0:
#         return "Qish kiyimi"
#     elif 0 <= harorat < 15 and yomgir_ehtimol > 50:
#         return "Kuz kiyimi va soyabon"
#     elif 15 <= harorat < 25:
#         return "Bahor kiyimi"
#     return "Yoz kiyimi"

# harorat = float(input("Havoning haroratini kiriting (°C): "))
# yomgir_ehtimol = float(input("Yomg'ir ehtimolini kiriting (%): "))
# print(kiyim_tavsiyasi(harorat, yomgir_ehtimol))

""" 🎯 52. O'yin ballini baholash """

# def oyin_baholash(ball):
#     if ball >= 90:
#         return "Ustoz"
#     elif 70 <= ball < 90:
#         return "Malakali"
#     elif 50 <= ball < 70:
#         return "O'rta"
#     return "Boshlang'ich"

# ball = float(input("O'yinchi ballini kiriting: "))
# print(oyin_baholash(ball))

""" 🌡️ 53.  Harorat Baholagich """

# def harorat_baholagich(harorat):
#     if harorat < 0:
#         return "Juda sovuq"
#     elif 0 <= harorat < 15:
#         return "Salqin"
#     elif 15 <= harorat < 30:
#         return "Iliq"
#     return "Issiq"

# harorat = float(input("Havoning haroratini kiriting (°C): "))
# print(harorat_baholagich(harorat))

""" 🎓 54. Talaba Reytingi """

# def talaba_reytingi(ball):
#     if 90 <= ball <= 100:
#         return "Baho: 5"
#     elif 71 <= ball < 90:
#         return "Baho: 4"
#     elif 60 <= ball < 71:
#         return "Baho: 3"
#     return "Ball yetarli emas!"

# ball = float(input("Talabaning umumiy balini kiriting: "))
# print(talaba_reytingi(ball))

""" 🚌 55. Avtobus Chipta Narxi """

# def avtobus_chipta_narxi(yosh, talaba):
#     if yosh < 7:
#         return "Bepul"
#     elif talaba:
#         return "5000 so‘m"
#     elif yosh >= 60:
#         return "Chegirma: 3000 so‘m"
#     return "7000 so‘m"

# yosh = int(input("Yoshingizni kiriting: "))
# talaba_input = input("Siz talaba misiz? (ha/yo'q): ").strip().lower()
# talaba = talaba_input == 'ha'
# print(avtobus_chipta_narxi(yosh, talaba))

""" 🗓️ 56. Yil Faslini Aniqlash """

# def yil_faslini_aniqlash(oy):
#     if oy in [12, 1, 2]:
#         return "Qish"
#     elif oy in [3, 4, 5]:
#         return "Bahor"
#     elif oy in [6, 7, 8]:
#         return "Yoz"
#     elif oy in [9, 10, 11]:
#         return "Kuz"
#     return "Noma’lum oy raqami"

# oy = int(input("Oy raqamini kiriting (1-12): "))
# print(yil_faslini_aniqlash(oy))

""" 📱 57. Telefon Narxi Hisoblash """

# def telefon_narxi(model, holat):
#     if model == "iPhone" and holat == "yangi":
#         return "Narxi: 1200$"
#     elif model == "iPhone" and holat == "ishlatilgan":
#         return "Narxi: 800$"
#     elif model == "Samsung" and holat == "yangi":
#         return "Narxi: 900$"
#     elif model == "Samsung" and holat == "ishlatilgan":
#         return "Narxi: 600$"
#     return "Noma’lum model yoki holat"

# model = input("Telefon modelini kiriting (iPhone/Samsung): ").strip().lower()
# holat = input("Telefon holatini kiriting (yangi/ishlatilgan): ").strip().lower()
# print(telefon_narxi(model, holat))

""" 🏫 58. Maktabga Qabul """

# def maktabga_qabul(yosh, ball):
#     if yosh >= 6 and ball >= 70:
#         return "Qabul qilindi"
#     return "Qabul qilinmadi"

# yosh = int(input("Bolaning yoshini kiriting: "))
# ball = float(input("Bolaning test ballarini kiriting: "))
# print(maktabga_qabul(yosh, ball))

""" 🌐 59. Internet Tezligi Tahlili """

# def internet_tezligi_tahlili(tezlik):
#     if tezlik < 5:
#         return "Juda sekin"
#     elif 5 <= tezlik < 20:
#         return "O‘rtacha"
#     elif 20 <= tezlik <= 100:
#         return "Tez"
#     return "Juda tez"

# tezlik = float(input("Internet tezligini kiriting (Mbps): "))
# print(internet_tezligi_tahlili(tezlik))

""" 🐶 60. Uy Hayvoni Tavsiyasi """

# def uy_hayvoni(vaqt, joy, sabr):
#     if vaqt == "kam" and joy == "kam":
#         return "Baliq"
#     elif vaqt == "kop" and sabr == "kop":
#         return "It"
#     elif vaqt == "ortacha" and joy == "ortacha" and sabr == "ortacha":
#         return "Mushuk"
#     return "Noma’lum sharoitlar"

# vaqt = input("Bo'sh vaqtingizni kiriting (kam/ortacha/kop): ").strip().lower()
# joy = input("Bo'sh joyingizni kiriting (kam/ortacha/kop): ").strip().lower()
# sabr = input("Sabr darajangizni kiriting (kam/ortacha/kop): ").strip().lower()
# print(uy_hayvoni(vaqt, joy, sabr))
