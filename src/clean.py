import json
import re

import click
import hebrew_tokenizer as ht
import nltk
import pysbd
import yiddish

segmenter = pysbd.Segmenter(language="en", clean=False)


def tokenize_yiddish(text):
    tokens = list(ht.tokenize(text))
    tokens = [token for _, token, _, _ in tokens]

    return tokens


def clean_doc(text: str) -> str:
    # normalize german-style quotations to "
    text = re.sub(r"„|“", '"', text)
    # normalize german-style apostrophes to '
    text = re.sub(r"’", "'", text)

    # normalize dashes to -
    text = re.sub(r"–", "-", text)

    # remove leading dashes
    text = re.sub(r"^-", "", text)

    return text


@click.command()
@click.argument("input_files", nargs=-1, type=click.Path(exists=True))
def main(input_files):

    # load files as streams
    rows = []

    for document_id, input_file in enumerate(input_files):
        with click.open_file(input_file, "r") as fin:
            doc = clean_doc(fin.read())

            sentences = segmenter.segment(doc)

            for sentence_id, sentence in enumerate(sentences):

                sentence = sentence.strip()

                # sentence
                sentence = re.sub(r"\\n", "", sentence)
                sentence_yivo = yiddish.replace_with_precombined(sentence)
                sentence_no_diacritics = yiddish.strip_diacritics(sentence_yivo)
                sentence_hasidic = yiddish.hasidify(sentence_yivo)
                sentence_romanized = yiddish.transliterate(
                    sentence_yivo, loshn_koydesh=True
                )

                # tokens
                tokens_yivo = tokenize_yiddish(sentence_yivo)
                tokens_no_diacritics = tokenize_yiddish(sentence_no_diacritics)
                tokens_hasidic = tokenize_yiddish(sentence_hasidic)
                tokens_romanized = nltk.word_tokenize(sentence_romanized)

                if not sentence:
                    continue

                rows.append(
                    {
                        "sentence_yivo": sentence,
                        "sentence_hasidic": sentence_hasidic,
                        "sentence_no_diacritics": sentence_no_diacritics,
                        "sentence_romanized": sentence_romanized,
                        "file": str(input_file),
                        "document_id": document_id,
                        "sentence_id": sentence_id,
                        "tokens_yivo": tokens_yivo,
                        "tokens_hasidic": tokens_hasidic,
                        "tokens_no_diacritics": tokens_no_diacritics,
                        "tokens_romanized": tokens_romanized,
                    }
                )

    # write to stdout

    for row in rows:
        click.echo(json.dumps(row, ensure_ascii=False))


if __name__ == "__main__":
    main()
