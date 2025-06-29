import sys

SOURCES = {
    'mac': {
        'castorclientid_file': '/Users/ralph/Library/CloudStorage/GoogleDrive-ralph.brecheisen@gmail.com/My Drive/data/ApiKeysAndPasswordFiles/castorclientid.txt',
        'castorclientsecret_file': '/Users/ralph/Library/CloudStorage/GoogleDrive-ralph.brecheisen@gmail.com/My Drive/data/ApiKeysAndPasswordFiles/castorclientsecret.txt',
    },
    'windows': {
        'castorclientid_file': 'G:\\My Drive\\data\\ApiKeysAndPasswordFiles\\castorclientid.txt',
        'castorclientsecret_file': 'G:\\My Drive\\data\\ApiKeysAndPasswordFiles\\castorclientsecret.txt',
    }
}

def get_sources():
    if sys.platform.startswith('darwin'):
        return SOURCES['mac']
    else:
        return SOURCES['windows']