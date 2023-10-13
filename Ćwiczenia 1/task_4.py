# CODE HERE
def num_fact(n):
    if n == 0:
        return 1
    else:
        return n * num_fact(n - 1)