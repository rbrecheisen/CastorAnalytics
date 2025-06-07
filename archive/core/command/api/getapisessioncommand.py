from castoranalytics.core.command.base import BaseCommand
from castoranalytics.core.command.commandresult import CommandResult
from castoranalytics.core.api import CastorApiClient


class GetApiClientCommand(BaseCommand):
    def execute(self):
        client = CastorApiClient(
            token_url=self.get_args('token_url'),
            api_base_url=self.get_args('api_base_url'),
            client_id=self.get_args('client_id'),
            client_secret=self.get_args('client_secret'),
        )
        result = CommandResult()
        result.set('client', client)
        result.set_status(CommandResult.Status.OK)
        return result