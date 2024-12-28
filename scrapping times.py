import time
start_time = time.time()
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    context = browser.new_context(
    locale="jp-JP",  
    geolocation={"latitude": -33.86882, "longitude": 151.209296, "accuracy": 100}
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

    data_times = [times[:5] for times in info_times] #limpa as informações desnecessárias, deixando apenas posição, nome, vitorias, empates e derrotas

    for q in range(times.count()): #busca o nome e o link dos tenicos de cada time e adiciona na lista
        pag_time = context.new_page()
        pag_time.goto("https://www.sofascore.com" + link_times[q])
        
        div_nota = pag_time.locator("xpath=//span[text()='Notas Sofascore']/ancestor::div[contains(@class, 'Box')]/following-sibling::div//span[@role='meter'][@aria-valuenow]")
        nota_time = div_nota.first.text_content()
        nota_time = float(nota_time)
        
        treinador_div = pag_time.locator('text=Treinador').locator('..')  
        link_tecnico = treinador_div.locator('a').get_attribute('href') 
        nome_tecnico = treinador_div.locator('a').inner_text()
        data_times[q].extend([nome_tecnico, link_tecnico, nota_time])
        pag_time.close()


    print("Links dos times:\n")
    for i in link_times:
        print(i)
    print("--------------------")
    print("Informação dos times:\nPos | Nome | Jogos | Vitorias | Empates | Derrotas\n")
    for i in data_times:
        print(i)

    end_time = time.time()
    print(f"Tempo de execução: {end_time - start_time:.2f} segundos")
    campeonato.close()
    browser.close()