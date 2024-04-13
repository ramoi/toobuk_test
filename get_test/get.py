from toobuk.tb import Toobuk

htb = Toobuk('test') #설정 파일 test.json, .json은 생략
print( htb.get('housetrade') )