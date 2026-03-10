from abc import ABC, abstractmethod


class Formula(ABC):
    """Base class for SMT-LIB formulas."""

    @abstractmethod
    def __str__(self) -> str:
        pass


class BoolConst(Formula):
    """Represents a boolean constant (true/false)."""

    def __init__(self, value: bool):
        self.value = value

    def __str__(self) -> str:
        return "true" if self.value else "false"


class And(Formula):
    """Represents a logical AND of multiple formulas."""

    def __init__(self, *args: Formula):
        self.args = args

    def __str__(self) -> str:
        args_str = "\n\t".join(str(arg) for arg in self.args)
        return f"(and {args_str})"


class Or(Formula):
    """Represents a logical OR of multiple formulas."""

    def __init__(self, *args: Formula):
        self.args = args

    def __str__(self) -> str:
        args_str = " ".join(str(arg) for arg in self.args)
        return f"(or {args_str})"


class Not(Formula):
    """Represents a logical NOT of a formula."""

    def __init__(self, arg: Formula):
        self.arg = arg

    def __str__(self) -> str:
        return f"(not {self.arg})"


class Equals(Formula):
    """Represents an equality formula (e.g., (= x y))."""

    def __init__(self, left: Formula, right: Formula):
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"(= {self.left} {self.right})"

class GreaterThan(Formula):
    """Represents a greater-than formula (e.g., (> x y))."""

    def __init__(self, left: Formula, right: Formula, strict: bool = True):
        self.left = left
        self.right = right
        self.strict = strict

    def __str__(self) -> str:
        return f"({'>' if self.strict else '>='} {self.left} {self.right})"


class LessThan(Formula):
    """Represents a less-than formula (e.g., (< x y))."""

    def __init__(self, left: Formula, right: Formula, strict: bool = True):
        self.left = left
        self.right = right
        self.strict = strict

    def __str__(self) -> str:
        return f"({'<' if self.strict else '<='} {self.left} {self.right})"


class Add(Formula):
    """Represents an addition formula (e.g., (+ x y))."""

    def __init__(self, *args: Formula):
        self.args = args

    def __str__(self) -> str:
        args_str = " ".join(str(arg) for arg in self.args)
        return f"(+ {args_str})"


class Mul(Formula):
    """Represents a multiplication formula (e.g., (* x y))."""

    def __init__(self, *args: Formula):
        self.args = args

    def __str__(self) -> str:
        args_str = " ".join(str(arg) for arg in self.args)
        return f"(* {args_str})"
