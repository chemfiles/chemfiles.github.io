#! /usr/bin/env python
# -*- coding: utf-8 -*-
from cactus.template_tags import register

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer


def remove_indent(content):
    '''Remove global indentation of a block of code'''
    lines = content.split("\n")[1:]
    indentation = 0
    for char in lines[0]:
        if char == " ":
            indentation += 1
        else:
            break
    content = ""
    for line in lines:
        content += line[indentation:] + "\n"
    return content


def highlight_code(content, language="text"):
    """Highlight code using Pygments"""

    content = remove_indent(content)

    # Replace the pulled code blocks with syntax-highlighted versions.
    formatter = HtmlFormatter(noclasses=True)
    try:
        lexer = get_lexer_by_name(language, stripnl=True, encoding=u'UTF-8')
    except ValueError:
        try:
            # Guess a lexer by the contents of the block.
            lexer = guess_lexer(content)
        except ValueError:
            # Just make it plain text.
            lexer = get_lexer_by_name(u'text', stripnl=True, encoding=u'UTF-8')
    return highlight(content, lexer, formatter)


def preBuild(_):
    register.filter('highlight', highlight_code)
