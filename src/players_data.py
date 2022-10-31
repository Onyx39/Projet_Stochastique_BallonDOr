import data
import averages_calculation

avg = averages_calculation.initialize_avg_object()

years = ["17/18", "18/19", "19/20", "20/21", "21/22"]
kbG = []
avgG = [avg["17/18"]["G"], avg["18/19"]["G"], avg["19/20"]["G"], avg["20/21"]["G"], avg["21/22"]["G"]]

kbG1 = data.karim_benzema["17/18"]["G"]
kbG2 = data.karim_benzema["18/19"]["G"]
kbG3 = data.karim_benzema["19/20"]["G"]
kbG4 = data.karim_benzema["20/21"]["G"]
kbG5 = data.karim_benzema["21/22"]["G"]

kbG.append(kbG1)
kbG.append(kbG2)
kbG.append(kbG3)
kbG.append(kbG4)
kbG.append(kbG5)


kbA = []

kbA1 = data.karim_benzema["17/18"]["A"]
kbA2 = data.karim_benzema["18/19"]["A"]
kbA3 = data.karim_benzema["19/20"]["A"]
kbA4 = data.karim_benzema["20/21"]["A"]
kbA5 = data.karim_benzema["21/22"]["A"]

kbA.append(kbA1)
kbA.append(kbA2)
kbA.append(kbA3)
kbA.append(kbA4)
kbA.append(kbA5)

print("AVGA 20/21", avg["20/21"]["A"])


avgA = [avg["17/18"]["A"], avg["18/19"]["A"], avg["19/20"]["A"], 7.5, avg["21/22"]["A"]] #j'ai mis "7.5" directement psk j'ai eu un souci en appliquant la meme formule que les autres

print("valeurs = ", kbG)
print("Avg valeur = ", avgG)
print("kbA = ", kbA)
print("avgA = ", avgA)


smG = []

smG1 = data.sadio_mane["17/18"]["G"]
smG2 = data.sadio_mane["18/19"]["G"]
smG3 = data.sadio_mane["19/20"]["G"]
smG4 = data.sadio_mane["20/21"]["G"]
smG5 = data.sadio_mane["21/22"]["G"]

smG.append(smG1)
smG.append(smG2)
smG.append(smG3)
smG.append(smG4)
smG.append(smG5)

smA = []

smA1 = data.sadio_mane["17/18"]["A"]
smA2 = data.sadio_mane["18/19"]["A"]
smA3 = data.sadio_mane["19/20"]["A"]
smA4 = data.sadio_mane["20/21"]["A"]
smA5 = data.sadio_mane["21/22"]["A"]

smA.append(smA1)
smA.append(smA2)
smA.append(smA3)
smA.append(smA4)
smA.append(smA5)

rlG = []

rlG1 = data.robert_lewandowski["17/18"]["G"]
rlG2 = data.robert_lewandowski["18/19"]["G"]
rlG3 = data.robert_lewandowski["19/20"]["G"]
rlG4 = data.robert_lewandowski["20/21"]["G"]
rlG5 = data.robert_lewandowski["21/22"]["G"]

rlG.append(rlG1)
rlG.append(rlG2)
rlG.append(rlG3)
rlG.append(rlG4)
rlG.append(rlG5)

rlA = []

rlA1 = data.robert_lewandowski["17/18"]["A"]
rlA2 = data.robert_lewandowski["18/19"]["A"]
rlA3 = data.robert_lewandowski["19/20"]["A"]
rlA4 = data.robert_lewandowski["20/21"]["A"]
rlA5 = data.robert_lewandowski["21/22"]["A"]

rlA.append(rlA1)
rlA.append(rlA2)
rlA.append(rlA3)
rlA.append(rlA4)
rlA.append(rlA5)

msG = []

msG1 = data.mohammed_salah["17/18"]["G"]
msG2 = data.mohammed_salah["17/18"]["G"]
msG3 = data.mohammed_salah["17/18"]["G"]
msG4 = data.mohammed_salah["17/18"]["G"]
msG5 = data.mohammed_salah["17/18"]["G"]

msG.append(msG1)
msG.append(msG2)
msG.append(msG3)
msG.append(msG4)
msG.append(msG5)

msA = []

msA1 = data.mohammed_salah["17/18"]["A"]
msA2 = data.mohammed_salah["18/19"]["A"]
msA3 = data.mohammed_salah["19/20"]["A"]
msA4 = data.mohammed_salah["20/21"]["A"]
msA5 = data.mohammed_salah["21/22"]["A"]

