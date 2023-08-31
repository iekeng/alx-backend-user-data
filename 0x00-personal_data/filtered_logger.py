#!/usr/bin/env python3
'''filtered_logger'''
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    for field in fields:
        '''Obfuscates personal details'''
        message: str = re.sub(
            field +
            '=.*?' +
            separator,
            field +
            '=' +
            redaction +
            separator,
            message)
    return message
