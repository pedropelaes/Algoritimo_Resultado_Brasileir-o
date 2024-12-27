import re
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500, args=["--disable-popup-blocking", "--new-window"])
    page = browser.new_page()
    page.goto("https://www.sofascore.com/pt/torneio/futebol/brazil/brasileirao-serie-a/325#id:58766")

    times = page.get_by_test_id("standings_row")
    print(f"Quantidade de times da liga:{times.count()}")
    l_times = []
    #for i in range(times.count()):
        #times.nth(i).screenshot(path="teste" + str(i) + ".png") tira print de cada time da pagina
        #l_times.append(times.nth(i).get_attribute("href"))
    #print(l_times)
    botafogo = browser.new_page()
    botafogo.goto("https://www.sofascore.com" + times.nth(0).get_attribute("href"), timeout=60000)
    
    botafogo.click("button.DropdownButton[role='combobox']")
    botafogo.wait_for_selector("ul.Box li.DropdownItem") 
    botafogo.click("ul.Box li.DropdownItem:nth-child(2)")
    
    #botafogo.wait_for_selector('label[for="listTeamPlayers-0.418401101465224"]', state="visible")
    #botafogo.click('label[for="listTeamPlayers-0.418401101465224"] span')
    
    browser.close()
