from toobuk import Toobuk
import util as ut

htb = Toobuk('post') #설정 파일 post.json, .json은 생략
ut.pprint( htb.grumble('qa') )
ut.pprint( htb.grumble('multi.param') )
