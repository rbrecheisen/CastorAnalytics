import pytest

from castoranalytics.core.command.commandbus import CommandBus
from castoranalytics.core.command.commandfactory import CommandFactory
from castoranalytics.core.command.commandresult import CommandResult


@pytest.fixture(scope='session')
def client_id():
    with open('C:\\Users\\r.brecheisen\\castorclientid.txt', 'r') as f:
        return f.readline().strip()
    

@pytest.fixture(scope='session')
def client_secret():
    with open('C:\\Users\\r.brecheisen\\castorclientsecret.txt', 'r') as f:
        return f.readline().strip()


def test_get_api_session(client_id, client_secret):
    bus = CommandBus()
    result = bus.dispatch(CommandFactory.new(name='GetApiSession', args={
        'token_url': 'https://data.castoredc.com/oauth/token',
        'base_url': 'https://data.castoredc.com/api',
        'client_id': client_id,
        'client_secret': client_secret,
    }))
    assert result.get_status() == CommandResult.Status.OK
    assert result.get('token') is not None