from pulp import LpProblem, LpVariable, LpMinimize, LpInteger, lpSum, PULP_CBC_CMD
import re

f = open('25-10.txt').read().split('\n')

def parse_input(input_str):
    """
    Parse input like: "(3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
    Returns:
        ops: list of tuples of indices
        target: list of target values
    """
    # Split into brackets and curly braces
    parts = input_str.split('{')
    brackets_str = parts[0].strip()
    target_str = parts[1].rstrip('}').strip()
    
    # Parse brackets
    ops = []
    bracket_pattern = r'\(([^)]+)\)'
    matches = re.findall(bracket_pattern, brackets_str)
    for match in matches:
        if ',' in match:
            indices = tuple(map(int, match.split(',')))
        else:
            indices = (int(match),)
        ops.append(indices)
    
    # Parse target
    target = list(map(int, target_str.split(',')))
    
    return ops, target

def solve_min_moves(ops, target):
    """
    Find minimum number of operations to reach target from zeros.
    
    Args:
        ops: list of tuples, each tuple contains indices to increment
        target: list of target values for each position
        
    Returns:
        dict: {
            'min_moves': int,
            'counts': list of operation counts,
            'solution_found': bool
        }
    """
    n_positions = len(target)
    n_ops = len(ops)
    
    # Create LP problem
    prob = LpProblem("MinimumOperations", LpMinimize)
    
    # Variables: how many times each operation is used
    x = [LpVariable(f"x{i}", lowBound=0, cat=LpInteger) for i in range(n_ops)]
    
    # Objective: minimize total number of operations
    prob += lpSum(x)
    
    # Constraints: for each position, sum of increments must equal target
    for pos in range(n_positions):
        # Sum contributions from all operations
        contributions = []
        for i, op_indices in enumerate(ops):
            if pos in op_indices:
                contributions.append(x[i])
        prob += lpSum(contributions) == target[pos]
    
    # Solve
    solver = PULP_CBC_CMD(msg=False)
    prob.solve(solver)
    
    # Extract solution
    if prob.status == 1:  # Optimal
        counts = [int(var.value()) for var in x]
        min_moves = sum(counts)
        return {
            'min_moves': min_moves,
            'counts': counts,
            'solution_found': True
        }
    else:
        return {
            'min_moves': None,
            'counts': None,
            'solution_found': False
        }

def solve_with_start(ops, start, target):
    """
    More general version with custom start vector.
    """
    n_positions = len(target)
    n_ops = len(ops)
    
    prob = LpProblem("MinimumOperations", LpMinimize)
    x = [LpVariable(f"x{i}", lowBound=0, cat=LpInteger) for i in range(n_ops)]
    prob += lpSum(x)
    
    # Convert operations to increment vectors
    inc_vectors = []
    for op_indices in ops:
        vec = [0] * n_positions
        for idx in op_indices:
            vec[idx] = 1
        inc_vectors.append(vec)
    
    # For each position: start[pos] + sum(op_contributions) = target[pos]
    for pos in range(n_positions):
        contributions = []
        for i in range(n_ops):
            if inc_vectors[i][pos] == 1:
                contributions.append(x[i])
        prob += (start[pos] + lpSum(contributions) == target[pos])
    
    solver = PULP_CBC_CMD(msg=False)
    prob.solve(solver)
    
    if prob.status == 1:
        counts = [int(var.value()) for var in x]
        min_moves = sum(counts)
        return min_moves, counts
    return None, None

def main():
    # Example usage
    tly = 0

    for prob in f:
        input_str = prob.split(']')[1]

        #input_str = "(3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
        #input_str = "(1,2,5,8) (0,2,3,4,5,6,8) (0,2,3,4,6,7,8) (0,2,3,5,7) (0,1,2,5,6,7) (1,2,3,5,7) (0,1,3,7) {77,43,93,66,39,74,58,65,51}"
        #input_str = "(0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"

        ops, target = parse_input(input_str)
        print(f"Operations: {ops}")
        print(f"Target: {target}")
        
        result = solve_min_moves(ops, target)

        tly += result['min_moves']
        
        if result['solution_found']:
            print(f"\nMinimum moves: {result['min_moves']}")
            print("\nOperation counts:")
            for i, count in enumerate(result['counts']):
                if count > 0:
                    print(f"  {ops[i]}: {count} times")
            
            # Verify
            print("\nVerification:")
            n_positions = len(target)
            current = [0] * n_positions
            for i, count in enumerate(result['counts']):
                if count > 0:
                    for _ in range(count):
                        for idx in ops[i]:
                            current[idx] += 1
            print(f"Start: {[0]*n_positions}")
            print(f"Reached: {current}")
            print(f"Target: {target}")
            print(f"Match: {current == target}")
        else:
            print("No solution found!")
    print(tly)

if __name__ == "__main__":
    main()
