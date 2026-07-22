class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_gas = 0
        start_idx = 0

        if sum(gas) < sum(cost): # no solution
            return -1
        
        for i in range(len(gas)):
            cur_gas += gas[i] - cost[i]
            
            if cur_gas < 0: # if this starting point leads to a dead end
                start_idx = i + 1 # greedily try to find the next starting point since the problem guarantees to have a unique solution
                cur_gas = 0

        
        return start_idx