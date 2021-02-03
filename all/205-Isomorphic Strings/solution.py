class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dish = {}
        dishh = {}
        flag = True
        for b,c in zip(s,t):
            if b not in dish:
                dish[b] = []
            if c not in dishh:
                dishh[c] = []
            if c not in dish[b]:
                dish[b].append(c)
            if b not in dishh[c]:
                dishh[c].append(b)
            if len(dish[b]) > 1 or len(dishh[c]) > 1:
                flag = False
                break
        
        return flag
