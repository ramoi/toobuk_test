from toobuk import Toobuk
from toobuk.conf import ConnetManager
from connectorTest import CustomGetConnector

print("connector를 등록한다.")
ConnetManager.addConnector("customGet", CustomGetConnector)

htb = Toobuk('connectorTest')
print(htb.grumble('housetrade'))

print(htb.grumble('housetrade2'))