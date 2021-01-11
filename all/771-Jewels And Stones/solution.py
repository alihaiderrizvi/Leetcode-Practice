class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set()
        for i in jewels:
            jewels_set.add(i)
        
        count = 0
        for i in stones:
            if i in jewels_set:
                count += 1
        
        return count
