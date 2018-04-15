import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import requests
from bs4 import BeautifulSoup
import os

from my_utils import get_links_from_bom_copypaste
from my_utils import write_to_file
from my_utils import not_available
from my_utils import _clean_gross

data_directory = os.path.join("..", "..", "data")
sw_gross_file = "BOM_SW_gross.csv"
sw_gross_path = os.path.join(data_directory, sw_gross_file)

#header of the csv file
header = ["bom_movie_name",
          "swedish_page_link",
          "swedish_gross"
         ]

def get_swedish_link(international_link_list):
    logger.info("Start")
    # if the swedish page contains a meaningful value,
    #   it keeps the link( and get swedish gross)
    # otherwise
    #   it get rid of the swedish link
    sw_link_gross_list = []
    to_sw_page = "page=intl&country=SE&"

    for row in international_link_list:
        #reset from previous iteration
        sw_gross = not_available
        sw_page_link = not_available

        title = row[0]
        international_link = row[1]
        if international_link == not_available:
            sw_page_link, sw_gross = not_available, not_available
        else:
            first_split = international_link[0:37]
            last_split = international_link[37:]
            #Generate the swedish page link
            artificial_sw_page_link = first_split + to_sw_page + last_split
            #Check if the page contains "Sweden" in the table
            sw_page_link, sw_gross = _parse_page(artificial_sw_page_link)
        logger.info("{} swedish link: {}; swedish gross: {}".format(title, sw_page_link, sw_gross))
        new_row = [title, sw_page_link, _clean_gross(sw_gross)]
        sw_link_gross_list.append(new_row)
    logger.info("Done")
    return sw_link_gross_list

def _parse_page(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "lxml")
    result = soup.body.findAll(text="Sweden")
    if len(result) == 0:
        #No Swedish record is available
        return not_available, not_available
    else:
        #link exist, try to get swedish gross
        sw_gross = soup.find('tr', {'bgcolor': '#ffff99'}).contents[4].text
        if len(sw_gross) == 0:
            sw_gross = not_available
        return link, sw_gross


if __name__ == "__main__":
    international_link_list = get_links_from_bom_copypaste()
    sw_link_gross = get_swedish_link(international_link_list)
    write_to_file(sw_gross_path, sw_link_gross, header)