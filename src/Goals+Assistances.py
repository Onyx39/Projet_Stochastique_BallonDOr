import matplotlib.pyplot as plt

import data
import players_data


kbC = []

kbC1 = players_data.kbG1+players_data.kbA1
kbC2 = players_data.kbG2+players_data.kbA2
kbC3 = players_data.kbG3+players_data.kbA3
kbC4 = players_data.kbG4+players_data.kbA4
kbC5 = players_data.kbG5+players_data.kbA5

kbC.append(kbC1)
kbC.append(kbC2)
kbC.append(kbC3)
kbC.append(kbC4)
kbC.append(kbC5)

smC = []

smC1 = players_data.smG1+players_data.smA1
smC2 = players_data.smG2+players_data.smA2
smC3 = players_data.smG3+players_data.smA3
smC4 = players_data.smG4+players_data.smA4
smC5 = players_data.smG5+players_data.smA5

smC.append(smC1)
smC.append(smC2)
smC.append(smC3)
smC.append(smC4)
smC.append(smC5)

rlC = []

rlC1 = players_data.rlG1+players_data.rlA1
rlC2 = players_data.rlG2+players_data.rlA2
rlC3 = players_data.rlG3+players_data.rlA3
rlC4 = players_data.rlG4+players_data.rlA4
rlC5 = players_data.rlG5+players_data.rlA5

rlC.append(rlC1)
rlC.append(rlC2)
rlC.append(rlC3)
rlC.append(rlC4)
rlC.append(rlC5)


msC = []

msC1 = players_data.msG1+players_data.msA1
msC2 = players_data.msG2+players_data.msA2
msC3 = players_data.msG3+players_data.msA3
msC4 = players_data.msG4+players_data.msA4
msC5 = players_data.msG5+players_data.msA5

msC.append(msC1)
msC.append(msC2)
msC.append(msC3)
msC.append(msC4)
msC.append(msC5)


kmC = []

kmC1 = players_data.kmG1+players_data.kmA1
kmC2 = players_data.kmG2+players_data.kmA2
kmC3 = players_data.kmG3+players_data.kmA3
kmC4 = players_data.kmG4+players_data.kmA4
kmC5 = players_data.kmG5+players_data.kmA5

kmC.append(kmC1)
kmC.append(kmC2)
kmC.append(kmC3)
kmC.append(kmC4)
kmC.append(kmC5)


crC = []

crC1 = players_data.crG1+players_data.crA1
crC2 = players_data.crG2+players_data.crA2
crC3 = players_data.crG3+players_data.crA3
crC4 = players_data.crG4+players_data.crA4
crC5 = players_data.crG5+players_data.crA5

crC.append(crC1)
crC.append(crC2)
crC.append(crC3)
crC.append(crC4)
crC.append(crC5)


lmC = []

lmC1 = players_data.lmG1+players_data.kmA1
lmC2 = players_data.lmG2+players_data.kmA2
lmC3 = players_data.lmG3+players_data.kmA3
lmC4 = players_data.lmG4+players_data.kmA4
lmC5 = players_data.lmG5+players_data.kmA5

lmC.append(kmC1)
lmC.append(kmC2)
lmC.append(kmC3)
lmC.append(kmC4)
lmC.append(kmC5)


hkC = []

hkC1 = players_data.hkG1+players_data.hkA1
hkC2 = players_data.hkG2+players_data.hkA2
hkC3 = players_data.hkG3+players_data.hkA3
hkC4 = players_data.hkG4+players_data.hkA4
hkC5 = players_data.hkG5+players_data.hkA5

hkC.append(hkC1)
hkC.append(hkC2)
hkC.append(hkC3)
hkC.append(hkC4)
hkC.append(hkC5)


plt.subplot(4,2,1)
plt.plot(players_data.years,kbC)
plt.title("Karim's G+A")

plt.subplot(4,2,2)
plt.plot(players_data.years,smC)
plt.title("Sadio's G+A")

plt.subplot(4,2,3)
plt.plot(players_data.years,rlC)
plt.title("Robert's G+A")

plt.subplot(4,2,4)
plt.plot(players_data.years,msC)
plt.title("Mohammed's G+A")

plt.subplot(4,2,5)
plt.plot(players_data.years,kmC)
plt.title("Kylian's G+A")

plt.subplot(4,2,6)
plt.plot(players_data.years,crC)
plt.title("Cristiano's G+A")

plt.subplot(4,2,7)
plt.plot(players_data.years,lmC)
plt.title("Lionel's G+A")

plt.subplot(4,2,8)
plt.plot(players_data.years,hkC)
plt.title("Harry's G+A")


plt.show()