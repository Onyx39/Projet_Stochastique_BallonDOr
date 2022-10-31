import data
import matplotlib.pyplot as plt
import players_data as pp

def show_all_players_plots () :
    plt.subplot(8,2,1)
    plt.plot(pp.years, pp.kbG)
    plt.plot(pp.avgG, color = 'red')
    plt.title("Karim's Goals")

    plt.subplot(8,2,2)
    plt.plot(pp.years, pp.kbA, color = 'green')
    plt.plot(pp.avgA, color = 'red')
    plt.title("Karim's Assists")


    plt.subplot(8,2,3)
    plt.plot(pp.years, pp.smG)
    plt.plot(pp.avgG, color = 'red')
    plt.title("Sadio's Goals")

    plt.subplot(8,2,4)
    plt.plot(pp.years, pp.smA, color = 'green')
    plt.plot(pp.avgA, color = 'red')
    plt.title("Sadio's Assists")


    plt.subplot(8,2,5)
    plt.plot(pp.years, pp.rlG)
    plt.plot(pp.avgG, color = 'red')
    plt.title("Robert's Goals")

    plt.subplot(8,2,6)
    plt.plot(pp.years, pp.rlA, color = 'green')
    plt.plot(pp.avgA, color = 'red')
    plt.title("Robert's Assists")


    plt.subplot(8,2,7)
    plt.plot(pp.years, pp.msG)
    plt.plot(pp.avgG, color = 'red')
    plt.title("Mohammed's Goals")

    plt.subplot(8,2,8)
    plt.plot(pp.years, pp.msA, color = 'green')
    plt.plot(pp.avgA, color = 'red')
    plt.title("Mohammed's Assists")


    plt.subplot(8,2,9)
    plt.plot(pp.years, pp.kmG)
    plt.plot(pp.avgG, color = 'red')
    plt.title("Kylian's Goals")

    plt.subplot(8,2,10)
    plt.plot(pp.years, pp.kmA, color = 'green')
    plt.plot(pp.avgA, color = 'red')
    plt.title("Kylian's Assists")


    plt.subplot(8,2,11)
    plt.plot(pp.years, pp.crG)
    plt.plot(pp.avgG, color = 'red')
    plt.title("Cristiano's Goals")

    plt.subplot(8,2,12)
    plt.plot(pp.years, pp.crA, color = 'green')
    plt.plot(pp.avgA, color = 'red')
    plt.title("Cristiano's Assists")


    plt.subplot(8,2,13)
    plt.plot(pp.years, pp.lmG)
    plt.plot(pp.avgG, color = 'red')
    plt.title("Lionel's Goals")

    plt.subplot(8,2,14)
    plt.plot(pp.years, pp.lmA, color = 'green')
    plt.plot(pp.avgA, color = 'red')
    plt.title("Lionel's Assists")


    plt.subplot(8,2,15)
    plt.plot(pp.years, pp.hkG)
    plt.plot(pp.avgG, color = 'red')
    plt.title("Harry's Goals")

    plt.subplot(8,2,16)
    plt.plot(pp.years, pp.hkA, color = 'green')
    plt.plot(pp.avgA, color = 'red')
    plt.title("Harry's Assists")

    plt.show()