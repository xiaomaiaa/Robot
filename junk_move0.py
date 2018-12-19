#!/usr/bin/env python
from junk_move_util import *

junk_num=3
for junk_id in xrange(junk_num):
    a=jm(junk_id)
    a.do()