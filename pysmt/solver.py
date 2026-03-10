import subprocess
import tempfile

from abc import ABC


class SMTSolver(ABC):
    """Base class for SMT solvers."""

    def __init__(self, name: str):
        self.name = name

    def solve(self, spec):
        """Solve the given SMT-LIB specification."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".smt2", delete=False) as tmp_file:
            tmp_file.write(str(spec))
            tmp_file.flush()
            result = subprocess.run([self.name, tmp_file.name], capture_output=True, text=True)
            return result.stdout.strip()


class Z3Solver(SMTSolver):
    """Z3 SMT solver interface."""

    def __init__(self):
        super().__init__("z3")

    def solve(self, spec):
        """Solve the given SMT-LIB specification using Z3 and parse output."""
        return super().solve(spec)
