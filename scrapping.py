import re
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.sofascore.com/pt/torneio/futebol/brazil/brasileirao-serie-a/325#id:58766")
    times = page.get_by_test_id("standings_row")
    print(f"Quantidade de times da liga:{times.count()}")
    #for i in range(times.count()):
        #times.nth(i).screenshot(path="teste" + str(i) + ".png") tira print de cada time da pagina
    botafogo = browser.new_page()
    botafogo.goto = "https://www.sofascore.com" + times.nth(0).get_attribute("href")
    print(botafogo.title())
    browser.close()
