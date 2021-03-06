#!/usr/bin/env python

import base64
import random

from flask import Flask, render_template, request

from flags import flags
from create_hearts import get_hearts_svg


app = Flask(__name__)


@app.template_filter("base64")
def encode_as_base64(xml_string):
    return base64.b64encode(xml_string.encode("ascii")).decode("ascii")


@app.template_filter("name")
def get_name(flag_pair):
    try:
        return flag_pair[1]["name"]
    except KeyError:
        return flag_pair[0]


@app.template_filter("url")
def get_url(flag_pair):
    return flag_pair[1]["url"]


RENAMED_FLAGS = {
    # Renamed after I realised the polyamory and polysexual flags are separate.
    # See https://github.com/queerjs/website/issues/59
    "poly": "polysexual",
}


@app.route("/")
def index():
    selected_flags = {
        "left_flag": random.choice(list(flags.items())),
        "right_flag": random.choice(list(flags.items())),
    }

    for label in selected_flags:
        try:
            flag_name = request.args[label]
            flag_name = RENAMED_FLAGS.get(flag_name, flag_name)
            flag_data = flags[flag_name]
        except KeyError:
            pass
        else:
            selected_flags[label] = (flag_name, flag_data)

    svg_xml = get_hearts_svg(**selected_flags)

    return render_template("index.html", svg_xml=svg_xml, flags=selected_flags)


if __name__ == "__main__":
    app.run(debug=True)
