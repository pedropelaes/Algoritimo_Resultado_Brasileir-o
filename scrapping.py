from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500, args=["--disable-popup-blocking", "--new-window"])
    
    context = browser.new_context(
    locale="pt-BR",  
    geolocation={"latitude": 38.71689, "longitude": -9.139705, "accuracy": 100}
    )

    page = context.new_page()
    page.goto("https://www.sofascore.com/pt/torneio/futebol/brazil/brasileirao-serie-a/325#id:58766")

    times = page.get_by_test_id("standings_row")
    print(f"Quantidade de times da liga:{times.count()}")
    l_times = []
    #for i in range(times.count()):
        #times.nth(i).screenshot(path="teste" + str(i) + ".png") tira print de cada time da pagina
        #l_times.append(times.nth(i).get_attribute("href"))
    #print(l_times)
    botafogo = context.new_page()
    botafogo.goto("https://www.sofascore.com" + times.nth(0).get_attribute("href"))
    
    
    botafogo.locator("button.DropdownButton[role='combobox']").nth(0).click() 
    botafogo.wait_for_selector("ul.Box li.DropdownItem") 
    botafogo.click("ul.Box li.DropdownItem:nth-child(2)")
    
    botafogo.wait_for_selector('label[for^="listTeamPlayers-"]') #exibe a lista de jogadores no site
    botafogo.click('label[for^="listTeamPlayers-"]')

    botafogo.wait_for_selector("table.Table.fEUhaC")
    tabela_jogadores = botafogo.locator("table.Table.fEUhaC")
    linhas = tabela_jogadores.locator("tr")

    links = []
    nomes_posicao = []
    for i in range(linhas.count()):
        celulas = linhas.nth(i).locator('td')  # Cada célula da linha
        linha_dados = [celulas.nth(j).inner_text() for j in range(celulas.count())]
        if(i != 0):
            linha_dados[0] = linha_dados[0].split('\n', 1)[-1]
            
            link = celulas.nth(0).locator('a').get_attribute('href')
            if link:
                links.append(link)
        nomes_posicao.append(linha_dados)
        
    for i in nomes_posicao:
        print(i)
    for i in links:
        print(i)


    page.close()
    botafogo.close()
    browser.close()
