import requests
from bs4 import BeautifulSoup

url = "enter tiktok username url here"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

profile_pic = soup.find('img', {'class': 'tiktok-1zpj2q-ImgAvatar'}).get('src')
print(profile_pic)