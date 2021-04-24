import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸, dpi是屏幕分辨率（像素/英寸）
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=1)

    # 突出起点与终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # plt.scatter(rw.x_values, rw.y_values, s=1)
    plt.show()

    keep_running = input("Make another random walk? (y/n)")
    if keep_running == 'n':
        break


