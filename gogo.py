from requests_html import HTMLSession
import numpy as np
import csv
import requests
import string
import os
from pathlib import Path

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
    image = r.html.find("div.anime_info_body_bg img", first=True).attrs["src"]
    print(image)

    def text(name):
        name = [n for n in name if n not in string.punctuation]
        name = "".join(name)
        name = name.replace(" ", "_")
        return name
    name = r.html.find("div.anime_info_body_bg h1", first=True).text
    name = text(name)
    
    os.chdir(str(Path.cwd()))
    folder = "image"
    p = [str(Path.cwd()), folder] 
    p = "\\".join(p)
    if not os.path.exists(p):
        os.makedirs(folder) 
    with open(f"{p}/{name}.jpg", 'wb') as f:
        im = requests.get(image)
        f.write(im.content)
    p = [str(Path.cwd()), folder, f.name]  
    image_dir = "\\".join(p)
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
        "other_names": other_names,
        "image_dir" : image_dir,
        
        
    }
    return product
def save_to_csv(results):
    keys = results[0].keys()
    
    with open("anime.csv", 'w', encoding="utf-8") as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)
    
results = []
for x in range(1,2):
    print(f"getting page: {x}")
    links = get_link(x)
    for url in links:
        results.append(load_link(url))
        
    save_to_csv(results)
    
