import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import requests
from bs4 import BeautifulSoup
import os

from my_utils import get_links_from_bom_copypaste
from my_utils import write_to_file
from my_utils import not_available
from my_utils import _clean_mpaa, _clean_prod_budget, _clean_gross

static_data_path = os.path.abspath("/Users/linnealindahl/Documents/KEX/scraper/BOM_mpaa_productionBudget_usTotalGross_usOpeningWeekend.csv")

#header of csv file
header = ["bom_movie_name",
          "bom_url",
          "mpaa_rating",
          "production_budget_usd",
          "total_gross_usa_usd",
          "opening_weekend_us"
         ]

def get_us_values(link_list):
    import re
    mpaa_regex = re.compile("MPAA")
    production_budget_regex = re.compile("Production")
    domestic_total_regex = re.compile(r"Domestic.Total")
    opening_weekend_regex = re.compile(r"Opening.Weekend")

    mpaa_production_list = []
    for row in link_list:
        #Reset values from previos iteration
        mpaa_rating = not_available
        production_budget = not_available
        us_total_gross = not_available
        opening_weekend = not_available

        title = row[0]
        # This film provides a broken link, do not use it
        if title == "I'll Push You": continue
        international_link = row[1]
        if international_link == not_available: continue
        response = requests.get(international_link)
        soup = BeautifulSoup(response.content, "lxml")

        #Look for Opening weekend
        op_wkn_div = soup.find_all('div', {'class':"mp_box_content"})
        tags = op_wkn_div[1].find_all('tr')  #--> need control with regex "eg The student" Before last one
        for tag in tags:
            if re.search(opening_weekend_regex, tag.text):
                opening_weekend = tag.contents[-1].text[1:]
        #Get mpaa rating and production...table
        table = soup.find('table', {'border':'0',
                                    'cellspacing':'1',
                                    'cellpadding':'4',
                                    'bgcolor':'#dcdcdc',
                                    'width':'95%'})
        #Look for values inside the previous table
        for i in table.find_all('td'):
            #Look for MPAA reting
            if re.match( mpaa_regex, str(i.contents[0])):
                mpaa_rating = i.contents[1].text
            #Look for production budget
            if re.match( production_budget_regex, str(i.contents[0])):
                production_budget = i.contents[1].text
            #Look for Domestic(us) total gross
            if re.search( domestic_total_regex, str(i.contents[0])):
                raw_text = str(i.contents[0].text)
                us_total_gross = raw_text.split(': ')[1]
        logger.info("{} has MPAA: {}; production cost: {}; domestic total: {}, opening weekend: {}".format(title,
                                                                                                           mpaa_rating,
                                                                                                           production_budget,
                                                                                                           us_total_gross,
                                                                                                           opening_weekend
                                                                                                           ))
        new_row = [title,
                   international_link,
                   _clean_mpaa(mpaa_rating),
                   _clean_prod_budget(production_budget),
                   _clean_gross(us_total_gross),
                   _clean_gross(opening_weekend)
                  ]
        mpaa_production_list.append(new_row)
    return mpaa_production_list


if __name__ == "__main__":
    link_list = get_links_from_bom_copypaste()
    static_data = get_us_values(link_list)
    write_to_file(static_data_path, static_data, header)
