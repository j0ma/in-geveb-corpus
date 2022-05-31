from helpers import *
import pandas as pd


@click.command()
@click.option("--input_path", help="Path to sentence corpus")
@click.option("--word_to_ix_path", help="Path to .pkl file mapping word => index")
@click.option("--ix_to_word_path", help="Path to .pkl file mapping index => word")
def main(input_path, word_to_ix_path, ix_to_word_path):
    print('Loading sentence corpus from "{}"'.format(input_path))

    sentence_corpus = pd.read_csv(input_path)
    sentences = sentence_corpus.sentence

    print("Done! Calculating unique words...")
    words = flatten_list([split_into_words(s) for s in sentences])
    unique_words = set(words)

    print("Done! Creating mapping objects...")
    word_to_index = {w: i for i, w in enumerate(unique_words)}
    index_to_word = {i: w for i, w in enumerate(unique_words)}

    print('Done! Outputting "word_to_index" to "{}"'.format(word_to_ix_path))
    dump_pickle(word_to_index, word_to_ix_path)

    print('Done! Outputting "index_to_word" to "{}"'.format(ix_to_word_path))
    dump_pickle(index_to_word, ix_to_word_path)

    print("Done!")


if __name__ == "__main__":
    main()
