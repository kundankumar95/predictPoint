from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs = np.array([1,2,3,4,5,6], dtype=np.float64)
ys = np.array([5,4,6,5,6,7], dtype=np.float64)

def beat_fit_slope_and_intersepts(xs,ys):
    m = ( ((mean(xs) * mean(ys)) - mean(xs * ys)) / ((mean(xs)*mean(ys)) - mean(xs * xs)))

    b = mean(ys) - m*mean(xs)
    return m,b

m,b = beat_fit_slope_and_intersepts(xs,ys)
regression_line = [(m*x) + b for x in xs]

predict_x = 8
predict_y = (m*predict_x) + b

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y)
plt.plot(xs,regression_line)
plt.show()