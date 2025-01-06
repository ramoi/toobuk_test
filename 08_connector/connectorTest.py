from urllib.request import urlopen
from toobuk.connector_v1 import AbstractConnector
from toobuk.tlogger import TLoggerFactory
from bs4 import BeautifulSoup

logger = TLoggerFactory.getLogger()


class CustomGetConnector(AbstractConnector):
    def beforeConnect(self, headers, parameter):
        logger.debug(parameter)

    def afterConnect(self, bs):
        logger.debug(bs)
        return bs

    def connect(self, url, headers, parameter):
        html = urlopen(url)
        logger.debug(html)

        bs = BeautifulSoup(html, self._bsType_, from_encoding=self._encoding_ )

        return bs

