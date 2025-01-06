from toobuk import Toobuk
import util as ut

htb = Toobuk('for') #설정 파일 test.json, .json은 생략
ut.pprint( htb.get('paging') )
# ut.pprint( htb.get('multi.param') )
ut.pprint( htb.get('multi.param_paging') )
