'''
871. Minimum Number of Refueling Stops

Problem Statment: A car: starting point --> destination (target)
input: Stations -> [[10,60],[20,30],[30,30],[60,40]], where 0th position is 
distance, and 1st is fuel 

TASK: Return the minimum number of refueling stops the car
 must make in order to reach its destination. 
If it cannot reach the destination, return -1.

starting from position 0 and goign to position 10, with 10 fuel 
Input: target = 100, startFuel = 1, stations = [[10,100]] => return -1
                            0[1] --> [10, 100] ----> 100
                
Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]

                                     0+60       50          40        10+40.        10
            startFuel = [0, 10] -> [[10,60] -> [20,30] -> [30,30] -> [60,40]] --> [100, inf]
                                      F                                 F
            stops = 2
            fuel = 60


EXAMPLE2: Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]

                                     0+60.      50.         40        10          -90
            startFuel = [0, 10] -> [[10,60] -> [20,30] -> [30,30] -> [60,10]] --> [100, inf]
                                      f  
                                   stops = 1,    1,          1         2
                                   fuel = 60,    50          40        40
                        max_heap =   [30, 30,10]

Approach: 
    -> Append destination to the stations with infinity gas
    -> setup a max heap (to keep track of gas available along the way)
    -> stop variable will keep track of stops we made
    -> Make first check: check if its possible to reach 0th index stop:
            -> If un reachable simple rturn -1, otherwise update the fuel,
              add 0th index fuel in max heap
    -> run loop on stations starting from 1 till n (n is the length of updates stations)

        -> update the gas:
        -> check if fuel is less than or equal to zero:
            -> run a while loop as long as we have elements in the max heap and fuel < 0:
                -> keep refueling and increment the stop by 1 
        -> if fuel is till less than 0: return -1
        -> add current stations fuel to max heap
    -> return stop

Time: O(n log n)
Space: O(n) max heap
'''
import heapq
from typing import List
class Solution:
    def min_refuel_stops(self, target: int, start_fuel: int, stations: List[List[int]]) -> int:
        '''
        Given target and list of stations: This functions returns 
        minimum number of stops required to reach the target
        '''

        stops = 0

        if len(stations) == 0:
            return 0 if (target - start_fuel) <= 0 else -1

        stations.append([target, float("inf")])
        curr_fuel = start_fuel
        max_heap = []

        curr_fuel -= stations[0][0]
        if curr_fuel < 0:
            return -1

        heapq.heappush(max_heap, -stations[0][1])

        for i in range(1, len(stations)):
            curr_fuel -= (stations[i][0] - stations[i - 1][0])

            while len(max_heap) > 0 and curr_fuel < 0:
                stops += 1
                curr_fuel += -heapq.heappop(max_heap)

            if curr_fuel < 0:
                return -1
            heapq.heappush(max_heap, -stations[i][1])

        return stops
