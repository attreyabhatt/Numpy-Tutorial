import numpy as np

stats = np.array([[1,2,3],[4,5,6]])
print(stats)

# min/max of all elements
min = np.min(stats)

# min/max on x/y
max_x = np.max(stats,axis=1)

# sum of all elements
sum = np.sum(stats)

# sum of elements on y-axis/x-axis
sum_y = np.sum(stats,axis=0)

# Mean/Average

mean = stats.mean()
print(mean)

