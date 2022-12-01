import matplotlib.pyplot as plt
import numpy.random as rd

def name_axis():
    plt.xlabel('cache-size')
    plt.ylabel('hate-rate')
    plt.title('cache-statics')


def plot_moroco_temp(x_axis):
    y_axis = rd.randint(100, size=(10))
    plt.plot(x_axis, y_axis)

def plot_auts_temp(x_axis):
    y_axis = rd.randint(60, size=(10))
    plt.plot(x_axis, y_axis)

def plot_legends():
    plt.legend(['maroc', 'austr'])

def show_graph():
    plot_legends()
    plt.show()

def main():
    x_axis = list(range(0, 10))
    plot_moroco_temp(x_axis)
    plot_auts_temp(x_axis)
    show_graph()

if __name__ == "__main__":
    main()
