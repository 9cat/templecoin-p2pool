import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'c1c1c1c1'.decode('hex')
P2P_PORT = 32581
ADDRESS_VERSION = 65
RPC_PORT = 9081
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'templecoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
#SUBSIDY_FUNC = lambda height: 1*100000000 >> (height + 1)//840000
SUBSIDY_FUNC = lambda height: 1*100000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'TPC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Templecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Templecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.templecoin'), 'templecoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://insight.templecoin.org//block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://insight.templecoin.org/address/'
TX_EXPLORER_URL_PREFIX = 'http://insight.templecoin.org/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//100000000 - 1) #default (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.001e8
