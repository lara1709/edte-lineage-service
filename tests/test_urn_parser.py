import pytest

from app.urn_parser import parse_urn

def test_valid_urn():
    result = parse_urn("urn:example:customer-123")

    assert result == "urn:example:customer-123"

def test_rejects_wrong_prefix():
    with pytest.raises(ValueError):
        parse_urn("hello")

def test_rejects_empty_namespace():
    with pytest.raises(ValueError):
        parse_urn("urn::customer-123")

def test_rejects_empty_identifier():
    with pytest.raises(ValueError):
        parse_urn("urn:example:")

def test_rejects_whitespace():
    with pytest.raises(ValueError):
        parse_urn("urn:example:customer 123")

