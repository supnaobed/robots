from data.CommandType import CommandType


class Command:
    def __init__(self,
                 commandType: CommandType,
                 value: float):
        self.commandType = commandType
        self.value = value
