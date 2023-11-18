import itertools as it
import os
import pickle
import sys

import click
import cssselect
import lxml.html as html
import nltk
import requests


def flatten_list(nested_list):
    _ = it.chain.from_iterable(nested_list)

    return [x for x in _]


def count_words(text):
    words = split_into_words(text)

    return len(words)


def count_sentences(document):
    sentences = split_into_sentences(document)

    return len(sentences)


def split_into_words(sentence):
    return nltk.word_tokenize(sentence)


def split_into_sentences(document):
    return nltk.sent_tokenize(document)


def url_to_tree(url):
    req = requests.get(url)
    html_text = req.text
    tree = html.fromstring(html_text)

    return tree


def find_elems(tree, css, filter=None):
    if filter is None:
        filter = lambda x: x

    return [elem for elem in tree.cssselect(css) if filter(elem) is not None]


def dump_pickle(obj, path):
    with open(path, "wb") as f:
        pickle.dump(obj, f)


def load_pickle(path):
    with open(path, "rb") as f:
        return pickle.load(f)


def load_text(path):
    with open(path, "r") as f:
        return f.read()


def dump_text(text, path, mode="a"):
    with open(path, mode) as f:
        f.write(text)
