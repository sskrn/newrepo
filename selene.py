from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# opt.add_argument("--headless")
opt.add_argument("--window-size=1920x1080")
opt.add_argument("--use-fake-ui-for-media-stream") 
# opt.add_argument("--no-sandbox")
# opt.add_argument('--disable-dev-shm-usage')
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })

driver = webdriver.Chrome(chrome_options=opt, executable_path=r'/usr/bin/chromedriver')

driver.get("https://test.widyaimersif.com")

room = driver.find_element_by_id("roomName")
room.send_keys("1234")

username = driver.find_element_by_id("userName")
username.send_keys("PC")

buton = driver.find_element_by_xpath('//*[@id="root"]/div/div/button')
buton.click()

# capture the screen
driver.get_screenshot_as_file("capture.png")

# driver.implicitly_wait(3600)
# driver.close()
# driver.quit()

try:
  tunggu = WebDriverWait(driver,3600).until(
    # element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
  driver.get_screenshot_as_file("capture2.png")
  # driver.close()
  driver.quit()
