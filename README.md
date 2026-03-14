#This is the first task
this python program calculates the distance between two points on a 2d plane,
and also calculate the ETA(Estimated Time of Arrival) provided the initial speed,
acceleration and the total speed achievable

##How it works
This uses cmdline arguments which can be provided directly from the CLI environment,
which is leveraged by the sys module in python.This provides us with the exit codes 
which are greatly used in terminal env's. 0 for sucess and 1 for failure

for ETA calculation,it checks if the distance travelled to achieve total speed is
greater than the distance between the two coordinates.if yes,it calculates the time
taken to reach the coordinate destination from source.if the distance to achieve total
speed is less than the distance between the coords,we find the time seperately,both for
the time taken to achieve top speed and the time taken to finish the rest of the distance
in cruise drive since acceleration would be set 0,since we achieved top speed.

##Usage

###clone the repo

```
git clone https://github.com/javed-habeeb/javedhabeeb_horizon_s2.git
```

###Method1: set executible permission to the file
```
chmod +x task1.py
```
###Run the executible
```
./task1.py x1 y1  x2 y2  initialVelocity acceleration totalSpeed
```

###Method2: run it using python3
```
python3 task1.py x1 y1  x2 y2  initialVelocity acceleration totalSpeed
```
