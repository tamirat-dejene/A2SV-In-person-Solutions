class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0

        ans = []

        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] <= secondList[j][0]:
                if firstList[i][1] >= secondList[j][0]:
                    ans.append([
                        secondList[j][0], min(firstList[i][1], secondList[j][1])
                    ])
            else:
                if secondList[j][1] >= firstList[i][0]:
                    ans.append([
                        firstList[i][0], min(firstList[i][1], secondList[j][1])
                    ])
            
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return ans