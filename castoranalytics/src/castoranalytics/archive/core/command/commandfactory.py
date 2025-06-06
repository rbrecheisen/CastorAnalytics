from castoranalytics.core.command.commandregistry import COMMAND_REGISTRY
from castoranalytics.core.command.error import CommandNotFoundError


class CommandFactory:
    def new(name, args=None):
        entry = COMMAND_REGISTRY.get(name, None)
        if entry is None:
            raise CommandNotFoundError(name)
        instance = entry['class'](args)
        return instance