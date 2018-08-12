# in-geveb-corpus

Corpus of Yiddish based on https://ingeveb.org

Last updated: 8/12/2018

## Contents
- Various texts in Yiddish, broken down to sentences
- Each sentence available in multiple orthographies
    - YIVO
    - Chassidic
    - Soviet
    - Romanized/Latin alphabet

## Directory structure 

```
.
├── LICENSE
├── README.md
├── run_server.sh
├── corpus
│   └── article_text_files_go_here.txt
├── data
│   └── random (meta)data files go here
├── scripts
│   └── various scripts used to create the corpus go here
└── server
    └── tokenization/translitteration server goes here
```

## Usage

1. Run the server with `./run_server.sh`
2. Navigate to [127.0.0.1:1234](https://127.0.0.1:1234) to view API docs

## Todo
- Scrape / extract texts from [in-geveb](https://ingeveb.org) 
- Write NLP processing server (Flask application?)
    - Tokenization
    - Translitteration
- Set up MongoDB to store things
- Demoable Swagger API docs
