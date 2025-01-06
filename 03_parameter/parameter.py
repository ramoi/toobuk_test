from toobuk import Toobuk
import util as ut

htb = Toobuk('parameter')

print("파라메터 없는 경우")
ut.pprint( htb.grumble('empty.param') )

print('설정파일을 통해서 파라메터 넘기기')
ut.pprint( htb.grumble('get') )
ut.pprint( htb.grumble('post') )

print('소스에서 파라메터 넘기기')
parameter = {
    "searchKeyword": "주택",
    "searchCondition": "subject"
}
ut.pprint( htb.grumble('empty.param', parameter) )
