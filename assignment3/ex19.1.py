def example(a, b):
    print(f"You have {a}.")
    print(f"You have {b}.")
    print("Ta da!")

example(1, 2)

c = 2
d = 3
example(c, d)

example(1 + 2, 2 + 3)

example(1 + c, 1 + d)

example(1 + c, c ^ 2)
