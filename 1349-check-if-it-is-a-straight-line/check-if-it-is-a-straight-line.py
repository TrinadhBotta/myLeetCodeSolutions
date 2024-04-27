class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x_dif = coordinates[1][0]-coordinates[0][0]
        y_dif = coordinates[1][1]-coordinates[0][1]
        if x_dif!=0:
            slope = y_dif/x_dif
        else:
            slope = float('inf')

        for i in range(2,len(coordinates)):
            pre_x = coordinates[i][0]-coordinates[i-1][0]
            pre_y = coordinates[i][1]-coordinates[i-1][1]
            if slope == float('inf') and pre_x==0:
                continue
            elif pre_x == 0 or slope != (pre_y/pre_x):
                return(False)
        return(True)