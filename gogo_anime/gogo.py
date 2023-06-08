from requests_html import HTMLSession
import numpy as np
import csv
s = HTMLSession()
def get_link(page):
    r = s.get(f"https://www3.gogoanimes.fi/anime-list.html?page={page}")
    links = []
    products = r.html.find("ul.listing li")
    for item in products:
        links.append(item.find("a", first=True).attrs["href"])
    return links


def load_link(url):
    l = []
    ft = []
    r = s.get(f"https://www3.gogoanimes.fi{url}")
    title = r.html.find("div.anime_info_body_bg h1", first=True).text
    content = r.html.find("p.type")
    for i in content:
        l.append(i.text)
        
    ft.append(l)
    arr = np.array(l)
    type = arr[0].split(":")[1]
    plot = arr[1].split(":")[1]
    genre = arr[2].split(":")[1]
    released = arr[3].split(":")[1]
    status = arr[4].split(":")[1]
    other_names = arr[5].split(":")[1]
    
    product = {
        "title": title,
        "type": type,
        "plot": plot,
        "genre": genre,
        "released": released,
        "status": status,
        "other_names": other_names
        
    }
    return product
def save_to_csv(results):
    keys = results[0].keys()
    
    with open("anime.csv", 'w', encoding="utf-8") as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)
    
results = []
for x in range(1,92):
    print(f"getting page: {x}")
    links = get_link(x)
    for url in links:
        results.append(load_link(url))
        
    save_to_csv(results)
    
