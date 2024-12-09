from typing import List

class Solution:
    def two_city_schedule_cost(self, costs: List[List[int]]) -> int:
        """
        Given a list of costs, this function returns the minimum cost to transport all employees.

        Approach:
	        1.	Sort the input array: Sort the costs array by the difference between the first and 
            second elements of each subarray (i.e., cost[0] - cost[1]).
	        2.	Divide the employees: Assign the first half of the sorted array to one 
            group (using the first element of each subarray) and the second half to the other 
            group (using the second element of each subarray).
	        3.	Compute the total cost: Sum up the costs based on these assignments and 
            return the result.
        """
        cost = 0
        n = len(costs)
        half = n // 2

        if n == 0:
            return cost
        sorted_costs = sorted(costs, key = lambda x: x[0] - x[1])

        for i in range(half):
            cost += sorted_costs[i][0]
            cost += sorted_costs[half + i][1]

        return cost
