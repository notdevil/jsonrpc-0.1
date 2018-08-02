# Cambrionix Ltd - 2015
# test_jsonrpc_dictionary.py
# @version $Id: test_jsonrpc_dictionary.py 1431 2017-02-08 09:58:08Z andrew.goodbody $
#
# This is sample software provided to you without implied warranty of any sort.
# You are free to use and adapt this for your own use.

# Note: the dictionary test has to run against a special build of cbrxd.
#       It will fail against the release build. 

import jsonrpc
import sys
import time
import unittest
from cbrxapi import cbrxapi

class TestDictionary(unittest.TestCase):
  handle = 0
  device = ""
  
  def setUp(self):
      TestDictionary.handle = cbrxapi.cbrx_connection_open(TestDictionary.device)

  def tearDown(self):
      cbrxapi.cbrx_connection_close(TestDictionary.handle)
      
  def test_get_nrOfPorts(self):
      # nrOfPorts : 8
      tag="nrOfPorts"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 8)

  def test_get_SystemTitle(self):
      # SystemTitle : cambrionix U8S-EXT 8 Port USB Charge+Sync
      tag="SystemTitle"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, "cambrionix U8S-EXT 8 Port USB Charge+Sync")
      
  def test_get_Hardware(self):
      # Hardware: U8S-EXT
      tag="Hardware"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, "U8S-EXT")
      
  def test_get_Firmware(self):
      # Firmware: 1.55
      tag="Firmware"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, "1.55")
      
  def test_get_Compiled(self):
      # Compiled : Jul 08 2015 10:43:20
      tag="Compiled"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, "Jul 08 2015 10:43:20")
      
  def test_get_Group(self):
      # Group : -
      tag="Group"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, "-")
      
  def test_get_PanelID(self):
      # PanelID: Absent
      tag="PanelID"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, "Absent")
      
  def test_get_lcdPresent(self):
      # lcdPresent: true
      tag="lcdPresent"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, True)
  
#  def test_get_Port_X_VID(self):
#      # Port.1.VID : 0
#      tag="Port.1.VID"
#      print tag
#      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
#      print value
#      self.assertEqual(value, 0)
   
