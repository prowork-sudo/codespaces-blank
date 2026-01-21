from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def createTxtFile(fileName, copied_text):
    if not fileName.endswith(".txt"):
        fileName += ".txt"
    with open(fileName, 'w', encoding="utf-8") as file:
        file.write(copied_text)

def logIn():
    driver.find_element(By.ID, "idcs-signin-basic-signin-form-username").send_keys("HCM.UserTech2")
    driver.find_element(By.ID, "idcs-signin-basic-signin-form-password").send_keys("Welcome2a")
    driver.find_element(By.ID, "ui-id-4").click()

def GlobalSearchNav():
    driver.find_element(By.ID, "pt1:_UIShome::icon").click()
    time.sleep(5)
    driver.find_element(By.ID, "pt1:_UIScmil2u").click()
    time.sleep(5)
    driver.find_element(By.ID, "pt1:_UIScmi4").click()
    time.sleep(5)
    driver.find_element(By.ID, "pt1:r1:0:r0:0:r1:0:AP1:sdi10::disAcr").click()
    time.sleep(5)
    driver.find_element(By.ID, "pt1:r1:0:r0:0:r1:0:AP1:r10:0:i3:7:cl11").click()

# ---- Configure Chrome Options ----
options = Options()
options.page_load_strategy = 'eager'   # 'normal' (default), 'eager', or 'none'
# options.add_argument("--headless=new")  # <-- uncomment if you want headless mode
# options.add_argument("--start-maximized")

url = "https://fa-esfe-dev19-saasfademo1.ds-fa.oraclepdemos.com"
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(10)

logIn()
time.sleep(8)
GlobalSearchNav()
time.sleep(10)
FastFormulaList = ["Absence and Calculation Card Details","Absence and Calculation Card Details"]

# search Fast Formulas
search_box = driver.find_element(By.ID, "pt1:r1:0:r0:1:AP1:s9:it1::content")
search_box.send_keys("Fast Formulas")
time.sleep(3)
search_box.send_keys(Keys.ENTER)
time.sleep(4)
driver.find_element(By.ID, "pt1:r1:0:r0:1:AP1:t1:1:cl2").click()
time.sleep(5)

for index in range(len(FastFormulaList)):

    # search Absence and Calculation Card Details
    driver.find_element(By.ID, "pt1:r1:0:rt:1:r2:0:dynamicRegion1:0:ap1:q1:value00::content").send_keys(FastFormulaList[index])
    driver.find_element(By.ID, "pt1:r1:0:rt:1:r2:0:dynamicRegion1:0:ap1:q1::search").click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//a[text()="Absence and Calculation Card Details"]').click()

    # extract text
    textarea_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'pt1:r1:0:rt:1:r2:0:dynamicRegion1:1:AP2:Manua1:0:richTextEditor1::content'))
    )

    copied_text = textarea_element.text   # Oracle rich text editor content
    print(f"Text copied from textarea: {copied_text}")

    # save to file
    createTxtFile("Absence and Calculation Card Details", copied_text)

    driver.find_element(By.ID, "pt1:r1:0:rt:1:r2:0:dynamicRegion1:1:AP2:activeCommandToolbarButton5").click()

time.sleep(1000)
