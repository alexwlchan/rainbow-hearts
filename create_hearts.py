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


def create_hearts(*, flag_left, flag_right):
    env = Environment(
        loader=FileSystemLoader("."), autoescape=select_autoescape(["xml"])
    )

    env.filters["inner_stripes"] = inner_stripes
    env.filters["outer_stripes"] = outer_stripes
    env.filters["middle_stripes"] = middle_stripes

    template = env.get_template("hearts_rainbow_template.svg")

    return template.render(flag_left=flag_left, flag_right=flag_right, stroke_width=24)


if __name__ == "__main__":
    os.makedirs("_out", exist_ok=True)

    svg_xml = create_hearts(
        flag_left=random.choice(list(flags.items())),
        flag_right=random.choice(list(flags.items())),
    )

    out_path = os.path.join("_out", f"rainbow-{secrets.token_hex(6)}.svg")

    with open(out_path, "w") as outfile:
        outfile.write(svg_xml)

    print(out_path)
    os.system(f"open -a safari {out_path}")

