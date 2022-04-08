import pytest
import logging

### Initialise Configuration ###


def test_successful_imports(caplog):
    """Check the imports"""
    try:
        import requests
    except ImportError as err:
        logging.error("couldn't import a package: %s", err)

    for log in caplog.records:
        assert log.levelno < logging.ERROR
