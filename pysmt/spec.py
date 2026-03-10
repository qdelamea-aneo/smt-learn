from .commands import Command


class SMTLIBSpec:
    def __init__(self, commands: list[Command]):
        self.commands = commands

    def __str__(self) -> str:
        return "\n".join(str(cmd) for cmd in self.commands)
