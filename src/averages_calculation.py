from data import players
import matplotlib.pyplot as plt


#%%
# Creation of the object avg
def initialize_avg_object () :
    
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

    for i in players :
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

    return avg

#%%
# Creation des graphs representant les moyennes

def avg_avg_calculation () :

    avg = initialize_avg_object()
    
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

    avg_avgG = [sum(avgG)/len(avgG)]*len(avgG)
    avg_avgXG = [sum(avgXG)/len(avgXG)]*len(avgXG)
    avg_avgA = [sum(avgA)/len(avgA)]*len(avgA)
    avg_avgXA = [sum(avgXA)/len(avgXA)]*len(avgXA)

    avg_data = [abs, avgG, avgXG, avgA, avgXA, avg_avgG, avg_avgXG, avg_avgA, avg_avgXA]

    return avg_data

def show_avgG () :

    avg_data = avg_avg_calculation()

    plt.plot(avg_data[0], avg_data[1], avg_data[5])
    plt.title("Evolution de la moyenne des buts")
    plt.legend("--b", "g")
    plt.show()

def show_avgXG () : 

    avg_data = avg_avg_calculation()

    plt.plot(avg_data[0], avg_data[2], avg_data[6])
    plt.title("Evolution de la moyenne de la differnce de buts")
    plt.legend("--b", "g")
    plt.show()

def show_avgA () :

    avg_data = avg_avg_calculation()

    plt.plot(avg_data[0], avg_data[3], avg_data[7])
    plt.title("Evolution de la moyenne des assistances")
    plt.legend("--b", "g")
    plt.show()

def show_avgXA () :

    avg_data = avg_avg_calculation()
    
    plt.plot(avg_data[0], avg_data[4], avg_data[8])
    plt.title("Evolution de la moyenne de la difference d'assistances")
    plt.legend("--b", "g")
    plt.show()

def show_all () :
    
    avg_data = avg_avg_calculation()

    show_avgG()
    show_avgXG()
    show_avgA()
    show_avgXA()
