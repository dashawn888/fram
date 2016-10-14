"""An example program that utilizes the fram framework.

examples:
    python example.py
        Produces the help screen since --config is a required argument.

    python example.py --config test.ini
        Runs the program with default logging.  If test.ini doesn't exist you
        can just `touch test.ini`.

    python example.py --config test.ini --daemon
        Same as above but backgrounds the process.

    python example.py --config test.ini --debug
        Turns on verbouse logging.

    python example.py --config test.ini --debug --syslog
        Same as above but sends output to syslog.

    python example.py --config test.ini --debug --syslog --console
        Same as above but also sends output to the console.

    python example.py --config test.ini --error
        Sets the logging level to error.

    python example.py --config test.ini --hello
        Uses the user defined argument --hello.

    python example.py --config test.ini --info
        Sets the logging level to info or below.

    python example.py --config test.ini --warning
        Sets the logging level to warning or below.
"""
# pylint:disable=unused-import

__author__      = "Shawn Lee"

import time

import fram
import fram_config
import fram_daemon
from fram_logging import FramLogging

# pylint:enable=unused-import

# The logging object must be defined as LOGGER.  This is performed implicitly
# since the fram_logging module uses introspection to find a logger named LOGGER
# of type FramLogging.
LOGGER = FramLogging.getLogger("example")


def argument_parser(parser):
    """Parse additional arguments.

    The fram framework will add arguments automatically.  It can also be
    instructed to parse additional user defined arguments.  To do this you
    pass in the argument_parser argument to fram.run and refrence your parser
    method.  The parser method will be passed in the parser argument and is
    expected to return a parser object.

    The parser object delivered is an argparse object."""
    parser.add_argument(
        "-s", "--hello", help="Say Hello.", action="store_true")
    return parser


def main(framework):
    """App starts here.

    This method is defined as the starting point of the application by fram.run
    below.  After the framework is up and fully completed it will call on this
    method and will pass in a framework object which contains the work of
    the framework.

    If you run this program this method will be passed a dict that looks
    like this.
    {
        "argparse": Namespace(
            All the values of the args passed in by the cli.),
        "config": <ConfigParser.ConfigParser instance at 0x7f8fe602bf80>
    }"""
    LOGGER.info("INFO MESSAGE")
    LOGGER.warning("WARNING MESSAGE")
    LOGGER.debug("DEBUG MESSAGE")
    LOGGER.error("ERROR MESSAGE")
    if framework["argparse"].hello:
        print "HELLO"
    if framework["argparse"].daemon:
        while True:
            time.sleep(5)

if __name__ == "__main__":
    """Bootstrap the framework.

    Normally you would just call main here but in order to bootstrap the
    framework you call fram.run instead.

    Some of the main arguments you would pass are:
        func: The callback that you want the framework to call after it is
            bootstrapped.  The framework will pass the callback a dict with
            the results of the bootstrapping process.

        description: The description of the program.  This is used as the
            description for argparser and viewable usaslly with -h or --help.
        argument_parser: The callback that the framework will call to parse
            any custom arguments your application requires.  This is an
            optional field.  The callback will be passed in an argparser object
            and it is expected that the callback will return the argparser
            object back to the framework."""
    fram.run(
        func=main,
        description="Test out the framework.",
        argument_parser=argument_parser)
