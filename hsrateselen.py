from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


zapros = input().lower()

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
url = "https://hearthstone.blizzard.com/en-us/community/leaderboards/?region=EU&leaderboardId=battlegrounds&seasonId=8"
driver_service = Service(executable_path="C:\\Users\\Гияс\\PycharmProjects\\poiskheartstone\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service, options=options)
driver.set_page_load_timeout(5)

spisok = []
bisok = []
gisok = []


for i in range(1, 5):

    try:
        url = f"https://hearthstone.blizzard.com/ru-ru/community/leaderboards/?region=EU&leaderboardId=battlegrounds&seasonId=8&page={i}"
        driver.get(url=url)

    except TimeoutException:
        driver.execute_script("window.stop();")

    block1 = driver.find_element(By.CLASS_NAME, "LeaderboardsTable-Rendered")
    block2 = block1.find_elements(By.CLASS_NAME, "row")

    for j in block2:
        spisok.append(j.text.lower())

driver.close()
driver.quit()

for o in spisok:
    bisok.append(o.split("\n"))

x = [d for p in bisok for d in p]

for z, q in enumerate(x):
    if q == zapros:
        gisok.append(str(x[z]))
        gisok.append(str(x[z-1]))
        gisok.append(str(x[z+1]))

f = f"Место = {gisok[1]}, ник = {gisok[0]}, рейтинг = {gisok[2]}"
print(f)