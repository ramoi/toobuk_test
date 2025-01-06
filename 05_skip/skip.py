from toobuk import Toobuk
import util as ut
from toobuk.pattern.list import Skipper
import func as fn

Skipper.addSkipper('skipJan', fn.skipJan )
htb = Toobuk('skip1')
ut.pprint(htb.get('trade'))
