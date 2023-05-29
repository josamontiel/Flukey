#!/usr/bin/env python3

# The MIT License (MIT)

# Copyright (c) 2023 Joseph A. M. 

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

################################################################################
################################################################################

# The code I used is from: https://codereview.stackexchange.com/questions/285058/truly-cryptographically-secure-password-generator-in-python-version-2


import json
import secrets
import typer
from password_strength import PasswordStats
from pathlib import Path
from rich import print
from rich.console import Console
from rich.table import Table
from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase, digits, punctuation
from typing import Any, List, Optional, Tuple
from typing_extensions import Annotated

RNG = secrets.SystemRandom()
CATEGORIES = (lowercase, uppercase, digits, punctuation)
CATEGORY_NAMES = ()
STYLES = tuple(
    "[{0}]{{}}[/{0}]".format(color) for color in ("magenta", "red", "cyan", "green")
)
CHARACTER_STYLES = {
    c: style.format(c) for style, category in zip(STYLES, CATEGORIES) for c in category
}
CHARACTER_STYLES["\\"] = "[green]\\\[/green]"
HELP_MSGS = (
    "desired password length ",
    "desired number of passwords generated",
    "determines if the passwords should contain unique characters only",
    "determines if the passwords should contain special characters",
    "determines if the characters in the passwords should be uniformly sampled",
    "if True, will only output the summary of password statistical information",
    "if True, the passwords will be analyzed and additional information will be shown",
    "if True, password summary will be more extensive",
    "filepath to redirect the output to, if given, will save the output as a JSON file located at the path given, instead of printing to console",
)
COLUMNS = (
    "Password",
    "lower",
    "UPPER",
    "Digit",
    "Special",
    "Length",
    "Unique",
    "Repetition",
    "Entropy",
    "Strength",
)
ATTRIBUTES = (
    "letters_lowercase",
    "letters_uppercase",
    "numbers",
    "special_characters",
    "length",
    "alphabet_cardinality",
    "repeated_patterns_length",
)


def annotate(arg_type: type, optional: bool, help_msg: str) -> Annotated:
    if not optional:
        return Annotated[arg_type, typer.Argument(help=help_msg)]

    return Annotated[Optional[arg_type], typer.Option(help=help_msg)]


LENGTH = annotate(int, False, HELP_MSGS[0])
COUNT = annotate(int, True, HELP_MSGS[1])
BOOLEANS = tuple(annotate(bool, True, help_msg) for help_msg in HELP_MSGS[2:8])
REDIRECT = annotate(str, True, HELP_MSGS[8])


class Cyclic_List(list):
    def __getitem__(self, index: int) -> Any:
        return list.__getitem__(self, index % len(self))


class CharacterSet:
    def __init__(self, chars: str | list, unique: bool = False) -> None:
        self.unique = unique
        self.remaining = list(chars)
        if unique:
            RNG.shuffle(self.remaining)

    def next_char(self) -> str:
        return self.remaining.pop() if self.unique else secrets.choice(self.remaining)

    def get_chars(self, length: int) -> List[str]:
        if self.unique:
            if length > len(self.remaining):
                raise ValueError("length is too big, not enough characters remain")

            return [self.remaining.pop() for _ in range(length)]

        return RNG.choices(self.remaining, k=length)

    @property
    def is_empty(self) -> bool:
        return self.unique and not self.remaining


def make_character_pool(
    unique: bool = False, symbol: bool = True, shuffle: bool = False
) -> Cyclic_List:
    pool = Cyclic_List(
        CharacterSet(category, unique) for category in CATEGORIES[: 3 + symbol]
    )
    if shuffle:
        for charset in pool:
            RNG.shuffle(charset.remaining)

    RNG.shuffle(pool)
    return pool


class CharacterPool:
    default_pool = make_character_pool(shuffle=True)
    default_pool_alnum = make_character_pool(symbol=False, shuffle=True)
    unified_charset = CharacterSet("".join(CATEGORIES))
    RNG.shuffle(unified_charset.remaining)
    unified_charset_alnum = CharacterSet("".join(CATEGORIES[:3]))
    RNG.shuffle(unified_charset_alnum.remaining)

    def __init__(self, unique: bool = False, symbol: bool = True) -> None:
        self.unique = unique
        self.symbol = symbol
        if not unique:
            self.pool = self.default_pool if symbol else self.default_pool_alnum
        else:
            self.pool = make_character_pool(True, symbol)

    def uniform_sample(self, length: int) -> List[str]:
        samples = []
        for i in range(length):
            while (charset := self.pool[i]).is_empty:
                self.pool.remove(charset)
                if not self.pool and length - i > 1:
                    raise ValueError("pool is empty")

            samples.append(charset.next_char())

        return samples

    def random_sample(self, length: int) -> List[str]:
        if not self.unique:
            charset = (
                self.unified_charset if self.symbol else self.unified_charset_alnum
            )
            return charset.get_chars(length)

        remaining = [char for charset in self.pool for char in charset.remaining]
        if len(remaining) < length:
            raise ValueError("not enough characters remaining")

        return CharacterSet(remaining, True).get_chars(length)


