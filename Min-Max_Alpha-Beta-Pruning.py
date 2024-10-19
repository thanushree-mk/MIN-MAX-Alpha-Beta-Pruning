import math
def minimax(depth, node_index, is_maximizing, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]

    if is_maximizing:
        max_value = -math.inf
        for i in range(2):  
            value = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            max_value = max(max_value, value)
            alpha = max(alpha, max_value)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break
        return max_value

    else:  # Minimizer's turn
        min_value = math.inf
        for i in range(2):  
            value = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            min_value = min(min_value, value)
            beta = min(beta, min_value)

            if beta <= alpha:
                break
        return min_value

max_depth = 3
values = [-1, 4, 2, 6, -3, -5, 0, 7]

alpha = -math.inf
beta = math.inf

optimal_value = minimax(0, 0, True, values, alpha, beta, max_depth)

print("The optimal value is:", optimal_value)
