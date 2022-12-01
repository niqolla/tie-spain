from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

APPOINTMENT = 0
hold = 1.5

link = "https://icp.administracionelectronica.gob.es/icpplustieb/index"
PATH = "C:/chromedriver.exe"

minutes = int(input("will check every x minutes:"))
print(isinstance(minutes, int))

while APPOINTMENT == 0:

    # FIRST PAGE
    driver = webdriver.Chrome(PATH)
    driver.get(link)
    time.sleep(hold)
    DrpM = driver.find_element(By.ID, "form")
    DrpM_O = Select(DrpM)
    DrpM_O.select_by_visible_text("Barcelona")
    btnAccept = driver.find_element(By.ID, "btnAceptar")
    time.sleep(hold)
    btnAccept.click()

    # FIND FINGERPRINT AND ACCEPT
    DrpF = driver.find_element(By.ID, "tramiteGrupo[1]")
    DrpF_O = Select(DrpF)
    DrpF_O.select_by_visible_text(
        "POLICIA-TOMA DE HUELLA (EXPEDICIÓN DE TARJETA), RENOVACIÓN DE TARJETA DE LARGA DURACIÓN Y DUPLICADO")
    btnAccept = driver.find_element(By.ID, "btnAceptar")
    time.sleep(hold)
    btnAccept.click()

    # ENTER
    btnAccept_forEnter = driver.find_element(By.ID, "cookie_action_close_header")
    btnAccept_forEnter.click()
    btnEnter = driver.find_element(By.ID, "btnEntrar")
    time.sleep(hold)
    btnEnter.click()

    # SELECT PASSPORT
    passport = driver.find_element(By.ID, "rdbTipoDocPas")
    passport.click()

    # ENTER DETAILS
    DNI = driver.find_element(By.ID, "txtIdCitado")
    DNI.send_keys("D983721")

    NAME = driver.find_element(By.ID, "txtDesCitado")
    NAME.send_keys("Dua Lipa")

    Nationality = driver.find_element(By.ID, "txtPaisNac")
    Nationality_O = Select(Nationality)
    Nationality_O.select_by_visible_text("ALBANIA")

    send = driver.find_element(By.ID, "btnEnviar")
    time.sleep(hold)
    send.click()

    # REQUEST APPOINTMENT
    SoliCita = driver.find_element(By.ID, "btnEnviar")
    time.sleep(hold)
    SoliCita.click()

    # IS THERE NEXT? btnSiguiente
    try:
        driver.find_element(By.ID, "btnSiguiente")
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
              "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
              "\n--------  APPOINTMENT AVAILABLE!!!!!!  ---------\n"
              "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
              "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
)
        APPOINTMENT = 1
        time.sleep(300)
        driver.quit()
    except:
        print("\nnot available, will check in", minutes, "minutes")
        APPOINTMENT = 0
        time.sleep(minutes * 60)
        driver.quit()

# END