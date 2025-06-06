from castoranalytics.core.command.api.getapisessioncommand import GetApiSessionCommand


COMMAND_REGISTRY = {

    'GetApiSession': {
        'class': GetApiSessionCommand,
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