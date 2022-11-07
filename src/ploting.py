from data import ballon_d_or
import matplotlib.pyplot as plt
import players_data as pp

ballon_d_or_goals = [ballon_d_or["17/18"]["G"], ballon_d_or["18/19"]["G"], ballon_d_or["19/20"]["G"], ballon_d_or["20/21"]["G"], ballon_d_or["21/22"]["G"]]
ballon_d_or_assists = [ballon_d_or["17/18"]["A"], ballon_d_or["18/19"]["A"], ballon_d_or["19/20"]["A"], ballon_d_or["20/21"]["A"], ballon_d_or["21/22"]["A"]]

def show_all_players_plots () :
    plt.subplot(7, 4, 1)
    plt.plot(pp.years, pp.kbG)
    plt.ylim(5,45)
    plt.plot(pp.avgG, color = 'red')
    plt.plot(ballon_d_or_goals, color = 'yellow')
    plt.title("Karim's Goals")

    plt.subplot(7, 4, 2)
    plt.plot(pp.years, pp.kbA, color = 'green')
    plt.ylim(0,25)
    plt.plot(pp.avgA, color = 'red')
    plt.plot(ballon_d_or_assists, color = 'yellow')
    plt.title("Karim's Assists")


    plt.subplot(7, 4, 3)
    plt.plot(pp.years, pp.smG)
    plt.ylim(5, 45)
    plt.plot(pp.avgG, color = 'red')
    plt.plot(ballon_d_or_goals, color = 'yellow')
    plt.title("Sadio's Goals")

    plt.subplot(7, 4, 4)
    plt.plot(pp.years, pp.smA, color = 'green')
    plt.ylim(0, 25)
    plt.plot(pp.avgA, color = 'red')
    plt.plot(ballon_d_or_assists, color = 'yellow')
    plt.title("Sadio's Assists")


    plt.subplot(7, 4, 9)
    plt.plot(pp.years, pp.rlG)
    plt.ylim(5, 45)
    plt.plot(pp.avgG, color = 'red')
    plt.plot(ballon_d_or_goals, color = 'yellow')
    plt.title("Robert's Goals")

    plt.subplot(7, 4, 10)
    plt.plot(pp.years, pp.rlA, color = 'green')
    plt.ylim(0, 25)
    plt.plot(pp.avgA, color = 'red')
    plt.plot(ballon_d_or_assists, color = 'yellow')
    plt.title("Robert's Assists")


    plt.subplot(7, 4, 11)
    plt.plot(pp.years, pp.msG)
    plt.ylim(5, 45)
    plt.plot(pp.avgG, color = 'red')
    plt.plot(ballon_d_or_goals, color = 'yellow')
    plt.title("Mohammed's Goals")

    plt.subplot(7, 4, 12)
    plt.plot(pp.years, pp.msA, color = 'green')
    plt.ylim(0, 25)
    plt.plot(pp.avgA, color = 'red')
    plt.plot(ballon_d_or_assists, color = 'yellow')
    plt.title("Mohammed's Assists")


    plt.subplot(7, 4, 17)
    plt.plot(pp.years, pp.kmG)
    plt.ylim(5, 45)
    plt.plot(pp.avgG, color = 'red')
    plt.plot(ballon_d_or_goals, color = 'yellow')
    plt.title("Kylian's Goals")

    plt.subplot(7, 4, 18)
    plt.plot(pp.years, pp.kmA, color = 'green')
    plt.ylim(0, 25)
    plt.plot(pp.avgA, color = 'red')
    plt.plot(ballon_d_or_assists, color = 'yellow')
    plt.title("Kylian's Assists")


    plt.subplot(7, 4, 19)
    plt.plot(pp.years, pp.crG)
    plt.ylim(5, 45)
    plt.plot(pp.avgG, color = 'red')
    plt.plot(ballon_d_or_goals, color = 'yellow')
    plt.title("Cristiano's Goals")

    plt.subplot(7, 4, 20)
    plt.plot(pp.years, pp.crA, color = 'green')
    plt.ylim(0, 25)
    plt.plot(pp.avgA, color = 'red')
    plt.plot(ballon_d_or_assists, color = 'yellow')
    plt.title("Cristiano's Assists")


    plt.subplot(7, 4, 25)
    plt.plot(pp.years, pp.lmG)
    plt.ylim(5, 45)
    plt.plot(pp.avgG, color = 'red')
    plt.plot(ballon_d_or_goals, color = 'yellow')
    plt.title("Lionel's Goals")

    plt.subplot(7, 4, 26)
    plt.plot(pp.years, pp.lmA, color = 'green')
    plt.ylim(0, 25)
    plt.plot(pp.avgA, color = 'red')
    plt.plot(ballon_d_or_assists, color = 'yellow')
    plt.title("Lionel's Assists")


    plt.subplot(7, 4, 27)
    plt.plot(pp.years, pp.hkG)
    plt.ylim(5, 45)
    plt.plot(pp.avgG, color = 'red')
    plt.plot(ballon_d_or_goals, color = 'yellow')
    plt.title("Harry's Goals")

    plt.subplot(7, 4, 28)
    plt.plot(pp.years, pp.hkA, color = 'green')
    plt.ylim(0, 25)
    plt.plot(pp.avgA, color = 'red')
    plt.plot(ballon_d_or_assists, color = 'yellow')
    plt.title("Harry's Assists")

    plt.show()