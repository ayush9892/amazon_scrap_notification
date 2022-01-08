from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


class AUTO_UP():
    stop = 0

    def Auto_update(self):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get('http://127.0.0.1:8000/')
        time.sleep(7)

        while(True):
            if(self.stop == 1):
                browser.close()
                break

            button = browser.find_element_by_link_text('Update')
            button.click()

            time.sleep(13)
            


class fst_chk():
    fst_val = 0     # Static val.
    html_upt_chk = 1
    html_stp_chk = 0
    