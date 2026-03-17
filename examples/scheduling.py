"""This script solves the MOOC homework on scheduling."""

from pysmt import *


if __name__ == "__main__":
    spec = SMTLIBSpec(commands=[
        DeclareFun("start", ["Int"], "Int"),
        DeclareFun("end", ["Int"], "Int"),
        DeclareConst("total", "Int"),

        Assert(
            And(
                *[GreaterThan(f"(start {i})", 0, strict=False) for i in range(1, 11)],
                *[LessThan(f"(end {i})", "total", strict=False) for i in range(1, 11)],
                *[Equals(f"(end {i})", Add(f"(start {i})", 10 + i)) for i in range(1, 11)],
                And(GreaterThan("(start 3)", "(end 1)", strict=False), GreaterThan("(start 3)", "(end 2)", strict=False)),
                And(GreaterThan("(start 6)", "(end 2)", strict=False), GreaterThan("(start 6)", "(end 4)", strict=False)),
                And(GreaterThan("(start 7)", "(end 1)", strict=False), GreaterThan("(start 7)", "(end 4)", strict=False), GreaterThan("(start 7)", "(end 5)", strict=False)),
                And(GreaterThan("(start 8)", "(end 3)", strict=False), GreaterThan("(start 8)", "(end 6)", strict=False)),
                And(GreaterThan("(start 9)", "(end 6)", strict=False), GreaterThan("(start 9)", "(end 7)", strict=False)),
                And(GreaterThan("(start 10)", "(end 8)", strict=False), GreaterThan("(start 10)", "(end 9)", strict=False)),
                GreaterThan("(start 7)", "(start 8)", strict=False),
                Or(GreaterThan("(start 3)", "(end 4)", strict=False), GreaterThan("(start 4)", "(end 3)", strict=False)),
                Or(GreaterThan("(start 3)", "(end 5)", strict=False), GreaterThan("(start 5)", "(end 3)", strict=False)),
                Or(GreaterThan("(start 5)", "(end 4)", strict=False), GreaterThan("(start 4)", "(end 5)", strict=False)),
            )
        ),
        Minimize("total"),
        CheckSat(),
        GetModel(),
        GetValue(["total"])
    ])

    print(spec)

    # Solve the specification using Z3
    solver = Z3Solver()
    result = solver.solve(spec)
    print(result)
