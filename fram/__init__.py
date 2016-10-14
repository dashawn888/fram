"""Fram framework bootstrap module."""

__author__ = "Shawn Lee"

import argparse
import sys


def fram_plugins():
    """Go through all the loaded modules and look for fram plugins.

    A plugin is defined by a module that defines a FRAM_PLUGIN variable that is
    a dict."""
    plugins = []
    for mod_name in list(sys.modules):
        instance = sys.modules[mod_name]
        if hasattr(instance, "FRAM_PLUGIN"):
            plugins.append(instance.FRAM_PLUGIN)
    return plugins


def parser_from_plugins(plugins, description):
    """Go through all the loaded plugins and build out a cli parser."""
    parser = argparse.ArgumentParser(description, conflict_handler="resolve")
    for plugin in plugins:
        if "argparse" in plugin:
            for argument, options in plugin["argparse"].iteritems():
                kwargs = {}
                for option in ["help", "action", "default", "required"]:
                    val = options.get(option)
                    if val:
                        kwargs[option] = options.get(option)
                args = [argument] + options.get(
                    "additional_args", [])
                parser.add_argument(*args, **kwargs)
    return parser


def decorated_main_from_plugins(plugins, func):
    """Go through all the loaded plugins and build the main decorators."""
    for plugin in plugins:
        if "main_decorator" in plugin:
            func = plugin["main_decorator"](func)
    return func


def parser_callbacks(plugins, parser):
    """Go through all the loaded plugins and run the parser callbacks."""
    framework = {}
    if parser:
        try:
            framework["argparse"] = parser.parse_args()
        except AttributeError:
            print (
                "ERROR: Did you return parser.parse_args() in your argument\n"
                "    parser?  Just return the parser. Fram framework will\n"
                "    call parse_args at a later time.")
            sys.exit(1)
        # Since we have parsed_args, go through all callbacks.
        for plugin in plugins:
            if "argparse" in plugin:
                for argument, options in plugin["argparse"].iteritems():
                    if "callback" in options:
                        framework[argument.strip("-")] = (
                            options["callback"](getattr(
                                framework["argparse"],
                                argument.strip("-"))))
    return framework


def run(func, description=None, argument_parser=None):
    """Bootstrap up the library."""
    plugins = fram_plugins()
    parser = parser_from_plugins(plugins, description)
    if argument_parser:
        try:
            parser = argument_parser(parser)
        except TypeError:
            print (
                "ERROR: Did you return parser.parse_args() in your argument\n"
                "    parser?  Just return the parser. Fram framework will\n"
                "    call parse_args at a later time.")
            sys.exit(1)
    func = decorated_main_from_plugins(plugins, func)
    framework = parser_callbacks(plugins, parser)
    return func(framework)
