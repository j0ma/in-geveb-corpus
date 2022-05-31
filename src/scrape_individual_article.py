from helpers import *


def create_article(elems):
    lines = [e.text_content() for e in elems]
    return "\n".join(lines)


@click.command()
@click.option("--url", help="URL of website")
@click.option("--css", help="CSS selector to use")
@click.option("--output", help="Output path")
@click.option("--format", help='Output format ("pickle", "text")')
def scrape_individual_article(url, css, output, format):
    USER_URL = url
    USER_CSS = css
    DESTINATION = output
    OUTPUT_FORMAT = format
    USER_TREE = url_to_tree(USER_URL)

    elems = find_elems(USER_TREE, USER_CSS)

    output = create_article(elems)

    if format == "pickle":
        dump_pickle(obj=output, path=DESTINATION)
    elif format == "text":
        dump_text(text=output, path=DESTINATION, mode="a")
    else:
        raise ValueError("Format must be one of (pickle, text)")


if __name__ == "__main__":
    scrape_individual_article()
