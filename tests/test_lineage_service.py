from unittest.mock import MagicMock, Mock
import pytest
from app.lineage_service import process_urn


def test_process_urn_validates_and_stores_urn():
    driver = Mock()
    session = MagicMock()
    driver.session = MagicMock()
    driver.session.return_value.__enter__.return_value = session

    result = process_urn(driver, "urn:example:customer-123")

    assert result == "urn:example:customer-123"
    driver.session.assert_called_once()
    session.run.assert_called_once()


def test_process_urn_rejects_invalid_urn():
    driver = Mock()

    with pytest.raises(ValueError):
        process_urn(driver, "hello")

    driver.session.assert_not_called()
