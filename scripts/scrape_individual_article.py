from scripts.helpers import *

@click.command()
@click.option('--url', help='URL of website')
@click.option('--css', help='CSS selector of links')
@click.option('--output', help='Output path')
def main(url, css, output):
    USER_URL = url
    USER_CSS = css
    DESTINATION = output

    USER_TREE = url_to_tree(USER_URL)

    elems = find_elems(USER_TREE, USER_CSS)
    hrefs = [a.attrib['href'] for a in elems]

    href_output = "\n".join(hrefs)

    with open(DESTINATION, 'a') as f:
        f.write(href_output)


if __name__ == '__main__':
    main()
