JWKS_FILE = 'tests/jwks.json'

from unittest.mock import patch

from src.fastapi_auth0 import Auth0


@patch('src.fastapi_auth0.auth.urllib.request.urlopen')
def test_local_jwks(urlopen_mock):
    """Test loading jwks from file."""
    auth0 = Auth0('test.auth0.com', 'test', jwks_file=JWKS_FILE)
    assert auth0.jwks['keys'][0]['n'] == 'test'
    urlopen_mock.assert_not_called()
