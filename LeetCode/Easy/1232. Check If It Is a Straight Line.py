from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        diff_x = abs(coordinates[0][0] - coordinates[1][0])
        diff_y = abs(coordinates[0][1] - coordinates[1][1])
        for i in range(2, len(coordinates)):
            point = coordinates[i]
            diff_x_p = abs(point[0] - coordinates[0][0])
            diff_y_p = abs(point[1] - coordinates[0][1])
            if diff_x_p * diff_y != diff_y_p * diff_x:
                return False
        return True