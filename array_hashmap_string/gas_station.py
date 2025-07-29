# https://leetcode.com/problems/gas-station/submissions/1705583975/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def canCompleteCircuit(self, gas, cost):
        # if the total gas is less than the total cost,
        # it is impossible to complete the circuit
        if sum(gas) < sum(cost):
            return -1
        total_tank = 0
        curr_tank = 0
        starting_station = 0
        for i in range(len(gas)):
            # the amount of gas in the current station
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # if the car runs out of gas at the current station
            if curr_tank < 0:
                # reset the current tank
                curr_tank = 0
                # set the starting station to the next station
                starting_station = i + 1
        if total_tank < 0:
            return -1
        # return the starting station
        return starting_station