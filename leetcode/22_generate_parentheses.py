class SolutionA:
    def generateParenthesis(self, n: int) -> List[str]:
        self.answer = []
        
        
        def helper(S = '', left = 0, right = 0):
            if left + right == 2*n:
                self.answer.append(S)
                return
            
            if left < n:
                helper(S + '(', left + 1, right)
                
            if right < left:
                helper(S + ')', left, right + 1)
        
    
        helper()
        return self.answer

###############################################################

class SolutionB:
    def generateParenthesis(self, n: int) -> List[str]:

        def helper(n):
            if n == 1:
                return ['()']

            prev_pars = helper(n-1)
            curr_pars = set()

            for prev_par in prev_pars:
                for i in range(len(prev_par)):
                    to_insert = prev_par[:i] + '()' + prev_par[i:]
                    curr_pars.add(to_insert)

            return list(curr_pars)


        return helper(n)
