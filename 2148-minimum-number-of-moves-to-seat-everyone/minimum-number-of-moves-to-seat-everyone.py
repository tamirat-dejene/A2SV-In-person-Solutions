class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0
        for i, student in enumerate(students):
            moves += abs(student - seats[i])
        return moves


        