from helpers import *
import pandas as pd
import os

# CONSTANTS
CORPUS_DIRECTORY = os.path.abspath("../corpus")
OUTPUT_FILENAME = "{}/in_geveb_document_corpus.csv".format(CORPUS_DIRECTORY)

# find all articles and their paths
print("Finding all articles & paths...")
file_names = [
    f for f in os.listdir(CORPUS_DIRECTORY) if os.path.splitext(f)[1] == ".txt"
]

file_paths = ["{}/{}".format(CORPUS_DIRECTORY, fn) for fn in file_names]

# extract document ids from each filename
print("Done. Extracting document ids...")
document_ids = [int(fn.split("-")[0]) for fn in file_names]
document_id_to_file_name = {did: fn for did, fn in zip(document_ids, file_names)}
document_id_to_file_path = {did: fp for did, fp in zip(document_ids, file_paths)}

# create a dictionary of all document
print("Done. Loading all documents from the corpus to RAM...")
document_dict = {did: load_text(document_id_to_file_path[did]) for did in document_ids}

# convert to data frame
print("Done. Converting to data frame...")
document_corpus = pd.DataFrame(
    {
        "document_id": sorted(document_ids),
        "file_name": [document_id_to_file_name[did] for did in sorted(document_ids)],
        "document": [document_dict[did] for did in sorted(document_ids)],
    },
    columns=["document_id", "file_name", "document"],
)

print("Done. Outputting to {}".format(CORPUS_DIRECTORY))
document_corpus.to_csv(OUTPUT_FILENAME, index=False, encoding="utf-8")
print("Done!")
