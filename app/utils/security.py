"""
Project Chimera: Security utilities (hashing, verification).
"""
import hashlib
import secrets
from typing import Optional


def hash_password(password: str, salt: Optional[str] = None) -> str:
    """
    Hash a password with optional salt (for storage/verification).

    :param password: Plain text password
    :param salt: Optional salt; if None, a random salt is used
    :return: Salted hash string (e.g. salt:hash)
    """
    if salt is None:
        salt = secrets.token_hex(16)
    value = f"{salt}{password}".encode("utf-8")
    digest = hashlib.sha256(value).hexdigest()
    return f"{salt}:{digest}"


def verify_password(password: str, stored: str) -> bool:
    """
    Verify a password against a stored hash (salt:hash format).

    :param password: Plain text password
    :param stored: Stored value from hash_password
    :return: True if password matches
    """
    if ":" not in stored:
        return False
    salt, _ = stored.split(":", 1)
    return hash_password(password, salt=salt) == stored
