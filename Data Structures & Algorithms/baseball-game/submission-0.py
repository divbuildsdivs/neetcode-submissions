class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        sum = 0
        for op in operations:
            if op == '+':
                score.append(score[-1] + score[-2])
                sum += score[-1]
            elif op == 'D':
                score.append(2 * score[-1])
                sum += score[-1]
            elif op == 'C':
                poppedScore = score.pop()
                sum -= poppedScore
            else:
                score.append(int(op))
                sum += score[-1]
        return sum
            
            
        