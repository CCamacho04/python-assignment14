from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
from time import sleep
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()), options = options)

url = 'https://www.baseball-almanac.com/yearmenu.shtml'

driver.get(url)
sleep(2)

year_links = []

links = driver.find_elements(By.CSS_SELECTOR, "a[href *= 'yearly']")

for link in links:
    href = link.get_attribute("href")
    text = link.text.strip()

    if href and text.isdigit():
        year_links.append((text, href))

print(f'Found {len(year_links)} year links')

rows = []

for year_text, href in year_links[:10]:
    driver.get(href)
    sleep(2)

    try:
        tables = driver.find_elements(By.TAG_NAME, "table")

        if not tables:
            print(f'No tables found for {year_text}')
            continue

        table = tables[0]

        for tr in table.find_elements(By.TAG_NAME, 'tr')[1:]:
            tds = tr.find_elements(By.TAG_NAME, 'td')
            if len(tds) < 2:
                continue

            stat = tds[0].text.strip()
            names = tds[1].text.strip()
            rows.append([year_text, stat, names])

    except Exception as e:
        print(f'Error scraping {year_text}:', e)

driver.quit()

df = pd.DataFrame(rows, columns = ['Year', 'Stat', 'Names'])
print(df)

df.to_csv('get_data.csv', index = False)