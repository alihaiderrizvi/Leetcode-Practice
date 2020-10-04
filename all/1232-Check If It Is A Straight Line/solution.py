class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        print(coordinates)
        if len(coordinates) == 2:
            return True
        s = set()
        
        for p1,p2,p3 in zip(coordinates[:-2], coordinates[1:-1], coordinates[2:]):
            if (p2[1]-p1[1])*(p3[0]-p2[0]) != (p3[1]-p2[1])*(p2[0]-p1[0]):
                return False
        return True
