#!/usr/bin/env python3
'''filtered_logger'''
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''Obfuscates personal details'''
    for field in fields:
        message: str = re.sub(field + '=.*?' + separator, field +
                              '=' + redaction + separator, message)
    return message
