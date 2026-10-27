def parse_urn(value: str) -> str:
    """Check whether a value has the basic URN structure"""

    if not isinstance(value, str):
        raise ValueError("URN must be a string")

    if not value.startswith("urn:"):
        raise ValueError("URN must start with 'urn:'")

    parts = value.split(":", 2)

    if len(parts) != 3 or not parts[1] or not parts[2]:
        raise ValueError("URN must have namespace and identifier")

    if any(char.isspace() for char in value):
        raise ValueError("URN must not contain whitespace")

    return value