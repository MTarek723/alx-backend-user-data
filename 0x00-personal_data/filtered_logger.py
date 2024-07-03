#!/usr/bin/env python3
import re


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str) -> str:
    """function to remove filter logs"""
    for j in fields:
        message = re.sub((j + '=.*?' + separator),
                         (j + "=" + redaction + separator), message)
    return message
