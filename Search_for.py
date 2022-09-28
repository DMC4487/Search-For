import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Search:

    def iniciar (self):
        self.procurando_produtos()
        self.pesquisando_produtos()

    def procurando_produtos (self):
        print("Bem vindo ao Search For")
        self.produto = input(
            'Digite o nome do produto que gostaria de saber o menor preço\n')
        print('Search For', self.produto)

    def pesquisando_produtos (self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.amazon.com.br/")
        driver.maximize_window()
        driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys(format(self.produto))
        time.sleep(2)
        driver.find_element(By.ID, "nav-search-submit-button").click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//span[@class="a-price-whole"]//span')
        time.sleep(2)
#https://www.youtube.com/watch?v=YlwzjyvSe2w&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz&index=79

start = Search()
start.iniciar()