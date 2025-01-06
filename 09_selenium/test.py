from toobuk import Toobuk

htb = Toobuk('selenium')  # 설정 파일 test.json, .json은 생략
newsList = htb.get('getTwinsNews')['station']
print(len(newsList))
print(newsList)
