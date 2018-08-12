import lxml.html as html
import requests
import cssselect
import click
import pickle
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

def dump_pickle(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)

def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def load_text(path):
    with open(path, 'r') as f:
        return f.read()

def dump_text(text, path, mode='a'):
    with open(path, mode) as f:
        f.write(text)


