def min_two(a, b): 
    if a < b:
        return a
    else:
        return b
def min_three(a, b, c):
    return min_two(min_two(a, b), c)
a, b, c = map(int, input().split())
print(min_three(a, b, c))