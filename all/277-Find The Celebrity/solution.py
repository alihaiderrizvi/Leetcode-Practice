# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        def is_celeb(i, lst):
            for j in range(len(lst)):
                if i == j:
                    continue
                if knows(i,j) or not knows(j,i):
                    return False
            return True
        
        
        
        lst = [i for i in range(n)]
        
        while len(lst) != 1:
            if knows(lst[0], lst[1]):
                lst.remove(lst[0])
            else:
                lst.remove(lst[1])
        celeb = lst[0]
        lst = [i for i in range(n)]
        if is_celeb(celeb, lst):
            return celeb
        return -1
