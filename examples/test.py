from pysmt import *


if __name__ == "__main__":
    # Create a simple SMT-LIB specification
    spec = SMTLIBSpec(commands=[
        DeclareConst("x", "Int"),
        DeclareConst("y", "Int"),
        Assert(GreaterThan("x", 5)),
        Assert(LessThan("y", 10)),
        Assert(Equals("x", "y")),
        Minimize("x"),
        CheckSat(),
        # GetValue("x"),
        GetModel()
    ])
    print(spec)
    # exit(0)

    # Solve the specification using Z3
    solver = Z3Solver()
    result = solver.solve(spec)
    print(result)
