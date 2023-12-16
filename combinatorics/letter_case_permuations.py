class Solution:
    def letterCasePermutation(self, input_str: str) -> List[str]:
        def fill_blanks(idx_subproblem, partial_solution):
            if idx_subproblem == len(input_str):
                res.append("".join(partial_solution))
                return
		
            if input_str[idx_subproblem].isdigit():
                partial_solution.append(input_str[idx_subproblem])
                fill_blanks(idx_subproblem + 1, partial_solution)
                partial_solution.pop()
            else:
                partial_solution.append(input_str[idx_subproblem].lower())
                fill_blanks(idx_subproblem + 1, partial_solution)
                partial_solution.pop()
			
                partial_solution.append(input_str[idx_subproblem].upper())
                fill_blanks(idx_subproblem + 1, partial_solution)
                partial_solution.pop()
    
        res = []
        fill_blanks(0, [])
        return res