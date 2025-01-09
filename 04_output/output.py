from toobuk import Toobuk
import util as ut

htb = Toobuk('output')

print("특정 output 하나")
ut.pprint( htb.grumble('housetrade/date') )

print(" output 여러개")
ut.pprint( htb.grumble('housetrade/date&changeRate') )

print(" output 전체")
ut.pprint( htb.grumble('housetrade') )

print(" output 속성")
ut.pprint( htb.grumble('attrList') )
