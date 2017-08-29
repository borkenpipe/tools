#!/usr/bin/env python
"""This module standard console logging"""

import colored
from colored import stylize
from colored import fg, bg, attr
from borkenutil.borken_logic import none_or_empty
from borkenutil.borken_logic import not_none_or_empty
from borkenutil.borken_exit import exit_plan
from borkenutil.borken_exit import EXIT_PLAN_DEFAULT

DEBUG = False

#if logging to tty that does color do color
#if going to a log file drop color
#sys.stdout.isatty()

EXIT_ON_FAIL = 1

#https://pypi.python.org/pypi/colored
GREEN_BOLD_STYLE = colored.fg("green")   + colored.attr("bold")
RED_BOLD_STYLE = colored.fg("red")     + colored.attr("bold")
ORANGE_BOLD_STYLE = colored.fg("orange_3")  + colored.attr("bold")
YELLOW_BOLD_STYLE = colored.fg("yellow")  + colored.attr("bold")
GREY_BOLD_STYLE = colored.fg("grey_100")    + colored.attr("bold")

def colorit(msg, style):
    """ color the text given to the specified style """
    return stylize(msg, style)

def can_handle_color():
    """ some sort of check to see if the host env supports color """
    #TODO some check if this is a tty that can do color
    return True

def print_console(msg):
    """ write to the console """
    print msg
    return 0

def do_color(msg, style):
    """ print the message in color if it can be handled"""
    return msg if can_handle_color() else colorit(msg, style)

WARN_PREFIX = do_color("[Warn]: ", YELLOW_BOLD_STYLE)
FAIL_PREFIX = do_color("[Fail]: ", RED_BOLD_STYLE)
ERROR_PREFIX = do_color("[Error]: ", RED_BOLD_STYLE)
INFO_PREFIX = do_color("[*]: ", GREY_BOLD_STYLE)
DEBUG_PREFIX = do_color("[DEBUG]: ", ORANGE_BOLD_STYLE)
SUCCESS_PREFIX = do_color("[SUCCESS]: ", GREEN_BOLD_STYLE)

def warn(msg):
    """ print a warning message """
    return print_console("%s%s" % (WARN_PREFIX, msg))

def fail(msg, exitstatus=1, exception=None):
    """ print a fail message and throw exception if provided"""
    print_console("%s%s%s" % (FAIL_PREFIX, msg, "%s" % (exitstatus)))
    if not_none_or_empty(exception):
        exit_plan(EXIT_PLAN_DEFAULT, exception=exception)

def error(msg, exitstatus=1):
    """ print an error message """
    return print_console("%s%s" % (ERROR_PREFIX, msg))

def info(msg, exitstatus=1):
    """ print an info message """
    return print_console("%s%s" % (INFO_PREFIX, msg))

def success(msg, exitstatus=1):
    """ print a success message """
    return print_console("%s%s" % (SUCCESS_PREFIX, msg))

def debug(msg, exitstatus=1):
    """ print a debug"""
    if DEBUG == True:
        return print_console("%s%s" % (DEBUG_PREFIX, msg))
    else:
        return 1
