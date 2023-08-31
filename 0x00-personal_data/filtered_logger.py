#!/usr/bin/env python3
'''filtered_logger'''
import os
import re
import logging
import mysql.connector
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''Obfuscates personal details'''
    for field in fields:
        message: str = re.sub(field + '=.*?' + separator, field +
                              '=' + redaction + separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''init function for the RedactingFormatter class'''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''format method'''
        message = super(RedactingFormatter, self).format(record)
        redacted = filter_datum(self.fields, self.REDACTION, message,
                                self.SEPARATOR)
        return redacted


def get_logger() -> logging.Logger:
    '''Creates custom logger'''
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    custom_fmt = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(custom_fmt)

    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''Creating db'''
    DB_USER = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    DB_PASSWORD = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    DB_HOST = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    DB_NAME = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(host=DB_HOST, user=DB_USER,
                                   password=DB_PASSWORD, database=DB_NAME)
