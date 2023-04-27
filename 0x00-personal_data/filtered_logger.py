#!/usr/bin/env python3
"""Handling personal data with the logging module"""


from typing import List
import logging
import re
import os


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Function that returns the log message """
    new = message
    for field in fields:
        new = re.sub(field + "=.*?" + separator,
                      field + "=" + redaction + separator, new)
    return new

