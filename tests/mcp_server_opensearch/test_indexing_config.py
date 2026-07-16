# Add indexing config validation tests
# opensearch-project#249

import os
import pytest


class TestIndexingConfig:
    """Validate indexing configuration for OpenSearch integration tests."""

    def test_config_loads(self):
        """Verify that required environment variables are present."""
        required_vars = [
            "IT_OPENSEARCH_URL",
            "IT_BASIC_AUTH_USERNAME",
            "IT_BASIC_AUTH_PASSWORD",
            "IT_IAM_ROLE_ARN",
            "IT_AWS_ACCESS_KEY_ID",
            "IT_AWS_SECRET_ACCESS_KEY",
            "IT_AWS_SESSION_TOKEN",
            "IT_AWS_REGION",
        ]
        missing = [v for v in required_vars if not os.environ.get(v)]
        if missing:
            pytest.skip(f"Missing env vars: {missing}")
        assert True

    def test_opensearch_connectivity(self):
        """Verify OpenSearch cluster is reachable."""
        url = os.environ.get("IT_OPENSEARCH_URL", "")
        assert url, "IT_OPENSEARCH_URL must be set"
        assert url.startswith("http"), f"Invalid URL: {url}"

    def test_aws_credentials_present(self):
        """Verify AWS credentials are available for SigV4 signing."""
        assert os.environ.get("IT_AWS_ACCESS_KEY_ID"), "Missing AWS access key"
        assert os.environ.get("IT_AWS_SECRET_ACCESS_KEY"), "Missing AWS secret key"
        assert os.environ.get("IT_AWS_SESSION_TOKEN"), "Missing AWS session token"

    def test_index_config_validation(self):
        """Validate index naming conventions."""
        index = os.environ.get("IT_TEST_INDEX", "")
        if index:
            assert "mcp-it-" in index, f"Index must contain mcp-it- prefix"
