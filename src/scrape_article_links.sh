# Grab helper function from same dir
source $(dirname $BASH_SOURCE)/helpers.sh

# Temporary scratch folder
scratch_folder=$(mktemp -d)

base_url="https://ingeveb.org/texts-and-translations"
for page_id in $(seq 1 11)
do
    url=$base_url
    if [ "${page_id}" -gt "1" ]
    then
        url="${url}/p${page_id}"
    fi

    get_hrefs_from_page $url > ${scratch_folder}/links${page_id}.txt &

done

wait

# Output
output_file=${1:-in_geveb_links.txt}
cat $scratch_folder/links*.txt | tee $output_file

rm -rf $scratch_folder
