import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = 'https://www.ptt.cc/bbs/NBA/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}   
response = requests.get(url, headers=headers)
 
# ----將網頁內容存入檔案----
if response.status_code == 200:
    with open('ptt.html', 'w',encoding='utf-8') as f:
        f.write(response.text)
    print('網頁抓取成功')
else:
    print('網頁抓取失敗')


soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all("div", "r-ent")   


data_list = []
for a in articles:
    data = {}
    
    title = a.find ('div',class_= 'title')  
    if title and title.a:
        title = title.a.text
    else:
        title = '沒有標題'
    data['標題'] = title

    popular = a.find('div', class_='nrec') 
    if popular and popular.span:
        popular = popular.span.text 
    else:
        popular = ('N/A')
    data['人氣'] = popular

    date = a.find('div', class_='date')
    if date :
        date = date.text
    else:
        date = 'N/A'

    data['日期'] = date
    data_list.append(data)
    print(f"標題:{title}  人氣:{popular}  日期:{date}")
print(data_list)



# -------將資料寫成excel------
df = pd.DataFrame(data_list)
df.to_excel('ptt.xlsx', index=False)


# ----將資料寫成json檔----
with open('ptt.json', 'w', encoding='utf-8') as f:
    json.dump(data_list, f, ensure_ascii=False, indent=2)



