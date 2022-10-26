import data
import matplotlib.pyplot as plt



avg_goal_17_18 = 0
for i in data.players :
    avg_goal_17_18 += i["17/18"]["G"]
avg_goal_17_18 /= 8
print(avg_goal_17_18)
