class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = list()
        res = 0

        for op in operations:
            if op == "D":
                new_score = scores[-1] * 2
                scores.append(new_score)
                res += new_score
            elif op == "C":
                invalid_score = scores.pop()
                res -= invalid_score
            elif op == "+":
                new_score = scores[-1] + scores[-2]
                scores.append(new_score)
                res += new_score
            else:
                new_score = int(op)
                scores.append(new_score)
                res += new_score

        return res

        

        
        