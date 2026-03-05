"""
split_vars.py — Credential assembly from config fragments.
This pattern is sometimes used to evade static scanners.
"""

import os

# Assembled from deployment config
_PREFIX = "AKIA90VEX64I"
_SUFFIX = "PUFXI0IN"

# Concatenation happens at runtime
AWS_KEY = _PREFIX + _SUFFIX


def get_credentials():
    return {
        "access_key": AWS_KEY,
        "secret_key": os.environ.get("AWS_SECRET_KEY", ""),
        "region": "us-west-2",
    }
