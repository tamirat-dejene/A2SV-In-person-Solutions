class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        labels = [label]

        while label >= 1:
            if label == 1:
                return labels[::-1]
            
            # find row
            crow = floor(log2(label)) + 1

            # find lower bound and upper bound for both parent and child row
            crow_lb = 1 << (crow - 1) 
            crow_ub = (1 << crow) - 1

            prow_lb = 1 << (crow - 2)
            prow_ub = (1 << (crow - 1)) - 1

            # find parent, and assign it to the label
            if crow % 2 == 0:
                label = prow_lb + ((crow_ub - label) // 2)
            else:
                label = prow_ub - ((label - crow_lb) // 2)

            labels.append(label)
