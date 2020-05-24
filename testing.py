from pylogthon.logenv import LogEnv
from pylogthon.logger.stdout import Stdout
from pylogthon.messenger.std import Std

lenv = LogEnv()
log1 = Stdout(name='l1')
log2 = Stdout(name='l2')
mess = Std(lenv, 'm1')

lenv.assign_to_notice(log1)
lenv.assign_to_info(log2)
lenv.assign_to_debug(log1)
lenv.assign_to_debug(log2)
