"""Print the table of a given number (n × 1 to n × 10)."""


def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")


table(7)