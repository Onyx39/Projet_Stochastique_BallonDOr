import data
import matplotlib.pyplot as plt


#%%
# Creation of the object avg

avg = {}

avg_goal_17_18 = 0
avg_goal_18_19 = 0
avg_goal_19_20 = 0
avg_goal_20_21 = 0
avg_goal_21_22 = 0
avg_ass_17_18 = 0
avg_ass_18_19 = 0
avg_ass_19_20 = 0
avg_ass_20_21 = 0
avg_ass_21_22 = 0
avg_Xgoal_17_18 = 0
avg_Xgoal_18_19 = 0
avg_Xgoal_19_20 = 0
avg_Xgoal_20_21 = 0
avg_Xgoal_21_22 = 0
avg_Xass_17_18 = 0
avg_Xass_18_19 = 0
avg_Xass_19_20 = 0
avg_Xass_20_21 = 0
avg_Xass_21_22 = 0

for i in data.players :
    avg_goal_17_18 += i["17/18"]["G"]
    avg_goal_18_19 += i["18/19"]["G"]
    avg_goal_19_20 += i["19/20"]["G"]
    avg_goal_20_21 += i["20/21"]["G"]
    avg_goal_21_22 += i["21/22"]["G"]
    avg_ass_17_18 += i["17/18"]["A"]
    avg_ass_18_19 += i["18/19"]["A"]
    avg_ass_19_20 += i["19/20"]["A"]
    avg_ass_20_21 += i["20/21"]["A"]
    avg_ass_21_22 += i["21/22"]["A"]
    avg_Xgoal_17_18 += i["17/18"]["dG"]
    avg_Xgoal_18_19 += i["18/19"]["dG"]
    avg_Xgoal_19_20 += i["19/20"]["dG"]
    avg_Xgoal_20_21 += i["20/21"]["dG"]
    avg_Xgoal_21_22 += i["21/22"]["dG"]
    avg_Xass_17_18 += i["17/18"]["dA"]
    avg_Xass_18_19 += i["18/19"]["dA"]
    avg_Xass_19_20 += i["19/20"]["dA"]
    avg_Xass_20_21 += i["20/21"]["dA"]
    avg_Xass_21_22 += i["21/22"]["dA"]

avg_goal_17_18 = round(100*avg_goal_17_18/8)/100
avg_goal_18_19 = round(100*avg_goal_18_19/8)/100
avg_goal_19_20 = round(100*avg_goal_19_20/8)/100
avg_goal_20_21 = round(100*avg_goal_20_21/8)/100
avg_goal_21_22 = round(100*avg_goal_21_22/8)/100
avg_ass_17_18 = round(100*avg_ass_17_18/8)/100
avg_ass_18_19 = round(100*avg_ass_18_19/8)/100
avg_ass_19_20 = round(100*avg_ass_19_20/8)/100
avg_ass_20_21 = round(100*avg_ass_20_21/8)/100
avg_ass_21_22 = round(100*avg_ass_21_22/8)/100
avg_Xgoal_17_18 = round(100*avg_Xgoal_17_18/8)/100
avg_Xgoal_18_19 = round(100*avg_Xgoal_18_19/8)/100
avg_Xgoal_19_20 = round(100*avg_Xgoal_19_20/8)/100
avg_Xgoal_20_21 = round(100*avg_Xgoal_20_21/8)/100
avg_Xgoal_21_22 = round(100*avg_Xgoal_21_22/8)/100
avg_Xass_17_18 = round(100*avg_Xass_17_18/8)/100
avg_Xass_18_19 = round(100*avg_Xass_18_19/8)/100
avg_Xass_19_20 = round(100*avg_Xass_19_20/8)/100
avg_Xass_20_21 = round(100*avg_Xass_20_21/8)/100
avg_Xass_21_22 = round(100*avg_Xass_21_22/8)/100

avg["17/18"] = {"G" : avg_goal_17_18, "A" : avg_ass_17_18, "dG" : avg_Xgoal_17_18, "dA" : avg_Xass_17_18} 
avg["18/19"] = {"G" : avg_goal_18_19, "A" : avg_ass_18_19, "dG" : avg_Xgoal_18_19, "dA" : avg_Xass_18_19} 
avg["19/20"] = {"G" : avg_goal_19_20, "A" : avg_ass_19_20, "dG" : avg_Xgoal_19_20, "dA" : avg_Xass_19_20} 
avg["20/21"] = {"G" : avg_goal_20_21, "A" : avg_ass_20_21, "dG" : avg_Xgoal_20_21, "dA" : avg_Xass_20_21} 
avg["21/22"] = {"G" : avg_goal_21_22, "A" : avg_ass_21_22, "dG" : avg_Xgoal_21_22, "dA" : avg_Xass_21_22} 


print("\n", avg, "\n")

#%%
# Creation des graphs representant les moyennes

avgG = []
avgA = []
avgXG = []
avgXA = []
abs = []

for i in avg :
    avgG.append(avg[i]["G"])
    avgXG.append(avg[i]["dG"])
    avgA.append(avg[i]["A"])
    avgXA.append(avg[i]["dA"])
    abs.append(i)

print(avgG)
print(abs)

plt.plot(abs, avgG, avgXG)
plt.title("Evolution de la moyene des buts")
plt.legend("--b", "g")
plt.show()

plt.plot(abs, avgA, avgXA)
plt.title("Evolution de la moyenne des assistances")
plt.legend("--b", "g")
plt.show()
