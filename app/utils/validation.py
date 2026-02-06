"""
Project Chimera: Input validation utilities.
"""
import re
from typing import Any, Dict, List, Optional


def validate_input(
    data: Dict[str, Any],
    required: Optional[List[str]] = None,
    optional: Optional[List[str]] = None,
    schema: Optional[Dict[str, type]] = None,
) -> tuple[bool, Optional[str]]:
    """
    Validate input dictionary (required keys, optional types).

    :param data: Input dict to validate
    :param required: List of required keys
    :param optional: List of optional keys (no type check if schema omitted)
    :param schema: Optional map of key -> type for validation
    :return: (is_valid, error_message)
    """
    required = required or []
    for key in required:
        if key not in data:
            return False, f"Missing required key: {key}"
    if schema:
        for key, expected_type in schema.items():
            if key not in data:
                continue
            if not isinstance(data[key], expected_type):
                return False, f"Invalid type for '{key}': expected {expected_type.__name__}"
    return True, None


def validate_eth_address(address: Optional[str]) -> bool:
    """Validate Ethereum-style address (0x + 40 hex chars)."""
    if not address:
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))
