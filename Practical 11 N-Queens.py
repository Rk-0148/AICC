class NQueens:
    def __init__(self, n):
        self.n = n
        self.columns = [-1] * n
        self.solutions = []
        
    def solve(self):
        self.backtrack(0)
        
    def backtrack(self, row):
        if row == self.n:
            solution = []
            for col in self.columns:
                queen_position = ['.'] * self.n
                queen_position[col] = 'Q'
                solution.append(''.join(queen_position))
            self.solutions.append(solution)
            return
        
        for col in range(self.n):
            if self.is_valid(row, col):
                self.columns[row] = col
                self.backtrack(row + 1)
    
    def is_valid(self, row, col):
        for i in range(row):
            if self.columns[i] == col or \
                    self.columns[i] - col == i - row or \
                    self.columns[i] - col == row - i:
                return False
        return True
        
    def get_solutions(self):
        return self.solutions


# Example usage
n = 6
queens = NQueens(n)
queens.solve()
solutions = queens.get_solutions()

print(f"Number of solutions for {n}-queens problem: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        print(row)
    print()
