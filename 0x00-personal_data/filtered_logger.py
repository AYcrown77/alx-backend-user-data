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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        Implement the format method to filter values in incoming log
        records using filter_datum. Values for fields in fields should
        be filtered.
        """
        log: logging.Formatter = super().format(record)
        return filter_datum(self.fields, self.REDACTION, log, self.SEPARATOR)
