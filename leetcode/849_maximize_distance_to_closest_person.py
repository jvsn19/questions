class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        size_seats = len(seats)
        last_person = -1
        answer = 0
        
        for idx, person in enumerate(seats):
            if person == 1:
                answer = idx if last_person == -1 else max(answer, (idx - last_person)//2)
                last_person = idx
                
        answer = max(answer, size_seats - last_person - 1)
        
        return answer
