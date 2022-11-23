import json
import requests as req
import time
import tqdm
from random import randint
from bs4 import BeautifulSoup, Tag
data = {"data":[]}

for page in range (6,18):
    url = f"https://hh.ru/search/vacancy?text=Python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&salary=100000&clusters=true&area=113&ored_clusters=true&enable_snippets=true&only_with_salary=true&page={page}&hhtmFrom=vacancy_search_list"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"
    }
    resp = req.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "lxml")
    tags = soup.find_all(attrs={"class":"serp-item__title"})
    for iter in tqdm.tqdm(tags):
        time.sleep(randint(5,8))
        
        url_object = iter.attrs["href"]
        #print(iter.attrs["href"])
        resp_object = req.get(url_object, headers=headers)
        soup_object = BeautifulSoup(resp_object.text, "lxml")
        if (soup_object.find(attrs={"class":"bloko-header-section-2 bloko-header-section-2_lite"}))!=None:
            tags_price = soup_object.find(attrs={"class":"bloko-header-section-2 bloko-header-section-2_lite"}).text
        else: tags_price = (" ")
        if (soup_object.find(attrs={"data-qa":"vacancy-view-raw-address"}))!=None:
            tags_region=soup_object.find(attrs={"data-qa":"vacancy-view-link-location"}).text
            adress = tags_region.split(",")          
            tag_region = adress[0]
        else:
            if (soup_object.find(attrs={"data-qa":"vacancy-view-location"}))!=None:
                tag_region=soup_object.find(attrs={"data-qa":"vacancy-view-location"}).text
            else:  tag_region = (" ")  
        if (soup_object.find(attrs={"data-qa":"vacancy-experience"}))!=None:
            tag_experience = soup_object.find(attrs={"data-qa":"vacancy-experience"}).text
        else: tag_experience = (" ") 
        data["data"].append({"Title":iter.text,"Salary":tags_price,"Region":tag_region, "Experience":tag_experience})
        #print (iter.text, tags_price.text, tag_region,tag_experience)
        #print (data)
        with open("data.json", "w", encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False)
            