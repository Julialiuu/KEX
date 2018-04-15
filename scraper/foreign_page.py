from my_utils import get_links_from_bom_copypaste
from my_utils import not_available
from my_utils import write_to_file
from my_utils import _clean_gross

import requests, os, re
from bs4 import BeautifulSoup

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#data_directory = os.path.join("..", "..", "data")
#foreign_file = "BOM_foreign_page_data.csv"
foreign_data_path = os.path.abspath("/Users/linnealindahl/Documents/KEX/scraper/BOM_foreign_page_data.csv")

def get_international_links(link_list):
    #international link list
    int_link_list = []
    to_int_page = "page=intl&"

    for row in link_list:
        title = row[0]
        international_link = row[1]
        if international_link == not_available:
            artificial_page_link = not_available
        else:
            first_split = international_link[0:37]
            last_split = international_link[37:]
            # Generate the swedish page link
            artificial_page_link = first_split + to_int_page + last_split
        new_row = [title, artificial_page_link]
        int_link_list.append(new_row)
    return int_link_list

def parse_international_page(link_list):
    #verify whether the links goes to a meaningful page
    # and eventually get the data
    foreign_data_list = []
    for row in link_list:
        title = row[0]
        international_link = row[1]
        if international_link == not_available:
            foreign_opening_weekend, foreign_total_gross, n_countries, sw_opening_gross, sw_opening_date = [not_available for i in range(5)]
        else:
        #Verify and scrape
            foreign_opening_weekend, foreign_total_gross, n_countries, sw_opening_gross, sw_opening_date = _verify_link_and_scrape(international_link)
        logger.info("{}; opening_weekend: {}; total_gross: {}; n_countries: {}; swedish_opening_gross: {}; swedish_opening_date: {} ".format(
                    title, foreign_opening_weekend, foreign_total_gross, n_countries, sw_opening_gross, sw_opening_date))
        if isinstance(foreign_total_gross, str):
            foreign_total_gross = _clean_gross(foreign_total_gross)
        if isinstance(foreign_opening_weekend, str):
            foreign_opening_weekend = _clean_gross(foreign_opening_weekend)
        if isinstance(sw_opening_gross, str):
            if sw_opening_gross == "-":
                sw_opening_gross = not_available
            else:
                sw_opening_gross = _clean_gross(sw_opening_gross)

        new_row = [title,
                   international_link,
                   foreign_opening_weekend,
                   foreign_total_gross,
                   n_countries,
                   sw_opening_gross,
                   sw_opening_date]
        foreign_data_list.append(new_row)
    return foreign_data_list

#if table does not exist ->
#   link does not make sense
#   the 3 values do not make sense
#==> 3 not_available values:
# international_link;foreign_opening_weekend, foreign_total_gross, n_countries
sweden_regex = re.compile(r"Sweden")
def _verify_link_and_scrape(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "lxml")
    table = soup.find_all('table', {'border':'0',
                                    'cellspacing':'1',
                                    'cellpadding':'3'})
    if table == None: #No match -> link does not make sense
        return [not_available for i in range(5)]
    assert len(table) == 1, "More than 1 table matches. Wrong!!!"
    #At this point only 1 table should match
    table = table[0]
    table_rows = table.find_all('tr')

    #Look for Sweden
    sw_opening_date, sw_opening_gross = not_available, not_available
    for row in table_rows:
        if re.search(sweden_regex, str(row.text)):
            sw_opening_gross = row.contents[6].text
            sw_opening_date = row.contents[4].text

    #count number of available states
    n_countries = len(table_rows) - 3

    #FOREIGN TOTAL should be in row[1]
    assert table_rows[1].contents[0].text == 'FOREIGN TOTAL', "Row index is not FOREIGN TOTAL"
    if len(table_rows[1].contents) != 14: #Row has irregular structure
        logger.info("anomalous structure")
        return [not_available for i in range(5)]


    foreign_opening_weekend = table_rows[1].contents[6].text
    #Sometimes scrape returns n/a -> change to N/A
    if foreign_opening_weekend == "n/a":
        foreign_opening_weekend = not_available

    foreign_total_gross = table_rows[1].contents[10].text
    if foreign_total_gross == "n/a":
        foreign_total_gross = not_available

    return foreign_opening_weekend, foreign_total_gross, n_countries, sw_opening_gross, sw_opening_date

if __name__ == "__main__":
    '''
    Output file: BOM_foreign_page_data.csv
    Format of the file:
    <film title>
    <foreign page link>
    <foreign opening weekend income>
    <foreign total gross income>
    <number of countries for which data is available>
    <swedish opening weekend gross>
    <swedish opening weekend date>
    '''
    link_list = get_links_from_bom_copypaste()
    #Just generate link, do NOT verify whether the page exist
    foreign_page_link_list = get_international_links(link_list)
    #Try access the link previously generated and parse page
    foreign_data_list = parse_international_page(foreign_page_link_list)
    header = [ "bom_movie_name",
               "bom_foreign_url",
               "foreign_opening_weekend",
               "foreign_total_gross",
               "n_countries",
               "swedish_opening_weekend_gross",
               "swedish_opening_weekend_date"
             ]
    write_to_file(foreign_data_path, foreign_data_list, header)