from helpers import *
import pandas as pd


@click.command()
@click.option("--input_path", help="Path to input file, i.e. the document corpus")
@click.option("--output_path", help="Path to output file, i.e. the sentence corpus")
def main(input_path, output_path):

    # load input document corpus
    print('Loading document corpus from "{}"'.format(input_path))
    document_corpus = pd.read_csv(input_path)

    # calculate quantities for sentence corpus
    print("Done! Splitting documents into sentences...")
    n_sentences = document_corpus.document.apply(count_sentences).tolist()
    sentences = document_corpus.document.apply(split_into_sentences).tolist()
    flat_sentences = flatten_list(sentences)

    print("Done! Calculating document_ids...")
    document_ids = [
        [doc_id] * n_sents
        for doc_id, n_sents in zip(document_corpus.document_id, n_sentences)
    ]
    flat_document_ids = flatten_list(document_ids)

    print("Done! Calculating sentence ids...")
    flat_sentence_ids = flatten_list([[i for i in range(n)] for n in n_sentences])
    global_sentence_ids = [i for i, s in enumerate(flat_sentences)]

    print("Done! Creating sentence corpus data frame...")
    sentence_corpus_dict = {
        "global_sentence_id": global_sentence_ids,
        "document_id": flat_document_ids,
        "sentence_id": flat_sentence_ids,
        "sentence": flat_sentences,
    }

    sentence_corpus_columns = [
        "global_sentence_id",
        "document_id",
        "sentence_id",
        "sentence",
    ]
    sentence_corpus = pd.DataFrame(
        sentence_corpus_dict, columns=sentence_corpus_columns
    )

    print('Done! Outputting to disk under "{}"'.format(output_path))
    sentence_corpus.to_csv(output_path, encoding="utf-8", index=False)

    print("Done")


if __name__ == "__main__":
    main()
