"""Fram core framework unittests."""
# pylint:disable=invalid-name,missing-docstring,too-many-public-methods
import sys

import unittest

import stubout

import fram  # pylint:disable=relative-import


####################
# Fake plugin start.
def main_decorator(_):
    """Stub decorator."""
    def wrapped(_):
        """Stub decorator."""
        return 5
    return wrapped


def callback(_):
    """Stub callback."""
    return {"Water": True}

FRAM_PLUGIN = {
    "argparse": {
        "--test": {
            "action": "store_true",
            "additional_args": ["-t"],
            "callback": callback,
            "default": 5,
            "help": "test",
            "required": True}},
    "main_decorator": main_decorator}
# Fake plugin end.
##################


class FramTests(unittest.TestCase):
    """Test the core framework."""
    parser = None
    plugin = None

    def setUp(self):
        self.stubs = stubout.StubOutForTesting()
        self.stubs.Set(sys, "argv", ["python", "--test"])
        plugins = fram.fram_plugins()
        self.stubs.Set(
            self, "parser", fram.parser_from_plugins(plugins, "NO DESCRIPTION"))
        self.stubs.Set(self, "plugin", plugins.pop())

    def tearDown(self):
        del self.stubs

    def test_fram_plugins_argparse_action(self):
        self.assertEqual(
            self.plugin["argparse"]["--test"]["action"], "store_true")

    def test_fram_plugins_argparse_help(self):
        self.assertEqual(self.plugin["argparse"]["--test"]["help"], "test")

    def test_fram_plugins_argparse_additional_args(self):
        self.assertEqual(
            self.plugin["argparse"]["--test"]["additional_args"], ["-t"])

    def test_fram_plugins_argparse_default(self):
        self.assertEqual(self.plugin["argparse"]["--test"]["default"], 5)

    def test_fram_plugins_argparse_required(self):
        self.assertEqual(self.plugin["argparse"]["--test"]["required"], True)

    def test_fram_plugins_argparse_callback(self):
        self.assertEqual(
            self.plugin["argparse"]["--test"]["callback"](True),
            {"Water": True})

    def test_fram_plugins_argparse_decorator(self):
        self.assertEqual(self.plugin["main_decorator"](True)(True), 5)

    def test_parser_from_plugins_args_description(self):
        self.assertEqual(self.parser.prog, "NO DESCRIPTION")

    def test_parser_from_plugins_args_test(self):
        args = self.parser.parse_args(["--test"])
        self.assertTrue(args.test)

    def test_parser_from_plugins_args_t(self):
        args = self.parser.parse_args(["-t"])
        self.assertTrue(args.test)

    def test_decorated_main_from_plugins(self):
        func = fram.decorated_main_from_plugins([self.plugin], lambda x: x)
        self.assertEqual(func(True), 5)

    def test_parser_callbacks_argparse(self):
        framework = fram.parser_callbacks([self.plugin], self.parser)
        self.assertTrue(framework["argparse"].test)

    def test_parser_callbacks_arg_test(self):
        framework = fram.parser_callbacks([self.plugin], self.parser)
        self.assertTrue(framework["test"]["Water"])

    def test_run(self):
        self.assertEqual(fram.run(lambda x: x), 5)

if __name__ == "__main__":
    unittest.main()
