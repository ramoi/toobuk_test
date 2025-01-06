from selenium import webdriver
from selenium.webdriver.common.by import By
from toobuk.connector_v1 import AbstractConnector
from toobuk.tlogger import TLoggerFactory
from bs4 import BeautifulSoup

logger = TLoggerFactory.getLogger()


class SeleniumConnector(AbstractConnector):

    def connect(self, url):
        # 이게 pc에 설치되어있는 chrome을 제어하는거라서 그냥 실행시키면 창이 나오고
        # 입력되고 하는게 다 보인다.
        # headless option을 주어서 background에서 실행이 되도록 하자
        driver_options = webdriver.ChromeOptions()
        driver_options.add_argument("headless")
        driver = webdriver.Chrome()
        driver.get(url)
        bs = BeautifulSoup(driver.page_source, self._json_['bs.type'],
                           from_encoding='utf-8' if self._json_.get('encoding') is None else self._json_['encoding'])
        # 잊지말고 동작이 끝나면 driver을 종료할것!
        driver.quit()

        return bs


class SeleniumLoopConnector(AbstractConnector):

    def connect(self, url, headers, parameter):

        # 이게 pc에 설치되어있는 chrome을 제어하는거라서 그냥 실행시키면 창이 나오고
        # 입력되고 하는게 다 보인다.
        # headless option을 주어서 background에서 실행이 되도록 하자
        driver_options = webdriver.ChromeOptions()
        driver_options.add_argument("headless")
        driver = webdriver.Chrome()
        driver.get(url)

        # while True :
        for i in range(10):
            print('idx==================>>', i)
            bs = BeautifulSoup(driver.page_source,  self._bsType_, from_encoding=self._encoding_ )
            dateList = bs.select('.newsContents  .tit_section')

            if len(dateList) > 3:
                # driver.execute_script("""
                # document.querySelector('.newsContents .head_section:nth-child(n+2) + .list_newsinfo').remove();
                # """)
                # bs = BeautifulSoup(driver.page_source, self._json_['bs.type'],
                #                    from_encoding='utf-8' if self._json_.get('encoding') is None else self._json_[
                #                        'encoding'])

                return bs
            driver.find_element(By.CSS_SELECTOR, '#newsListMore').click()

        # 잊지말고 동작이 끝나면 driver을 종료할것!
        driver.quit()
        return bs

    def afterConnect(self, bs):
        # print(bs)
        # for e in bs.select('.newsContents .head_section:nth-child(n+2) + .list_newsinfo'):
        #     e.decompose()

        return bs
