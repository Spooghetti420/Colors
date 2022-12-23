from __future__ import annotations
import re
from tkinter.font import ITALIC
from typing import Collection, NewType, Union
from dataclasses import dataclass
"""
This module is made to encode xterm-256color escape sequences as convenient
variables and functions for use in a command-line utility.
A newer update has made it more featureful to allow nested behaviour.
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

@dataclass
class FormattedText:
    text: Collection[Textlike]
    formatting: set[str] # One of the above color constants

    NEIGHBOURING_ESCAPE_CODE_PATTERN = re.compile("\033\[0m(\033\[\d+(?:; *\d+)*m)")

    def get_escape_code(self):
        if self.formatting:
            return f'\033[{";".join(self.formatting)}m'
        return ""

    def render(self, /, compress=False) -> str:
        output_str = self.get_escape_code()
        for t in self.text:
            if isinstance(t, str):
                output_str += t
            elif isinstance(t, FormattedText):
                output_str += t.render() + self.get_escape_code()

        if not output_str.endswith(f'\033[{RESET}m'):
            output_str += f'\033[{RESET}m'

        if compress:
            output_str = re.sub(FormattedText.NEIGHBOURING_ESCAPE_CODE_PATTERN, "\1", output_str)
        
        return output_str

    def print(self, *args) -> None:
        print(self.render(), *args)

def printc(text, formatting, *args) -> None:
    """Print stylised text."""
    return FormattedText(text, formatting).print(*args)

Textlike = Union[FormattedText, str]

def bold(text: Textlike) -> FormattedText:
    """Embolden a string."""
    return FormattedText([text], {BOLD})

def italic(text: Textlike) -> FormattedText:
    """Italicise a string."""
    return FormattedText([text], {ITALIC})