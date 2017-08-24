from borken_exit import *
from . import borken_logger

def fail_if_none_or_empty(s, msg=None):
    if _none_or_empty(s):
        borken_logger.fail(msg)
        exit_plan("exitonfail")

def fail_if_value(lhs, rhs, msg=None, exception=None):
    if is_value(lhs , rhs):
        borken_logger.fail(msg)
        exit_plan("exitonfail", exception=exception)

def warn_if_none_or_empty(s, msg=None):
    if _none_or_empty(s):
        borken_logger.warn(msg)
        exit_plan("exitonwarn")

def none_or_empty(s):
    return _none_or_empty(s)

def not_none_or_empty(s):
    return not _none_or_empty(s)

def _none_or_empty(s):
    return s == None or len(s) == 0

def is_value(s, v):
    return _is_value(s, v)

def _is_value(s, v):
    return s == v

