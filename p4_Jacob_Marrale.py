import math
import matplotlib.pyplot as plt

def plot_function(fun_str, domain, ns): # (math function - string, (xmin, xmax) - float tuple,number of samples - integer)

# plot code
    xmin, xmax = domain
    low = xmin
    high = xmax
    step = (high - low) / (ns - 1)
    xs = [] # x points
    ys = [] # y points
    for i in range(ns):
        x = low + i * step
        y = eval(fun_str)
        xs.append(x)
        ys.append(y)
    plt.plot(xs, ys, marker = 'o', markersize=2)
    plt.xlim(xmin,xmax)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(fun_str)
    plt.grid(True)
    plt.show()

    # print some points
    
    print(" "*5,"x"," "*5,"y")
    print('-'*15)
    for i in range(10):
        print(f"{xs[i]}     {ys[i]}")
    print("...........")

    

while True:

    fun_str = input("Enter function with variable x: ")
    samples = int(input("Enter number of samples: "))
    xmin = int(input("Enter xmin: "))
    xmax = int(input("Enter xmax: "))
    domain = (xmin,xmax)

    plot_function(fun_str, domain, samples)
    break