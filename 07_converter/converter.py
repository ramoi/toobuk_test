from toobuk import Toobuk
import util as ut
from toobuk.pattern.abstract import Converter
import func as fn

Converter.addConverter("dateformat", fn.dateformat)

htb = Toobuk('converter')
ut.pprint(htb.get('trade'))
