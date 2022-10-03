from selenium import webdriver


class Chrome():
    def chrome_init(self):
        driver = webdriver.Chrome(executable_path="G:\\python\\Drivers\\chromedriver_win32 (2)\\chromedriver.exe")
        driver.get("https://www.google.com/")
        driver.close()

abcd = Chrome()
abcd.chrome_init()