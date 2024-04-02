import requests
from bs4 import BeautifulSoup
import os

def download_image(url, save_path):
    print(f"正在下載圖片{url}")
    response = requests.get(url)
    with open(save_path, "wb") as file:
        file.write(response.content)
    print('-'*30)



def main():
    url = "https://www.ptt.cc/bbs/Beauty/M.1702479070.A.590.html"
    headers ={"Cookie":"over18=1"}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    span = soup.find_all("span", class_="article-meta-value")
    title = span[2].text
    # 建立資料夾
    dir_name = f"images/{title}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    #找出所有的圖片連結
    links = soup.find_all("a")
    allow_file_name = ["jpg", "jpeg", "png", "gif"]
    for link in links:
        href = link.get("href")
        
        file_name = href.split("/")[-1]
        if not href:
            continue 
        
        extension = href.split(".")[-1]
        if extension in allow_file_name:
            download_image(href, f"{dir_name}/{file_name}")
            print(f"'檔案型態:{extension}")
            print(f"網址:{href}")
        
    


if __name__ == "__main__":
    main()
