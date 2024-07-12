# convex-hull(컨벡스 홀)

기하 시험공부를 하다가 내적을 구하는 방법이 두개라 풀면서 흥미로웠고(이래서 화학이 재밌음) 내적이 있으면 외적인 있겠다 싶어 찾아보다가 외적을 이용한 알고리즘인 convex hull 알고리즘이 있어서 이를 푸는 알고리즘에 대해 조사해보았다.

-----

* 외적
  2차원 공간에서 두 벡터 a = (a1, a2)와 b = (b1, b2)의 외적
  a x b = a1 * b2 - a2 * b1
  두 벡터가 시계 방향으로 배치되면 양의 값
  두 벡터가 반시계 방향으로 배치되면 음의 값
  두 벡터가 이루는 각도의 방향을 알 수 있다.
  

* convex hull
  Convex Hull은 주어진 점들을 모두 포함하면서, 그 점들 중 일부를 연결하여 만든 가장 작은 볼록 다각형을 말한다.



이를 구하는 효율적인 알고리즘들이 많이 연구되어 왔으며, 대표적으로 Graham Scan 알고리즘, Jarvis March 알고리즘 등이 있다.

------

# Graham Scan 알고리즘(그래엄 스캔 알고리즘)

* 가장 작은 y좌표인 점을 기준점으러 삼는디.(가장 작은 y좌표인 점이 여러개 있으면 x좌표가 작은 점)

```python
p0 = min(points, key=lambda p: (p.y, p.x))
```

* 기준점 p0을 기준으로 다른 모든 점들을 반시계 방향으로 정렬한다.

```python
points.sort(key=lambda p: (math.atan2(p.y - p0.y, p.x - p0.x), (p.y - p0.y) ** 2 + (p.x - p0.x) ** 2))
```

1. 각도: math.atan2(p.y - p0.y, p.x - p0.x) 함수는 p0과 점 p 사이의 각도를 계산한다.
2. 거리: 각도가 같을 경우에는 p0으로부터의 거리를 기준으로 정렬한다. 거리 계산은 피타고라스 정리를 사용하여 (p.y - p0.y) ** 2 + (p.x - p0.x) ** 2로 한다

* 정렬된 점들 중에서 p0과 각도가 가장 작은점을 볼록 껍질의 초기 점으로 설정합니다

```python
hull = [p0, points[1]]
```

* 세 점 사이의 외적(cross product)을 계산하여, 세 점이 시계 방향, 반시계 방향, 직선상에 있는지를 판별한다.

```python
for i in range(2, len(points)):
    while len(hull) > 1 and cross(hull[-2], hull[-1], points[i]) <= 0:
        hull.pop()
    hull.append(points[i])
```

* 현재 점이 시계 방향으로 돌거나 직선 상에 있을 때 그 점을 제거한다.
```python
while len(hull) > 1 and cross(hull[-2], hull[-1], points[i]) <= 0:
```

* 외적 구하는 코드
```python
def cross(p1: Point, p2: Point, p3: Point) -> float:
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
```
남은 점들로 볼록 껍질을 생성한다.

-----

# Jarvis March 알고리즘(자비스 행진 알고리즘)

* x 좌표가 가장 작은 점을 찾고, 만약 x 좌표가 같은 점들이 여러 개 있다면 y 좌표가 가장 작은 점을 선택한다.
```python
def leftmost_point(points):
    min_point = points[0]
    for p in points[1:]:
        if p.x < min_point.x or (p.x == min_point.x and p.y < min_point.y):
            min_point = p
    return min_point
```

* 세 점의 방향을 계산한다.
```python
def cross(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)
```

* 'next_point가 현재 점과 같거나, point, next_point, q 세 점이 반시계 방향이면 next_point를 q로 갱신한다.

```python
while True:
    hull.append(point)
    next_point = points[0]
    for q in points[1:]:
        if next_point == point or orientation(point, next_point, q) > 0:
            next_point = q
    point = next_point
    if point == start:
        break
```