def generate_password(
    length: int, unique: bool = False, 
    symbol: bool = True, 
    uniform: bool = False
    ) -> str:
    if length < 8 or unique and length > (94 if symbol else 62):
        raise ValueError(
            "argument `length` should be an `int` greater than or equal to 8, "
            "and if duplicates aren't allowed, no greater than 94 if symbols are allowed, or 62 if they aren't"
        )

    first_part = length if uniform else 8
    pool = CharacterPool(unique, symbol)
    password = pool.uniform_sample(first_part)
    if length > first_part:
        password += pool.random_sample(length - first_part)

    RNG.shuffle(password)
    return "".join(password)


def flatten_password_stats(stats: PasswordStats, simple: bool = False) -> tuple:
    fields = tuple(getattr(stats, name) for name in ATTRIBUTES[: 7 - 3 * simple])
    if simple:
        return fields

    return fields + (
        round(stats.entropy_bits * stats.entropy_density, 3),
        round(stats.strength(), 3),
    )


def analyze_password(password: str) -> tuple:
    return flatten_password_stats(PasswordStats(password))


def tally_passwords(passwords: List[str], extensive: bool) -> tuple:
    count = len(passwords)
    if not extensive:
        stats = PasswordStats("".join(passwords))
        return tuple(
            zip(
                COLUMNS[1:5],
                (round(n / count, 3) for n in flatten_password_stats(stats, True)),
            )
        )

    fields = zip(*(analyze_password(password) for password in passwords))
    fields = (round(sum(field) / count, 3) for field in fields)
    return tuple(zip(COLUMNS[1:], fields))


def print_table(columns: Tuple[str], rows: List[list]) -> None:
    console = Console()
    table = Table(*columns)
    for row in rows:
        table.add_row(*map(str, row))

    console.print(table)


def output_tally(
    passwords: List[str], extensive: bool = False, redirect: str = None
) -> None:
    stats = tally_passwords(passwords, extensive)
    if not redirect:
        print_table(("Category", "Value"), stats)
    else:
        Path(redirect).write_text(json.dumps(dict(stats), indent=4))


def stylize_password(password: str) -> str:
    return "".join(CHARACTER_STYLES[c] for c in password)


def print_passwords(passwords: List[str]) -> None:
    for password in passwords:
        print(stylize_password(password))


def print_password_analytics(passwords: List[str]) -> None:
    rows = (
        (stylize_password(password), *analyze_password(password))
        for password in passwords
    )
    rows = sorted(rows, key=lambda x: (-x[-1], x[-3]))
    print_table(COLUMNS, rows)


def get_password_analytics(passwords: List[str]) -> List[dict]:
    rows = (
        dict(zip(COLUMNS, (password, *analyze_password(password))))
        for password in passwords
    )
    rows = sorted(rows, key=lambda x: (-x["Strength"], x["Repetition"]))
    return rows


def process_passwords(
    passwords: List[str], analyze: bool, redirect: str = None
) -> list:
    if redirect:
        return get_password_analytics(passwords) if analyze else passwords
    if analyze:
        print_password_analytics(passwords)
    else:
        print_passwords(passwords)


def serialize_table(table: List[dict]) -> str:
    return "[\n" + ",\n".join("\t" + json.dumps(row) for row in table) + "\n]"


def serialize(obj: Any, custom: bool = False):
    return serialize_table(obj) if custom else json.dumps(obj, indent=4)


def output_passwords(passwords: List[str], analyze: bool, redirect: str = None) -> None:
    rows = process_passwords(passwords, analyze, redirect)
    if redirect:
        Path(redirect).write_text(serialize(rows, analyze))


def main(
    length: LENGTH,
    count: COUNT = 1,
    unique: BOOLEANS[0] = False,
    symbol: BOOLEANS[1] = True,
    uniform: BOOLEANS[2] = False,
    summary: BOOLEANS[3] = False,
    analyze: BOOLEANS[4] = True,
    extensive: BOOLEANS[5] = False,
    redirect: REDIRECT = None,
) -> None:
    """This program generates cryptographically secure passwords.
    The passwords will always contain UPPERCASE ASCII letters, lowercase letters, and digits.
    You can specify whether or not the passwords should contain special characters, by default they are included.
    The characters in the passwords are randomly chosen using cryptographically secure Python `secrets` standard library.
    The passwords generated will have a minimum length of 8, and will contain at least 2 characters from each selected character types.
    You can specify whether or not the passwords should contain unqiue characters only, by default duplicates are allowed.
    If duplicates aren't allowed, there will be password length constraint depending on whether or not special characters are included.
    There are no length constraints otherwise. You can also specify whether or not the characters from each category should be uniformly distributed in the passwords.
    """
    passwords = [
        generate_password(length, unique, symbol, uniform) for _ in range(count)
    ]

    if not summary:
        output_passwords(passwords, analyze, redirect)

    else:
        output_tally(passwords, extensive, redirect)


if __name__ == "__main__":
    typer.run(main)