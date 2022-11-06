from data import players
import matplotlib.pyplot as plt

"""
This file calculate the serveral averages we need to analyse the data
Some functions allow to show them into plots
"""

def initialize_avg_object () :
    """
    This function create a dictionnary "avg".
    It is bluit like the objects "player" in data.py and contains all the averages of the the data.
    Input : None
    Output : A dictionnary "avg"
    """
    
    #Creation of the dictionnary
    avg = {}

    # Initialization of the varaibles
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

    # Loop to add the values into the variables
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

    # Make the averages (the data are rounded to hundredths)
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

    # Enter the values into the dictionnary
    avg["17/18"] = {"G" : avg_goal_17_18, "A" : avg_ass_17_18, "dG" : avg_Xgoal_17_18, "dA" : avg_Xass_17_18} 
    avg["18/19"] = {"G" : avg_goal_18_19, "A" : avg_ass_18_19, "dG" : avg_Xgoal_18_19, "dA" : avg_Xass_18_19} 
    avg["19/20"] = {"G" : avg_goal_19_20, "A" : avg_ass_19_20, "dG" : avg_Xgoal_19_20, "dA" : avg_Xass_19_20} 
    avg["20/21"] = {"G" : avg_goal_20_21, "A" : avg_ass_20_21, "dG" : avg_Xgoal_20_21, "dA" : avg_Xass_20_21} 
    avg["21/22"] = {"G" : avg_goal_21_22, "A" : avg_ass_21_22, "dG" : avg_Xgoal_21_22, "dA" : avg_Xass_21_22} 

    return avg

def avg_avg_calculation () :
    """
    This function creates a list that contains the averages and the average of the averages of the values.
    We use this list for the plots.
    Input : None
    Output : A list "avg_data"
    """

    # Creation of the object avg
    avg = initialize_avg_object()
    
    # Initialization of the varaibles
    avgG = []
    avgA = []
    avgXG = []
    avgXA = []
    abs = []

    # Loop to create the average lists
    for i in avg :
        avgG.append(avg[i]["G"])
        avgXG.append(avg[i]["dG"])
        avgA.append(avg[i]["A"])
        avgXA.append(avg[i]["dA"])
        abs.append(i)

    # Calculation of the average of the averages
    avg_avgG = [sum(avgG)/len(avgG)]*len(avgG)
    avg_avgXG = [sum(avgXG)/len(avgXG)]*len(avgXG)
    avg_avgA = [sum(avgA)/len(avgA)]*len(avgA)
    avg_avgXA = [sum(avgXA)/len(avgXA)]*len(avgXA)

    # Creation of the list "avg_data"
    avg_data = [abs, avgG, avgXG, avgA, avgXA, avg_avgG, avg_avgXG, avg_avgA, avg_avgXA]

    return avg_data

def average_plots () :
    """
    This function displays all the data averages
    Input : None
    Output : 4 plots
    """

    # Calculate the data needed
    avg_data = avg_avg_calculation()

    plt.subplot(2, 2, 1)
    plt.plot(avg_data[0], avg_data[1], avg_data[5])
    plt.title("Evolution de la moyenne des buts")

    plt.subplot(2, 2, 2)
    plt.plot(avg_data[0], avg_data[2], avg_data[6])
    plt.title("Evolution de la moyenne de la difference de buts")

    plt.subplot(2, 2, 3)
    plt.plot(avg_data[0], avg_data[3], avg_data[7])
    plt.title("Evolution de la moyenne des assistances")

    plt.subplot(2, 2, 4)
    plt.plot(avg_data[0], avg_data[4], avg_data[8])
    plt.title("Evolution de la moyenne de la difference d'assistances")

    plt.show()