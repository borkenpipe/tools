#!/usr/bin/env python
"""This module provides ways to express types of exits"""
import sys
from borkenutil.borken_logic import none_or_empty

EXIT_PLAN_DEFAULT = "EXIT_PLAN_DEFAULT"

def exit_plan(plan, status=1, exception=Exception()):
    """Exit the application

    plan -- string representing exit plan
    status -- POSIX return code for shell
    exception -- The exception to raise if it was provided it will be raised
    """

    if plan == EXIT_PLAN_DEFAULT:
        pass # do things for normal exit
    else
        print "Unknown exit plan %s" % (plan)
    print "Exit plan was: %s" % (plan)
    if none_or_empty(exception):
        sys.exit(status)

    raise exception
