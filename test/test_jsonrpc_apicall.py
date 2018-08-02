# Cambrionix Ltd - 2015
# test_jsonrpc_apicall.py
# @version $Id: test_jsonrpc_apicall.py 1431 2017-02-08 09:58:08Z andrew.goodbody $
#
# This is sample software provided to you without implied warranty of any sort.
# You are free to use and adapt this for your own use.

# create JSON-RPC client
import jsonrpc
import sys
import time
import unittest
from cbrxapi import cbrxapi

JSONRPC_ERRORCODE_INVALIDPARAMETERS = -32602
JSONRPC_ERRORCODE_UNKNOWNMETHOD = -32601

CBRXAPI_ERRORCODE_TIMEOUT = -10006
CBRXAPI_ERRORCODE_INVALIDHANDLE = -10005
CBRXAPI_ERRORCODE_ERRORSETTINGVALUE = -10004
CBRXAPI_ERRORCODE_KEYNOTFOUND = -10003
CBRXAPI_ERRORCODE_NODEVICETHREAD = -10002
CBRXAPI_ERRORCODE_IDNOTFOUND = -10001

handle = ""
device = ""
noDevicePlugging = True

class TestApiMethods(unittest.TestCase):


  def test015_cbrx_cbrx_discover_id_to_os_reference(self):
      print "\ntest015_cbrx_discover_id_to_os_reference",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      os_reference = cbrxapi.cbrx_discover_id_to_os_reference(device)
      self.assertNotEqual( os_reference, "")
      self.assertNotEqual( os_reference, False)

      # ensure the os reference returned starts with "COM" or "/dev"
      valid_reference = False

      print device,
      print "=",
      print os_reference,
      print " ",
      
      if os_reference.startswith('COM'):
        valid_reference = True

      if os_reference.startswith('/dev/'):
        valid_reference = True
        
      self.assertEqual( valid_reference, True)
            

  def test014_discover_empty(self):
      print "\ntest014_discover_emptyname ",

      gotException = False
      errorCode = 0
      result = ""

      try: 
        result = cbrxapi.cbrx_discover("")
      except jsonrpc.RPCFault as e:
        gotException = True
        errorCode = e.error_code

      self.assertEqual( gotException, True)
      self.assertEqual( errorCode, JSONRPC_ERRORCODE_INVALIDPARAMETERS)


  def test013_discover_invalidname(self):
      print "\ntest013_discover_invalidname ",

      gotException = False
      errorCode = 0
      result = ""

      try: 
        result = cbrxapi.cbrx_discover("INVALID")
      except jsonrpc.RPCFault as e:
        gotException = True
        errorCode = e.error_code

      self.assertEqual( gotException, True)
      self.assertEqual( errorCode, JSONRPC_ERRORCODE_INVALIDPARAMETERS)


  def test012_discover_getresult_two_devices(self):
      print "\ntest012_discover_getresult_two_devices ",
      if noDevicePlugging:
        print "Test skipped ",
        return
      
      raw_input("Connect two devices, press Enter to continue...")
      
      result = cbrxapi.cbrx_discover("local")
      self.assertEqual( len(result), 2 )

      device = False
      for i in range(len(result)):
        device = result[i]
        self.assertNotEqual(device, "")
        print device
                          
      self.assertNotEqual( device, False )

      raw_input("Remove one device, keeping one device connected, press Enter to continue...")
      
      result = cbrxapi.cbrx_discover("local")
      self.assertEqual( len(result), 1 )

      device = False
      for i in range(len(result)):
        device = result[i]
        self.assertNotEqual(device, "")
        print device
                          
      self.assertNotEqual( device, False )


  def test011_discover_getresult_no_device(self):
      print "\ntest011_discover_getresult ",
      if noDevicePlugging:
        print "Test skipped ",
        return

      raw_input("Disconnect all devices, press Enter to continue...")
      
      result = cbrxapi.cbrx_discover("local")
      self.assertEqual( result, False )


  def test010_discover_getresult_one_device(self):
      print "\ntest010_discover_getresult_one_device ",
      if noDevicePlugging:
        print "Test skipped ",
        return
      
      raw_input("Connect one device, press Enter to continue...")

      result = cbrxapi.cbrx_discover("local")
      self.assertEqual( len(result), 1 )

      if result:
        device = result[0]
      else:
        device = False

      print device

      self.assertNotEqual( device, False )


  def test009_cbrx_connection_close_device_invalidhandle(self):
      print "\ntest009_cbrx_connection_close_device_invalidhandle ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      handle1 = cbrxapi.cbrx_connection_open(device)
      self.assertNotEqual( handle1, "")
      self.assertNotEqual( handle1, False)

      gotException = False
      errorCode = 0
      result = ""

      try: 
        cbrxapi.cbrx_connection_close("INVALIDHANDLE")
      except jsonrpc.RPCFault as e:
        gotException = True
        errorCode = e.error_code

      self.assertEqual( gotException, True)
      self.assertEqual( errorCode, CBRXAPI_ERRORCODE_INVALIDHANDLE)

      cbrxapi.cbrx_connection_close(handle1)
      

  def test008_cbrx_connection_close_handle_twice(self):
      print "\ntest008_cbrx_connection_close_handle_twice ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      handle1 = cbrxapi.cbrx_connection_open(device)
      self.assertNotEqual( handle1, "")
      self.assertNotEqual( handle1, False)

      cbrxapi.cbrx_connection_close(handle1)
      
      try: 
        cbrxapi.cbrx_connection_close(handle1)
      except jsonrpc.RPCFault as e:
        gotException = True
        errorCode = e.error_code

      self.assertEqual( gotException, True)
      self.assertEqual( errorCode, CBRXAPI_ERRORCODE_INVALIDHANDLE)

      

  def test007_cbrx_connection_open_device_twice(self):
      print "\ntest007_cbrx_connection_open_device_twice ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      handle1 = cbrxapi.cbrx_connection_open(device)
      self.assertNotEqual( handle1, "")
      self.assertNotEqual( handle1, False)
      handle2 = cbrxapi.cbrx_connection_open(device)
      self.assertNotEqual( handle2, "")
      self.assertNotEqual( handle2, False)

      cbrxapi.cbrx_connection_close(handle2)
      cbrxapi.cbrx_connection_close(handle1)
      

  def test006_cbrx_connection_open_baddevice(self):
      print "\ntest006_cbrx_connection_open ",
      device = "baddevice"

      gotException = False
      errorCode = 0
      handle = ""

      try:
        handle = cbrxapi.cbrx_connection_open(device)
      except jsonrpc.RPCFault as e:
        gotException = True
        errorCode = e.error_code

      self.assertEqual( gotException, True)
      self.assertEqual( errorCode, CBRXAPI_ERRORCODE_IDNOTFOUND)      
      self.assertEqual( handle, "")
      self.assertNotEqual( handle, "baddevice")   
      
      
      
  def test005_cbrx_connection_close(self):
      print "\ntest005_cbrx_connection_close ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      handle = cbrxapi.cbrx_connection_open(device)

      result = cbrxapi.cbrx_connection_close(handle)
      self.assertEqual(result, True)


  def test0041_cbrx_connection_set_invalid_tag(self):
      print "\ntest0041_cbrx_connection_set ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      handle = cbrxapi.cbrx_connection_open(device)

      gotException = False
      errorCode = 0
      result = ""

      try: 
        result = cbrxapi.cbrx_connection_set(handle, "INVALID_TAG", "INVALID")
      except jsonrpc.RPCFault as e:
        gotException = True
        errorCode = e.error_code

      print "Result: ",
      print result,
      print " "

      self.assertEqual( gotException, True)
      self.assertEqual( errorCode, CBRXAPI_ERRORCODE_ERRORSETTINGVALUE)
      self.assertEqual( result, "")

      result = cbrxapi.cbrx_connection_close(handle)


  def test0040_cbrx_connection_set(self):
      print "\ntest0040_cbrx_connection_set ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      handle = cbrxapi.cbrx_connection_open(device)
      result = cbrxapi.cbrx_connection_set(handle, "Port.3.mode", "c")

      print "\nResult: ",
      print result
      self.assertEqual(result, True)
      result = cbrxapi.cbrx_connection_close(handle)


  def test0034_cbrx_connection_get_invalid_handle(self):
      print "\ntest0034_cbrx_connection_get_invalid_handle ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      handle = cbrxapi.cbrx_connection_open(device)

      badhandle = "INVALID"
      gotException = False
      errorCode = 0
      result = ""

      try: 
        result = cbrxapi.cbrx_connection_get(badhandle, "nrOfPorts")
      except jsonrpc.RPCFault as e:
        gotException = True
        errorCode = e.error_code

      self.assertEqual( gotException, True)
      self.assertEqual( errorCode, CBRXAPI_ERRORCODE_INVALIDHANDLE)
      self.assertEqual( result, "")

      result = cbrxapi.cbrx_connection_close(handle)


  def test0033_cbrx_connection_get_missing_tag(self):
      print "\ntest0032_cbrx_connection_get_missing_tag ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      handle = cbrxapi.cbrx_connection_open(device)
      gotException = False
      errorCode = 0
      result = ""

      try: 
        result = cbrxapi.cbrx_connection_get(handle)
      except jsonrpc.RPCFault as e:
        gotException = True
        errorCode = e.error_code

      self.assertEqual( gotException, True)
      self.assertEqual( errorCode, JSONRPC_ERRORCODE_INVALIDPARAMETERS)
      self.assertEqual( result, "")

      result = cbrxapi.cbrx_connection_close(handle)


  def test0032_cbrx_connection_get_empty_tag(self):
      print "\ntest0032_cbrx_connection_get_empty_tag ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      handle = cbrxapi.cbrx_connection_open(device)
      
      gotException = False
      errorCode = 0
      result = ""

      try: 
        result = cbrxapi.cbrx_connection_get(handle, "")
      except jsonrpc.RPCFault as e:
        gotException = True
        errorCode = e.error_code

      self.assertEqual( gotException, True)
      self.assertEqual( errorCode, CBRXAPI_ERRORCODE_KEYNOTFOUND)
      self.assertEqual( result, "")

      result = cbrxapi.cbrx_connection_close(handle)


  def test0031_cbrx_connection_get_invalid_tag(self):
      print "\ntest0031_cbrx_connection_get_invalid_tag ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      handle = cbrxapi.cbrx_connection_open(device)
      
      gotException = False
      errorCode = 0
      result = ""

      try: 
        result = cbrxapi.cbrx_connection_get(handle, "INVALID")
      except jsonrpc.RPCFault as e:
        gotException = True
        errorCode = e.error_code

      self.assertEqual( gotException, True)
      self.assertEqual( errorCode, CBRXAPI_ERRORCODE_KEYNOTFOUND)
      self.assertEqual( result, "")

      result = cbrxapi.cbrx_connection_close(handle)


  def test0030_cbrx_connection_get(self):
      print "\ntest0030_cbrx_connection_get ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      handle = cbrxapi.cbrx_connection_open(device)
      result = cbrxapi.cbrx_connection_get(handle, "nrOfPorts")
      self.assertNotEqual(result, 0)
      result = cbrxapi.cbrx_connection_close(handle)


  def test0021_cbrx_connection_getdictionary_invalidhandle(self):
      print "\ntest0021_cbrx_connection_getdictionary_invalidhandle ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      handle = cbrxapi.cbrx_connection_open(device)
      
      badhandle = "INVALID"
      gotException = False
      errorCode = 0
      dictionary = ""

      try: 
        dictionary = cbrxapi.cbrx_connection_getdictionary(badhandle)
      except jsonrpc.RPCFault as e:
        gotException = True
        errorCode = e.error_code
        
      self.assertEqual( gotException, True)
      self.assertEqual( errorCode, CBRXAPI_ERRORCODE_INVALIDHANDLE)
      self.assertEqual( dictionary, "")
      
      cbrxapi.cbrx_connection_close(handle)


  def test0020_cbrx_connection_getdictionary(self):
      print "\ntest0020_cbrx_connection_getdictionary ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      handle = cbrxapi.cbrx_connection_open(device)
      dictionary = cbrxapi.cbrx_connection_getdictionary(handle)
      self.assertNotEqual( dictionary, "")
      self.assertNotEqual( dictionary, False)
      
      handle = cbrxapi.cbrx_connection_close(handle)


  def test0013_cbrx_connection_open_locked_unlocked(self):
      print "\ntest0013_cbrx_connection_open_locked_unlocked ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      gotException = False
      errorCode = 0
      handle = ""

      result = cbrxapi.cbrx_connection_closeandlock(device)
      self.assertEqual( result, True)

      result = cbrxapi.cbrx_connection_unlock(device)
      self.assertEqual( result, True)
      
      try:
        handle = cbrxapi.cbrx_connection_open(device)
      except jsonrpc.RPCFault as e:
        gotException = True
        errorCode = e.error_code

      self.assertEqual( gotException, False)
      self.assertNotEqual( handle, "")


  def test0012_cbrx_connection_open_locked(self):
      print "\ntest0012_cbrx_connection_open_locked ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      gotException = False
      errorCode = 0
      handle = ""

      result = cbrxapi.cbrx_connection_closeandlock(device)
      self.assertEqual( result, True)
      
      try:
        handle = cbrxapi.cbrx_connection_open(device)
      except jsonrpc.RPCFault as e:
        gotException = True
        errorCode = e.error_code

      self.assertEqual( gotException, True)
      self.assertEqual( errorCode, CBRXAPI_ERRORCODE_NODEVICETHREAD)
      self.assertEqual( handle, "")

      result = cbrxapi.cbrx_connection_unlock(device)
      self.assertEqual( result, True)   


  def test0011_cbrx_connection_open_invalid(self):
      print "\ntest0011_cbrx_connection_open_invalid ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      gotException = False
      errorCode = 0
      handle = ""
      
      try:
        handle = cbrxapi.cbrx_connection_open("BADDEVICE")
      except jsonrpc.RPCFault as e:
        gotException = True
        errorCode = e.error_code

      self.assertEqual( gotException, True)
      self.assertEqual( errorCode, CBRXAPI_ERRORCODE_IDNOTFOUND)
      self.assertEqual( handle, "")


  def test0010_cbrx_connection_open_valid(self):
      print "\ntest0010_cbrx_connection_open_valid ",
      result = cbrxapi.cbrx_discover("local")
      if result:
        device = result[0]

      handle = cbrxapi.cbrx_connection_open(device)
      self.assertNotEqual( handle, "")
      self.assertNotEqual( handle, False)
      cbrxapi.cbrx_connection_close(handle)


  def test0000_cbrx_apiversion_valid(self):
      print "\ntest0000_cbrx_apiversion ",
      result = cbrxapi.cbrx_apiversion()
#      print "result"
#      print result

#      print "major "
      major = result[0]
#      print major

#      print "minor "
      minor = result[1]
#      print minor
          
      self.assertEqual( major, 1)
      self.assertEqual( minor, 0)
      

if __name__ == '__main__':
    if noDevicePlugging:
      print "Skipping device unplugging / plugging back in tests"
    else:
      raw_input("Make sure a Cambrionix device is plugged in. Press Enter to continue...")

    result = cbrxapi.cbrx_discover("local")
    if result:
      device = result[0]
        
    if device == "":
      print "Can't find Cambrionix unit."
      sys.exit(-1)

    try:
      unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised if tests failed
          raise
        

    
