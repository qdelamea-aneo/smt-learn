"""This script solves the MOOC homework on program verification."""

from pysmt import *


if __name__ == "__main__":
    spec = SMTLIBSpec(commands=[
        DeclareFun("a", ["Int"], "Int"),
        DeclareFun("b", ["Int"], "Int"),
        DeclareConst("n", "Int"),

        Assert(
            And(
                Equals("n", 10),
                Equals("(a 0)", 1),
                Equals("(b 0)", 1),
                *[Or(
                    And(Equals(f"(a {i})", Add(f"(a {i - 1})", Mul(2, f"(b {i - 1})"))), Equals(f"(b {i})", Add(i, f"(b {i - 1})"))),
                    And(Equals(f"(a {i})", Add(i, f"(a {i - 1})")), Equals(f"(b {i})", Add(f"(a {i - 1})", f"(b {i - 1})"))))
                    for i in range(1, 11)
                ],
                # Or(*[Equals(f"(b {i})", Add(600, "n")) for i in range(1, 11)]),
                Equals("(b 10)", Add(600, "n")),
            )
        ),
        CheckSat(),
        GetModel(),
    ])

    print(spec)

    # Solve the specification using Z3
    solver = Z3Solver()
    result = solver.solve(spec)
    print(result)
