# Cambrionix Ltd - 2015
# test_jsonrpc_api.py
# @version $Id: test_jsonrpc_api.py 1431 2017-02-08 09:58:08Z andrew.goodbody $
#
# This is sample software provided to you without implied warranty of any sort.
# You are free to use and adapt this for your own use.

import jsonrpc
import sys
import time
from cbrxapi import cbrxapi

print "cbrx_discover"
result = cbrxapi.cbrx_discover("local")
print result

if result:
    device = result[0]
else:
    device = False

print "---"

if not device:
    print "No device found."
    sys.exit()

unitId = result[0]
cbrxapi.cbrx_connection_closeandlock(unitId)
cbrxapi.cbrx_connection_unlock(unitId)

print "cbrx_connection_open"
handle = cbrxapi.cbrx_connection_open(device)
print handle

print "cbrx_connection_getdictionary"
dictionary = cbrxapi.cbrx_connection_getdictionary(handle)
print dictionary

print "cbrx_connection_setdictionary"
dictionary = cbrxapi.cbrx_connection_setdictionary(handle)
print dictionary

what = "nrOfPorts"
nrOfPorts = cbrxapi.cbrx_connection_get(handle, what)
print "cbrx_connection_get " + what + ": " + str(nrOfPorts)

what = "Port.1.Current_mA"
result = cbrxapi.cbrx_connection_get(handle, what)
print "cbrx_connection_get " + what + ": " + str(result)

what = "Port.1.PID"
result = cbrxapi.cbrx_connection_get(handle, what)
print "cbrx_connection_get " + what + ": " + str(result)

what = "Port.1.VID"
result = cbrxapi.cbrx_connection_get(handle, what)
print "cbrx_connection_get " + what + ": " + str(result)

what = "Rebooted"
result = cbrxapi.cbrx_connection_get(handle, what, False)
print "cbrx_connection_get " + what + ": " + str(result)

# --

what = "FiveVoltRail.OverVoltage"
result = cbrxapi.cbrx_connection_set(handle, what, True)
print "cbrx_connection_set " + what + ": " + str(result)

what = "FiveVoltRail_flags"
result = cbrxapi.cbrx_connection_get(handle, what)
print "cbrx_connection_get " + what + ": " + str(result)

what = "FiveVoltRail.UnderVoltage"
result = cbrxapi.cbrx_connection_set(handle, what, True)
print "cbrx_connection_set " + what + ": " + str(result)

what = "FiveVoltRail_flags"
result = cbrxapi.cbrx_connection_get(handle, what)
print "cbrx_connection_get " + what + ": " + str(result)

# --

what = "TwelveVoltRail.OverVoltage"
result = cbrxapi.cbrx_connection_set(handle, what, True)
print "cbrx_connection_set " + what + ": " + str(result)

what = "TwelveVoltRail_flags"
result = cbrxapi.cbrx_connection_get(handle, what)
print "cbrx_connection_get " + what + ": " + str(result)

what = "TwelveVoltRail.UnderVoltage"
result = cbrxapi.cbrx_connection_set(handle, what, True)
print "cbrx_connection_set " + what + ": " + str(result)

what = "TwelveVoltRail_flags"
result = cbrxapi.cbrx_connection_get(handle, what)
print "cbrx_connection_get " + what + ": " + str(result)

# --

what = "Temperature.OverTemperature"
result = cbrxapi.cbrx_connection_set(handle, what, True)
print "cbrx_connection_set " + what + ": " + str(result)

what = "Temperature_flags"
result = cbrxapi.cbrx_connection_get(handle, what)
print "cbrx_connection_get " + what + ": " + str(result)

# --

what = "ClearErrorFlags"
result = cbrxapi.cbrx_connection_set(handle, what, True)
print "cbrx_connection_set " + what + ": " + str(result)

# --

what = "Mode"
result = cbrxapi.cbrx_connection_set(handle, what, "s")
print "cbrx_connection_set " + what + ": " + str(result)

# --

what = "TwelveVoltRail_flags"
result = cbrxapi.cbrx_connection_get(handle, what)
print "cbrx_connection_get " + what + ": " + str(result)

what = "FiveVoltRail_flags"
result = cbrxapi.cbrx_connection_get(handle, what)
print "cbrx_connection_get " + what + ": " + str(result)

what = "Temperature_flags"
result = cbrxapi.cbrx_connection_get(handle, what)
print "cbrx_connection_get " + what + ": " + str(result)

# print "cbrx_connection_getdictionary"
# dictionary = cbrxapi.cbrx_connection_getdictionary(handle)
# print dictionary

# for key in dictionary:
#   print key, "=", 
#   value = cbrxapi.cbrx_connection_get(handle, key)
#   print value, "; ",

print

# what = "Reboot"
# result = cbrxapi.cbrx_connection_set(handle, what, True)
# print "cbrx_connection_set " + what + ": " + str(result)

print "cbrx_connection_close"
result = cbrxapi.cbrx_connection_close(handle)
print result
