from flask import Flask, send_file
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary  # Adds chromedriver binary to path

app = Flask(__name__)

# The following options are required to make headless Chrome
# work in a Docker container
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("window-size=2560,1440")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument("--disable-extensions")

# Initialize a new browser
driver = webdriver.Chrome(chrome_options=chrome_options)


@app.route("/")
def hello_world():
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    driver.get("https://www.google.co.th/maps/place/OfficeMate+Rangsit+Branch/@13.9930123,100.6145012,18z/data=!3m1!5s0x30e281d8ceff72fb:0xd4532d963ac8c9c9!4m14!1m7!3m6!1s0x30e299865e94f839:0x6c2fe07e58637d60!2sFuture+Park+Rangsit!8m2!3d13.9891667!4d100.6180717!16s%2Fm%2F0274j04!3m5!1s0x30e281d9a35caf89:0x7ffe149408aa1fae!8m2!3d13.9919169!4d100.6158406!16s%2Fg%2F11g9dbwxkr!5m1!1e1")
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, 'q2sIQ')))
    driver.implicitly_wait(30)
    driver.find_element(By.CLASS_NAME,"gYkzb").click()
    driver.implicitly_wait(30)
    driver.save_screenshot("screen.png")
    return send_file("screen.png")