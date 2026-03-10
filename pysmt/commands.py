from abc import ABC, abstractmethod

from .formula import Formula


class Command(ABC):
    """Base class for SMT-LIB commands."""

    @abstractmethod
    def __str__(self) -> str:
        pass


class SetLogic(Command):
    """Represents the SMT-LIB 'set-logic' command."""

    def __init__(self, logic: str):
        self.logic = logic

    def __str__(self) -> str:
        return f"(set-logic {self.logic})"


class DeclareConst(Command):
    """Represents the SMT-LIB 'declare-const' command."""

    def __init__(self, name: str, sort: str):
        self.name = name
        self.sort = sort

    def __str__(self) -> str:
        return f"(declare-const {self.name} {self.sort})"


class DeclareFun(Command):
    """Represents the SMT-LIB 'declare-fun' command."""

    def __init__(self, name: str, arg_sorts: list[str], return_sort: str):
        self.name = name
        self.arg_sorts = arg_sorts
        self.return_sort = return_sort

    def __str__(self) -> str:
        arg_sorts_str = " ".join(self.arg_sorts)
        return f"(declare-fun {self.name} ({arg_sorts_str}) {self.return_sort})"


class Assert(Command):
    """Represents the SMT-LIB 'assert' command."""

    def __init__(self, formula: Formula):
        self.formula = formula

    def __str__(self) -> str:
        return f"(assert {self.formula})"


class CheckSat(Command):
    """Represents the SMT-LIB 'check-sat' command."""

    def __str__(self) -> str:
        return "(check-sat)"


class GetModel(Command):
    """Represents the SMT-LIB 'get-model' command."""

    def __str__(self) -> str:
        return "(get-model)"


class GetValue(Command):
    """Represents the SMT-LIB 'get-value' command."""

    def __init__(self, terms: list[str]):
        self.terms = terms

    def __str__(self) -> str:
        terms_str = " ".join(self.terms)
        return f"(get-value ({terms_str}))"


class Maximize(Command):
    """Represents the SMT-LIB 'maximize' command."""

    def __init__(self, term: str):
        self.term = term

    def __str__(self) -> str:
        return f"(maximize {self.term})"


class Minimize(Command):
    """Represents the SMT-LIB 'minimize' command."""

    def __init__(self, term: str):
        self.term = term

    def __str__(self) -> str:
        return f"(minimize {self.term})"
