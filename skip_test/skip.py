from toobuk import Toobuk
import util as ut
from toobuk.pattern.list import Skipper
import func as fn

Skipper.addSkipper('space', fn.isSpace )
htb = Toobuk('skip1')
ut.pprint(htb.get('trade'))