msA.append(msA1)
msA.append(msA2)
msA.append(msA3)
msA.append(msA4)
msA.append(msA5)


kmG = []

kmG1 = data.kylian_mbappe["17/18"]["G"]
kmG2 = data.kylian_mbappe["18/19"]["G"]
kmG3 = data.kylian_mbappe["19/20"]["G"]
kmG4 = data.kylian_mbappe["20/21"]["G"]
kmG5 = data.kylian_mbappe["21/22"]["G"]

kmG.append(kmG1)
kmG.append(kmG2)
kmG.append(kmG3)
kmG.append(kmG4)
kmG.append(kmG5)

kmA = []

kmA1 = data.kylian_mbappe["17/18"]["A"]
kmA2 = data.kylian_mbappe["18/19"]["A"]
kmA3 = data.kylian_mbappe["19/20"]["A"]
kmA4 = data.kylian_mbappe["20/21"]["A"]
kmA5 = data.kylian_mbappe["21/22"]["A"]

kmA.append(kmA1)
kmA.append(kmA2)
kmA.append(kmA3)
kmA.append(kmA4)
kmA.append(kmA5)


crG = []

crG1 = data.cristinao_ronaldo["17/18"]["G"]
crG2 = data.cristinao_ronaldo["18/19"]["G"]
crG3 = data.cristinao_ronaldo["19/20"]["G"]
crG4 = data.cristinao_ronaldo["20/21"]["G"]
crG5 = data.cristinao_ronaldo["21/22"]["G"]

crG.append(crG1)
crG.append(crG2)
crG.append(crG3)
crG.append(crG4)
crG.append(crG5)

crA = []

crA1 =data.cristinao_ronaldo["17/18"]["A"]
crA2 =data.cristinao_ronaldo["18/19"]["A"]
crA3 =data.cristinao_ronaldo["19/20"]["A"]
crA4 =data.cristinao_ronaldo["20/21"]["A"]
crA5 =data.cristinao_ronaldo["21/22"]["A"]

crA.append(crA1)
crA.append(crA2)
crA.append(crA3)
crA.append(crA4)
crA.append(crA5)


lmG = []

lmG1 = data.lionel_messi["17/18"]["G"]
lmG2 = data.lionel_messi["18/19"]["G"]
lmG3 = data.lionel_messi["19/20"]["G"]
lmG4 = data.lionel_messi["20/21"]["G"]
lmG5 = data.lionel_messi["21/22"]["G"]

lmG.append(lmG1)
lmG.append(lmG2)
lmG.append(lmG3)
lmG.append(lmG4)
lmG.append(lmG5)

lmA = []

lmA1 = data.lionel_messi["17/18"]["A"]
lmA2 = data.lionel_messi["18/19"]["A"]
lmA3 = data.lionel_messi["19/20"]["A"]
lmA4 = data.lionel_messi["20/21"]["A"]
lmA5 = data.lionel_messi["21/22"]["A"]

lmA.append(lmA1)
lmA.append(lmA2)
lmA.append(lmA3)
lmA.append(lmA4)
lmA.append(lmA5)


hkG = []

hkG1 = data.harry_kane["17/18"]["G"]
hkG2 = data.harry_kane["18/19"]["G"]
hkG3 = data.harry_kane["19/20"]["G"]
hkG4 = data.harry_kane["20/21"]["G"]
hkG5 = data.harry_kane["21/22"]["G"]

hkG.append(hkG1)
hkG.append(hkG2)
hkG.append(hkG3)
hkG.append(hkG4)
hkG.append(hkG5)

hkA = []

hkA1 = data.harry_kane["17/18"]["A"]
hkA2 = data.harry_kane["18/19"]["A"]
hkA3 = data.harry_kane["19/20"]["A"]
hkA4 = data.harry_kane["20/21"]["A"]
hkA5 = data.harry_kane["21/22"]["A"]

hkA.append(hkA1)
hkA.append(hkA2)
hkA.append(hkA3)
hkA.append(hkA4)
hkA.append(hkA5)

"""
ax1 = plt.subplot()
ax1.plot(years, kbG, marker = 'o')
ax2 = plt.subplot()
ax2.plot(avgG, color ='red', marker ='o')

plt.show()
"""
