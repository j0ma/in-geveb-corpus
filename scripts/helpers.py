import lxml.html as html
import requests
import cssselect
import click
import sys
import os

def url_to_tree(url):
    req = requests.get(url)
    html_text = req.text
    tree = html.fromstring(html_text)
    return tree

def find_elems(tree, css, filter=None):
    if filter is None:
        filter = lambda x: x
    return [elem for elem
                 in tree.cssselect(css)
                 if filter(elem)]