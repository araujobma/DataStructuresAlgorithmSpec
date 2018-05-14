# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    print(segments)
    points = []
    #write your code here
    for i in range(0,len(segments)):
        if segments[i] == -1:
            continue
        for j in range(i+1,len(segments)):
            if segments[j] == -1:
                continue
            if segments[i].end >= segments[j].start:
                segments[i] = -1
            else:
                break
        points.append(segments[i].end)
		
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
