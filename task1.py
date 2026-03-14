#!/usr/bin/env python3

import sys

def distance():
    x1 = int(sys.argv[1]);y1 = int(sys.argv[2]);
    x2 = int(sys.argv[3]);y2 = int(sys.argv[4]);
    dist = ( (x2-x1)**2 + (y2-y1)**2 )**0.5
    return dist


def ETA(distanceByCoordinates):
    initialVelocity = int(sys.argv[5])
    acceleration = int(sys.argv[6])
    topSpeed = int(sys.argv[7])
    distanceToTopSpeed = (topSpeed**2 - initialVelocity**2)/(2*acceleration)

    if distanceToTopSpeed >= distanceByCoordinates:
        totalTime = -initialVelocity/acceleration + (initialVelocity**2/acceleration**2 + 2*distanceByCoordinates/acceleration)**0.5 

    else:
        time1 = (topSpeed - initialVelocity)/acceleration

        distancePartOne = initialVelocity*time1 + (0.5)*acceleration*(time1)**2
        distancePartTwo = distanceByCoordinates - distancePartOne
        time2 = distancePartTwo/topSpeed
        totalTime = time1+time2
    return totalTime


def main():
    dist = distance()
    print(f"distance to destination: {dist:.2f}m")
    time = ETA(dist)
    print(f"time required: {time:.2f}sec")


if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print("usage: ./distance.py x1 y1 x2 y2  initialVelocity Acceleration topSpeed")
        sys.exit(1)
