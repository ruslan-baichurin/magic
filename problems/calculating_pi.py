def calculate_pi(n_terms: int) -> float:
    numerator, denominator, operation, pi = 4.0, 1.0, 1.0, 0.0

    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0

    return pi


print(calculate_pi(100000000))
