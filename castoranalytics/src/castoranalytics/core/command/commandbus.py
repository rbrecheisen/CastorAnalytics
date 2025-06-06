class CommandBus:
    def dispatch(self, command):
        return command.execute()