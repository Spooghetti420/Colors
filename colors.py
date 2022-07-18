"""
This moudle is made to encode xterm-256color escape sequences as convenient
variables and functions for use in a command-line utility.
"""

BLACK = "30"
RED = "31"
GREEN = "32"
YELLOW = "33"
BLUE = "34"
MAGENTA = "35"
CYAN = "36"
WHITE = "37"

BLACK_BG = "40"
RED_BG = "41"
GREEN_BG = "42"
YELLOW_BG = "43"
BLUE_BG = "44"
MAGENTA_BG = "45"
CYAN_BG = "46"
WHITE_BG = "47"

RESET = "0"
BOLD = "1"
UNDERLINE = "4"
INVERSE = "7"
BOLD_OFF = "21"
UNDERLINE_OFF = "24"
INVERSE_OFF = "27"


def wrap_string(s: str, start_wrapping: str, end_wrapping=None) -> str:
    """
    Surrounds the input string `s` in the input wrapping.
    If the string is to be wrapped in two separate wrappings,
    one start and one end, then the `end_wrapping` can be specified
    separately. Else, if the end wrapping is not specified, it
    defaults to the start wrapping.
    """
    return f"{start_wrapping}{s}{end_wrapping if end_wrapping is not None else start_wrapping}"


def wrap_colors(s: str, *colors: str) -> str:
    """
    Returns a string corresponding to the escape sequence for a
    number of terminal colors, followed by the escape sequence to reset the color.  
    """
    return wrap_string(s, f'\033[{";".join(colors)}m', f'\033[{RESET}m')


def printc(s: str, *formats, **kwargs):
    """
    Prints a string with a list of formatting options.
    Use `kwargs` for options to the `print` function.
    """
    print(wrap_colors(s, *formats), **kwargs)