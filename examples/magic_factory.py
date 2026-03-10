"""This script solves the MOOC homework on the magic factory."""

from pysmt import *


if __name__ == "__main__":
    spec = SMTLIBSpec(commands=[
        DeclareFun("n_nuzzles", ["Int"], "Int"),
        DeclareFun("n_prittles", ["Int"], "Int"),
        DeclareFun("n_skipples", ["Int"], "Int"),
        DeclareFun("n_crottles", ["Int"], "Int"),
        DeclareFun("n_dupples", ["Int"], "Int"),
        DeclareFun("weights", ["Int"], "Int"),
        DeclareConst("total_prittles", "Int"),

        Assert(
            And(
                Equals(Add(*[f'(n_nuzzles {i})' for i in range(8)]), 4),
                Equals(Add(*[f'(n_prittles {i})' for i in range(8)]), "total_prittles"),
                Equals(Add(*[f'(n_skipples {i})' for i in range(8)]), 8),
                Equals(Add(*[f'(n_crottles {i})' for i in range(8)]), 10),
                Equals(Add(*[f'(n_dupples {i})' for i in range(8)]), 20),
                *[LessThan(Add(f"(n_nuzzles {i})", f"(n_prittles {i})", f"(n_skipples {i})", f"(n_crottles {i})", f"(n_dupples {i})"), 8, strict=False) for i in range(8)],
                *[GreaterThan(f"(weights {i})", 0, strict=False) for i in range(8)],
                *[LessThan(f"(weights {i})", 8000, strict=False) for i in range(8)],
                *[LessThan(f"(n_nuzzles {i})", 1, strict=False) for i in range(8)],
                *[Equals(Add(Mul(f"(n_nuzzles {i})", 800), Mul(f"(n_prittles {i})", 1100), Mul(f"(n_skipples {i})", 1000), Mul(f"(n_crottles {i})", 2500), Mul(f"(n_dupples {i})", 200)), f"(weights {i})") for i in range(8)],
                *[Equals(f"(n_skipples {i})", 0) for i in range(3, 8)],
                *[GreaterThan(f"(n_nuzzles {i})", 0, strict=False) for i in range(8)],
                *[GreaterThan(f"(n_prittles {i})", 0, strict=False) for i in range(8)],
                *[GreaterThan(f"(n_skipples {i})", 0, strict=False) for i in range(8)],
                *[GreaterThan(f"(n_crottles {i})", 0, strict=False) for i in range(8)],
                *[GreaterThan(f"(n_dupples {i})", 0, strict=False) for i in range(8)],
                # Next condition is for question 2 only.
                *[Or(Equals(f"(n_crottles {i})", 0), Equals(f"(n_prittles {i})", 0)) for i in range(8)],
            )
        ),

        Maximize("total_prittles"),
        CheckSat(),
        GetModel()
    ])

    print(spec)

    # Solve the specification using Z3
    solver = Z3Solver()
    result = solver.solve(spec)
    print(result)
