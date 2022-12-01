import matplotlib.pyplot as plt
import numpy.random as rd



def name_axis():
    plt.xlabel('cache-size')
    plt.ylabel('hate-rate')
    plt.title('cache-statics')


def plot_moroco_temp(x_axis):
    y_axis = rd.randint(100, size=(10))
    plt.plot(x_axis, y_axis, 'k-',marker='.', label='maroc')

def plot_auts_temp(x_axis):
    y_axis = rd.randint(60, size=(10))
    plt.plot(x_axis, y_axis, color='b', marker= 'o',linestyle='--', label='austr')

def plot_legends():
    plt.legend()

def show_graph():
    plot_legends()
    plt.grid(True)
    plt.savefig('plot.png')
    plt.show()

def main():
    x_axis = list(range(0, 10))
    plot_moroco_temp(x_axis)
    plot_auts_temp(x_axis)
    plt.style.use('ggplot')
    show_graph()


if __name__ == "__main__":
    main()
