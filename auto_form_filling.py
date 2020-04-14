from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


def page_is_loaded(chrome):
    return driver.find_element_by_tag_name('body') != None


driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdTWwfdQUKmxP8XYFy8AEEepEIuNwVz_xXuY7Znn5ZG_CDcjw/viewform') # endereço da página a ser acessada

wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)

for x in range(0,499): # selecione o número de vezes que o script vai rodar (neste caso, 100 vezes)
    opt_body = driver.find_elements_by_tag_name('Span')
    for option in opt_body:
        if option.text == 'Opção 4': # selecione uma opção (para este caso, a opção 4 que mostra uma vaca animada)
            option.click()
            break

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span/span').click()

    opt_big = driver.find_elements_by_tag_name('Span')
    for opt in opt_big:
        if opt.text == 'Big': # selecione um nome
            opt.click()
            break

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span/span').click()

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input').send_keys("daniel.buck@gmail.com") # coloque aqui o email para validar a votação
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span').click()
    
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

    opt_body = driver.find_elements_by_tag_name('Span')
    for option in opt_body:
        if option.text == 'Opção 4': # selecione uma opção (para este caso, a opção 4 que mostra uma vaca animada)
            option.click()
            break

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span/span').click()

    opt_big = driver.find_elements_by_tag_name('Span')
    for opt in opt_big:
        if opt.text == 'Big': # selecione um nome
            opt.click()
            break

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span/span').click()

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input').send_keys("erika.carollpaiva@gmail.com") # coloque aqui o email para validar a votação
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span').click()
    
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

    opt_body = driver.find_elements_by_tag_name('Span')
    for option in opt_body:
        if option.text == 'Opção 4': # selecione uma opção (para este caso, a opção 4 que mostra uma vaca animada)
            option.click()
            break

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span/span').click()

    opt_big = driver.find_elements_by_tag_name('Span')
    for opt in opt_big:
        if opt.text == 'Big': # selecione um nome
            opt.click()
            break

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span/span').click()

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input').send_keys("teixeira.mgt1@gmail.com") # coloque aqui o email para validar a votação
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span').click()
    
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

    opt_body = driver.find_elements_by_tag_name('Span')
    for option in opt_body:
        if option.text == 'Opção 4': # selecione uma opção (para este caso, a opção 4 que mostra uma vaca animada)
            option.click()
            break

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span/span').click()

    opt_big = driver.find_elements_by_tag_name('Span')
    for opt in opt_big:
        if opt.text == 'Big': # selecione um nome
            opt.click()
            break

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span/span').click()

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input').send_keys("ipod.buck@gmail.com") # coloque aqui o email para validar a votação
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span').click()
    
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
