def linear_search(values, target):
    f = 0
    for value in values:
        f = f + 1
        if target == value:
            return f"(249,{f})"


def binary_search(values, target):
    binary_search.counter +=1
    if target == values[len(values) // 2]:
        return f"(249,{binary_search.counter})"
    if target > values[len(values) // 2]:
        values = values[len(values) // 2:]
        return binary_search(values, target)
    elif target < values[len(values) // 2]:
        values = values[0:len(values) // 2]
        return binary_search(values, target)




def f(x):
    return x * x - 2


def bisection_root(function, left, right, tolerance):
    fa = f(left)
    fb = f(right)
    if abs(right - left) < tolerance:
        return (left + right) / 2.0

    c = (left + right) / 2.0
    fc = f(c)

    if fc == 0.0:
        return c

    if fa * fc < 0.0:
        return bisection_root(f,left, c, tolerance)
    else:
        return bisection_root(f, c, right, tolerance)




def main():
    import random
    values = random.sample(range(0, 1000), 500)
    values.sort()
    # Find the 500th value in the list
    search_value = values[249]
    binary_search.counter = 0
    print("Search Tests")
    print("------------")
    print("Linear search for ", search_value," --> (index,comps) = ", linear_search(values, search_value))
    print("Binary search for ", search_value," --> (index,comps) = ", binary_search(values, search_value))

    print()
    print("Root Finding")
    print("------------")
    root = bisection_root(f, 1, 2, 0.0001)
    print("Approximate root of x^2 - 2:", root)

main()
