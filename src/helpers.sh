get_hrefs_from_page () {
    # Given a page, find all the listing/article links in it
    local url=$1
    local href_selector="div.listing > a"
    curl --silent $url | htmlq --attribute href $href_selector
}

scrape_yiddish_from_article () {
    # Given an article, find all Yiddish text in it
    local url=$1
    local yi_selector="section#main-content > div.block-translatedText > div.translation-wrapper  > div.yiddish-text > p"
    
    curl --silent $url \
        | htmlq -t $yi_selector \
        | sed "s/^\s*//g"
}
