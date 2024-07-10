# convex-hull(컨벡스 홀)

기하 시험공부를 하다가 원래 알고있던 것을 기하적으로 풀수 있는게 있어(미적분으로 풀수 있지만 기하에서 공식 외워서 푸는 문제들..) 기하에 흥미가 생겼고 전에 알고리즘 문제를 풀다가 convex hull이 나와 이를 기하적으로 푸는 알고리즘이 있다고 하여 조사해보려 한다.

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
