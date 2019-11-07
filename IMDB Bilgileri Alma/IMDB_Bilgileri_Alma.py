from bs4 import BeautifulSoup
import requests

print("-"*30)
print("IMDB En İyi Filmler Bölümünde ki Bütün Filmler")
print("-"*30)

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")
list = soup.find("tbody", {"class":"lister-list"}).find_all("tr")

count = 0
for tr in list:
    title = tr.find("td", {"class":"titleColumn"}).find("a").text
    year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    count+=1
    print(f"{count}- Filmin İsmi: {title.ljust(100)} Filmin Yılı: {year} Filmin Puanı: {rating}")





