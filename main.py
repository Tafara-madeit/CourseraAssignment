import page as page
import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://api.spacexdata.com/v4/launches/past"
response = requests.get(url)
response.json()
df = pd.DataFrame(response.json())
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
print(df)
# falcon9_launches = df[df['name'] == 'Starlink']
# print(falcon9_launches)


