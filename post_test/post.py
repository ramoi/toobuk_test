from toobuk import Toobuk
import util as ut

htb = Toobuk('post') #설정 파일 test.json, .json은 생략
ut.pprint( htb.get('qa') )