#!/usr/bin/env python3
'''filtered_logger'''
import re


def filter_datum(fields, redaction, message, separator):
    '''obfuscates data from fields'''
    return re.sub(fr'\b({"|".join(fields)})\b', redaction, message)
