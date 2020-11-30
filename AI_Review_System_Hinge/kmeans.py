import random
import math
import sys
import time
from collections import defaultdict


def kmeans(points, centroids, numIters):
    """
    :param points: List[Tuple], containing all the data points to be segmented
    :param centroids: List[Tuple], containing K number of centroids
    :param numIters: int, the number of iterations to be exacuted
                     (Attention: make sure to break if converged)
    :return: centorids, assignments, cost, segments (See assignemnt 3 handout for details)
    """
    cost = 0
    assignments_prev = []
    for i in range(numIters):
        assignments = []
        segments = defaultdict(list)
        for point in points:
            Min = 100
            m = 0
            assignment = 0
            for centroid in centroids:
                if Min > distance_square(centroid, point):
                    assignment = m
                    Min = distance_square(centroid, point)
                m += 1
            assignments.append(assignment)
            segments[assignment].append(point)

        if assignments_prev == assignments:
            for n in range(len(centroids)):
                for point in segments[n]:
                    cost += (distance_square(centroids[n], point))**0.5
            return centroids, assignments, cost, segments
        assignments_prev = assignments

        for j in range(len(centroids)):
            x = 0
            y = 0
            for k in range(len(segments[j])):
                x += segments[j][k][0]
                y += segments[j][k][1]
            x = x / len(segments[j])
            y = y / len(segments[j])
            centroids[j] = [x, y]

    for i in range(len(centroids)):
        for point in segments[i]:
            cost += (distance_square(centroids[i], point))**0.5
    return centroids, assignments, cost, segments


def distance_square(point1, point2):
    return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

############## DO NOT EDIT THE CODES BELOW THIS LINE ##############


def problem2_a():
    points0 = generate0()
    centroids, assignments, cost, segments = kmeans(points0, [(2, 3), (2, -1)], 3)
    print('Centroids:', centroids, end=' // ')
    print('Assignments:', assignments, end=' // ')
    print('Cost:', cost)


def problem2_b():
    points0 = generate0()
    centroids, assignments, cost, _ = kmeans(points0, [(0, 1), (3, 2)], 3)
    print('Centroids:', centroids, end=' // ')
    print('Assignments:', assignments, end=' // ')
    print('Cost:', cost)


def problem2_c():
    points1 = generate1()
    tic = time.time()
    centroids, assignments, cost, segments = kmeans(points1, [(0.27, 0.27), (0.43, 0.43)], 5000)
    toc = time.time()
    if toc - tic > 0.5:
        print('Time Out! Please try to speed up your program.')
    else:
        print('Centroids:', centroids)
        print('Number of points in 1:', len(segments[1]))
        print('Number of points in 0:', len(segments[0]))
        print('Cost:', cost)


def problem2_d():
    points1 = generate1()
    tic = time.time()
    centroids, assignments, cost, segments = kmeans(points1, [(0.27, 0.27), (0.35, 0.35), (0.43, 0.43)], 5000)
    toc = time.time()
    if toc - tic > 0.5:
        print('Time Out! Please try to speed up your program.')
    else:
        print('Centroids:', centroids)
        print('Number of points in 2:', len(segments[2]))
        print('Number of points in 1:', len(segments[1]))
        print('Number of points in 0:', len(segments[0]))
        print('Cost:', cost)


def generate0():
    return [(1, 0), (1, 2), (3, 0), (2, 2)]


def generate1():
    random.seed(42)
    x1 = [random.randint(30, 50) / 100 for i in range(100)]
    y1 = [random.randint(28, 48) / 100 for i in range(100)]
    x2 = [random.randint(18, 38) / 100 for i in range(100)]
    y2 = [random.randint(18, 38) / 100 for i in range(100)]
    data1 = []
    for i in range(len(x1)):
        data1.append((x1[i], y1[i]))
    data2 = []
    for i in range(len(x2)):
        data1.append((x2[i], y2[i]))
    all_data = data1 + data2
    random.shuffle(all_data)
    return all_data


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print('Please Enter the test you would like to run.')
        print('For example:')
        print('Python3 kmeans.py 2a')
        print('Python3 kmeans.py 2b')
        print('Python3 kmeans.py 2c')
        print('Python3 kmeans.py 2d')
    elif len(args) == 1:
        if args[0] == '2a':
            problem2_a()
        elif args[0] == '2b':
            problem2_b()
        elif args[0] == '2c':
            problem2_c()
        elif args[0] == '2d':
            problem2_d()
        else:
            print('Illegal...')
    else:
        print('Illegal...')


if __name__ == '__main__':
    main()
