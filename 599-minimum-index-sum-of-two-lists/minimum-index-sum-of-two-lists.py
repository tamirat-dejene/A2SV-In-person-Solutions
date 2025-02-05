class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        container_1, container_2 = {}, {}
        for i, string in enumerate(list1): 
            if string not in container_1: container_1[string] = i
        for i, string in enumerate(list2): 
            if string not in container_2: container_2[string] = i

        common = { string for string in container_1 if string in container_2 }
        
        min_ind_sum = float('inf')
        for string in common:
            min_ind_sum = min(min_ind_sum, container_1[string] + container_2[string])
        
        return [string for string in common if container_1[string] + container_2[string] == min_ind_sum]

                
        