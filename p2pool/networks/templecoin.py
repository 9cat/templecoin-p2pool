from p2pool.bitcoin import networks

PARENT = networks.nets['templecoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'e03255b8c6923410'.decode('hex')
PREFIX = '7238c1a53ef629b0'.decode('hex')
P2P_PORT = 19325
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 19327
BOOTSTRAP_ADDRS = 'seed.templecoin.org seed.templecoin.com'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-tpc'
VERSION_CHECK = lambda v: True
VERSION_WARNING = lambda v: 'Upgrade Templecoin to >=2.8.7.1!' if v < 2080701 else None
