"""This script solves the MOOC homework on the sudoku variant."""

from pysmt import *


if __name__ == "__main__":
    spec = SMTLIBSpec(commands=[
        DeclareFun("A", ["Int", "Int"], "Int"),

        Assert(
            And(
                *[GreaterThan(f"(A {i} {j})", 0) for i in range(9) for j in range(9)],
                *[LessThan(f"(A {i} {j})", 10) for i in range(9) for j in range(9)],

                *[Distinct(*[f"(A {i} {j})" for j in range(9)]) for i in range(9)],
                *[Distinct(*[f"(A {i} {j})" for i in range(9)]) for j in range(9)],
                *[Distinct(*[f"(A {i + k} {j + l})" for i in range(3) for j in range(3)]) for k in [0, 3, 6] for l in [0, 3, 6]],

                # *[Equals(f"(A 0 {j})", Add(f"(A 0 {j + 1})", 1)) for j in [1, 3, 6]],
                # *[LessThan(f"(A 1 {j})", f"(A 1 {j + 1})") for j in [3, 4, 5, 6, 7]],
                # *[Equals(f"(A 2 {j})", Add(f"(A 2 {j + 1})", 1)) for j in [1, 3, 4]],
                # *[LessThan(f"(A 3 {j})", f"(A 3 {j + 1})") for j in [0, 1, 2, 3, 4]],
                # *[Equals(f"(A 4 {j})", Add(f"(A 4 {j + 1})", 1)) for j in [0, 1, 3, 5, 7]],
                # *[LessThan(f"(A 5 {j})", f"(A 5 {j + 1})") for j in [3, 4, 5, 6, 7]],
                # *[Equals(f"(A 5 {j})", Add(f"(A 5 {j + 1})", 1)) for j in [2]],
                # *[Equals(f"(A 6 {j})", Add(f"(A 6 {j + 1})", 1)) for j in [2]],
                # *[Equals(f"(A 7 {j})", Add(f"(A 7 {j + 1})", 1)) for j in [5]],
                # *[LessThan(f"(A 7 {j})", f"(A 7 {j + 1})") for j in [0, 1, 2, 3, 4]],
                # *[Equals(f"(A {i} 2)", Add(f"(A {i + 1} 2)", 1)) for i in [3, 5]],
                # *[Equals(f"(A {i} 3)", Add(f"(A {i + 1} 3)", 1)) for i in [5]],
                # *[Equals(f"(A {i} 5)", Add(f"(A {i + 1} 5)", 1)) for i in [0, 5]],
                # *[Equals(f"(A {i} 6)", Add(f"(A {i + 1} 6)", 1)) for i in [1, 2, 3, 5]],
                # *[Equals(f"(A {i} 8)", Add(f"(A {i + 1} 8)", 1)) for i in [2, 3]],

                *[Or(Equals(f"(A 0 {j})", Add(f"(A 0 {j + 1})", 1)), Equals(f"(A 0 {j})", Minus(f"(A 0 {j + 1})", 1))) for j in [1, 3, 6]],
                *[LessThan(f"(A 1 {j})", f"(A 1 {j + 1})") for j in [3, 4, 5, 6, 7]],
                *[Or(Equals(f"(A 2 {j})", Add(f"(A 2 {j + 1})", 1)), Equals(f"(A 2 {j})", Minus(f"(A 2 {j + 1})", 1))) for j in [1, 3, 4]],
                *[LessThan(f"(A 3 {j})", f"(A 3 {j + 1})") for j in [0, 1, 2, 3, 4]],
                *[Or(Equals(f"(A 4 {j})", Add(f"(A 4 {j + 1})", 1)), Equals(f"(A 4 {j})", Minus(f"(A 4 {j + 1})", 1))) for j in [0, 1, 3, 5, 7]],
                *[LessThan(f"(A 5 {j})", f"(A 5 {j + 1})") for j in [3, 4, 5, 6, 7]],
                *[Or(Equals(f"(A 5 {j})", Add(f"(A 5 {j + 1})", 1)), Equals(f"(A 5 {j})", Minus(f"(A 5 {j + 1})", 1))) for j in [2]],
                *[Or(Equals(f"(A 6 {j})", Add(f"(A 6 {j + 1})", 1)), Equals(f"(A 6 {j})", Minus(f"(A 6 {j + 1})", 1))) for j in [2]],
                *[Or(Equals(f"(A 7 {j})", Add(f"(A 7 {j + 1})", 1)), Equals(f"(A 7 {j})", Minus(f"(A 7 {j + 1})", 1))) for j in [5]],
                *[LessThan(f"(A 7 {j})", f"(A 7 {j + 1})") for j in [0, 1, 2, 3, 4]],
                *[Or(Equals(f"(A {i} 2)", Add(f"(A {i + 1} 2)", 1)), Equals(f"(A {i} 2)", Minus(f"(A {i + 1} 2)", 1))) for i in [3, 5]],
                *[Or(Equals(f"(A {i} 3)", Add(f"(A {i + 1} 3)", 1)), Equals(f"(A {i} 3)", Minus(f"(A {i + 1} 3)", 1))) for i in [5]],
                *[Or(Equals(f"(A {i} 5)", Add(f"(A {i + 1} 5)", 1)), Equals(f"(A {i} 5)", Minus(f"(A {i + 1} 5)", 1))) for i in [0, 5]],
                *[Or(Equals(f"(A {i} 6)", Add(f"(A {i + 1} 6)", 1)), Equals(f"(A {i} 6)", Minus(f"(A {i + 1} 6)", 1))) for i in [1, 2, 3, 5]],
                *[Or(Equals(f"(A {i} 8)", Add(f"(A {i + 1} 8)", 1)), Equals(f"(A {i} 8)", Minus(f"(A {i + 1} 8)", 1))) for i in [2, 3]],
            )
        ),

        CheckSat(),
        GetModel()
    ])

    print(spec)

    # Solve the specification using Z3
    solver = Z3Solver()
    result = solver.solve(spec)
    print(result)
