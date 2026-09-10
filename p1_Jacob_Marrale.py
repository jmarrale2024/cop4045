import math
import matplotlib.pyplot as plt

end = True

while end == True:
    a = float(input(f"input a: "))
    b = float(input(f"input b: "))
    c = float(input(f"input c: "))
    end = input("press enter to get results")

    insqrt = (b**2)-(4*a*c)

    n = 150 # amount of points for the plots

    if insqrt < 0:
        print("no real solutions")
    # plot code
        xopt = -b/(2*a)
        low = xopt - 2
        high = xopt + 2
        step = (high - low) / (n - 1)
        xs = [] # X points
        ys = [] # Y points
        for i in range(n):
            x = low + i * step
            y = (a*(x**2)) + (b*x) + c
            xs.append(x)
            ys.append(y)
        plt.plot(xs, ys, marker = 'o', markersize = 2)
        plt.grid(True)
        plt.show()
    elif insqrt == 0:
        x1 = -b/(2*a)
        #x1
        print(f"one solution: {x1}")
    # plot code
        low = min(x1) - 2
        high = max(x1) + 2
        step = (high - low) / (n - 1)
        xs = [] # X points
        ys = [] # Y points
        for i in range(n):
            x = low + i * step
            y = (a*(x**2)) + (b*x) + c
            xs.append(x)
            ys.append(y)
        plt.plot(xs, ys, marker = 'o', markersize = 2)
        plt.axhline(0, color='red') # y = 0 highlighted to show root line
        plt.grid(True)
        plt.show()

    elif insqrt > 0:
        #x1 and x2
        outsqrt = math.sqrt(insqrt)
        x1 = ((-b + outsqrt)/(2*a))
        x2 = ((-b - outsqrt)/(2*a))
        print(f"two solutions: x1={x1} x2={x2}")
    # plot code
        low = min(x1, x2) - 2
        high = max(x1, x2) + 2
        step = (high - low) / (n - 1)
        xs = [] # X points
        ys = [] # Y points
        for i in range(n):
            x = low + i * step
            y = (a*(x**2)) + (b*x) + c
            xs.append(x)
            ys.append(y)
        plt.plot(xs, ys, marker = 'o', markersize = 2)
        plt.axhline(0, color='red') # y = 0 highlighted to show root line
        plt.grid(True)
        plt.show()