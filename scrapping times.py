from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    context = browser.new_context(
    locale="jp-JP",  
    geolocation={"latitude": 38.71689, "longitude": -9.139705, "accuracy": 100}
    )

    campeonato = context.new_page()
    campeonato.goto("https://www.sofascore.com/pt/torneio/futebol/brazil/brasileirao-serie-a/325#id:58766")

    times = campeonato.get_by_test_id("standings_row")
    
    print(f"Quantidade de times da liga:{times.count()}")
    link_times = []
    info_times = [] 
    for i in range(times.count()):
        #times.nth(i).screenshot(path="teste" + str(i) + ".png") #tira print de cada time da pagina
        link_times.append(times.nth(i).get_attribute("href"))
        info_times.append(times.nth(i).inner_text())
        
    for i in range(len(info_times)):
        info_times[i] = str(info_times[i]).split('\n', -1)

    print("Links dos times:\n")
    for i in link_times:
        print(i)
    print("--------------------")
    print("Informação dos times:\nPos | Nome | Jogos | Vitorias | Empates | Derrotas")
    for i in info_times:
        print(i)

    campeonato.close()
    browser.close()