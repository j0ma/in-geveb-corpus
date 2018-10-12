from helpers import *

@click.command()
@click.option('--url', help='URL of website')
@click.option('--css', help='CSS selector of links')
@click.option('--output', help='Output path')
def scrape_article_links(url, css, output):
    USER_URL = url
    USER_CSS = css
    DESTINATION = output

    USER_TREE = url_to_tree(USER_URL)

    elems = find_elems(USER_TREE, USER_CSS)
    hrefs = [a.attrib['href'] for a in elems]

    href_output = "\n".join(hrefs)

    dump_text(text=href_output,
              path=DESTINATION, 
              mode='a')

if __name__ == '__main__':
    scrape_article_links()
