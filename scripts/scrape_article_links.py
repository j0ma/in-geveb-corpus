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

@click.command()
@click.option('--url', help='URL of website')
@click.option('--css', help='CSS selector of links')
@click.option('--output', help='Output path')
def main():
    USER_URL = url
    USER_CSS = css
    DESTINATION = output

    USER_TREE = url_to_tree(USER_URL)

    elems = find_elems(USER_TREE, USER_CSS)
    hrefs = [a.attrib['href'] for a in elems]

    href_output = "\n".join(hrefs)

    with open(DESTINATION, 'w') as f:
        f.write(href_output)


if __name__ == '__main__':
    main()