# def test_get_Port_X_PID(self):
#      # Port.2.PID : 0
#      tag="Port.2.PID"
#      print tag
#      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
#      print value
#      self.assertEqual(value, 0)
 
  def test_get_Port_X_Current_mA(self):
      # Port.3.Current_mA
      tag="Port.3.Current_mA"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 0)
  
  def test_get_Port_X_Flags(self):
      # Port.4.Flags: R D S
      tag="Port.4.Flags"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, " R D S")
  
  def test_get_Port_X_ProfileID(self):
      # Port.5.ProfileID: 0
      tag="Port.5.ProfileID"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 0)
  
  def test_get_Port_X_TimeCharging_sec(self):
      # Port.6.TimeCharging_sec: 0
      tag="Port.6.TimeCharging_sec"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 0)
  
  def test_get_Port_X_TimeCharged_sec(self):
      # Port.7.TimeCharged_sec: -1
      tag="Port.7.TimeCharged_sec"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, -1)
  
  def test_get_Port_X_Energy_Wh(self):
      # Port.8.Energy_Wh: 0.0
      tag="Port.8.Energy_Wh"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 0.0)
  
  def test_get_TotalCurrent_mA(self):
      # TotalCurrent_mA: 0
      tag="TotalCurrent_ma"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 0)
      
  def test_get_Uptime_sec(self):
      # Uptime_sec : 151304.0
      tag="Uptime_sec"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 151304.0)
      
  def test_get_FiveVoltRail_V(self):
      # FiveVoltRail_V : 5.23
      tag="FiveVoltRail_V"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 5.23)
      
  def test_get_FiveVoltRailMin_V(self):
      # FiveVoltRailMin_V : 5.2
      tag="FiveVoltRailMin_V"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 5.20)
      
  def test_get_FiveVoltRailMax_V(self):
      # FiveVoltRailMax_V : 5.25
      tag="FiveVoltRailMax_V"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 5.25)
      
  def test_get_FiveVoltRail_Flags(self):
      # FiveVoltRail_Flags : 
      tag="FiveVoltRail_Flags"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, "")

  def test_get_TwelveVoltRail_V(self):
      # TwelveVoltRail_V : 12.43
      tag="TwelveVoltRail_V"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 12.43)

  def test_get_TwelveVoltRailMin_V(self):
      # TwelveVoltRailMin_V : 12.31
      tag="TwelveVoltRailMin_V"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 12.31)

  def test_get_TwelveVoltRailMax_V(self):
      # TwelveVoltRailMax_V : 12.52
      tag="TwelveVoltRailMax_V"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 12.52)

  def test_get_TwelveVoltRail_flags(self):
      # TwelveVoltRail_flags : 
      tag="TwelveVoltRail_flags"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, "")

  def test_get_Temperature_C(self):
      # Temperature_C : 37.7
      tag="Temperature_C"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 37.70)

  def test_get_TemperatureMax_C(self):
      # TemperatureMax_C : 39.9
      tag="TemperatureMax_C"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 39.90)

  def test_get_Temperature_flags(self):
      # Temperature_flags : 
      tag="Temperature_flags"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, "")

  def test_get_pwm_percent(self):
      # pwm_percent : 0.0
      tag="pwm_percent"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 0)

  def test_get_Rebooted(self):
      # Rebooted : True
      tag="Rebooted"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, True)

  def test_get_HostPresent(self):
      # HostPresent : True
      tag="HostPresent"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, True)

  def test_get_ModeChangeAuto(self):
      # ModeChangeAuto : True
      tag="ModeChangeAuto"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, True)
  
  def test_get_FiveVoltRail_Limit_Min_V(self):
      # FiveVoltRail_Limit_Min_V : 3.5
      tag="FiveVoltRail_Limit_Min_V"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 3.5)

  def test_get_FiveVoltRail_Limit_Max_V(self):
      # FiveVoltRail_Limit_Max_V : 5.58
      tag="FiveVoltRail_Limit_Max_V"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 5.58)

  def test_get_TwelveVoltRail_Limit_Min_V(self):
      # TwelveVoltRail_Limit_Min_V : 9.59
      tag="TwelveVoltRail_Limit_Min_V"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 9.59)

  def test_get_TwelveVoltRail_Limit_Max_V(self):
      # TwelveVoltRail_Limit_Max_V : 14.5
      tag="TwelveVoltRail_Limit_Max_V"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 14.5)

  def test_get_Temperature_Limit_Max_C(self):
      # Temperature_Limit_Max_C : 65.0
      tag="Temperature_Limit_Max_C"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, 65.0)
  
  def test_get_Profile_1_enabled(self):
      # Profile.1.enabled : False
      tag="Profile.1.enabled"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, False)

  def test_get_Profile_2_enabled(self):
      # Profile.2.enabled : False
      tag="Profile.2.enabled"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, False)

  def test_get_Profile_3_enabled(self):
      # Profile.3.enabled : False
      tag="Profile.3.enabled"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, False)

  def test_get_Profile_4_enabled(self):
      # Profile.4.enabled : False
      tag="Profile.4.enabled"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, False)

  def test_get_Profile_5_enabled(self):
      # Profile.5.enabled : False
      tag="Profile.5.enabled"
      print tag
      value = cbrxapi.cbrx_connection_get(TestDictionary.handle, tag)
      print value
      self.assertEqual(value, False)      

if __name__ == '__main__':

    # find first local cambrionix device
    result = cbrxapi.cbrx_discover("local")
    if result:
        TestDictionary.device = result[0]
    else:
        TestDictionary.device = False

    if not TestDictionary.device:
        print "No device found, cannot run test"
        sys.exit()

    TestDictionary.handle = cbrxapi.cbrx_connection_open(TestDictionary.device)
    cbrxapi.cbrx_connection_getdictionary(TestDictionary.handle)
    cbrxapi.cbrx_connection_close(TestDictionary.handle)

    print "Running tests"
    
    unittest.main()
