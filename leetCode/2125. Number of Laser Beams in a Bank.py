class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        answer = 0
        last_beam = 0 
        for col in bank:
            now_beam = col.count("1")
            if now_beam:
                answer += (last_beam*now_beam)
                last_beam = now_beam
        return answer 
