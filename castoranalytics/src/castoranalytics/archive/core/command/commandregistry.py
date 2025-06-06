from castoranalytics.core.command.api.getapisessioncommand import GetApiClientCommand


COMMAND_REGISTRY = {

    'GetApiSession': {
        'class': GetApiClientCommand,
        'args': [
            {'name': 'token_url'},
            {'name': 'api_base_url'},
            {'name': 'client_id'},
            {'name': 'client_secret'},
        ],
        'result': [
            {'name': 'token'},
        ],
    },
}