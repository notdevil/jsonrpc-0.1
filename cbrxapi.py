# Cambrionix Ltd - 2015
# cbrxapi.py
# @version $Id: cbrxapi.py 980 2015-09-23 12:38:06Z arno.brevoort $
#
# This is sample software provided to you without implied warranty of any sort.
# You are free to use and adapt this for your own use.

import jsonrpc

CBRXAPI_ERRORCODE_DROPPED            = -10007
CBRXAPI_ERRORCODE_TIMEOUT            = -10006
CBRXAPI_ERRORCODE_INVALIDHANDLE      = -10005
CBRXAPI_ERRORCODE_ERRORSETTINGVALUE  = -10004
CBRXAPI_ERRORCODE_KEYNOTFOUND        = -10003
CBRXAPI_ERRORCODE_NOHANDLINGTHREAD   = -10002
CBRXAPI_ERRORCODE_IDNOTFOUND         = -10001

CBRXAPI_LISTENINGPORT = -1

try:
    f=open('/usr/local/share/cbrxd/config/listeningport')
    CBRXAPI_LISTENINGPORT = int(f.read())
    f.close
except:
    CBRXAPI_LISTENINGPORT = 43424

cbrxapi = jsonrpc.ServerProxy(
    jsonrpc.JsonRpc20(),
    jsonrpc.TransportTcpIp(addr=("localhost", CBRXAPI_LISTENINGPORT),
    timeout=200.0)
    )
