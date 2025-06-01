import requests

# 台北經緯度
latitude = 25.0478
longitude = 121.5319

# 組 API URL
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

# 發送 GET 請求
response = requests.get(url)

# 解析 JSON
data = response.json()

# 抓出現在溫度
temperature = data["current_weather"]["temperature"]

print("台北市現在氣溫是：", temperature, "°C")



