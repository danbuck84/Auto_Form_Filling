from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


def page_is_loaded(chrome):
    return driver.find_element_by_tag_name('body') != None


driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdTWwfdQUKmxP8XYFy8AEEepEIuNwVz_xXuY7Znn5ZG_CDcjw/viewform')

wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)

for x in range(0,99):
    opt_body = driver.find_elements_by_tag_name('Span')
    for option in opt_body:
        if option.text == 'Opção 6':
            option.click()
            break

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span/span').click()

    opt_tang = driver.find_elements_by_tag_name('Span')
    for opt in opt_tang:
        if opt.text == 'Tang':
            opt.click()
            break

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span/span').click()

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input').send_keys("ipod.buck@gmail.com")
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span').click()
    
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

    opt_body = driver.find_elements_by_tag_name('Span')
    for option in opt_body:
        if option.text == 'Opção 6':
            option.click()
            break

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span/span').click()

    opt_victor = driver.find_elements_by_tag_name('Span')
    for opt in opt_victor:
        if opt.text == 'Victor':
            opt.click()
            break

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span/span').click()

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input').send_keys("ipod.buck@gmail.com")
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span').click()
    
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

    opt_body = driver.find_elements_by_tag_name('Span')
    for option in opt_body:
        if option.text == 'Opção 6':
            option.click()
            break

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span/span').click()

    opt_ju = driver.find_elements_by_tag_name('Span')
    for opt in opt_ju:
        if opt.text == 'Ju Bonello':
            opt.click()
            break

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span/span').click()

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input').send_keys("ipod.buck@gmail.com")
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span').click()
    
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
