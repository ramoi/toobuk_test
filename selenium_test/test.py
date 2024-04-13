from toobuk.tb import Toobuk

htb = Toobuk('selenium')  # 설정 파일 test.json, .json은 생략
print(htb.get('getTwinsNews'))
