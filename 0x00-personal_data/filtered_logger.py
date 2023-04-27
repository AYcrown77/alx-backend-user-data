#!/usr/bin/env python3
"""Handling personal data with the logging module"""

from typing import List
import mysql.connector
import csv
import logging
import re
import os



def get_db() -> mysql.connector.connection.MySQLConnection:
    """functoion that returns a connector to the database"""
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")
    db_username = os.getenv("PERSONAL_DATA_DB_USERNAME")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST")
    db = mysql.connector.connect(
        database=db_name if db_name else 'my_db',
        host=db_host if db_host else 'localhost',
        user=db_username if db_username else 'root',
        password=db_password if db_password else 'root'
    )

    return db

def get_logger() -> logging.Logger:
    """function that returns a logging user data"""
    new_logger = logging.Logger("user_data")
    new_logger.setLevel(logging.INFO)
    new_logger.propagate = False

    handlers = logging.StreamHandler()
    handlers.setFormatter(RedactingFormatter(PII_FIELDS))
    new_logger.addHandler(handlers)
    return new_logger


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
