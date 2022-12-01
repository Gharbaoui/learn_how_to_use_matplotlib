import matplotlib.pyplot as plt
import numpy.random as rd

def main():
    x_axis = list(range(0, 10))
    y_axis = rd.randint(100, size=(10))
    plt.plot(x_axis, y_axis)
    plt.xlabel('cache-size')
    plt.ylabel('hate-rate')
    plt.title('cache-statics')
    plt.show()

if __name__ == "__main__":
    main()
