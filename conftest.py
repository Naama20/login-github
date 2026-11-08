import pytest


@pytest.fixture(scope="session")
def base_url(pytestconfig: pytest.Config) -> str | None:
    # Override pytest-playwright's instance-method fixture for pytest 9.2+.
    return (
        pytestconfig.getoption("--base-url")
        or pytestconfig.getini("base_url")
        or None
    )
