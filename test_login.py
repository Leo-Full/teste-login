from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_login_com_sucesso():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Espera a URL mudar para /secure (só acontece após login bem-sucedido)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("secure"))

    assert "You logged into a secure area" in driver.page_source

    driver.quit()


def test_login_com_senha_errada():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("senhaerrada123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # O <div id="flash"> só existe no HTML depois que o servidor processa
    # o login e devolve a página com a mensagem de erro (não existe no
    # carregamento inicial, diferente do #flash-messages que é o container vazio)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "flash")))

    assert "Your password is invalid!" in driver.page_source

    driver.quit()