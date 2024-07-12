import random
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index must be 0 or 1")

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

num_points = 20
points = [Point(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(num_points)]

def jarvis_march(points):
    def leftmost_point(points):
        min_point = points[0]
        for p in points[1:]:
            if p.x < min_point.x or (p.x == min_point.x and p.y < min_point.y):
                min_point = p
        return min_point

    def cross(o, a, b):
        return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

    hull = []
    start = leftmost_point(points)
    point = start

    while True:
        hull.append(point)
        next_point = points[0]
        for q in points:
            if next_point == point or cross(point, next_point, q) < 0:
                next_point = q
        point = next_point
        if point == start:
            break

    return hull

def plot_hull(points, hull):
    plt.figure()
    plt.plot([p.x for p in points], [p.y for p in points], 'ro')
    for i in range(len(hull)):
        p1 = hull[i]
        p2 = hull[(i + 1) % len(hull)]
        plt.plot([p1.x, p2.x], [p1.y, p2.y], 'b-')
    plt.show()


convex_hull = jarvis_march(points)
plot_hull(points, convex_hull)
