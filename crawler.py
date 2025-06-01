import requests
from bs4 import BeautifulSoup

url = "https://www.cwa.gov.tw/V8/C/W/TemperatureTop.html"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("tr")  # 找所有表格列

    for row in rows:
        cells = row.find_all("td")
        if len(cells) > 0 and "臺北" in cells[0].text:
            temp = cells[1].text.strip()  # 第 1 欄是地點，第 2 欄是溫度
            print("台北市現在氣溫是：", temp, "°C")
            break  # 找到就不用繼續找了
else:
    print("網站讀取失敗！")

