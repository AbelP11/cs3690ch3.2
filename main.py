MAX, MIN = float('inf'), -float('inf')


def get_best_value(is_maximizing, a, b):
    return max(a, b) if is_maximizing else min(a, b)


def minimax(depth, nodeIndex, maximizing,
            values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    current_val = MAX if not maximizing else MIN

    for i in range(0, 2):
        val = minimax(depth + 1, nodeIndex * 2 + i, not maximizing, values, alpha, beta)
        current_val = get_best_value(maximizing, current_val, val)

        if maximizing:
            alpha = max(alpha, current_val)
            if beta <= alpha:
                break
        else:
            beta = min(beta, current_val)
            if beta <= alpha:
                break

    return current_val

if __name__ == "__main__":
    values = [3, 5, 17, 8, -2, 5, -1, 7]
    print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))

