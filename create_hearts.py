#!/usr/bin/env python

import os
import random
import secrets

from jinja2 import Environment, FileSystemLoader, select_autoescape

from flags import flags


def inner_stripes(stripes):
    if len(stripes) % 2 == 0:
        return stripes[len(stripes) // 2:]
    else:
        return stripes[len(stripes) // 2 + 1:]


def outer_stripes(stripes):
    if len(stripes) % 2 == 0:
        return stripes[:len(stripes) // 2]
    else:
        return stripes[:len(stripes) // 2]


def middle_stripes(stripes):
    if len(stripes) % 2 == 0:
        return []
    else:
        return [stripes[len(stripes) // 2]]


def get_hearts_svg(**kwargs):
    env = Environment(
        loader=FileSystemLoader("templates"), autoescape=select_autoescape(["xml"])
    )

    env.filters["inner_stripes"] = inner_stripes
    env.filters["outer_stripes"] = outer_stripes
    env.filters["middle_stripes"] = middle_stripes

    template = env.get_template("hearts_rainbow_template.svg")

    return template.render(**kwargs, stroke_width=24)
