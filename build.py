#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import glob
import shutil
from datetime import datetime

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from jinja2 import nodes
from jinja2.ext import Extension

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_ROOT = os.path.join(ROOT, "src")
BUILD_ROOT = os.path.join(ROOT, "build")


SVG_WIDTH = re.compile(' width="(.*?)" ')
SVG_HEIGHT = re.compile(' height="(.*?)" ')


class OctoiconExtension(Extension):
    tags = {"octoicon"}

    def __init__(self, environment):
        super(OctoiconExtension, self).__init__(environment)

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        args = [parser.parse_expression()]

        if parser.stream.skip_if("comma"):
            args.append(parser.parse_expression())
        else:
            args.append(nodes.Const(None))

        return nodes.CallBlock(
            self.call_method("_render_icon", args), [], [], []
        ).set_lineno(lineno)

    def _render_icon(self, name, factor, caller):
        with open(
            os.path.join(SRC_ROOT, "templates", "octoicons", f"{name}.svg")
        ) as fd:
            svg = fd.read()

        if factor is not None:
            match_width = SVG_WIDTH.search(svg)
            match_height = SVG_HEIGHT.search(svg)
            width = int(match_width.group(1))
            height = int(match_height.group(1))
            svg = svg.replace(match_width.group(0), f' width="{factor * width}" ')
            svg = svg.replace(match_height.group(0), f' height="{factor * height}" ')

        svg = svg.replace("<svg", '<svg class="octoicon"')

        return svg


def raw_include(path):
    with open(os.path.join(SRC_ROOT, path)) as fd:
        return fd.read()


def render(file, env, context):
    basename = os.path.basename(file)
    print(f"---- {basename}")
    with open(file) as fd:
        content = fd.read()

    template = env.from_string(content)
    output = template.render(context)

    with open(os.path.join(BUILD_ROOT, basename), "w") as fd:
        fd.write(output)


def build():
    print(f"building {ROOT} ...")
    shutil.rmtree(BUILD_ROOT, ignore_errors=True)
    shutil.copytree(src=os.path.join(SRC_ROOT, "root"), dst=BUILD_ROOT)

    env = Environment(
        extensions=["jinja2_highlight.HighlightExtension", OctoiconExtension],
        loader=FileSystemLoader(os.path.join(SRC_ROOT, "templates")),
        undefined=StrictUndefined,
    )

    env.globals["raw_include"] = raw_include
    context = {}
    context["current_date"] = datetime.now().replace(microsecond=0).isoformat()

    all_pages = []
    for file in glob.glob(os.path.join(SRC_ROOT, "pages/*.html")):
        context["current_page"] = os.path.basename(file)
        all_pages.append(context["current_page"])

        render(file, env, context)

    context["all_pages"] = all_pages
    render(os.path.join(SRC_ROOT, "pages/sitemap.xml"), env, context)

    print()


if __name__ == "__main__":
    build()
