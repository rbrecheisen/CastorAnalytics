from castoranalytics.core.command.base import BaseCommand
from castoranalytics.core.command.commandresult import CommandResult


class GetApiSessionCommand(BaseCommand):
    def execute(self):
        result = CommandResult()
        result.set('token', 'some text')
        result.set_status(CommandResult.Status.OK)
        return result