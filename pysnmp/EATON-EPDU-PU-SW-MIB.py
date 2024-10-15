# SNMP MIB module (EATON-EPDU-PU-SW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EATON-EPDU-PU-SW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:21 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

pulizzi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20677)
)
pulizzi.setRevisions(
        ("2009-10-16 12:00",
         "2008-12-22 12:00",
         "2008-02-13 12:00",
         "2006-05-01 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ipv3600_ObjectIdentity = ObjectIdentity
ipv3600 = _Ipv3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2)
)
_UnitConfig_ObjectIdentity = ObjectIdentity
unitConfig = _UnitConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 1)
)


class _UnitName_Type(OctetString):
    """Custom type unitName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_UnitName_Type.__name__ = "OctetString"
_UnitName_Object = MibScalar
unitName = _UnitName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 1, 1),
    _UnitName_Type()
)
unitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitName.setStatus("current")


class _StrappingId_Type(Integer32):
    """Custom type strappingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_StrappingId_Type.__name__ = "Integer32"
_StrappingId_Object = MibScalar
strappingId = _StrappingId_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 1, 2),
    _StrappingId_Type()
)
strappingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strappingId.setStatus("current")


class _UnitTime_Type(OctetString):
    """Custom type unitTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_UnitTime_Type.__name__ = "OctetString"
_UnitTime_Object = MibScalar
unitTime = _UnitTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 1, 3),
    _UnitTime_Type()
)
unitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTime.setStatus("current")


class _UnitDate_Type(OctetString):
    """Custom type unitDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_UnitDate_Type.__name__ = "OctetString"
_UnitDate_Object = MibScalar
unitDate = _UnitDate_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 1, 4),
    _UnitDate_Type()
)
unitDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitDate.setStatus("current")


class _UnitDayOfWeek_Type(Integer32):
    """Custom type unitDayOfWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_UnitDayOfWeek_Type.__name__ = "Integer32"
_UnitDayOfWeek_Object = MibScalar
unitDayOfWeek = _UnitDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 1, 5),
    _UnitDayOfWeek_Type()
)
unitDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitDayOfWeek.setStatus("current")


class _VaLoggingInterval_Type(Integer32):
    """Custom type vaLoggingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("fifteenminutes", 2),
          ("fiveminutes", 1),
          ("hourly", 3))
    )


_VaLoggingInterval_Type.__name__ = "Integer32"
_VaLoggingInterval_Object = MibScalar
vaLoggingInterval = _VaLoggingInterval_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 1, 6),
    _VaLoggingInterval_Type()
)
vaLoggingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vaLoggingInterval.setStatus("current")
_LoginTimeout_Type = Integer32
_LoginTimeout_Object = MibScalar
loginTimeout = _LoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 1, 7),
    _LoginTimeout_Type()
)
loginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginTimeout.setStatus("current")


class _InvertDisplay_Type(Integer32):
    """Custom type invertDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 1),
          ("normal", 0))
    )


_InvertDisplay_Type.__name__ = "Integer32"
_InvertDisplay_Object = MibScalar
invertDisplay = _InvertDisplay_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 1, 8),
    _InvertDisplay_Type()
)
invertDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invertDisplay.setStatus("current")


class _FahrenheitOrCelsius_Type(Integer32):
    """Custom type fahrenheitOrCelsius based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 0))
    )


_FahrenheitOrCelsius_Type.__name__ = "Integer32"
_FahrenheitOrCelsius_Object = MibScalar
fahrenheitOrCelsius = _FahrenheitOrCelsius_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 1, 9),
    _FahrenheitOrCelsius_Type()
)
fahrenheitOrCelsius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fahrenheitOrCelsius.setStatus("current")
_NetworkSettings_ObjectIdentity = ObjectIdentity
networkSettings = _NetworkSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 2)
)
_UnitIPAddress_Type = IpAddress
_UnitIPAddress_Object = MibScalar
unitIPAddress = _UnitIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 2, 1),
    _UnitIPAddress_Type()
)
unitIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitIPAddress.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 2, 2),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 2, 3),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("current")
_WebPort_Type = Integer32
_WebPort_Object = MibScalar
webPort = _WebPort_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 2, 4),
    _WebPort_Type()
)
webPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webPort.setStatus("current")


class _WebEnabled_Type(Integer32):
    """Custom type webEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WebEnabled_Type.__name__ = "Integer32"
_WebEnabled_Object = MibScalar
webEnabled = _WebEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 2, 5),
    _WebEnabled_Type()
)
webEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webEnabled.setStatus("current")


class _MacAddress_Type(OctetString):
    """Custom type macAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MacAddress_Type.__name__ = "OctetString"
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 2, 6),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")


class _EnablePing_Type(Integer32):
    """Custom type enablePing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EnablePing_Type.__name__ = "Integer32"
_EnablePing_Object = MibScalar
enablePing = _EnablePing_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 2, 7),
    _EnablePing_Type()
)
enablePing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablePing.setStatus("current")


class _PingInterval_Type(Integer32):
    """Custom type pingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_PingInterval_Type.__name__ = "Integer32"
_PingInterval_Object = MibScalar
pingInterval = _PingInterval_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 2, 8),
    _PingInterval_Type()
)
pingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingInterval.setStatus("current")
_LogManagerConfig_ObjectIdentity = ObjectIdentity
logManagerConfig = _LogManagerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3)
)
_MailServerIPAddress_Type = IpAddress
_MailServerIPAddress_Object = MibScalar
mailServerIPAddress = _MailServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 1),
    _MailServerIPAddress_Type()
)
mailServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailServerIPAddress.setStatus("current")
_SendLogFrom_Type = OctetString
_SendLogFrom_Object = MibScalar
sendLogFrom = _SendLogFrom_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 2),
    _SendLogFrom_Type()
)
sendLogFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendLogFrom.setStatus("current")
_SendLogToUser1Address_Type = OctetString
_SendLogToUser1Address_Object = MibScalar
sendLogToUser1Address = _SendLogToUser1Address_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 3),
    _SendLogToUser1Address_Type()
)
sendLogToUser1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendLogToUser1Address.setStatus("current")
_SendLogToUser2Address_Type = OctetString
_SendLogToUser2Address_Object = MibScalar
sendLogToUser2Address = _SendLogToUser2Address_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 4),
    _SendLogToUser2Address_Type()
)
sendLogToUser2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendLogToUser2Address.setStatus("current")
_SendAlertsToUser1Address_Type = OctetString
_SendAlertsToUser1Address_Object = MibScalar
sendAlertsToUser1Address = _SendAlertsToUser1Address_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 5),
    _SendAlertsToUser1Address_Type()
)
sendAlertsToUser1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendAlertsToUser1Address.setStatus("current")
_SendAlertsToUser2Address_Type = OctetString
_SendAlertsToUser2Address_Object = MibScalar
sendAlertsToUser2Address = _SendAlertsToUser2Address_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 6),
    _SendAlertsToUser2Address_Type()
)
sendAlertsToUser2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendAlertsToUser2Address.setStatus("current")


class _SendLogFrequency_Type(Integer32):
    """Custom type sendLogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("daily", 8),
          ("never", 10),
          ("weeklyOnFriday", 6),
          ("weeklyOnMonday", 2),
          ("weeklyOnSaturday", 7),
          ("weeklyOnSunday", 1),
          ("weeklyOnThursday", 5),
          ("weeklyOnTuesday", 3),
          ("weeklyOnWednesday", 4),
          ("whenFull", 9))
    )


_SendLogFrequency_Type.__name__ = "Integer32"
_SendLogFrequency_Object = MibScalar
sendLogFrequency = _SendLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 7),
    _SendLogFrequency_Type()
)
sendLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendLogFrequency.setStatus("current")
_SendLogTime_Type = OctetString
_SendLogTime_Object = MibScalar
sendLogTime = _SendLogTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 8),
    _SendLogTime_Type()
)
sendLogTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendLogTime.setStatus("current")


class _UserLogInLogOut_Type(Integer32):
    """Custom type userLogInLogOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sendAlert", 3),
          ("sendToLog", 2),
          ("sendtoLogAndAlert", 4))
    )


_UserLogInLogOut_Type.__name__ = "Integer32"
_UserLogInLogOut_Object = MibScalar
userLogInLogOut = _UserLogInLogOut_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 9),
    _UserLogInLogOut_Type()
)
userLogInLogOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userLogInLogOut.setStatus("current")


class _UserLogInLogOutFailed_Type(Integer32):
    """Custom type userLogInLogOutFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sendAlert", 3),
          ("sendToLog", 2),
          ("sendtoLogAndAlert", 4))
    )


_UserLogInLogOutFailed_Type.__name__ = "Integer32"
_UserLogInLogOutFailed_Object = MibScalar
userLogInLogOutFailed = _UserLogInLogOutFailed_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 10),
    _UserLogInLogOutFailed_Type()
)
userLogInLogOutFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userLogInLogOutFailed.setStatus("current")


class _OutletActivity_Type(Integer32):
    """Custom type outletActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sendAlert", 3),
          ("sendToLog", 2),
          ("sendtoLogAndAlert", 4))
    )


_OutletActivity_Type.__name__ = "Integer32"
_OutletActivity_Object = MibScalar
outletActivity = _OutletActivity_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 11),
    _OutletActivity_Type()
)
outletActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletActivity.setStatus("current")


class _SystemOnOff_Type(Integer32):
    """Custom type systemOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sendAlert", 3),
          ("sendToLog", 2),
          ("sendtoLogAndAlert", 4))
    )


_SystemOnOff_Type.__name__ = "Integer32"
_SystemOnOff_Object = MibScalar
systemOnOff = _SystemOnOff_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 12),
    _SystemOnOff_Type()
)
systemOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemOnOff.setStatus("current")


class _OutletSection1Alert_Type(Integer32):
    """Custom type outletSection1Alert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("sendAlert", 1))
    )


_OutletSection1Alert_Type.__name__ = "Integer32"
_OutletSection1Alert_Object = MibScalar
outletSection1Alert = _OutletSection1Alert_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 13),
    _OutletSection1Alert_Type()
)
outletSection1Alert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection1Alert.setStatus("current")


class _OutletSection2Alert_Type(Integer32):
    """Custom type outletSection2Alert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("sendAlert", 1))
    )


_OutletSection2Alert_Type.__name__ = "Integer32"
_OutletSection2Alert_Object = MibScalar
outletSection2Alert = _OutletSection2Alert_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 14),
    _OutletSection2Alert_Type()
)
outletSection2Alert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection2Alert.setStatus("current")


class _OutletSection3Alert_Type(Integer32):
    """Custom type outletSection3Alert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("sendAlert", 1))
    )


_OutletSection3Alert_Type.__name__ = "Integer32"
_OutletSection3Alert_Object = MibScalar
outletSection3Alert = _OutletSection3Alert_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 15),
    _OutletSection3Alert_Type()
)
outletSection3Alert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection3Alert.setStatus("current")


class _TempSensor1Alert_Type(Integer32):
    """Custom type tempSensor1Alert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("sendAlert", 1))
    )


_TempSensor1Alert_Type.__name__ = "Integer32"
_TempSensor1Alert_Object = MibScalar
tempSensor1Alert = _TempSensor1Alert_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 16),
    _TempSensor1Alert_Type()
)
tempSensor1Alert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor1Alert.setStatus("current")


class _TempSensor2Alert_Type(Integer32):
    """Custom type tempSensor2Alert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("sendAlert", 1))
    )


_TempSensor2Alert_Type.__name__ = "Integer32"
_TempSensor2Alert_Object = MibScalar
tempSensor2Alert = _TempSensor2Alert_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 17),
    _TempSensor2Alert_Type()
)
tempSensor2Alert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor2Alert.setStatus("current")


class _HumSensor1Alert_Type(Integer32):
    """Custom type humSensor1Alert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("sendAlert", 1))
    )


_HumSensor1Alert_Type.__name__ = "Integer32"
_HumSensor1Alert_Object = MibScalar
humSensor1Alert = _HumSensor1Alert_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 18),
    _HumSensor1Alert_Type()
)
humSensor1Alert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humSensor1Alert.setStatus("current")


class _ContactClosure1Alert_Type(Integer32):
    """Custom type contactClosure1Alert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("sendAlert", 1))
    )


_ContactClosure1Alert_Type.__name__ = "Integer32"
_ContactClosure1Alert_Object = MibScalar
contactClosure1Alert = _ContactClosure1Alert_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 19),
    _ContactClosure1Alert_Type()
)
contactClosure1Alert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure1Alert.setStatus("current")


class _ContactClosure2Alert_Type(Integer32):
    """Custom type contactClosure2Alert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("sendAlert", 1))
    )


_ContactClosure2Alert_Type.__name__ = "Integer32"
_ContactClosure2Alert_Object = MibScalar
contactClosure2Alert = _ContactClosure2Alert_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 20),
    _ContactClosure2Alert_Type()
)
contactClosure2Alert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure2Alert.setStatus("current")


class _ContactClosure3Alert_Type(Integer32):
    """Custom type contactClosure3Alert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("sendAlert", 1))
    )


_ContactClosure3Alert_Type.__name__ = "Integer32"
_ContactClosure3Alert_Object = MibScalar
contactClosure3Alert = _ContactClosure3Alert_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 3, 21),
    _ContactClosure3Alert_Type()
)
contactClosure3Alert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure3Alert.setStatus("current")
_SerialSettings_ObjectIdentity = ObjectIdentity
serialSettings = _SerialSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 4)
)


class _BaudRate_Type(Integer32):
    """Custom type baudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("baud19200", 1),
          ("baud38400", 2),
          ("baud9600", 0))
    )


_BaudRate_Type.__name__ = "Integer32"
_BaudRate_Object = MibScalar
baudRate = _BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 4, 1),
    _BaudRate_Type()
)
baudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baudRate.setStatus("current")
_TelnetSettings_ObjectIdentity = ObjectIdentity
telnetSettings = _TelnetSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 5)
)
_TelnetPort_Type = Integer32
_TelnetPort_Object = MibScalar
telnetPort = _TelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 5, 1),
    _TelnetPort_Type()
)
telnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPort.setStatus("current")


class _TelnetEnabled_Type(Integer32):
    """Custom type telnetEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_TelnetEnabled_Type.__name__ = "Integer32"
_TelnetEnabled_Object = MibScalar
telnetEnabled = _TelnetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 5, 2),
    _TelnetEnabled_Type()
)
telnetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetEnabled.setStatus("current")
_OutletMngt_ObjectIdentity = ObjectIdentity
outletMngt = _OutletMngt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6)
)
_OutletConfig_ObjectIdentity = ObjectIdentity
outletConfig = _OutletConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1)
)
_Outlet1_ObjectIdentity = ObjectIdentity
outlet1 = _Outlet1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 1)
)


class _Outlet1Name_Type(OctetString):
    """Custom type outlet1Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet1Name_Type.__name__ = "OctetString"
_Outlet1Name_Object = MibScalar
outlet1Name = _Outlet1Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 1, 1),
    _Outlet1Name_Type()
)
outlet1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet1Name.setStatus("current")
_Outlet1PingIpAddress_Type = IpAddress
_Outlet1PingIpAddress_Object = MibScalar
outlet1PingIpAddress = _Outlet1PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 1, 2),
    _Outlet1PingIpAddress_Type()
)
outlet1PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet1PingIpAddress.setStatus("current")
_Outlet1Link_Type = OctetString
_Outlet1Link_Object = MibScalar
outlet1Link = _Outlet1Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 1, 3),
    _Outlet1Link_Type()
)
outlet1Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet1Link.setStatus("current")
_Outlet1SequenceTime_Type = Integer32
_Outlet1SequenceTime_Object = MibScalar
outlet1SequenceTime = _Outlet1SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 1, 4),
    _Outlet1SequenceTime_Type()
)
outlet1SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet1SequenceTime.setStatus("current")
_Outlet1RebootTime_Type = Integer32
_Outlet1RebootTime_Object = MibScalar
outlet1RebootTime = _Outlet1RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 1, 5),
    _Outlet1RebootTime_Type()
)
outlet1RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet1RebootTime.setStatus("current")
_Outlet2_ObjectIdentity = ObjectIdentity
outlet2 = _Outlet2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 2)
)


class _Outlet2Name_Type(OctetString):
    """Custom type outlet2Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet2Name_Type.__name__ = "OctetString"
_Outlet2Name_Object = MibScalar
outlet2Name = _Outlet2Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 2, 1),
    _Outlet2Name_Type()
)
outlet2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet2Name.setStatus("current")
_Outlet2PingIpAddress_Type = IpAddress
_Outlet2PingIpAddress_Object = MibScalar
outlet2PingIpAddress = _Outlet2PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 2, 2),
    _Outlet2PingIpAddress_Type()
)
outlet2PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet2PingIpAddress.setStatus("current")
_Outlet2Link_Type = OctetString
_Outlet2Link_Object = MibScalar
outlet2Link = _Outlet2Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 2, 3),
    _Outlet2Link_Type()
)
outlet2Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet2Link.setStatus("current")
_Outlet2SequenceTime_Type = Integer32
_Outlet2SequenceTime_Object = MibScalar
outlet2SequenceTime = _Outlet2SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 2, 4),
    _Outlet2SequenceTime_Type()
)
outlet2SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet2SequenceTime.setStatus("current")
_Outlet2RebootTime_Type = Integer32
_Outlet2RebootTime_Object = MibScalar
outlet2RebootTime = _Outlet2RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 2, 5),
    _Outlet2RebootTime_Type()
)
outlet2RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet2RebootTime.setStatus("current")
_Outlet3_ObjectIdentity = ObjectIdentity
outlet3 = _Outlet3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 3)
)


class _Outlet3Name_Type(OctetString):
    """Custom type outlet3Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet3Name_Type.__name__ = "OctetString"
_Outlet3Name_Object = MibScalar
outlet3Name = _Outlet3Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 3, 1),
    _Outlet3Name_Type()
)
outlet3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet3Name.setStatus("current")
_Outlet3PingIpAddress_Type = IpAddress
_Outlet3PingIpAddress_Object = MibScalar
outlet3PingIpAddress = _Outlet3PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 3, 2),
    _Outlet3PingIpAddress_Type()
)
outlet3PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet3PingIpAddress.setStatus("current")
_Outlet3Link_Type = OctetString
_Outlet3Link_Object = MibScalar
outlet3Link = _Outlet3Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 3, 3),
    _Outlet3Link_Type()
)
outlet3Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet3Link.setStatus("current")
_Outlet3SequenceTime_Type = Integer32
_Outlet3SequenceTime_Object = MibScalar
outlet3SequenceTime = _Outlet3SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 3, 4),
    _Outlet3SequenceTime_Type()
)
outlet3SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet3SequenceTime.setStatus("current")
_Outlet3RebootTime_Type = Integer32
_Outlet3RebootTime_Object = MibScalar
outlet3RebootTime = _Outlet3RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 3, 5),
    _Outlet3RebootTime_Type()
)
outlet3RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet3RebootTime.setStatus("current")
_Outlet4_ObjectIdentity = ObjectIdentity
outlet4 = _Outlet4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 4)
)


class _Outlet4Name_Type(OctetString):
    """Custom type outlet4Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet4Name_Type.__name__ = "OctetString"
_Outlet4Name_Object = MibScalar
outlet4Name = _Outlet4Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 4, 1),
    _Outlet4Name_Type()
)
outlet4Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet4Name.setStatus("current")
_Outlet4PingIpAddress_Type = IpAddress
_Outlet4PingIpAddress_Object = MibScalar
outlet4PingIpAddress = _Outlet4PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 4, 2),
    _Outlet4PingIpAddress_Type()
)
outlet4PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet4PingIpAddress.setStatus("current")
_Outlet4Link_Type = OctetString
_Outlet4Link_Object = MibScalar
outlet4Link = _Outlet4Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 4, 3),
    _Outlet4Link_Type()
)
outlet4Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet4Link.setStatus("current")
_Outlet4SequenceTime_Type = Integer32
_Outlet4SequenceTime_Object = MibScalar
outlet4SequenceTime = _Outlet4SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 4, 4),
    _Outlet4SequenceTime_Type()
)
outlet4SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet4SequenceTime.setStatus("current")
_Outlet4RebootTime_Type = Integer32
_Outlet4RebootTime_Object = MibScalar
outlet4RebootTime = _Outlet4RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 4, 5),
    _Outlet4RebootTime_Type()
)
outlet4RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet4RebootTime.setStatus("current")
_Outlet5_ObjectIdentity = ObjectIdentity
outlet5 = _Outlet5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 5)
)


class _Outlet5Name_Type(OctetString):
    """Custom type outlet5Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet5Name_Type.__name__ = "OctetString"
_Outlet5Name_Object = MibScalar
outlet5Name = _Outlet5Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 5, 1),
    _Outlet5Name_Type()
)
outlet5Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet5Name.setStatus("current")
_Outlet5PingIpAddress_Type = IpAddress
_Outlet5PingIpAddress_Object = MibScalar
outlet5PingIpAddress = _Outlet5PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 5, 2),
    _Outlet5PingIpAddress_Type()
)
outlet5PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet5PingIpAddress.setStatus("current")
_Outlet5Link_Type = OctetString
_Outlet5Link_Object = MibScalar
outlet5Link = _Outlet5Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 5, 3),
    _Outlet5Link_Type()
)
outlet5Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet5Link.setStatus("current")
_Outlet5SequenceTime_Type = Integer32
_Outlet5SequenceTime_Object = MibScalar
outlet5SequenceTime = _Outlet5SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 5, 4),
    _Outlet5SequenceTime_Type()
)
outlet5SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet5SequenceTime.setStatus("current")
_Outlet5RebootTime_Type = Integer32
_Outlet5RebootTime_Object = MibScalar
outlet5RebootTime = _Outlet5RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 5, 5),
    _Outlet5RebootTime_Type()
)
outlet5RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet5RebootTime.setStatus("current")
_Outlet6_ObjectIdentity = ObjectIdentity
outlet6 = _Outlet6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 6)
)


class _Outlet6Name_Type(OctetString):
    """Custom type outlet6Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet6Name_Type.__name__ = "OctetString"
_Outlet6Name_Object = MibScalar
outlet6Name = _Outlet6Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 6, 1),
    _Outlet6Name_Type()
)
outlet6Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet6Name.setStatus("current")
_Outlet6PingIpAddress_Type = IpAddress
_Outlet6PingIpAddress_Object = MibScalar
outlet6PingIpAddress = _Outlet6PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 6, 2),
    _Outlet6PingIpAddress_Type()
)
outlet6PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet6PingIpAddress.setStatus("current")
_Outlet6Link_Type = OctetString
_Outlet6Link_Object = MibScalar
outlet6Link = _Outlet6Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 6, 3),
    _Outlet6Link_Type()
)
outlet6Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet6Link.setStatus("current")
_Outlet6SequenceTime_Type = Integer32
_Outlet6SequenceTime_Object = MibScalar
outlet6SequenceTime = _Outlet6SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 6, 4),
    _Outlet6SequenceTime_Type()
)
outlet6SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet6SequenceTime.setStatus("current")
_Outlet6RebootTime_Type = Integer32
_Outlet6RebootTime_Object = MibScalar
outlet6RebootTime = _Outlet6RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 6, 5),
    _Outlet6RebootTime_Type()
)
outlet6RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet6RebootTime.setStatus("current")
_Outlet7_ObjectIdentity = ObjectIdentity
outlet7 = _Outlet7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 7)
)


class _Outlet7Name_Type(OctetString):
    """Custom type outlet7Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet7Name_Type.__name__ = "OctetString"
_Outlet7Name_Object = MibScalar
outlet7Name = _Outlet7Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 7, 1),
    _Outlet7Name_Type()
)
outlet7Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet7Name.setStatus("current")
_Outlet7PingIpAddress_Type = IpAddress
_Outlet7PingIpAddress_Object = MibScalar
outlet7PingIpAddress = _Outlet7PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 7, 2),
    _Outlet7PingIpAddress_Type()
)
outlet7PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet7PingIpAddress.setStatus("current")
_Outlet7Link_Type = OctetString
_Outlet7Link_Object = MibScalar
outlet7Link = _Outlet7Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 7, 3),
    _Outlet7Link_Type()
)
outlet7Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet7Link.setStatus("current")
_Outlet7SequenceTime_Type = Integer32
_Outlet7SequenceTime_Object = MibScalar
outlet7SequenceTime = _Outlet7SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 7, 4),
    _Outlet7SequenceTime_Type()
)
outlet7SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet7SequenceTime.setStatus("current")
_Outlet7RebootTime_Type = Integer32
_Outlet7RebootTime_Object = MibScalar
outlet7RebootTime = _Outlet7RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 7, 5),
    _Outlet7RebootTime_Type()
)
outlet7RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet7RebootTime.setStatus("current")
_Outlet8_ObjectIdentity = ObjectIdentity
outlet8 = _Outlet8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 8)
)


class _Outlet8Name_Type(OctetString):
    """Custom type outlet8Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet8Name_Type.__name__ = "OctetString"
_Outlet8Name_Object = MibScalar
outlet8Name = _Outlet8Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 8, 1),
    _Outlet8Name_Type()
)
outlet8Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet8Name.setStatus("current")
_Outlet8PingIpAddress_Type = IpAddress
_Outlet8PingIpAddress_Object = MibScalar
outlet8PingIpAddress = _Outlet8PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 8, 2),
    _Outlet8PingIpAddress_Type()
)
outlet8PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet8PingIpAddress.setStatus("current")
_Outlet8Link_Type = OctetString
_Outlet8Link_Object = MibScalar
outlet8Link = _Outlet8Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 8, 3),
    _Outlet8Link_Type()
)
outlet8Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet8Link.setStatus("current")
_Outlet8SequenceTime_Type = Integer32
_Outlet8SequenceTime_Object = MibScalar
outlet8SequenceTime = _Outlet8SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 8, 4),
    _Outlet8SequenceTime_Type()
)
outlet8SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet8SequenceTime.setStatus("current")
_Outlet8RebootTime_Type = Integer32
_Outlet8RebootTime_Object = MibScalar
outlet8RebootTime = _Outlet8RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 8, 5),
    _Outlet8RebootTime_Type()
)
outlet8RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet8RebootTime.setStatus("current")
_Outlet9_ObjectIdentity = ObjectIdentity
outlet9 = _Outlet9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 9)
)


class _Outlet9Name_Type(OctetString):
    """Custom type outlet9Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet9Name_Type.__name__ = "OctetString"
_Outlet9Name_Object = MibScalar
outlet9Name = _Outlet9Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 9, 1),
    _Outlet9Name_Type()
)
outlet9Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet9Name.setStatus("current")
_Outlet9PingIpAddress_Type = IpAddress
_Outlet9PingIpAddress_Object = MibScalar
outlet9PingIpAddress = _Outlet9PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 9, 2),
    _Outlet9PingIpAddress_Type()
)
outlet9PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet9PingIpAddress.setStatus("current")
_Outlet9Link_Type = OctetString
_Outlet9Link_Object = MibScalar
outlet9Link = _Outlet9Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 9, 3),
    _Outlet9Link_Type()
)
outlet9Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet9Link.setStatus("current")
_Outlet9SequenceTime_Type = Integer32
_Outlet9SequenceTime_Object = MibScalar
outlet9SequenceTime = _Outlet9SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 9, 4),
    _Outlet9SequenceTime_Type()
)
outlet9SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet9SequenceTime.setStatus("current")
_Outlet9RebootTime_Type = Integer32
_Outlet9RebootTime_Object = MibScalar
outlet9RebootTime = _Outlet9RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 9, 5),
    _Outlet9RebootTime_Type()
)
outlet9RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet9RebootTime.setStatus("current")
_Outlet10_ObjectIdentity = ObjectIdentity
outlet10 = _Outlet10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 10)
)


class _Outlet10Name_Type(OctetString):
    """Custom type outlet10Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet10Name_Type.__name__ = "OctetString"
_Outlet10Name_Object = MibScalar
outlet10Name = _Outlet10Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 10, 1),
    _Outlet10Name_Type()
)
outlet10Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet10Name.setStatus("current")
_Outlet10PingIpAddress_Type = IpAddress
_Outlet10PingIpAddress_Object = MibScalar
outlet10PingIpAddress = _Outlet10PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 10, 2),
    _Outlet10PingIpAddress_Type()
)
outlet10PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet10PingIpAddress.setStatus("current")
_Outlet10Link_Type = OctetString
_Outlet10Link_Object = MibScalar
outlet10Link = _Outlet10Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 10, 3),
    _Outlet10Link_Type()
)
outlet10Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet10Link.setStatus("current")
_Outlet10SequenceTime_Type = Integer32
_Outlet10SequenceTime_Object = MibScalar
outlet10SequenceTime = _Outlet10SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 10, 4),
    _Outlet10SequenceTime_Type()
)
outlet10SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet10SequenceTime.setStatus("current")
_Outlet10RebootTime_Type = Integer32
_Outlet10RebootTime_Object = MibScalar
outlet10RebootTime = _Outlet10RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 10, 5),
    _Outlet10RebootTime_Type()
)
outlet10RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet10RebootTime.setStatus("current")
_Outlet11_ObjectIdentity = ObjectIdentity
outlet11 = _Outlet11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 11)
)


class _Outlet11Name_Type(OctetString):
    """Custom type outlet11Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet11Name_Type.__name__ = "OctetString"
_Outlet11Name_Object = MibScalar
outlet11Name = _Outlet11Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 11, 1),
    _Outlet11Name_Type()
)
outlet11Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet11Name.setStatus("current")
_Outlet11PingIpAddress_Type = IpAddress
_Outlet11PingIpAddress_Object = MibScalar
outlet11PingIpAddress = _Outlet11PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 11, 2),
    _Outlet11PingIpAddress_Type()
)
outlet11PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet11PingIpAddress.setStatus("current")
_Outlet11Link_Type = OctetString
_Outlet11Link_Object = MibScalar
outlet11Link = _Outlet11Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 11, 3),
    _Outlet11Link_Type()
)
outlet11Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet11Link.setStatus("current")
_Outlet11SequenceTime_Type = Integer32
_Outlet11SequenceTime_Object = MibScalar
outlet11SequenceTime = _Outlet11SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 11, 4),
    _Outlet11SequenceTime_Type()
)
outlet11SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet11SequenceTime.setStatus("current")
_Outlet11RebootTime_Type = Integer32
_Outlet11RebootTime_Object = MibScalar
outlet11RebootTime = _Outlet11RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 11, 5),
    _Outlet11RebootTime_Type()
)
outlet11RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet11RebootTime.setStatus("current")
_Outlet12_ObjectIdentity = ObjectIdentity
outlet12 = _Outlet12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 12)
)


class _Outlet12Name_Type(OctetString):
    """Custom type outlet12Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet12Name_Type.__name__ = "OctetString"
_Outlet12Name_Object = MibScalar
outlet12Name = _Outlet12Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 12, 1),
    _Outlet12Name_Type()
)
outlet12Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet12Name.setStatus("current")
_Outlet12PingIpAddress_Type = IpAddress
_Outlet12PingIpAddress_Object = MibScalar
outlet12PingIpAddress = _Outlet12PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 12, 2),
    _Outlet12PingIpAddress_Type()
)
outlet12PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet12PingIpAddress.setStatus("current")
_Outlet12Link_Type = OctetString
_Outlet12Link_Object = MibScalar
outlet12Link = _Outlet12Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 12, 3),
    _Outlet12Link_Type()
)
outlet12Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet12Link.setStatus("current")
_Outlet12SequenceTime_Type = Integer32
_Outlet12SequenceTime_Object = MibScalar
outlet12SequenceTime = _Outlet12SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 12, 4),
    _Outlet12SequenceTime_Type()
)
outlet12SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet12SequenceTime.setStatus("current")
_Outlet12RebootTime_Type = Integer32
_Outlet12RebootTime_Object = MibScalar
outlet12RebootTime = _Outlet12RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 12, 5),
    _Outlet12RebootTime_Type()
)
outlet12RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet12RebootTime.setStatus("current")
_Outlet13_ObjectIdentity = ObjectIdentity
outlet13 = _Outlet13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 13)
)


class _Outlet13Name_Type(OctetString):
    """Custom type outlet13Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet13Name_Type.__name__ = "OctetString"
_Outlet13Name_Object = MibScalar
outlet13Name = _Outlet13Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 13, 1),
    _Outlet13Name_Type()
)
outlet13Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet13Name.setStatus("current")
_Outlet13PingIpAddress_Type = IpAddress
_Outlet13PingIpAddress_Object = MibScalar
outlet13PingIpAddress = _Outlet13PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 13, 2),
    _Outlet13PingIpAddress_Type()
)
outlet13PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet13PingIpAddress.setStatus("current")
_Outlet13Link_Type = OctetString
_Outlet13Link_Object = MibScalar
outlet13Link = _Outlet13Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 13, 3),
    _Outlet13Link_Type()
)
outlet13Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet13Link.setStatus("current")
_Outlet13SequenceTime_Type = Integer32
_Outlet13SequenceTime_Object = MibScalar
outlet13SequenceTime = _Outlet13SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 13, 4),
    _Outlet13SequenceTime_Type()
)
outlet13SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet13SequenceTime.setStatus("current")
_Outlet13RebootTime_Type = Integer32
_Outlet13RebootTime_Object = MibScalar
outlet13RebootTime = _Outlet13RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 13, 5),
    _Outlet13RebootTime_Type()
)
outlet13RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet13RebootTime.setStatus("current")
_Outlet14_ObjectIdentity = ObjectIdentity
outlet14 = _Outlet14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 14)
)


class _Outlet14Name_Type(OctetString):
    """Custom type outlet14Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet14Name_Type.__name__ = "OctetString"
_Outlet14Name_Object = MibScalar
outlet14Name = _Outlet14Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 14, 1),
    _Outlet14Name_Type()
)
outlet14Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet14Name.setStatus("current")
_Outlet14PingIpAddress_Type = IpAddress
_Outlet14PingIpAddress_Object = MibScalar
outlet14PingIpAddress = _Outlet14PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 14, 2),
    _Outlet14PingIpAddress_Type()
)
outlet14PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet14PingIpAddress.setStatus("current")
_Outlet14Link_Type = OctetString
_Outlet14Link_Object = MibScalar
outlet14Link = _Outlet14Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 14, 3),
    _Outlet14Link_Type()
)
outlet14Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet14Link.setStatus("current")
_Outlet14SequenceTime_Type = Integer32
_Outlet14SequenceTime_Object = MibScalar
outlet14SequenceTime = _Outlet14SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 14, 4),
    _Outlet14SequenceTime_Type()
)
outlet14SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet14SequenceTime.setStatus("current")
_Outlet14RebootTime_Type = Integer32
_Outlet14RebootTime_Object = MibScalar
outlet14RebootTime = _Outlet14RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 14, 5),
    _Outlet14RebootTime_Type()
)
outlet14RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet14RebootTime.setStatus("current")
_Outlet15_ObjectIdentity = ObjectIdentity
outlet15 = _Outlet15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 15)
)


class _Outlet15Name_Type(OctetString):
    """Custom type outlet15Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet15Name_Type.__name__ = "OctetString"
_Outlet15Name_Object = MibScalar
outlet15Name = _Outlet15Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 15, 1),
    _Outlet15Name_Type()
)
outlet15Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet15Name.setStatus("current")
_Outlet15PingIpAddress_Type = IpAddress
_Outlet15PingIpAddress_Object = MibScalar
outlet15PingIpAddress = _Outlet15PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 15, 2),
    _Outlet15PingIpAddress_Type()
)
outlet15PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet15PingIpAddress.setStatus("current")
_Outlet15Link_Type = OctetString
_Outlet15Link_Object = MibScalar
outlet15Link = _Outlet15Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 15, 3),
    _Outlet15Link_Type()
)
outlet15Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet15Link.setStatus("current")
_Outlet15SequenceTime_Type = Integer32
_Outlet15SequenceTime_Object = MibScalar
outlet15SequenceTime = _Outlet15SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 15, 4),
    _Outlet15SequenceTime_Type()
)
outlet15SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet15SequenceTime.setStatus("current")
_Outlet15RebootTime_Type = Integer32
_Outlet15RebootTime_Object = MibScalar
outlet15RebootTime = _Outlet15RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 15, 5),
    _Outlet15RebootTime_Type()
)
outlet15RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet15RebootTime.setStatus("current")
_Outlet16_ObjectIdentity = ObjectIdentity
outlet16 = _Outlet16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 16)
)


class _Outlet16Name_Type(OctetString):
    """Custom type outlet16Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet16Name_Type.__name__ = "OctetString"
_Outlet16Name_Object = MibScalar
outlet16Name = _Outlet16Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 16, 1),
    _Outlet16Name_Type()
)
outlet16Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet16Name.setStatus("current")
_Outlet16PingIpAddress_Type = IpAddress
_Outlet16PingIpAddress_Object = MibScalar
outlet16PingIpAddress = _Outlet16PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 16, 2),
    _Outlet16PingIpAddress_Type()
)
outlet16PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet16PingIpAddress.setStatus("current")
_Outlet16Link_Type = OctetString
_Outlet16Link_Object = MibScalar
outlet16Link = _Outlet16Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 16, 3),
    _Outlet16Link_Type()
)
outlet16Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet16Link.setStatus("current")
_Outlet16SequenceTime_Type = Integer32
_Outlet16SequenceTime_Object = MibScalar
outlet16SequenceTime = _Outlet16SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 16, 4),
    _Outlet16SequenceTime_Type()
)
outlet16SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet16SequenceTime.setStatus("current")
_Outlet16RebootTime_Type = Integer32
_Outlet16RebootTime_Object = MibScalar
outlet16RebootTime = _Outlet16RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 16, 5),
    _Outlet16RebootTime_Type()
)
outlet16RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet16RebootTime.setStatus("current")
_Outlet17_ObjectIdentity = ObjectIdentity
outlet17 = _Outlet17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 17)
)


class _Outlet17Name_Type(OctetString):
    """Custom type outlet17Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet17Name_Type.__name__ = "OctetString"
_Outlet17Name_Object = MibScalar
outlet17Name = _Outlet17Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 17, 1),
    _Outlet17Name_Type()
)
outlet17Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet17Name.setStatus("current")
_Outlet17PingIpAddress_Type = IpAddress
_Outlet17PingIpAddress_Object = MibScalar
outlet17PingIpAddress = _Outlet17PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 17, 2),
    _Outlet17PingIpAddress_Type()
)
outlet17PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet17PingIpAddress.setStatus("current")
_Outlet17Link_Type = OctetString
_Outlet17Link_Object = MibScalar
outlet17Link = _Outlet17Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 17, 3),
    _Outlet17Link_Type()
)
outlet17Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet17Link.setStatus("current")
_Outlet17SequenceTime_Type = Integer32
_Outlet17SequenceTime_Object = MibScalar
outlet17SequenceTime = _Outlet17SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 17, 4),
    _Outlet17SequenceTime_Type()
)
outlet17SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet17SequenceTime.setStatus("current")
_Outlet17RebootTime_Type = Integer32
_Outlet17RebootTime_Object = MibScalar
outlet17RebootTime = _Outlet17RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 17, 5),
    _Outlet17RebootTime_Type()
)
outlet17RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet17RebootTime.setStatus("current")
_Outlet18_ObjectIdentity = ObjectIdentity
outlet18 = _Outlet18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 18)
)


class _Outlet18Name_Type(OctetString):
    """Custom type outlet18Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet18Name_Type.__name__ = "OctetString"
_Outlet18Name_Object = MibScalar
outlet18Name = _Outlet18Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 18, 1),
    _Outlet18Name_Type()
)
outlet18Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet18Name.setStatus("current")
_Outlet18PingIpAddress_Type = IpAddress
_Outlet18PingIpAddress_Object = MibScalar
outlet18PingIpAddress = _Outlet18PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 18, 2),
    _Outlet18PingIpAddress_Type()
)
outlet18PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet18PingIpAddress.setStatus("current")
_Outlet18Link_Type = OctetString
_Outlet18Link_Object = MibScalar
outlet18Link = _Outlet18Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 18, 3),
    _Outlet18Link_Type()
)
outlet18Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet18Link.setStatus("current")
_Outlet18SequenceTime_Type = Integer32
_Outlet18SequenceTime_Object = MibScalar
outlet18SequenceTime = _Outlet18SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 18, 4),
    _Outlet18SequenceTime_Type()
)
outlet18SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet18SequenceTime.setStatus("current")
_Outlet18RebootTime_Type = Integer32
_Outlet18RebootTime_Object = MibScalar
outlet18RebootTime = _Outlet18RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 18, 5),
    _Outlet18RebootTime_Type()
)
outlet18RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet18RebootTime.setStatus("current")
_Outlet19_ObjectIdentity = ObjectIdentity
outlet19 = _Outlet19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 19)
)


class _Outlet19Name_Type(OctetString):
    """Custom type outlet19Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet19Name_Type.__name__ = "OctetString"
_Outlet19Name_Object = MibScalar
outlet19Name = _Outlet19Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 19, 1),
    _Outlet19Name_Type()
)
outlet19Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet19Name.setStatus("current")
_Outlet19PingIpAddress_Type = IpAddress
_Outlet19PingIpAddress_Object = MibScalar
outlet19PingIpAddress = _Outlet19PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 19, 2),
    _Outlet19PingIpAddress_Type()
)
outlet19PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet19PingIpAddress.setStatus("current")
_Outlet19Link_Type = OctetString
_Outlet19Link_Object = MibScalar
outlet19Link = _Outlet19Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 19, 3),
    _Outlet19Link_Type()
)
outlet19Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet19Link.setStatus("current")
_Outlet19SequenceTime_Type = Integer32
_Outlet19SequenceTime_Object = MibScalar
outlet19SequenceTime = _Outlet19SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 19, 4),
    _Outlet19SequenceTime_Type()
)
outlet19SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet19SequenceTime.setStatus("current")
_Outlet19RebootTime_Type = Integer32
_Outlet19RebootTime_Object = MibScalar
outlet19RebootTime = _Outlet19RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 19, 5),
    _Outlet19RebootTime_Type()
)
outlet19RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet19RebootTime.setStatus("current")
_Outlet20_ObjectIdentity = ObjectIdentity
outlet20 = _Outlet20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 20)
)


class _Outlet20Name_Type(OctetString):
    """Custom type outlet20Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet20Name_Type.__name__ = "OctetString"
_Outlet20Name_Object = MibScalar
outlet20Name = _Outlet20Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 20, 1),
    _Outlet20Name_Type()
)
outlet20Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet20Name.setStatus("current")
_Outlet20PingIpAddress_Type = IpAddress
_Outlet20PingIpAddress_Object = MibScalar
outlet20PingIpAddress = _Outlet20PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 20, 2),
    _Outlet20PingIpAddress_Type()
)
outlet20PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet20PingIpAddress.setStatus("current")
_Outlet20Link_Type = OctetString
_Outlet20Link_Object = MibScalar
outlet20Link = _Outlet20Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 20, 3),
    _Outlet20Link_Type()
)
outlet20Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet20Link.setStatus("current")
_Outlet20SequenceTime_Type = Integer32
_Outlet20SequenceTime_Object = MibScalar
outlet20SequenceTime = _Outlet20SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 20, 4),
    _Outlet20SequenceTime_Type()
)
outlet20SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet20SequenceTime.setStatus("current")
_Outlet20RebootTime_Type = Integer32
_Outlet20RebootTime_Object = MibScalar
outlet20RebootTime = _Outlet20RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 20, 5),
    _Outlet20RebootTime_Type()
)
outlet20RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet20RebootTime.setStatus("current")
_Outlet21_ObjectIdentity = ObjectIdentity
outlet21 = _Outlet21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 21)
)


class _Outlet21Name_Type(OctetString):
    """Custom type outlet21Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet21Name_Type.__name__ = "OctetString"
_Outlet21Name_Object = MibScalar
outlet21Name = _Outlet21Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 21, 1),
    _Outlet21Name_Type()
)
outlet21Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet21Name.setStatus("current")
_Outlet21PingIpAddress_Type = IpAddress
_Outlet21PingIpAddress_Object = MibScalar
outlet21PingIpAddress = _Outlet21PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 21, 2),
    _Outlet21PingIpAddress_Type()
)
outlet21PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet21PingIpAddress.setStatus("current")
_Outlet21Link_Type = OctetString
_Outlet21Link_Object = MibScalar
outlet21Link = _Outlet21Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 21, 3),
    _Outlet21Link_Type()
)
outlet21Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet21Link.setStatus("current")
_Outlet21SequenceTime_Type = Integer32
_Outlet21SequenceTime_Object = MibScalar
outlet21SequenceTime = _Outlet21SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 21, 4),
    _Outlet21SequenceTime_Type()
)
outlet21SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet21SequenceTime.setStatus("current")
_Outlet21RebootTime_Type = Integer32
_Outlet21RebootTime_Object = MibScalar
outlet21RebootTime = _Outlet21RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 21, 5),
    _Outlet21RebootTime_Type()
)
outlet21RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet21RebootTime.setStatus("current")
_Outlet22_ObjectIdentity = ObjectIdentity
outlet22 = _Outlet22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 22)
)


class _Outlet22Name_Type(OctetString):
    """Custom type outlet22Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet22Name_Type.__name__ = "OctetString"
_Outlet22Name_Object = MibScalar
outlet22Name = _Outlet22Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 22, 1),
    _Outlet22Name_Type()
)
outlet22Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet22Name.setStatus("current")
_Outlet22PingIpAddress_Type = IpAddress
_Outlet22PingIpAddress_Object = MibScalar
outlet22PingIpAddress = _Outlet22PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 22, 2),
    _Outlet22PingIpAddress_Type()
)
outlet22PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet22PingIpAddress.setStatus("current")
_Outlet22Link_Type = OctetString
_Outlet22Link_Object = MibScalar
outlet22Link = _Outlet22Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 22, 3),
    _Outlet22Link_Type()
)
outlet22Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet22Link.setStatus("current")
_Outlet22SequenceTime_Type = Integer32
_Outlet22SequenceTime_Object = MibScalar
outlet22SequenceTime = _Outlet22SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 22, 4),
    _Outlet22SequenceTime_Type()
)
outlet22SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet22SequenceTime.setStatus("current")
_Outlet22RebootTime_Type = Integer32
_Outlet22RebootTime_Object = MibScalar
outlet22RebootTime = _Outlet22RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 22, 5),
    _Outlet22RebootTime_Type()
)
outlet22RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet22RebootTime.setStatus("current")
_Outlet23_ObjectIdentity = ObjectIdentity
outlet23 = _Outlet23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 23)
)


class _Outlet23Name_Type(OctetString):
    """Custom type outlet23Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet23Name_Type.__name__ = "OctetString"
_Outlet23Name_Object = MibScalar
outlet23Name = _Outlet23Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 23, 1),
    _Outlet23Name_Type()
)
outlet23Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet23Name.setStatus("current")
_Outlet23PingIpAddress_Type = IpAddress
_Outlet23PingIpAddress_Object = MibScalar
outlet23PingIpAddress = _Outlet23PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 23, 2),
    _Outlet23PingIpAddress_Type()
)
outlet23PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet23PingIpAddress.setStatus("current")
_Outlet23Link_Type = OctetString
_Outlet23Link_Object = MibScalar
outlet23Link = _Outlet23Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 23, 3),
    _Outlet23Link_Type()
)
outlet23Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet23Link.setStatus("current")
_Outlet23SequenceTime_Type = Integer32
_Outlet23SequenceTime_Object = MibScalar
outlet23SequenceTime = _Outlet23SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 23, 4),
    _Outlet23SequenceTime_Type()
)
outlet23SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet23SequenceTime.setStatus("current")
_Outlet23RebootTime_Type = Integer32
_Outlet23RebootTime_Object = MibScalar
outlet23RebootTime = _Outlet23RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 23, 5),
    _Outlet23RebootTime_Type()
)
outlet23RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet23RebootTime.setStatus("current")
_Outlet24_ObjectIdentity = ObjectIdentity
outlet24 = _Outlet24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 24)
)


class _Outlet24Name_Type(OctetString):
    """Custom type outlet24Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet24Name_Type.__name__ = "OctetString"
_Outlet24Name_Object = MibScalar
outlet24Name = _Outlet24Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 24, 1),
    _Outlet24Name_Type()
)
outlet24Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet24Name.setStatus("current")
_Outlet24PingIpAddress_Type = IpAddress
_Outlet24PingIpAddress_Object = MibScalar
outlet24PingIpAddress = _Outlet24PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 24, 2),
    _Outlet24PingIpAddress_Type()
)
outlet24PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet24PingIpAddress.setStatus("current")
_Outlet24Link_Type = OctetString
_Outlet24Link_Object = MibScalar
outlet24Link = _Outlet24Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 24, 3),
    _Outlet24Link_Type()
)
outlet24Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet24Link.setStatus("current")
_Outlet24SequenceTime_Type = Integer32
_Outlet24SequenceTime_Object = MibScalar
outlet24SequenceTime = _Outlet24SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 24, 4),
    _Outlet24SequenceTime_Type()
)
outlet24SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet24SequenceTime.setStatus("current")
_Outlet24RebootTime_Type = Integer32
_Outlet24RebootTime_Object = MibScalar
outlet24RebootTime = _Outlet24RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 24, 5),
    _Outlet24RebootTime_Type()
)
outlet24RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet24RebootTime.setStatus("current")
_Outlet25_ObjectIdentity = ObjectIdentity
outlet25 = _Outlet25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 25)
)


class _Outlet25Name_Type(OctetString):
    """Custom type outlet25Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet25Name_Type.__name__ = "OctetString"
_Outlet25Name_Object = MibScalar
outlet25Name = _Outlet25Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 25, 1),
    _Outlet25Name_Type()
)
outlet25Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet25Name.setStatus("current")
_Outlet25PingIpAddress_Type = IpAddress
_Outlet25PingIpAddress_Object = MibScalar
outlet25PingIpAddress = _Outlet25PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 25, 2),
    _Outlet25PingIpAddress_Type()
)
outlet25PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet25PingIpAddress.setStatus("current")
_Outlet25Link_Type = OctetString
_Outlet25Link_Object = MibScalar
outlet25Link = _Outlet25Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 25, 3),
    _Outlet25Link_Type()
)
outlet25Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet25Link.setStatus("current")
_Outlet25SequenceTime_Type = Integer32
_Outlet25SequenceTime_Object = MibScalar
outlet25SequenceTime = _Outlet25SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 25, 4),
    _Outlet25SequenceTime_Type()
)
outlet25SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet25SequenceTime.setStatus("current")
_Outlet25RebootTime_Type = Integer32
_Outlet25RebootTime_Object = MibScalar
outlet25RebootTime = _Outlet25RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 25, 5),
    _Outlet25RebootTime_Type()
)
outlet25RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet25RebootTime.setStatus("current")
_Outlet26_ObjectIdentity = ObjectIdentity
outlet26 = _Outlet26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 26)
)


class _Outlet26Name_Type(OctetString):
    """Custom type outlet26Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet26Name_Type.__name__ = "OctetString"
_Outlet26Name_Object = MibScalar
outlet26Name = _Outlet26Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 26, 1),
    _Outlet26Name_Type()
)
outlet26Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet26Name.setStatus("current")
_Outlet26PingIpAddress_Type = IpAddress
_Outlet26PingIpAddress_Object = MibScalar
outlet26PingIpAddress = _Outlet26PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 26, 2),
    _Outlet26PingIpAddress_Type()
)
outlet26PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet26PingIpAddress.setStatus("current")
_Outlet26Link_Type = OctetString
_Outlet26Link_Object = MibScalar
outlet26Link = _Outlet26Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 26, 3),
    _Outlet26Link_Type()
)
outlet26Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet26Link.setStatus("current")
_Outlet26SequenceTime_Type = Integer32
_Outlet26SequenceTime_Object = MibScalar
outlet26SequenceTime = _Outlet26SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 26, 4),
    _Outlet26SequenceTime_Type()
)
outlet26SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet26SequenceTime.setStatus("current")
_Outlet26RebootTime_Type = Integer32
_Outlet26RebootTime_Object = MibScalar
outlet26RebootTime = _Outlet26RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 26, 5),
    _Outlet26RebootTime_Type()
)
outlet26RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet26RebootTime.setStatus("current")
_Outlet27_ObjectIdentity = ObjectIdentity
outlet27 = _Outlet27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 27)
)


class _Outlet27Name_Type(OctetString):
    """Custom type outlet27Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet27Name_Type.__name__ = "OctetString"
_Outlet27Name_Object = MibScalar
outlet27Name = _Outlet27Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 27, 1),
    _Outlet27Name_Type()
)
outlet27Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet27Name.setStatus("current")
_Outlet27PingIpAddress_Type = IpAddress
_Outlet27PingIpAddress_Object = MibScalar
outlet27PingIpAddress = _Outlet27PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 27, 2),
    _Outlet27PingIpAddress_Type()
)
outlet27PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet27PingIpAddress.setStatus("current")
_Outlet27Link_Type = OctetString
_Outlet27Link_Object = MibScalar
outlet27Link = _Outlet27Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 27, 3),
    _Outlet27Link_Type()
)
outlet27Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet27Link.setStatus("current")
_Outlet27SequenceTime_Type = Integer32
_Outlet27SequenceTime_Object = MibScalar
outlet27SequenceTime = _Outlet27SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 27, 4),
    _Outlet27SequenceTime_Type()
)
outlet27SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet27SequenceTime.setStatus("current")
_Outlet27RebootTime_Type = Integer32
_Outlet27RebootTime_Object = MibScalar
outlet27RebootTime = _Outlet27RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 27, 5),
    _Outlet27RebootTime_Type()
)
outlet27RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet27RebootTime.setStatus("current")
_Outlet28_ObjectIdentity = ObjectIdentity
outlet28 = _Outlet28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 28)
)


class _Outlet28Name_Type(OctetString):
    """Custom type outlet28Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet28Name_Type.__name__ = "OctetString"
_Outlet28Name_Object = MibScalar
outlet28Name = _Outlet28Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 28, 1),
    _Outlet28Name_Type()
)
outlet28Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet28Name.setStatus("current")
_Outlet28PingIpAddress_Type = IpAddress
_Outlet28PingIpAddress_Object = MibScalar
outlet28PingIpAddress = _Outlet28PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 28, 2),
    _Outlet28PingIpAddress_Type()
)
outlet28PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet28PingIpAddress.setStatus("current")
_Outlet28Link_Type = OctetString
_Outlet28Link_Object = MibScalar
outlet28Link = _Outlet28Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 28, 3),
    _Outlet28Link_Type()
)
outlet28Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet28Link.setStatus("current")
_Outlet28SequenceTime_Type = Integer32
_Outlet28SequenceTime_Object = MibScalar
outlet28SequenceTime = _Outlet28SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 28, 4),
    _Outlet28SequenceTime_Type()
)
outlet28SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet28SequenceTime.setStatus("current")
_Outlet28RebootTime_Type = Integer32
_Outlet28RebootTime_Object = MibScalar
outlet28RebootTime = _Outlet28RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 28, 5),
    _Outlet28RebootTime_Type()
)
outlet28RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet28RebootTime.setStatus("current")
_Outlet29_ObjectIdentity = ObjectIdentity
outlet29 = _Outlet29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 29)
)


class _Outlet29Name_Type(OctetString):
    """Custom type outlet29Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet29Name_Type.__name__ = "OctetString"
_Outlet29Name_Object = MibScalar
outlet29Name = _Outlet29Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 29, 1),
    _Outlet29Name_Type()
)
outlet29Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet29Name.setStatus("current")
_Outlet29PingIpAddress_Type = IpAddress
_Outlet29PingIpAddress_Object = MibScalar
outlet29PingIpAddress = _Outlet29PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 29, 2),
    _Outlet29PingIpAddress_Type()
)
outlet29PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet29PingIpAddress.setStatus("current")
_Outlet29Link_Type = OctetString
_Outlet29Link_Object = MibScalar
outlet29Link = _Outlet29Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 29, 3),
    _Outlet29Link_Type()
)
outlet29Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet29Link.setStatus("current")
_Outlet29SequenceTime_Type = Integer32
_Outlet29SequenceTime_Object = MibScalar
outlet29SequenceTime = _Outlet29SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 29, 4),
    _Outlet29SequenceTime_Type()
)
outlet29SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet29SequenceTime.setStatus("current")
_Outlet29RebootTime_Type = Integer32
_Outlet29RebootTime_Object = MibScalar
outlet29RebootTime = _Outlet29RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 29, 5),
    _Outlet29RebootTime_Type()
)
outlet29RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet29RebootTime.setStatus("current")
_Outlet30_ObjectIdentity = ObjectIdentity
outlet30 = _Outlet30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 30)
)


class _Outlet30Name_Type(OctetString):
    """Custom type outlet30Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet30Name_Type.__name__ = "OctetString"
_Outlet30Name_Object = MibScalar
outlet30Name = _Outlet30Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 30, 1),
    _Outlet30Name_Type()
)
outlet30Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet30Name.setStatus("current")
_Outlet30PingIpAddress_Type = IpAddress
_Outlet30PingIpAddress_Object = MibScalar
outlet30PingIpAddress = _Outlet30PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 30, 2),
    _Outlet30PingIpAddress_Type()
)
outlet30PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet30PingIpAddress.setStatus("current")
_Outlet30Link_Type = OctetString
_Outlet30Link_Object = MibScalar
outlet30Link = _Outlet30Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 30, 3),
    _Outlet30Link_Type()
)
outlet30Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet30Link.setStatus("current")
_Outlet30SequenceTime_Type = Integer32
_Outlet30SequenceTime_Object = MibScalar
outlet30SequenceTime = _Outlet30SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 30, 4),
    _Outlet30SequenceTime_Type()
)
outlet30SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet30SequenceTime.setStatus("current")
_Outlet30RebootTime_Type = Integer32
_Outlet30RebootTime_Object = MibScalar
outlet30RebootTime = _Outlet30RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 30, 5),
    _Outlet30RebootTime_Type()
)
outlet30RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet30RebootTime.setStatus("current")
_Outlet31_ObjectIdentity = ObjectIdentity
outlet31 = _Outlet31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 31)
)


class _Outlet31Name_Type(OctetString):
    """Custom type outlet31Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet31Name_Type.__name__ = "OctetString"
_Outlet31Name_Object = MibScalar
outlet31Name = _Outlet31Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 31, 1),
    _Outlet31Name_Type()
)
outlet31Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet31Name.setStatus("current")
_Outlet31PingIpAddress_Type = IpAddress
_Outlet31PingIpAddress_Object = MibScalar
outlet31PingIpAddress = _Outlet31PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 31, 2),
    _Outlet31PingIpAddress_Type()
)
outlet31PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet31PingIpAddress.setStatus("current")
_Outlet31Link_Type = OctetString
_Outlet31Link_Object = MibScalar
outlet31Link = _Outlet31Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 31, 3),
    _Outlet31Link_Type()
)
outlet31Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet31Link.setStatus("current")
_Outlet31SequenceTime_Type = Integer32
_Outlet31SequenceTime_Object = MibScalar
outlet31SequenceTime = _Outlet31SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 31, 4),
    _Outlet31SequenceTime_Type()
)
outlet31SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet31SequenceTime.setStatus("current")
_Outlet31RebootTime_Type = Integer32
_Outlet31RebootTime_Object = MibScalar
outlet31RebootTime = _Outlet31RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 31, 5),
    _Outlet31RebootTime_Type()
)
outlet31RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet31RebootTime.setStatus("current")
_Outlet32_ObjectIdentity = ObjectIdentity
outlet32 = _Outlet32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 32)
)


class _Outlet32Name_Type(OctetString):
    """Custom type outlet32Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet32Name_Type.__name__ = "OctetString"
_Outlet32Name_Object = MibScalar
outlet32Name = _Outlet32Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 32, 1),
    _Outlet32Name_Type()
)
outlet32Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet32Name.setStatus("current")
_Outlet32PingIpAddress_Type = IpAddress
_Outlet32PingIpAddress_Object = MibScalar
outlet32PingIpAddress = _Outlet32PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 32, 2),
    _Outlet32PingIpAddress_Type()
)
outlet32PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet32PingIpAddress.setStatus("current")
_Outlet32Link_Type = OctetString
_Outlet32Link_Object = MibScalar
outlet32Link = _Outlet32Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 32, 3),
    _Outlet32Link_Type()
)
outlet32Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet32Link.setStatus("current")
_Outlet32SequenceTime_Type = Integer32
_Outlet32SequenceTime_Object = MibScalar
outlet32SequenceTime = _Outlet32SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 32, 4),
    _Outlet32SequenceTime_Type()
)
outlet32SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet32SequenceTime.setStatus("current")
_Outlet32RebootTime_Type = Integer32
_Outlet32RebootTime_Object = MibScalar
outlet32RebootTime = _Outlet32RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 32, 5),
    _Outlet32RebootTime_Type()
)
outlet32RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet32RebootTime.setStatus("current")
_Outlet33_ObjectIdentity = ObjectIdentity
outlet33 = _Outlet33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 33)
)


class _Outlet33Name_Type(OctetString):
    """Custom type outlet33Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet33Name_Type.__name__ = "OctetString"
_Outlet33Name_Object = MibScalar
outlet33Name = _Outlet33Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 33, 1),
    _Outlet33Name_Type()
)
outlet33Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet33Name.setStatus("current")
_Outlet33PingIpAddress_Type = IpAddress
_Outlet33PingIpAddress_Object = MibScalar
outlet33PingIpAddress = _Outlet33PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 33, 2),
    _Outlet33PingIpAddress_Type()
)
outlet33PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet33PingIpAddress.setStatus("current")
_Outlet33Link_Type = OctetString
_Outlet33Link_Object = MibScalar
outlet33Link = _Outlet33Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 33, 3),
    _Outlet33Link_Type()
)
outlet33Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet33Link.setStatus("current")
_Outlet33SequenceTime_Type = Integer32
_Outlet33SequenceTime_Object = MibScalar
outlet33SequenceTime = _Outlet33SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 33, 4),
    _Outlet33SequenceTime_Type()
)
outlet33SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet33SequenceTime.setStatus("current")
_Outlet33RebootTime_Type = Integer32
_Outlet33RebootTime_Object = MibScalar
outlet33RebootTime = _Outlet33RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 33, 5),
    _Outlet33RebootTime_Type()
)
outlet33RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet33RebootTime.setStatus("current")
_Outlet34_ObjectIdentity = ObjectIdentity
outlet34 = _Outlet34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 34)
)


class _Outlet34Name_Type(OctetString):
    """Custom type outlet34Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet34Name_Type.__name__ = "OctetString"
_Outlet34Name_Object = MibScalar
outlet34Name = _Outlet34Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 34, 1),
    _Outlet34Name_Type()
)
outlet34Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet34Name.setStatus("current")
_Outlet34PingIpAddress_Type = IpAddress
_Outlet34PingIpAddress_Object = MibScalar
outlet34PingIpAddress = _Outlet34PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 34, 2),
    _Outlet34PingIpAddress_Type()
)
outlet34PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet34PingIpAddress.setStatus("current")
_Outlet34Link_Type = OctetString
_Outlet34Link_Object = MibScalar
outlet34Link = _Outlet34Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 34, 3),
    _Outlet34Link_Type()
)
outlet34Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet34Link.setStatus("current")
_Outlet34SequenceTime_Type = Integer32
_Outlet34SequenceTime_Object = MibScalar
outlet34SequenceTime = _Outlet34SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 34, 4),
    _Outlet34SequenceTime_Type()
)
outlet34SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet34SequenceTime.setStatus("current")
_Outlet34RebootTime_Type = Integer32
_Outlet34RebootTime_Object = MibScalar
outlet34RebootTime = _Outlet34RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 34, 5),
    _Outlet34RebootTime_Type()
)
outlet34RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet34RebootTime.setStatus("current")
_Outlet35_ObjectIdentity = ObjectIdentity
outlet35 = _Outlet35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 35)
)


class _Outlet35Name_Type(OctetString):
    """Custom type outlet35Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet35Name_Type.__name__ = "OctetString"
_Outlet35Name_Object = MibScalar
outlet35Name = _Outlet35Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 35, 1),
    _Outlet35Name_Type()
)
outlet35Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet35Name.setStatus("current")
_Outlet35PingIpAddress_Type = IpAddress
_Outlet35PingIpAddress_Object = MibScalar
outlet35PingIpAddress = _Outlet35PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 35, 2),
    _Outlet35PingIpAddress_Type()
)
outlet35PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet35PingIpAddress.setStatus("current")
_Outlet35Link_Type = OctetString
_Outlet35Link_Object = MibScalar
outlet35Link = _Outlet35Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 35, 3),
    _Outlet35Link_Type()
)
outlet35Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet35Link.setStatus("current")
_Outlet35SequenceTime_Type = Integer32
_Outlet35SequenceTime_Object = MibScalar
outlet35SequenceTime = _Outlet35SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 35, 4),
    _Outlet35SequenceTime_Type()
)
outlet35SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet35SequenceTime.setStatus("current")
_Outlet35RebootTime_Type = Integer32
_Outlet35RebootTime_Object = MibScalar
outlet35RebootTime = _Outlet35RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 35, 5),
    _Outlet35RebootTime_Type()
)
outlet35RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet35RebootTime.setStatus("current")
_Outlet36_ObjectIdentity = ObjectIdentity
outlet36 = _Outlet36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 36)
)


class _Outlet36Name_Type(OctetString):
    """Custom type outlet36Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Outlet36Name_Type.__name__ = "OctetString"
_Outlet36Name_Object = MibScalar
outlet36Name = _Outlet36Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 36, 1),
    _Outlet36Name_Type()
)
outlet36Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet36Name.setStatus("current")
_Outlet36PingIpAddress_Type = IpAddress
_Outlet36PingIpAddress_Object = MibScalar
outlet36PingIpAddress = _Outlet36PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 36, 2),
    _Outlet36PingIpAddress_Type()
)
outlet36PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet36PingIpAddress.setStatus("current")
_Outlet36Link_Type = OctetString
_Outlet36Link_Object = MibScalar
outlet36Link = _Outlet36Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 36, 3),
    _Outlet36Link_Type()
)
outlet36Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet36Link.setStatus("current")
_Outlet36SequenceTime_Type = Integer32
_Outlet36SequenceTime_Object = MibScalar
outlet36SequenceTime = _Outlet36SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 36, 4),
    _Outlet36SequenceTime_Type()
)
outlet36SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet36SequenceTime.setStatus("current")
_Outlet36RebootTime_Type = Integer32
_Outlet36RebootTime_Object = MibScalar
outlet36RebootTime = _Outlet36RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 1, 36, 5),
    _Outlet36RebootTime_Type()
)
outlet36RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet36RebootTime.setStatus("current")
_OutletControl_ObjectIdentity = ObjectIdentity
outletControl = _OutletControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2)
)


class _GlobalCommand_Type(Integer32):
    """Custom type globalCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("globalOff", 2),
          ("globalOn", 1),
          ("nochange", 0),
          ("sequenceOff", 4),
          ("sequenceOn", 3))
    )


_GlobalCommand_Type.__name__ = "Integer32"
_GlobalCommand_Object = MibScalar
globalCommand = _GlobalCommand_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 1),
    _GlobalCommand_Type()
)
globalCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalCommand.setStatus("current")


class _Outlet1Command_Type(Integer32):
    """Custom type outlet1Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet1Command_Type.__name__ = "Integer32"
_Outlet1Command_Object = MibScalar
outlet1Command = _Outlet1Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 2),
    _Outlet1Command_Type()
)
outlet1Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet1Command.setStatus("current")


class _Outlet2Command_Type(Integer32):
    """Custom type outlet2Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet2Command_Type.__name__ = "Integer32"
_Outlet2Command_Object = MibScalar
outlet2Command = _Outlet2Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 3),
    _Outlet2Command_Type()
)
outlet2Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet2Command.setStatus("current")


class _Outlet3Command_Type(Integer32):
    """Custom type outlet3Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet3Command_Type.__name__ = "Integer32"
_Outlet3Command_Object = MibScalar
outlet3Command = _Outlet3Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 4),
    _Outlet3Command_Type()
)
outlet3Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet3Command.setStatus("current")


class _Outlet4Command_Type(Integer32):
    """Custom type outlet4Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet4Command_Type.__name__ = "Integer32"
_Outlet4Command_Object = MibScalar
outlet4Command = _Outlet4Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 5),
    _Outlet4Command_Type()
)
outlet4Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet4Command.setStatus("current")


class _Outlet5Command_Type(Integer32):
    """Custom type outlet5Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet5Command_Type.__name__ = "Integer32"
_Outlet5Command_Object = MibScalar
outlet5Command = _Outlet5Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 6),
    _Outlet5Command_Type()
)
outlet5Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet5Command.setStatus("current")


class _Outlet6Command_Type(Integer32):
    """Custom type outlet6Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet6Command_Type.__name__ = "Integer32"
_Outlet6Command_Object = MibScalar
outlet6Command = _Outlet6Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 7),
    _Outlet6Command_Type()
)
outlet6Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet6Command.setStatus("current")


class _Outlet7Command_Type(Integer32):
    """Custom type outlet7Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet7Command_Type.__name__ = "Integer32"
_Outlet7Command_Object = MibScalar
outlet7Command = _Outlet7Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 8),
    _Outlet7Command_Type()
)
outlet7Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet7Command.setStatus("current")


class _Outlet8Command_Type(Integer32):
    """Custom type outlet8Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet8Command_Type.__name__ = "Integer32"
_Outlet8Command_Object = MibScalar
outlet8Command = _Outlet8Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 9),
    _Outlet8Command_Type()
)
outlet8Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet8Command.setStatus("current")


class _Outlet9Command_Type(Integer32):
    """Custom type outlet9Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet9Command_Type.__name__ = "Integer32"
_Outlet9Command_Object = MibScalar
outlet9Command = _Outlet9Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 10),
    _Outlet9Command_Type()
)
outlet9Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet9Command.setStatus("current")


class _Outlet10Command_Type(Integer32):
    """Custom type outlet10Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet10Command_Type.__name__ = "Integer32"
_Outlet10Command_Object = MibScalar
outlet10Command = _Outlet10Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 11),
    _Outlet10Command_Type()
)
outlet10Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet10Command.setStatus("current")


class _Outlet11Command_Type(Integer32):
    """Custom type outlet11Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet11Command_Type.__name__ = "Integer32"
_Outlet11Command_Object = MibScalar
outlet11Command = _Outlet11Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 12),
    _Outlet11Command_Type()
)
outlet11Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet11Command.setStatus("current")


class _Outlet12Command_Type(Integer32):
    """Custom type outlet12Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("noChange", 4),
          ("reboot", 3))
    )


_Outlet12Command_Type.__name__ = "Integer32"
_Outlet12Command_Object = MibScalar
outlet12Command = _Outlet12Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 13),
    _Outlet12Command_Type()
)
outlet12Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet12Command.setStatus("current")


class _Outlet13Command_Type(Integer32):
    """Custom type outlet13Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet13Command_Type.__name__ = "Integer32"
_Outlet13Command_Object = MibScalar
outlet13Command = _Outlet13Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 14),
    _Outlet13Command_Type()
)
outlet13Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet13Command.setStatus("current")


class _Outlet14Command_Type(Integer32):
    """Custom type outlet14Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet14Command_Type.__name__ = "Integer32"
_Outlet14Command_Object = MibScalar
outlet14Command = _Outlet14Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 15),
    _Outlet14Command_Type()
)
outlet14Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet14Command.setStatus("current")


class _Outlet15Command_Type(Integer32):
    """Custom type outlet15Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet15Command_Type.__name__ = "Integer32"
_Outlet15Command_Object = MibScalar
outlet15Command = _Outlet15Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 16),
    _Outlet15Command_Type()
)
outlet15Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet15Command.setStatus("current")


class _Outlet16Command_Type(Integer32):
    """Custom type outlet16Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet16Command_Type.__name__ = "Integer32"
_Outlet16Command_Object = MibScalar
outlet16Command = _Outlet16Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 17),
    _Outlet16Command_Type()
)
outlet16Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet16Command.setStatus("current")


class _Outlet17Command_Type(Integer32):
    """Custom type outlet17Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet17Command_Type.__name__ = "Integer32"
_Outlet17Command_Object = MibScalar
outlet17Command = _Outlet17Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 18),
    _Outlet17Command_Type()
)
outlet17Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet17Command.setStatus("current")


class _Outlet18Command_Type(Integer32):
    """Custom type outlet18Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet18Command_Type.__name__ = "Integer32"
_Outlet18Command_Object = MibScalar
outlet18Command = _Outlet18Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 19),
    _Outlet18Command_Type()
)
outlet18Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet18Command.setStatus("current")


class _Outlet19Command_Type(Integer32):
    """Custom type outlet19Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet19Command_Type.__name__ = "Integer32"
_Outlet19Command_Object = MibScalar
outlet19Command = _Outlet19Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 20),
    _Outlet19Command_Type()
)
outlet19Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet19Command.setStatus("current")


class _Outlet20Command_Type(Integer32):
    """Custom type outlet20Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet20Command_Type.__name__ = "Integer32"
_Outlet20Command_Object = MibScalar
outlet20Command = _Outlet20Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 21),
    _Outlet20Command_Type()
)
outlet20Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet20Command.setStatus("current")


class _Outlet21Command_Type(Integer32):
    """Custom type outlet21Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet21Command_Type.__name__ = "Integer32"
_Outlet21Command_Object = MibScalar
outlet21Command = _Outlet21Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 22),
    _Outlet21Command_Type()
)
outlet21Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet21Command.setStatus("current")


class _Outlet22Command_Type(Integer32):
    """Custom type outlet22Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet22Command_Type.__name__ = "Integer32"
_Outlet22Command_Object = MibScalar
outlet22Command = _Outlet22Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 23),
    _Outlet22Command_Type()
)
outlet22Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet22Command.setStatus("current")


class _Outlet23Command_Type(Integer32):
    """Custom type outlet23Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet23Command_Type.__name__ = "Integer32"
_Outlet23Command_Object = MibScalar
outlet23Command = _Outlet23Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 24),
    _Outlet23Command_Type()
)
outlet23Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet23Command.setStatus("current")


class _Outlet24Command_Type(Integer32):
    """Custom type outlet24Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet24Command_Type.__name__ = "Integer32"
_Outlet24Command_Object = MibScalar
outlet24Command = _Outlet24Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 25),
    _Outlet24Command_Type()
)
outlet24Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet24Command.setStatus("current")


class _Outlet25Command_Type(Integer32):
    """Custom type outlet25Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet25Command_Type.__name__ = "Integer32"
_Outlet25Command_Object = MibScalar
outlet25Command = _Outlet25Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 26),
    _Outlet25Command_Type()
)
outlet25Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet25Command.setStatus("current")


class _Outlet26Command_Type(Integer32):
    """Custom type outlet26Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet26Command_Type.__name__ = "Integer32"
_Outlet26Command_Object = MibScalar
outlet26Command = _Outlet26Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 27),
    _Outlet26Command_Type()
)
outlet26Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet26Command.setStatus("current")


class _Outlet27Command_Type(Integer32):
    """Custom type outlet27Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet27Command_Type.__name__ = "Integer32"
_Outlet27Command_Object = MibScalar
outlet27Command = _Outlet27Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 28),
    _Outlet27Command_Type()
)
outlet27Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet27Command.setStatus("current")


class _Outlet28Command_Type(Integer32):
    """Custom type outlet28Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet28Command_Type.__name__ = "Integer32"
_Outlet28Command_Object = MibScalar
outlet28Command = _Outlet28Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 29),
    _Outlet28Command_Type()
)
outlet28Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet28Command.setStatus("current")


class _Outlet29Command_Type(Integer32):
    """Custom type outlet29Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet29Command_Type.__name__ = "Integer32"
_Outlet29Command_Object = MibScalar
outlet29Command = _Outlet29Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 30),
    _Outlet29Command_Type()
)
outlet29Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet29Command.setStatus("current")


class _Outlet30Command_Type(Integer32):
    """Custom type outlet30Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet30Command_Type.__name__ = "Integer32"
_Outlet30Command_Object = MibScalar
outlet30Command = _Outlet30Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 31),
    _Outlet30Command_Type()
)
outlet30Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet30Command.setStatus("current")


class _Outlet31Command_Type(Integer32):
    """Custom type outlet31Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet31Command_Type.__name__ = "Integer32"
_Outlet31Command_Object = MibScalar
outlet31Command = _Outlet31Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 32),
    _Outlet31Command_Type()
)
outlet31Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet31Command.setStatus("current")


class _Outlet32Command_Type(Integer32):
    """Custom type outlet32Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet32Command_Type.__name__ = "Integer32"
_Outlet32Command_Object = MibScalar
outlet32Command = _Outlet32Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 33),
    _Outlet32Command_Type()
)
outlet32Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet32Command.setStatus("current")


class _Outlet33Command_Type(Integer32):
    """Custom type outlet33Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet33Command_Type.__name__ = "Integer32"
_Outlet33Command_Object = MibScalar
outlet33Command = _Outlet33Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 34),
    _Outlet33Command_Type()
)
outlet33Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet33Command.setStatus("current")


class _Outlet34Command_Type(Integer32):
    """Custom type outlet34Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet34Command_Type.__name__ = "Integer32"
_Outlet34Command_Object = MibScalar
outlet34Command = _Outlet34Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 35),
    _Outlet34Command_Type()
)
outlet34Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet34Command.setStatus("current")


class _Outlet35Command_Type(Integer32):
    """Custom type outlet35Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet35Command_Type.__name__ = "Integer32"
_Outlet35Command_Object = MibScalar
outlet35Command = _Outlet35Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 36),
    _Outlet35Command_Type()
)
outlet35Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet35Command.setStatus("current")


class _Outlet36Command_Type(Integer32):
    """Custom type outlet36Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet36Command_Type.__name__ = "Integer32"
_Outlet36Command_Object = MibScalar
outlet36Command = _Outlet36Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 2, 37),
    _Outlet36Command_Type()
)
outlet36Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet36Command.setStatus("current")
_OutletStatus_ObjectIdentity = ObjectIdentity
outletStatus = _OutletStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3)
)


class _Outlet1Status_Type(Integer32):
    """Custom type outlet1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet1Status_Type.__name__ = "Integer32"
_Outlet1Status_Object = MibScalar
outlet1Status = _Outlet1Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 1),
    _Outlet1Status_Type()
)
outlet1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet1Status.setStatus("current")


class _Outlet2Status_Type(Integer32):
    """Custom type outlet2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet2Status_Type.__name__ = "Integer32"
_Outlet2Status_Object = MibScalar
outlet2Status = _Outlet2Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 2),
    _Outlet2Status_Type()
)
outlet2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet2Status.setStatus("current")


class _Outlet3Status_Type(Integer32):
    """Custom type outlet3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet3Status_Type.__name__ = "Integer32"
_Outlet3Status_Object = MibScalar
outlet3Status = _Outlet3Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 3),
    _Outlet3Status_Type()
)
outlet3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet3Status.setStatus("current")


class _Outlet4Status_Type(Integer32):
    """Custom type outlet4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet4Status_Type.__name__ = "Integer32"
_Outlet4Status_Object = MibScalar
outlet4Status = _Outlet4Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 4),
    _Outlet4Status_Type()
)
outlet4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet4Status.setStatus("current")


class _Outlet5Status_Type(Integer32):
    """Custom type outlet5Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet5Status_Type.__name__ = "Integer32"
_Outlet5Status_Object = MibScalar
outlet5Status = _Outlet5Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 5),
    _Outlet5Status_Type()
)
outlet5Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet5Status.setStatus("current")


class _Outlet6Status_Type(Integer32):
    """Custom type outlet6Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet6Status_Type.__name__ = "Integer32"
_Outlet6Status_Object = MibScalar
outlet6Status = _Outlet6Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 6),
    _Outlet6Status_Type()
)
outlet6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet6Status.setStatus("current")


class _Outlet7Status_Type(Integer32):
    """Custom type outlet7Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet7Status_Type.__name__ = "Integer32"
_Outlet7Status_Object = MibScalar
outlet7Status = _Outlet7Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 7),
    _Outlet7Status_Type()
)
outlet7Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet7Status.setStatus("current")


class _Outlet8Status_Type(Integer32):
    """Custom type outlet8Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet8Status_Type.__name__ = "Integer32"
_Outlet8Status_Object = MibScalar
outlet8Status = _Outlet8Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 8),
    _Outlet8Status_Type()
)
outlet8Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet8Status.setStatus("current")


class _Outlet9Status_Type(Integer32):
    """Custom type outlet9Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet9Status_Type.__name__ = "Integer32"
_Outlet9Status_Object = MibScalar
outlet9Status = _Outlet9Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 9),
    _Outlet9Status_Type()
)
outlet9Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet9Status.setStatus("current")


class _Outlet10Status_Type(Integer32):
    """Custom type outlet10Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet10Status_Type.__name__ = "Integer32"
_Outlet10Status_Object = MibScalar
outlet10Status = _Outlet10Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 10),
    _Outlet10Status_Type()
)
outlet10Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet10Status.setStatus("current")


class _Outlet11Status_Type(Integer32):
    """Custom type outlet11Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet11Status_Type.__name__ = "Integer32"
_Outlet11Status_Object = MibScalar
outlet11Status = _Outlet11Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 11),
    _Outlet11Status_Type()
)
outlet11Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet11Status.setStatus("current")


class _Outlet12Status_Type(Integer32):
    """Custom type outlet12Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet12Status_Type.__name__ = "Integer32"
_Outlet12Status_Object = MibScalar
outlet12Status = _Outlet12Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 12),
    _Outlet12Status_Type()
)
outlet12Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet12Status.setStatus("current")


class _Outlet13Status_Type(Integer32):
    """Custom type outlet13Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet13Status_Type.__name__ = "Integer32"
_Outlet13Status_Object = MibScalar
outlet13Status = _Outlet13Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 13),
    _Outlet13Status_Type()
)
outlet13Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet13Status.setStatus("current")


class _Outlet14Status_Type(Integer32):
    """Custom type outlet14Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet14Status_Type.__name__ = "Integer32"
_Outlet14Status_Object = MibScalar
outlet14Status = _Outlet14Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 14),
    _Outlet14Status_Type()
)
outlet14Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet14Status.setStatus("current")


class _Outlet15Status_Type(Integer32):
    """Custom type outlet15Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet15Status_Type.__name__ = "Integer32"
_Outlet15Status_Object = MibScalar
outlet15Status = _Outlet15Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 15),
    _Outlet15Status_Type()
)
outlet15Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet15Status.setStatus("current")


class _Outlet16Status_Type(Integer32):
    """Custom type outlet16Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet16Status_Type.__name__ = "Integer32"
_Outlet16Status_Object = MibScalar
outlet16Status = _Outlet16Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 16),
    _Outlet16Status_Type()
)
outlet16Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet16Status.setStatus("current")


class _Outlet17Status_Type(Integer32):
    """Custom type outlet17Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet17Status_Type.__name__ = "Integer32"
_Outlet17Status_Object = MibScalar
outlet17Status = _Outlet17Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 17),
    _Outlet17Status_Type()
)
outlet17Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet17Status.setStatus("current")


class _Outlet18Status_Type(Integer32):
    """Custom type outlet18Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet18Status_Type.__name__ = "Integer32"
_Outlet18Status_Object = MibScalar
outlet18Status = _Outlet18Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 18),
    _Outlet18Status_Type()
)
outlet18Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet18Status.setStatus("current")


class _Outlet19Status_Type(Integer32):
    """Custom type outlet19Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet19Status_Type.__name__ = "Integer32"
_Outlet19Status_Object = MibScalar
outlet19Status = _Outlet19Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 19),
    _Outlet19Status_Type()
)
outlet19Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet19Status.setStatus("current")


class _Outlet20Status_Type(Integer32):
    """Custom type outlet20Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet20Status_Type.__name__ = "Integer32"
_Outlet20Status_Object = MibScalar
outlet20Status = _Outlet20Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 20),
    _Outlet20Status_Type()
)
outlet20Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet20Status.setStatus("current")


class _Outlet21Status_Type(Integer32):
    """Custom type outlet21Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet21Status_Type.__name__ = "Integer32"
_Outlet21Status_Object = MibScalar
outlet21Status = _Outlet21Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 21),
    _Outlet21Status_Type()
)
outlet21Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet21Status.setStatus("current")


class _Outlet22Status_Type(Integer32):
    """Custom type outlet22Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet22Status_Type.__name__ = "Integer32"
_Outlet22Status_Object = MibScalar
outlet22Status = _Outlet22Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 22),
    _Outlet22Status_Type()
)
outlet22Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet22Status.setStatus("current")


class _Outlet23Status_Type(Integer32):
    """Custom type outlet23Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet23Status_Type.__name__ = "Integer32"
_Outlet23Status_Object = MibScalar
outlet23Status = _Outlet23Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 23),
    _Outlet23Status_Type()
)
outlet23Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet23Status.setStatus("current")


class _Outlet24Status_Type(Integer32):
    """Custom type outlet24Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet24Status_Type.__name__ = "Integer32"
_Outlet24Status_Object = MibScalar
outlet24Status = _Outlet24Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 24),
    _Outlet24Status_Type()
)
outlet24Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet24Status.setStatus("current")


class _Outlet25Status_Type(Integer32):
    """Custom type outlet25Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet25Status_Type.__name__ = "Integer32"
_Outlet25Status_Object = MibScalar
outlet25Status = _Outlet25Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 25),
    _Outlet25Status_Type()
)
outlet25Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet25Status.setStatus("current")


class _Outlet26Status_Type(Integer32):
    """Custom type outlet26Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet26Status_Type.__name__ = "Integer32"
_Outlet26Status_Object = MibScalar
outlet26Status = _Outlet26Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 26),
    _Outlet26Status_Type()
)
outlet26Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet26Status.setStatus("current")


class _Outlet27Status_Type(Integer32):
    """Custom type outlet27Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet27Status_Type.__name__ = "Integer32"
_Outlet27Status_Object = MibScalar
outlet27Status = _Outlet27Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 27),
    _Outlet27Status_Type()
)
outlet27Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet27Status.setStatus("current")


class _Outlet28Status_Type(Integer32):
    """Custom type outlet28Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet28Status_Type.__name__ = "Integer32"
_Outlet28Status_Object = MibScalar
outlet28Status = _Outlet28Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 28),
    _Outlet28Status_Type()
)
outlet28Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet28Status.setStatus("current")


class _Outlet29Status_Type(Integer32):
    """Custom type outlet29Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet29Status_Type.__name__ = "Integer32"
_Outlet29Status_Object = MibScalar
outlet29Status = _Outlet29Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 29),
    _Outlet29Status_Type()
)
outlet29Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet29Status.setStatus("current")


class _Outlet30Status_Type(Integer32):
    """Custom type outlet30Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet30Status_Type.__name__ = "Integer32"
_Outlet30Status_Object = MibScalar
outlet30Status = _Outlet30Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 30),
    _Outlet30Status_Type()
)
outlet30Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet30Status.setStatus("current")


class _Outlet31Status_Type(Integer32):
    """Custom type outlet31Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet31Status_Type.__name__ = "Integer32"
_Outlet31Status_Object = MibScalar
outlet31Status = _Outlet31Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 31),
    _Outlet31Status_Type()
)
outlet31Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet31Status.setStatus("current")


class _Outlet32Status_Type(Integer32):
    """Custom type outlet32Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet32Status_Type.__name__ = "Integer32"
_Outlet32Status_Object = MibScalar
outlet32Status = _Outlet32Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 32),
    _Outlet32Status_Type()
)
outlet32Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet32Status.setStatus("current")


class _Outlet33Status_Type(Integer32):
    """Custom type outlet33Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet33Status_Type.__name__ = "Integer32"
_Outlet33Status_Object = MibScalar
outlet33Status = _Outlet33Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 33),
    _Outlet33Status_Type()
)
outlet33Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet33Status.setStatus("current")


class _Outlet34Status_Type(Integer32):
    """Custom type outlet34Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet34Status_Type.__name__ = "Integer32"
_Outlet34Status_Object = MibScalar
outlet34Status = _Outlet34Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 34),
    _Outlet34Status_Type()
)
outlet34Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet34Status.setStatus("current")


class _Outlet35Status_Type(Integer32):
    """Custom type outlet35Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet35Status_Type.__name__ = "Integer32"
_Outlet35Status_Object = MibScalar
outlet35Status = _Outlet35Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 35),
    _Outlet35Status_Type()
)
outlet35Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet35Status.setStatus("current")


class _Outlet36Status_Type(Integer32):
    """Custom type outlet36Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Outlet36Status_Type.__name__ = "Integer32"
_Outlet36Status_Object = MibScalar
outlet36Status = _Outlet36Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 6, 3, 36),
    _Outlet36Status_Type()
)
outlet36Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet36Status.setStatus("current")
_SnmpSettings_ObjectIdentity = ObjectIdentity
snmpSettings = _SnmpSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7)
)


class _PublicCommunityName_Type(OctetString):
    """Custom type publicCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PublicCommunityName_Type.__name__ = "OctetString"
_PublicCommunityName_Object = MibScalar
publicCommunityName = _PublicCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 1),
    _PublicCommunityName_Type()
)
publicCommunityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    publicCommunityName.setStatus("obsolete")


class _PrivateCommunityName_Type(OctetString):
    """Custom type privateCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PrivateCommunityName_Type.__name__ = "OctetString"
_PrivateCommunityName_Object = MibScalar
privateCommunityName = _PrivateCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 2),
    _PrivateCommunityName_Type()
)
privateCommunityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    privateCommunityName.setStatus("obsolete")


class _TrapCommunityName_Type(OctetString):
    """Custom type trapCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TrapCommunityName_Type.__name__ = "OctetString"
_TrapCommunityName_Object = MibScalar
trapCommunityName = _TrapCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 3),
    _TrapCommunityName_Type()
)
trapCommunityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapCommunityName.setStatus("obsolete")


class _PublicCommunityPassword_Type(OctetString):
    """Custom type publicCommunityPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PublicCommunityPassword_Type.__name__ = "OctetString"
_PublicCommunityPassword_Object = MibScalar
publicCommunityPassword = _PublicCommunityPassword_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 4),
    _PublicCommunityPassword_Type()
)
publicCommunityPassword.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    publicCommunityPassword.setStatus("obsolete")


class _PrivateCommunityPassword_Type(OctetString):
    """Custom type privateCommunityPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PrivateCommunityPassword_Type.__name__ = "OctetString"
_PrivateCommunityPassword_Object = MibScalar
privateCommunityPassword = _PrivateCommunityPassword_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 5),
    _PrivateCommunityPassword_Type()
)
privateCommunityPassword.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    privateCommunityPassword.setStatus("obsolete")
_TrapIpAddress_Type = IpAddress
_TrapIpAddress_Object = MibScalar
trapIpAddress = _TrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 6),
    _TrapIpAddress_Type()
)
trapIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIpAddress.setStatus("current")


class _SnmpEnabled_Type(Integer32):
    """Custom type snmpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnmpEnabled_Type.__name__ = "Integer32"
_SnmpEnabled_Object = MibScalar
snmpEnabled = _SnmpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 7),
    _SnmpEnabled_Type()
)
snmpEnabled.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpEnabled.setStatus("obsolete")
_SnmpTraps_ObjectIdentity = ObjectIdentity
snmpTraps = _SnmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 8)
)


class _TrapUserLoginLogout_Type(Integer32):
    """Custom type trapUserLoginLogout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapUserLoginLogout_Type.__name__ = "Integer32"
_TrapUserLoginLogout_Object = MibScalar
trapUserLoginLogout = _TrapUserLoginLogout_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 8, 1),
    _TrapUserLoginLogout_Type()
)
trapUserLoginLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapUserLoginLogout.setStatus("current")


class _TrapFailedLogin_Type(Integer32):
    """Custom type trapFailedLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapFailedLogin_Type.__name__ = "Integer32"
_TrapFailedLogin_Object = MibScalar
trapFailedLogin = _TrapFailedLogin_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 8, 2),
    _TrapFailedLogin_Type()
)
trapFailedLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapFailedLogin.setStatus("current")


class _TrapOutletActivity_Type(Integer32):
    """Custom type trapOutletActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapOutletActivity_Type.__name__ = "Integer32"
_TrapOutletActivity_Object = MibScalar
trapOutletActivity = _TrapOutletActivity_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 8, 3),
    _TrapOutletActivity_Type()
)
trapOutletActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapOutletActivity.setStatus("current")


class _TrapSystemOnOff_Type(Integer32):
    """Custom type trapSystemOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapSystemOnOff_Type.__name__ = "Integer32"
_TrapSystemOnOff_Object = MibScalar
trapSystemOnOff = _TrapSystemOnOff_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 8, 4),
    _TrapSystemOnOff_Type()
)
trapSystemOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSystemOnOff.setStatus("current")


class _TrapOutletSection1Threshold_Type(Integer32):
    """Custom type trapOutletSection1Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapOutletSection1Threshold_Type.__name__ = "Integer32"
_TrapOutletSection1Threshold_Object = MibScalar
trapOutletSection1Threshold = _TrapOutletSection1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 8, 5),
    _TrapOutletSection1Threshold_Type()
)
trapOutletSection1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapOutletSection1Threshold.setStatus("current")


class _TrapOutletSection2Threshold_Type(Integer32):
    """Custom type trapOutletSection2Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapOutletSection2Threshold_Type.__name__ = "Integer32"
_TrapOutletSection2Threshold_Object = MibScalar
trapOutletSection2Threshold = _TrapOutletSection2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 8, 6),
    _TrapOutletSection2Threshold_Type()
)
trapOutletSection2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapOutletSection2Threshold.setStatus("current")


class _TrapOutletSection3Threshold_Type(Integer32):
    """Custom type trapOutletSection3Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapOutletSection3Threshold_Type.__name__ = "Integer32"
_TrapOutletSection3Threshold_Object = MibScalar
trapOutletSection3Threshold = _TrapOutletSection3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 8, 7),
    _TrapOutletSection3Threshold_Type()
)
trapOutletSection3Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapOutletSection3Threshold.setStatus("current")


class _TrapTemperatureSensor1Threshold_Type(Integer32):
    """Custom type trapTemperatureSensor1Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapTemperatureSensor1Threshold_Type.__name__ = "Integer32"
_TrapTemperatureSensor1Threshold_Object = MibScalar
trapTemperatureSensor1Threshold = _TrapTemperatureSensor1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 8, 8),
    _TrapTemperatureSensor1Threshold_Type()
)
trapTemperatureSensor1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapTemperatureSensor1Threshold.setStatus("current")


class _TrapTemperatureSensor2Threshold_Type(Integer32):
    """Custom type trapTemperatureSensor2Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapTemperatureSensor2Threshold_Type.__name__ = "Integer32"
_TrapTemperatureSensor2Threshold_Object = MibScalar
trapTemperatureSensor2Threshold = _TrapTemperatureSensor2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 8, 9),
    _TrapTemperatureSensor2Threshold_Type()
)
trapTemperatureSensor2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapTemperatureSensor2Threshold.setStatus("current")


class _TrapHumiditySensorThreshold_Type(Integer32):
    """Custom type trapHumiditySensorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapHumiditySensorThreshold_Type.__name__ = "Integer32"
_TrapHumiditySensorThreshold_Object = MibScalar
trapHumiditySensorThreshold = _TrapHumiditySensorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 8, 10),
    _TrapHumiditySensorThreshold_Type()
)
trapHumiditySensorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapHumiditySensorThreshold.setStatus("current")


class _TrapContactClosure1Threshold_Type(Integer32):
    """Custom type trapContactClosure1Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapContactClosure1Threshold_Type.__name__ = "Integer32"
_TrapContactClosure1Threshold_Object = MibScalar
trapContactClosure1Threshold = _TrapContactClosure1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 8, 11),
    _TrapContactClosure1Threshold_Type()
)
trapContactClosure1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapContactClosure1Threshold.setStatus("current")


class _TrapContactClosure2Threshold_Type(Integer32):
    """Custom type trapContactClosure2Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapContactClosure2Threshold_Type.__name__ = "Integer32"
_TrapContactClosure2Threshold_Object = MibScalar
trapContactClosure2Threshold = _TrapContactClosure2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 8, 12),
    _TrapContactClosure2Threshold_Type()
)
trapContactClosure2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapContactClosure2Threshold.setStatus("current")


class _TrapContactClosure3Threshold_Type(Integer32):
    """Custom type trapContactClosure3Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapContactClosure3Threshold_Type.__name__ = "Integer32"
_TrapContactClosure3Threshold_Object = MibScalar
trapContactClosure3Threshold = _TrapContactClosure3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 7, 8, 13),
    _TrapContactClosure3Threshold_Type()
)
trapContactClosure3Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapContactClosure3Threshold.setStatus("current")
_EnvironmentalSettings_ObjectIdentity = ObjectIdentity
environmentalSettings = _EnvironmentalSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8)
)
_TemperatureSensorConfig_ObjectIdentity = ObjectIdentity
temperatureSensorConfig = _TemperatureSensorConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1)
)
_TempSensor1_ObjectIdentity = ObjectIdentity
tempSensor1 = _TempSensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 1)
)


class _TempSensor1Name_Type(OctetString):
    """Custom type tempSensor1Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TempSensor1Name_Type.__name__ = "OctetString"
_TempSensor1Name_Object = MibScalar
tempSensor1Name = _TempSensor1Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 1, 1),
    _TempSensor1Name_Type()
)
tempSensor1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor1Name.setStatus("current")


class _TempSensor1Enable_Type(Integer32):
    """Custom type tempSensor1Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TempSensor1Enable_Type.__name__ = "Integer32"
_TempSensor1Enable_Object = MibScalar
tempSensor1Enable = _TempSensor1Enable_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 1, 2),
    _TempSensor1Enable_Type()
)
tempSensor1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor1Enable.setStatus("current")


class _TempSensor1HighThresh_Type(Integer32):
    """Custom type tempSensor1HighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 300),
    )


_TempSensor1HighThresh_Type.__name__ = "Integer32"
_TempSensor1HighThresh_Object = MibScalar
tempSensor1HighThresh = _TempSensor1HighThresh_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 1, 3),
    _TempSensor1HighThresh_Type()
)
tempSensor1HighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor1HighThresh.setStatus("current")


class _TempSensor1LowThresh_Type(Integer32):
    """Custom type tempSensor1LowThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 300),
    )


_TempSensor1LowThresh_Type.__name__ = "Integer32"
_TempSensor1LowThresh_Object = MibScalar
tempSensor1LowThresh = _TempSensor1LowThresh_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 1, 4),
    _TempSensor1LowThresh_Type()
)
tempSensor1LowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor1LowThresh.setStatus("current")


class _TempSensor1ControlOutlet_Type(Integer32):
    """Custom type tempSensor1ControlOutlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TempSensor1ControlOutlet_Type.__name__ = "Integer32"
_TempSensor1ControlOutlet_Object = MibScalar
tempSensor1ControlOutlet = _TempSensor1ControlOutlet_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 1, 5),
    _TempSensor1ControlOutlet_Type()
)
tempSensor1ControlOutlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor1ControlOutlet.setStatus("current")


class _TempSensor1OutletName_Type(OctetString):
    """Custom type tempSensor1OutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TempSensor1OutletName_Type.__name__ = "OctetString"
_TempSensor1OutletName_Object = MibScalar
tempSensor1OutletName = _TempSensor1OutletName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 1, 6),
    _TempSensor1OutletName_Type()
)
tempSensor1OutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor1OutletName.setStatus("current")


class _TempSensor1OutletState_Type(Integer32):
    """Custom type tempSensor1OutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("turnOutletOff", 1),
          ("turnOutletOn", 0))
    )


_TempSensor1OutletState_Type.__name__ = "Integer32"
_TempSensor1OutletState_Object = MibScalar
tempSensor1OutletState = _TempSensor1OutletState_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 1, 7),
    _TempSensor1OutletState_Type()
)
tempSensor1OutletState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor1OutletState.setStatus("current")
_TempSensor2_ObjectIdentity = ObjectIdentity
tempSensor2 = _TempSensor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 2)
)


class _TempSensor2Name_Type(OctetString):
    """Custom type tempSensor2Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TempSensor2Name_Type.__name__ = "OctetString"
_TempSensor2Name_Object = MibScalar
tempSensor2Name = _TempSensor2Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 2, 1),
    _TempSensor2Name_Type()
)
tempSensor2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor2Name.setStatus("current")


class _TempSensor2Enable_Type(Integer32):
    """Custom type tempSensor2Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TempSensor2Enable_Type.__name__ = "Integer32"
_TempSensor2Enable_Object = MibScalar
tempSensor2Enable = _TempSensor2Enable_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 2, 2),
    _TempSensor2Enable_Type()
)
tempSensor2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor2Enable.setStatus("current")


class _TempSensor2HighThresh_Type(Integer32):
    """Custom type tempSensor2HighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 300),
    )


_TempSensor2HighThresh_Type.__name__ = "Integer32"
_TempSensor2HighThresh_Object = MibScalar
tempSensor2HighThresh = _TempSensor2HighThresh_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 2, 3),
    _TempSensor2HighThresh_Type()
)
tempSensor2HighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor2HighThresh.setStatus("current")


class _TempSensor2LowThresh_Type(Integer32):
    """Custom type tempSensor2LowThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 300),
    )


_TempSensor2LowThresh_Type.__name__ = "Integer32"
_TempSensor2LowThresh_Object = MibScalar
tempSensor2LowThresh = _TempSensor2LowThresh_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 2, 4),
    _TempSensor2LowThresh_Type()
)
tempSensor2LowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor2LowThresh.setStatus("current")


class _TempSensor2ControlOutlet_Type(Integer32):
    """Custom type tempSensor2ControlOutlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TempSensor2ControlOutlet_Type.__name__ = "Integer32"
_TempSensor2ControlOutlet_Object = MibScalar
tempSensor2ControlOutlet = _TempSensor2ControlOutlet_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 2, 5),
    _TempSensor2ControlOutlet_Type()
)
tempSensor2ControlOutlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor2ControlOutlet.setStatus("current")


class _TempSensor2OutletName_Type(OctetString):
    """Custom type tempSensor2OutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TempSensor2OutletName_Type.__name__ = "OctetString"
_TempSensor2OutletName_Object = MibScalar
tempSensor2OutletName = _TempSensor2OutletName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 2, 6),
    _TempSensor2OutletName_Type()
)
tempSensor2OutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor2OutletName.setStatus("current")


class _TempSensor2OutletState_Type(Integer32):
    """Custom type tempSensor2OutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("turnOutletOff", 1),
          ("turnOutletOn", 0))
    )


_TempSensor2OutletState_Type.__name__ = "Integer32"
_TempSensor2OutletState_Object = MibScalar
tempSensor2OutletState = _TempSensor2OutletState_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 1, 2, 7),
    _TempSensor2OutletState_Type()
)
tempSensor2OutletState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensor2OutletState.setStatus("current")
_HumiditySensorConfig_ObjectIdentity = ObjectIdentity
humiditySensorConfig = _HumiditySensorConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 2)
)
_HumSensor1_ObjectIdentity = ObjectIdentity
humSensor1 = _HumSensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 2, 1)
)


class _HumSensor1Name_Type(OctetString):
    """Custom type humSensor1Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HumSensor1Name_Type.__name__ = "OctetString"
_HumSensor1Name_Object = MibScalar
humSensor1Name = _HumSensor1Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 2, 1, 1),
    _HumSensor1Name_Type()
)
humSensor1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humSensor1Name.setStatus("current")


class _HumSensor1Enable_Type(Integer32):
    """Custom type humSensor1Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HumSensor1Enable_Type.__name__ = "Integer32"
_HumSensor1Enable_Object = MibScalar
humSensor1Enable = _HumSensor1Enable_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 2, 1, 2),
    _HumSensor1Enable_Type()
)
humSensor1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humSensor1Enable.setStatus("current")


class _HumSensor1HighThresh_Type(Integer32):
    """Custom type humSensor1HighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HumSensor1HighThresh_Type.__name__ = "Integer32"
_HumSensor1HighThresh_Object = MibScalar
humSensor1HighThresh = _HumSensor1HighThresh_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 2, 1, 3),
    _HumSensor1HighThresh_Type()
)
humSensor1HighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humSensor1HighThresh.setStatus("current")


class _HumSensor1LowThresh_Type(Integer32):
    """Custom type humSensor1LowThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HumSensor1LowThresh_Type.__name__ = "Integer32"
_HumSensor1LowThresh_Object = MibScalar
humSensor1LowThresh = _HumSensor1LowThresh_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 2, 1, 4),
    _HumSensor1LowThresh_Type()
)
humSensor1LowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humSensor1LowThresh.setStatus("current")


class _HumSensor1ControlOutlet_Type(Integer32):
    """Custom type humSensor1ControlOutlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HumSensor1ControlOutlet_Type.__name__ = "Integer32"
_HumSensor1ControlOutlet_Object = MibScalar
humSensor1ControlOutlet = _HumSensor1ControlOutlet_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 2, 1, 5),
    _HumSensor1ControlOutlet_Type()
)
humSensor1ControlOutlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humSensor1ControlOutlet.setStatus("current")


class _HumSensor1OutletName_Type(OctetString):
    """Custom type humSensor1OutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HumSensor1OutletName_Type.__name__ = "OctetString"
_HumSensor1OutletName_Object = MibScalar
humSensor1OutletName = _HumSensor1OutletName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 2, 1, 6),
    _HumSensor1OutletName_Type()
)
humSensor1OutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humSensor1OutletName.setStatus("current")


class _HumSensor1OutletState_Type(Integer32):
    """Custom type humSensor1OutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("turnOutletOff", 1),
          ("turnOutletOn", 0))
    )


_HumSensor1OutletState_Type.__name__ = "Integer32"
_HumSensor1OutletState_Object = MibScalar
humSensor1OutletState = _HumSensor1OutletState_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 2, 1, 7),
    _HumSensor1OutletState_Type()
)
humSensor1OutletState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humSensor1OutletState.setStatus("current")
_ContactClosureConfig_ObjectIdentity = ObjectIdentity
contactClosureConfig = _ContactClosureConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3)
)
_ContactClosure1_ObjectIdentity = ObjectIdentity
contactClosure1 = _ContactClosure1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 1)
)


class _ContactClosure1Name_Type(OctetString):
    """Custom type contactClosure1Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ContactClosure1Name_Type.__name__ = "OctetString"
_ContactClosure1Name_Object = MibScalar
contactClosure1Name = _ContactClosure1Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 1, 1),
    _ContactClosure1Name_Type()
)
contactClosure1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure1Name.setStatus("current")


class _ContactClosure1Enable_Type(Integer32):
    """Custom type contactClosure1Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ContactClosure1Enable_Type.__name__ = "Integer32"
_ContactClosure1Enable_Object = MibScalar
contactClosure1Enable = _ContactClosure1Enable_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 1, 2),
    _ContactClosure1Enable_Type()
)
contactClosure1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure1Enable.setStatus("current")


class _ContactClosure1ControlOutlet_Type(Integer32):
    """Custom type contactClosure1ControlOutlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ContactClosure1ControlOutlet_Type.__name__ = "Integer32"
_ContactClosure1ControlOutlet_Object = MibScalar
contactClosure1ControlOutlet = _ContactClosure1ControlOutlet_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 1, 3),
    _ContactClosure1ControlOutlet_Type()
)
contactClosure1ControlOutlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure1ControlOutlet.setStatus("current")


class _ContactClosure1OutletName_Type(OctetString):
    """Custom type contactClosure1OutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ContactClosure1OutletName_Type.__name__ = "OctetString"
_ContactClosure1OutletName_Object = MibScalar
contactClosure1OutletName = _ContactClosure1OutletName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 1, 4),
    _ContactClosure1OutletName_Type()
)
contactClosure1OutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure1OutletName.setStatus("current")


class _ContactClosure1OutletState_Type(Integer32):
    """Custom type contactClosure1OutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("turnOutletOff", 1),
          ("turnOutletOn", 0))
    )


_ContactClosure1OutletState_Type.__name__ = "Integer32"
_ContactClosure1OutletState_Object = MibScalar
contactClosure1OutletState = _ContactClosure1OutletState_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 1, 5),
    _ContactClosure1OutletState_Type()
)
contactClosure1OutletState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure1OutletState.setStatus("current")
_ContactClosure2_ObjectIdentity = ObjectIdentity
contactClosure2 = _ContactClosure2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 2)
)


class _ContactClosure2Name_Type(OctetString):
    """Custom type contactClosure2Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ContactClosure2Name_Type.__name__ = "OctetString"
_ContactClosure2Name_Object = MibScalar
contactClosure2Name = _ContactClosure2Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 2, 1),
    _ContactClosure2Name_Type()
)
contactClosure2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure2Name.setStatus("current")


class _ContactClosure2Enable_Type(Integer32):
    """Custom type contactClosure2Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ContactClosure2Enable_Type.__name__ = "Integer32"
_ContactClosure2Enable_Object = MibScalar
contactClosure2Enable = _ContactClosure2Enable_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 2, 2),
    _ContactClosure2Enable_Type()
)
contactClosure2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure2Enable.setStatus("current")


class _ContactClosure2ControlOutlet_Type(Integer32):
    """Custom type contactClosure2ControlOutlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ContactClosure2ControlOutlet_Type.__name__ = "Integer32"
_ContactClosure2ControlOutlet_Object = MibScalar
contactClosure2ControlOutlet = _ContactClosure2ControlOutlet_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 2, 3),
    _ContactClosure2ControlOutlet_Type()
)
contactClosure2ControlOutlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure2ControlOutlet.setStatus("current")


class _ContactClosure2OutletName_Type(OctetString):
    """Custom type contactClosure2OutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ContactClosure2OutletName_Type.__name__ = "OctetString"
_ContactClosure2OutletName_Object = MibScalar
contactClosure2OutletName = _ContactClosure2OutletName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 2, 4),
    _ContactClosure2OutletName_Type()
)
contactClosure2OutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure2OutletName.setStatus("current")


class _ContactClosure2OutletState_Type(Integer32):
    """Custom type contactClosure2OutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("turnOutletOff", 1),
          ("turnOutletOn", 0))
    )


_ContactClosure2OutletState_Type.__name__ = "Integer32"
_ContactClosure2OutletState_Object = MibScalar
contactClosure2OutletState = _ContactClosure2OutletState_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 2, 5),
    _ContactClosure2OutletState_Type()
)
contactClosure2OutletState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure2OutletState.setStatus("current")
_ContactClosure3_ObjectIdentity = ObjectIdentity
contactClosure3 = _ContactClosure3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 3)
)


class _ContactClosure3Name_Type(OctetString):
    """Custom type contactClosure3Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ContactClosure3Name_Type.__name__ = "OctetString"
_ContactClosure3Name_Object = MibScalar
contactClosure3Name = _ContactClosure3Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 3, 1),
    _ContactClosure3Name_Type()
)
contactClosure3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure3Name.setStatus("current")


class _ContactClosure3Enable_Type(Integer32):
    """Custom type contactClosure3Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ContactClosure3Enable_Type.__name__ = "Integer32"
_ContactClosure3Enable_Object = MibScalar
contactClosure3Enable = _ContactClosure3Enable_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 3, 2),
    _ContactClosure3Enable_Type()
)
contactClosure3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure3Enable.setStatus("current")


class _ContactClosure3ControlOutlet_Type(Integer32):
    """Custom type contactClosure3ControlOutlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ContactClosure3ControlOutlet_Type.__name__ = "Integer32"
_ContactClosure3ControlOutlet_Object = MibScalar
contactClosure3ControlOutlet = _ContactClosure3ControlOutlet_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 3, 3),
    _ContactClosure3ControlOutlet_Type()
)
contactClosure3ControlOutlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure3ControlOutlet.setStatus("current")


class _ContactClosure3OutletName_Type(OctetString):
    """Custom type contactClosure3OutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ContactClosure3OutletName_Type.__name__ = "OctetString"
_ContactClosure3OutletName_Object = MibScalar
contactClosure3OutletName = _ContactClosure3OutletName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 3, 4),
    _ContactClosure3OutletName_Type()
)
contactClosure3OutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure3OutletName.setStatus("current")


class _ContactClosure3OutletState_Type(Integer32):
    """Custom type contactClosure3OutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("turnOutletOff", 1),
          ("turnOutletOn", 0))
    )


_ContactClosure3OutletState_Type.__name__ = "Integer32"
_ContactClosure3OutletState_Object = MibScalar
contactClosure3OutletState = _ContactClosure3OutletState_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 3, 3, 5),
    _ContactClosure3OutletState_Type()
)
contactClosure3OutletState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosure3OutletState.setStatus("current")
_OutletSectionConfig_ObjectIdentity = ObjectIdentity
outletSectionConfig = _OutletSectionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4)
)
_OutletSection1Config_ObjectIdentity = ObjectIdentity
outletSection1Config = _OutletSection1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 1)
)
_OutletSection1VoltageHighThreshold_Type = Integer32
_OutletSection1VoltageHighThreshold_Object = MibScalar
outletSection1VoltageHighThreshold = _OutletSection1VoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 1, 1),
    _OutletSection1VoltageHighThreshold_Type()
)
outletSection1VoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection1VoltageHighThreshold.setStatus("current")
_OutletSection1VoltageLowThreshold_Type = Integer32
_OutletSection1VoltageLowThreshold_Object = MibScalar
outletSection1VoltageLowThreshold = _OutletSection1VoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 1, 2),
    _OutletSection1VoltageLowThreshold_Type()
)
outletSection1VoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection1VoltageLowThreshold.setStatus("current")


class _OutletSection1CurrentHighThreshold_Type(Integer32):
    """Custom type outletSection1CurrentHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_OutletSection1CurrentHighThreshold_Type.__name__ = "Integer32"
_OutletSection1CurrentHighThreshold_Object = MibScalar
outletSection1CurrentHighThreshold = _OutletSection1CurrentHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 1, 3),
    _OutletSection1CurrentHighThreshold_Type()
)
outletSection1CurrentHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection1CurrentHighThreshold.setStatus("current")


class _OutletSection1CurrentLowThreshold_Type(Integer32):
    """Custom type outletSection1CurrentLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_OutletSection1CurrentLowThreshold_Type.__name__ = "Integer32"
_OutletSection1CurrentLowThreshold_Object = MibScalar
outletSection1CurrentLowThreshold = _OutletSection1CurrentLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 1, 4),
    _OutletSection1CurrentLowThreshold_Type()
)
outletSection1CurrentLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection1CurrentLowThreshold.setStatus("current")


class _OutletSection1ControlOutlet_Type(Integer32):
    """Custom type outletSection1ControlOutlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_OutletSection1ControlOutlet_Type.__name__ = "Integer32"
_OutletSection1ControlOutlet_Object = MibScalar
outletSection1ControlOutlet = _OutletSection1ControlOutlet_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 1, 5),
    _OutletSection1ControlOutlet_Type()
)
outletSection1ControlOutlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection1ControlOutlet.setStatus("current")


class _OutletSection1OutletName_Type(OctetString):
    """Custom type outletSection1OutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_OutletSection1OutletName_Type.__name__ = "OctetString"
_OutletSection1OutletName_Object = MibScalar
outletSection1OutletName = _OutletSection1OutletName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 1, 6),
    _OutletSection1OutletName_Type()
)
outletSection1OutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection1OutletName.setStatus("current")
_OutletSection2Config_ObjectIdentity = ObjectIdentity
outletSection2Config = _OutletSection2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 2)
)
_OutletSection2VoltageHighThreshold_Type = Integer32
_OutletSection2VoltageHighThreshold_Object = MibScalar
outletSection2VoltageHighThreshold = _OutletSection2VoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 2, 1),
    _OutletSection2VoltageHighThreshold_Type()
)
outletSection2VoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection2VoltageHighThreshold.setStatus("current")
_OutletSection2VoltageLowThreshold_Type = Integer32
_OutletSection2VoltageLowThreshold_Object = MibScalar
outletSection2VoltageLowThreshold = _OutletSection2VoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 2, 2),
    _OutletSection2VoltageLowThreshold_Type()
)
outletSection2VoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection2VoltageLowThreshold.setStatus("current")


class _OutletSection2CurrentHighThreshold_Type(Integer32):
    """Custom type outletSection2CurrentHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_OutletSection2CurrentHighThreshold_Type.__name__ = "Integer32"
_OutletSection2CurrentHighThreshold_Object = MibScalar
outletSection2CurrentHighThreshold = _OutletSection2CurrentHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 2, 3),
    _OutletSection2CurrentHighThreshold_Type()
)
outletSection2CurrentHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection2CurrentHighThreshold.setStatus("current")


class _OutletSection2CurrentLowThreshold_Type(Integer32):
    """Custom type outletSection2CurrentLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_OutletSection2CurrentLowThreshold_Type.__name__ = "Integer32"
_OutletSection2CurrentLowThreshold_Object = MibScalar
outletSection2CurrentLowThreshold = _OutletSection2CurrentLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 2, 4),
    _OutletSection2CurrentLowThreshold_Type()
)
outletSection2CurrentLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection2CurrentLowThreshold.setStatus("current")


class _OutletSection2ControlOutlet_Type(Integer32):
    """Custom type outletSection2ControlOutlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_OutletSection2ControlOutlet_Type.__name__ = "Integer32"
_OutletSection2ControlOutlet_Object = MibScalar
outletSection2ControlOutlet = _OutletSection2ControlOutlet_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 2, 5),
    _OutletSection2ControlOutlet_Type()
)
outletSection2ControlOutlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection2ControlOutlet.setStatus("current")


class _OutletSection2OutletName_Type(OctetString):
    """Custom type outletSection2OutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_OutletSection2OutletName_Type.__name__ = "OctetString"
_OutletSection2OutletName_Object = MibScalar
outletSection2OutletName = _OutletSection2OutletName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 2, 6),
    _OutletSection2OutletName_Type()
)
outletSection2OutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection2OutletName.setStatus("current")
_OutletSection3Config_ObjectIdentity = ObjectIdentity
outletSection3Config = _OutletSection3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 3)
)
_OutletSection3VoltageHighThreshold_Type = Integer32
_OutletSection3VoltageHighThreshold_Object = MibScalar
outletSection3VoltageHighThreshold = _OutletSection3VoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 3, 1),
    _OutletSection3VoltageHighThreshold_Type()
)
outletSection3VoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection3VoltageHighThreshold.setStatus("current")
_OutletSection3VoltageLowThreshold_Type = Integer32
_OutletSection3VoltageLowThreshold_Object = MibScalar
outletSection3VoltageLowThreshold = _OutletSection3VoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 3, 2),
    _OutletSection3VoltageLowThreshold_Type()
)
outletSection3VoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection3VoltageLowThreshold.setStatus("current")


class _OutletSection3CurrentHighThreshold_Type(Integer32):
    """Custom type outletSection3CurrentHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_OutletSection3CurrentHighThreshold_Type.__name__ = "Integer32"
_OutletSection3CurrentHighThreshold_Object = MibScalar
outletSection3CurrentHighThreshold = _OutletSection3CurrentHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 3, 3),
    _OutletSection3CurrentHighThreshold_Type()
)
outletSection3CurrentHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection3CurrentHighThreshold.setStatus("current")


class _OutletSection3CurrentLowThreshold_Type(Integer32):
    """Custom type outletSection3CurrentLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_OutletSection3CurrentLowThreshold_Type.__name__ = "Integer32"
_OutletSection3CurrentLowThreshold_Object = MibScalar
outletSection3CurrentLowThreshold = _OutletSection3CurrentLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 3, 4),
    _OutletSection3CurrentLowThreshold_Type()
)
outletSection3CurrentLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection3CurrentLowThreshold.setStatus("current")


class _OutletSection3ControlOutlet_Type(Integer32):
    """Custom type outletSection3ControlOutlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_OutletSection3ControlOutlet_Type.__name__ = "Integer32"
_OutletSection3ControlOutlet_Object = MibScalar
outletSection3ControlOutlet = _OutletSection3ControlOutlet_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 3, 5),
    _OutletSection3ControlOutlet_Type()
)
outletSection3ControlOutlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection3ControlOutlet.setStatus("current")


class _OutletSection3OutletName_Type(OctetString):
    """Custom type outletSection3OutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_OutletSection3OutletName_Type.__name__ = "OctetString"
_OutletSection3OutletName_Object = MibScalar
outletSection3OutletName = _OutletSection3OutletName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 3, 6),
    _OutletSection3OutletName_Type()
)
outletSection3OutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection3OutletName.setStatus("current")
_OutletSection4Config_ObjectIdentity = ObjectIdentity
outletSection4Config = _OutletSection4Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 4)
)
_OutletSection4VoltageHighThreshold_Type = Integer32
_OutletSection4VoltageHighThreshold_Object = MibScalar
outletSection4VoltageHighThreshold = _OutletSection4VoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 4, 1),
    _OutletSection4VoltageHighThreshold_Type()
)
outletSection4VoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection4VoltageHighThreshold.setStatus("current")
_OutletSection4VoltageLowThreshold_Type = Integer32
_OutletSection4VoltageLowThreshold_Object = MibScalar
outletSection4VoltageLowThreshold = _OutletSection4VoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 4, 2),
    _OutletSection4VoltageLowThreshold_Type()
)
outletSection4VoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection4VoltageLowThreshold.setStatus("current")


class _OutletSection4CurrentHighThreshold_Type(Integer32):
    """Custom type outletSection4CurrentHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_OutletSection4CurrentHighThreshold_Type.__name__ = "Integer32"
_OutletSection4CurrentHighThreshold_Object = MibScalar
outletSection4CurrentHighThreshold = _OutletSection4CurrentHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 4, 3),
    _OutletSection4CurrentHighThreshold_Type()
)
outletSection4CurrentHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection4CurrentHighThreshold.setStatus("current")


class _OutletSection4CurrentLowThreshold_Type(Integer32):
    """Custom type outletSection4CurrentLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_OutletSection4CurrentLowThreshold_Type.__name__ = "Integer32"
_OutletSection4CurrentLowThreshold_Object = MibScalar
outletSection4CurrentLowThreshold = _OutletSection4CurrentLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 4, 4),
    _OutletSection4CurrentLowThreshold_Type()
)
outletSection4CurrentLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection4CurrentLowThreshold.setStatus("current")


class _OutletSection4ControlOutlet_Type(Integer32):
    """Custom type outletSection4ControlOutlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_OutletSection4ControlOutlet_Type.__name__ = "Integer32"
_OutletSection4ControlOutlet_Object = MibScalar
outletSection4ControlOutlet = _OutletSection4ControlOutlet_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 4, 5),
    _OutletSection4ControlOutlet_Type()
)
outletSection4ControlOutlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection4ControlOutlet.setStatus("current")


class _OutletSection4OutletName_Type(OctetString):
    """Custom type outletSection4OutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_OutletSection4OutletName_Type.__name__ = "OctetString"
_OutletSection4OutletName_Object = MibScalar
outletSection4OutletName = _OutletSection4OutletName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 4, 6),
    _OutletSection4OutletName_Type()
)
outletSection4OutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection4OutletName.setStatus("current")
_OutletSection5Config_ObjectIdentity = ObjectIdentity
outletSection5Config = _OutletSection5Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 5)
)
_OutletSection5VoltageHighThreshold_Type = Integer32
_OutletSection5VoltageHighThreshold_Object = MibScalar
outletSection5VoltageHighThreshold = _OutletSection5VoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 5, 1),
    _OutletSection5VoltageHighThreshold_Type()
)
outletSection5VoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection5VoltageHighThreshold.setStatus("current")
_OutletSection5VoltageLowThreshold_Type = Integer32
_OutletSection5VoltageLowThreshold_Object = MibScalar
outletSection5VoltageLowThreshold = _OutletSection5VoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 5, 2),
    _OutletSection5VoltageLowThreshold_Type()
)
outletSection5VoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection5VoltageLowThreshold.setStatus("current")


class _OutletSection5CurrentHighThreshold_Type(Integer32):
    """Custom type outletSection5CurrentHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_OutletSection5CurrentHighThreshold_Type.__name__ = "Integer32"
_OutletSection5CurrentHighThreshold_Object = MibScalar
outletSection5CurrentHighThreshold = _OutletSection5CurrentHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 5, 3),
    _OutletSection5CurrentHighThreshold_Type()
)
outletSection5CurrentHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection5CurrentHighThreshold.setStatus("current")


class _OutletSection5CurrentLowThreshold_Type(Integer32):
    """Custom type outletSection5CurrentLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_OutletSection5CurrentLowThreshold_Type.__name__ = "Integer32"
_OutletSection5CurrentLowThreshold_Object = MibScalar
outletSection5CurrentLowThreshold = _OutletSection5CurrentLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 5, 4),
    _OutletSection5CurrentLowThreshold_Type()
)
outletSection5CurrentLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection5CurrentLowThreshold.setStatus("current")


class _OutletSection5ControlOutlet_Type(Integer32):
    """Custom type outletSection5ControlOutlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_OutletSection5ControlOutlet_Type.__name__ = "Integer32"
_OutletSection5ControlOutlet_Object = MibScalar
outletSection5ControlOutlet = _OutletSection5ControlOutlet_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 5, 5),
    _OutletSection5ControlOutlet_Type()
)
outletSection5ControlOutlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection5ControlOutlet.setStatus("current")


class _OutletSection5OutletName_Type(OctetString):
    """Custom type outletSection5OutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_OutletSection5OutletName_Type.__name__ = "OctetString"
_OutletSection5OutletName_Object = MibScalar
outletSection5OutletName = _OutletSection5OutletName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 5, 6),
    _OutletSection5OutletName_Type()
)
outletSection5OutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection5OutletName.setStatus("current")
_OutletSection6Config_ObjectIdentity = ObjectIdentity
outletSection6Config = _OutletSection6Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 6)
)
_OutletSection6VoltageHighThreshold_Type = Integer32
_OutletSection6VoltageHighThreshold_Object = MibScalar
outletSection6VoltageHighThreshold = _OutletSection6VoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 6, 1),
    _OutletSection6VoltageHighThreshold_Type()
)
outletSection6VoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection6VoltageHighThreshold.setStatus("current")
_OutletSection6VoltageLowThreshold_Type = Integer32
_OutletSection6VoltageLowThreshold_Object = MibScalar
outletSection6VoltageLowThreshold = _OutletSection6VoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 6, 2),
    _OutletSection6VoltageLowThreshold_Type()
)
outletSection6VoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection6VoltageLowThreshold.setStatus("current")


class _OutletSection6CurrentHighThreshold_Type(Integer32):
    """Custom type outletSection6CurrentHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_OutletSection6CurrentHighThreshold_Type.__name__ = "Integer32"
_OutletSection6CurrentHighThreshold_Object = MibScalar
outletSection6CurrentHighThreshold = _OutletSection6CurrentHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 6, 3),
    _OutletSection6CurrentHighThreshold_Type()
)
outletSection6CurrentHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection6CurrentHighThreshold.setStatus("current")


class _OutletSection6CurrentLowThreshold_Type(Integer32):
    """Custom type outletSection6CurrentLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_OutletSection6CurrentLowThreshold_Type.__name__ = "Integer32"
_OutletSection6CurrentLowThreshold_Object = MibScalar
outletSection6CurrentLowThreshold = _OutletSection6CurrentLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 6, 4),
    _OutletSection6CurrentLowThreshold_Type()
)
outletSection6CurrentLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection6CurrentLowThreshold.setStatus("current")


class _OutletSection6ControlOutlet_Type(Integer32):
    """Custom type outletSection6ControlOutlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_OutletSection6ControlOutlet_Type.__name__ = "Integer32"
_OutletSection6ControlOutlet_Object = MibScalar
outletSection6ControlOutlet = _OutletSection6ControlOutlet_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 6, 5),
    _OutletSection6ControlOutlet_Type()
)
outletSection6ControlOutlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection6ControlOutlet.setStatus("current")


class _OutletSection6OutletName_Type(OctetString):
    """Custom type outletSection6OutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_OutletSection6OutletName_Type.__name__ = "OctetString"
_OutletSection6OutletName_Object = MibScalar
outletSection6OutletName = _OutletSection6OutletName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 4, 6, 6),
    _OutletSection6OutletName_Type()
)
outletSection6OutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSection6OutletName.setStatus("current")
_CurrentSensorValues_ObjectIdentity = ObjectIdentity
currentSensorValues = _CurrentSensorValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 5)
)


class _TempSensor1Temp_Type(Integer32):
    """Custom type tempSensor1Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 300),
    )


_TempSensor1Temp_Type.__name__ = "Integer32"
_TempSensor1Temp_Object = MibScalar
tempSensor1Temp = _TempSensor1Temp_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 5, 1),
    _TempSensor1Temp_Type()
)
tempSensor1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensor1Temp.setStatus("current")


class _TempSensor2Temp_Type(Integer32):
    """Custom type tempSensor2Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 300),
    )


_TempSensor2Temp_Type.__name__ = "Integer32"
_TempSensor2Temp_Object = MibScalar
tempSensor2Temp = _TempSensor2Temp_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 5, 2),
    _TempSensor2Temp_Type()
)
tempSensor2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensor2Temp.setStatus("current")


class _HumSensor1Humidity_Type(Integer32):
    """Custom type humSensor1Humidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HumSensor1Humidity_Type.__name__ = "Integer32"
_HumSensor1Humidity_Object = MibScalar
humSensor1Humidity = _HumSensor1Humidity_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 5, 3),
    _HumSensor1Humidity_Type()
)
humSensor1Humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humSensor1Humidity.setStatus("current")


class _ContactClosure1State_Type(Integer32):
    """Custom type contactClosure1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("contactClosed", 1),
          ("contactOpen", 0))
    )


_ContactClosure1State_Type.__name__ = "Integer32"
_ContactClosure1State_Object = MibScalar
contactClosure1State = _ContactClosure1State_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 5, 4),
    _ContactClosure1State_Type()
)
contactClosure1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactClosure1State.setStatus("current")


class _ContactClosure2State_Type(Integer32):
    """Custom type contactClosure2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("contactClosed", 1),
          ("contactOpen", 0))
    )


_ContactClosure2State_Type.__name__ = "Integer32"
_ContactClosure2State_Object = MibScalar
contactClosure2State = _ContactClosure2State_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 5, 5),
    _ContactClosure2State_Type()
)
contactClosure2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactClosure2State.setStatus("current")


class _ContactClosure3State_Type(Integer32):
    """Custom type contactClosure3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("contactClosed", 1),
          ("contactOpen", 0))
    )


_ContactClosure3State_Type.__name__ = "Integer32"
_ContactClosure3State_Object = MibScalar
contactClosure3State = _ContactClosure3State_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 5, 6),
    _ContactClosure3State_Type()
)
contactClosure3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactClosure3State.setStatus("current")
_CurrentOutletSectionValues_ObjectIdentity = ObjectIdentity
currentOutletSectionValues = _CurrentOutletSectionValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6)
)
_OutletSection1_ObjectIdentity = ObjectIdentity
outletSection1 = _OutletSection1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 1)
)
_OutletSection1Voltage_Type = Integer32
_OutletSection1Voltage_Object = MibScalar
outletSection1Voltage = _OutletSection1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 1, 1),
    _OutletSection1Voltage_Type()
)
outletSection1Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection1Voltage.setStatus("current")
_OutletSection1Current_Type = Integer32
_OutletSection1Current_Object = MibScalar
outletSection1Current = _OutletSection1Current_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 1, 2),
    _OutletSection1Current_Type()
)
outletSection1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection1Current.setStatus("current")
_OutletSection1Va_Type = Integer32
_OutletSection1Va_Object = MibScalar
outletSection1Va = _OutletSection1Va_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 1, 3),
    _OutletSection1Va_Type()
)
outletSection1Va.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection1Va.setStatus("current")
_OutletSection2_ObjectIdentity = ObjectIdentity
outletSection2 = _OutletSection2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 2)
)
_OutletSection2Voltage_Type = Integer32
_OutletSection2Voltage_Object = MibScalar
outletSection2Voltage = _OutletSection2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 2, 1),
    _OutletSection2Voltage_Type()
)
outletSection2Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection2Voltage.setStatus("current")
_OutletSection2Current_Type = Integer32
_OutletSection2Current_Object = MibScalar
outletSection2Current = _OutletSection2Current_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 2, 2),
    _OutletSection2Current_Type()
)
outletSection2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection2Current.setStatus("current")
_OutletSection2Va_Type = Integer32
_OutletSection2Va_Object = MibScalar
outletSection2Va = _OutletSection2Va_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 2, 3),
    _OutletSection2Va_Type()
)
outletSection2Va.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection2Va.setStatus("current")
_OutletSection3_ObjectIdentity = ObjectIdentity
outletSection3 = _OutletSection3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 3)
)
_OutletSection3Voltage_Type = Integer32
_OutletSection3Voltage_Object = MibScalar
outletSection3Voltage = _OutletSection3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 3, 1),
    _OutletSection3Voltage_Type()
)
outletSection3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection3Voltage.setStatus("current")
_OutletSection3Current_Type = Integer32
_OutletSection3Current_Object = MibScalar
outletSection3Current = _OutletSection3Current_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 3, 2),
    _OutletSection3Current_Type()
)
outletSection3Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection3Current.setStatus("current")
_OutletSection3Va_Type = Integer32
_OutletSection3Va_Object = MibScalar
outletSection3Va = _OutletSection3Va_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 3, 3),
    _OutletSection3Va_Type()
)
outletSection3Va.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection3Va.setStatus("current")
_Total_ObjectIdentity = ObjectIdentity
total = _Total_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 4)
)
_TotalVoltage_Type = Integer32
_TotalVoltage_Object = MibScalar
totalVoltage = _TotalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 4, 1),
    _TotalVoltage_Type()
)
totalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalVoltage.setStatus("obsolete")
_TotalCurrent_Type = Integer32
_TotalCurrent_Object = MibScalar
totalCurrent = _TotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 4, 2),
    _TotalCurrent_Type()
)
totalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCurrent.setStatus("current")
_TotalVa_Type = Integer32
_TotalVa_Object = MibScalar
totalVa = _TotalVa_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 4, 3),
    _TotalVa_Type()
)
totalVa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalVa.setStatus("current")
_OutletSection4_ObjectIdentity = ObjectIdentity
outletSection4 = _OutletSection4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 5)
)
_OutletSection4Voltage_Type = Integer32
_OutletSection4Voltage_Object = MibScalar
outletSection4Voltage = _OutletSection4Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 5, 1),
    _OutletSection4Voltage_Type()
)
outletSection4Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection4Voltage.setStatus("current")
_OutletSection4Current_Type = Integer32
_OutletSection4Current_Object = MibScalar
outletSection4Current = _OutletSection4Current_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 5, 2),
    _OutletSection4Current_Type()
)
outletSection4Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection4Current.setStatus("current")
_OutletSection4Va_Type = Integer32
_OutletSection4Va_Object = MibScalar
outletSection4Va = _OutletSection4Va_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 5, 3),
    _OutletSection4Va_Type()
)
outletSection4Va.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection4Va.setStatus("current")
_OutletSection5_ObjectIdentity = ObjectIdentity
outletSection5 = _OutletSection5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 6)
)
_OutletSection5Voltage_Type = Integer32
_OutletSection5Voltage_Object = MibScalar
outletSection5Voltage = _OutletSection5Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 6, 1),
    _OutletSection5Voltage_Type()
)
outletSection5Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection5Voltage.setStatus("current")
_OutletSection5Current_Type = Integer32
_OutletSection5Current_Object = MibScalar
outletSection5Current = _OutletSection5Current_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 6, 2),
    _OutletSection5Current_Type()
)
outletSection5Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection5Current.setStatus("current")
_OutletSection5Va_Type = Integer32
_OutletSection5Va_Object = MibScalar
outletSection5Va = _OutletSection5Va_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 6, 3),
    _OutletSection5Va_Type()
)
outletSection5Va.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection5Va.setStatus("current")
_OutletSection6_ObjectIdentity = ObjectIdentity
outletSection6 = _OutletSection6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 7)
)
_OutletSection6Voltage_Type = Integer32
_OutletSection6Voltage_Object = MibScalar
outletSection6Voltage = _OutletSection6Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 7, 1),
    _OutletSection6Voltage_Type()
)
outletSection6Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection6Voltage.setStatus("current")
_OutletSection6Current_Type = Integer32
_OutletSection6Current_Object = MibScalar
outletSection6Current = _OutletSection6Current_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 7, 2),
    _OutletSection6Current_Type()
)
outletSection6Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection6Current.setStatus("current")
_OutletSection6Va_Type = Integer32
_OutletSection6Va_Object = MibScalar
outletSection6Va = _OutletSection6Va_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 8, 6, 7, 3),
    _OutletSection6Va_Type()
)
outletSection6Va.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSection6Va.setStatus("current")
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 9)
)
_EventInfo_ObjectIdentity = ObjectIdentity
eventInfo = _EventInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 10)
)
_InfoItemIdx_Type = Integer32
_InfoItemIdx_Object = MibScalar
infoItemIdx = _InfoItemIdx_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 10, 1),
    _InfoItemIdx_Type()
)
infoItemIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    infoItemIdx.setStatus("current")
_InfoItemName_Type = OctetString
_InfoItemName_Object = MibScalar
infoItemName = _InfoItemName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 10, 2),
    _InfoItemName_Type()
)
infoItemName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    infoItemName.setStatus("current")


class _InfoOutletState_Type(Integer32):
    """Custom type infoOutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_InfoOutletState_Type.__name__ = "Integer32"
_InfoOutletState_Object = MibScalar
infoOutletState = _InfoOutletState_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 10, 3),
    _InfoOutletState_Type()
)
infoOutletState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    infoOutletState.setStatus("current")


class _InfoThresholdState_Type(Integer32):
    """Custom type infoThresholdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("good", 0),
          ("highWarning", 3),
          ("lowWarning", 1))
    )


_InfoThresholdState_Type.__name__ = "Integer32"
_InfoThresholdState_Object = MibScalar
infoThresholdState = _InfoThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 10, 4),
    _InfoThresholdState_Type()
)
infoThresholdState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    infoThresholdState.setStatus("current")


class _InfoThresholdValue_Type(Integer32):
    """Custom type infoThresholdValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 300),
    )


_InfoThresholdValue_Type.__name__ = "Integer32"
_InfoThresholdValue_Object = MibScalar
infoThresholdValue = _InfoThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 10, 5),
    _InfoThresholdValue_Type()
)
infoThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    infoThresholdValue.setStatus("current")


class _InfoMeasuredValue_Type(Integer32):
    """Custom type infoMeasuredValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 300),
    )


_InfoMeasuredValue_Type.__name__ = "Integer32"
_InfoMeasuredValue_Object = MibScalar
infoMeasuredValue = _InfoMeasuredValue_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 10, 6),
    _InfoMeasuredValue_Type()
)
infoMeasuredValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    infoMeasuredValue.setStatus("current")


class _InfoContactState_Type(Integer32):
    """Custom type infoContactState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("contactClosed", 1),
          ("contactOpen", 0))
    )


_InfoContactState_Type.__name__ = "Integer32"
_InfoContactState_Object = MibScalar
infoContactState = _InfoContactState_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 10, 7),
    _InfoContactState_Type()
)
infoContactState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    infoContactState.setStatus("current")
_InfoUserName_Type = OctetString
_InfoUserName_Object = MibScalar
infoUserName = _InfoUserName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 2, 10, 8),
    _InfoUserName_Type()
)
infoUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    infoUserName.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 25)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 2, 25, 5)
)

# Managed Objects groups

allObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20677, 2, 25, 5, 1)
)
allObjects.setObjects(
      *(("EATON-EPDU-PU-SW-MIB", "baudRate"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure1Alert"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure1ControlOutlet"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure1Enable"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure1Name"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure1OutletName"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure1OutletState"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure1State"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure2Alert"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure2ControlOutlet"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure2Enable"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure2Name"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure2OutletName"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure2OutletState"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure2State"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure3Alert"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure3ControlOutlet"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure3Enable"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure3Name"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure3OutletName"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure3OutletState"),
        ("EATON-EPDU-PU-SW-MIB", "contactClosure3State"),
        ("EATON-EPDU-PU-SW-MIB", "defaultGateway"),
        ("EATON-EPDU-PU-SW-MIB", "enablePing"),
        ("EATON-EPDU-PU-SW-MIB", "fahrenheitOrCelsius"),
        ("EATON-EPDU-PU-SW-MIB", "globalCommand"),
        ("EATON-EPDU-PU-SW-MIB", "humSensor1Alert"),
        ("EATON-EPDU-PU-SW-MIB", "humSensor1ControlOutlet"),
        ("EATON-EPDU-PU-SW-MIB", "humSensor1Enable"),
        ("EATON-EPDU-PU-SW-MIB", "humSensor1HighThresh"),
        ("EATON-EPDU-PU-SW-MIB", "humSensor1Humidity"),
        ("EATON-EPDU-PU-SW-MIB", "humSensor1LowThresh"),
        ("EATON-EPDU-PU-SW-MIB", "humSensor1Name"),
        ("EATON-EPDU-PU-SW-MIB", "humSensor1OutletName"),
        ("EATON-EPDU-PU-SW-MIB", "humSensor1OutletState"),
        ("EATON-EPDU-PU-SW-MIB", "infoContactState"),
        ("EATON-EPDU-PU-SW-MIB", "infoItemIdx"),
        ("EATON-EPDU-PU-SW-MIB", "infoItemName"),
        ("EATON-EPDU-PU-SW-MIB", "infoMeasuredValue"),
        ("EATON-EPDU-PU-SW-MIB", "infoOutletState"),
        ("EATON-EPDU-PU-SW-MIB", "infoThresholdState"),
        ("EATON-EPDU-PU-SW-MIB", "infoThresholdValue"),
        ("EATON-EPDU-PU-SW-MIB", "infoUserName"),
        ("EATON-EPDU-PU-SW-MIB", "invertDisplay"),
        ("EATON-EPDU-PU-SW-MIB", "loginTimeout"),
        ("EATON-EPDU-PU-SW-MIB", "macAddress"),
        ("EATON-EPDU-PU-SW-MIB", "mailServerIPAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet10Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet10Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet10Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet10PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet10RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet10SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet10Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet11Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet11Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet11Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet11PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet11RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet11SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet11Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet12Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet12Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet12Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet12PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet12RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet12SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet12Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet13Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet13Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet13Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet13PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet13RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet13SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet13Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet14Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet14Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet14Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet14PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet14RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet14SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet14Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet15Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet15Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet15Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet15PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet15RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet15SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet15Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet16Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet16Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet16Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet16PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet16RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet16SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet16Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet17Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet17Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet17Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet17PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet17RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet17SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet17Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet18Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet18Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet18Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet18PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet18RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet18SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet18Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet19Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet19Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet19Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet19PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet19RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet19SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet19Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet1Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet1Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet1Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet1PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet1RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet1SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet1Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet20Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet20Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet20Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet20PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet20RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet20SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet20Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet21Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet21Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet21Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet21PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet21RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet21SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet21Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet22Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet22Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet22Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet22PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet22RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet22SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet22Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet23Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet23Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet23Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet23PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet23RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet23SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet23Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet24Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet24Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet24Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet24PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet24RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet24SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet24Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet25Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet25Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet25Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet25PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet25RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet25SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet25Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet26Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet26Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet26Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet26PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet26RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet26SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet26Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet27Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet27Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet27Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet27PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet27RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet27SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet27Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet28Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet28Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet28Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet28PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet28RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet28SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet28Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet29Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet29Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet29Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet29PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet29RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet29SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet29Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet2Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet2Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet2Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet2PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet2RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet2SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet2Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet30Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet30Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet30Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet30PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet30RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet30SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet30Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet31Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet31Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet31Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet31PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet31RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet31SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet31Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet32Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet32Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet32Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet32PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet32RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet32SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet32Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet33Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet33Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet33Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet33PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet33RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet33SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet33Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet34Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet34Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet34Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet34PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet34RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet34SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet34Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet35Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet35Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet35Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet35PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet35RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet35SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet35Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet36Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet36Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet36Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet36PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet36RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet36SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet36Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet3Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet3Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet3Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet3PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet3RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet3SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet3Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet4Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet4Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet4Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet4PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet4RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet4SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet4Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet5Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet5Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet5Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet5PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet5RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet5SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet5Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet6Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet6Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet6Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet6PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet6RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet6SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet6Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet7Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet7Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet7Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet7PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet7RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet7SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet7Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet8Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet8Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet8Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet8PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet8RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet8SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet8Status"),
        ("EATON-EPDU-PU-SW-MIB", "outlet9Command"),
        ("EATON-EPDU-PU-SW-MIB", "outlet9Link"),
        ("EATON-EPDU-PU-SW-MIB", "outlet9Name"),
        ("EATON-EPDU-PU-SW-MIB", "outlet9PingIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "outlet9RebootTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet9SequenceTime"),
        ("EATON-EPDU-PU-SW-MIB", "outlet9Status"),
        ("EATON-EPDU-PU-SW-MIB", "outletActivity"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection1Alert"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection1Current"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection1CurrentHighThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection1CurrentLowThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection1Va"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection1Voltage"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection1VoltageHighThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection1VoltageLowThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection2Alert"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection2Current"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection2CurrentHighThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection2CurrentLowThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection2Va"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection2Voltage"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection2VoltageHighThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection2VoltageLowThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection3Alert"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection3Current"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection3CurrentHighThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection3CurrentLowThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection3Va"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection3Voltage"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection3VoltageHighThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection3VoltageLowThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection4Current"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection4CurrentHighThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection4CurrentLowThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection4Va"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection4Voltage"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection4VoltageHighThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection4VoltageLowThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection5Current"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection5CurrentHighThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection5CurrentLowThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection5Va"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection5Voltage"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection5VoltageHighThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection5VoltageLowThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection6Current"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection6CurrentHighThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection6CurrentLowThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection6Va"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection6Voltage"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection6VoltageHighThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection6VoltageLowThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "pingInterval"),
        ("EATON-EPDU-PU-SW-MIB", "sendAlertsToUser1Address"),
        ("EATON-EPDU-PU-SW-MIB", "sendAlertsToUser2Address"),
        ("EATON-EPDU-PU-SW-MIB", "sendLogFrequency"),
        ("EATON-EPDU-PU-SW-MIB", "sendLogFrom"),
        ("EATON-EPDU-PU-SW-MIB", "sendLogTime"),
        ("EATON-EPDU-PU-SW-MIB", "sendLogToUser1Address"),
        ("EATON-EPDU-PU-SW-MIB", "sendLogToUser2Address"),
        ("EATON-EPDU-PU-SW-MIB", "strappingId"),
        ("EATON-EPDU-PU-SW-MIB", "subnetMask"),
        ("EATON-EPDU-PU-SW-MIB", "systemOnOff"),
        ("EATON-EPDU-PU-SW-MIB", "telnetEnabled"),
        ("EATON-EPDU-PU-SW-MIB", "telnetPort"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor1Alert"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor1ControlOutlet"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor1Enable"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor1HighThresh"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor1LowThresh"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor1Name"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor1OutletName"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor1OutletState"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor1Temp"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor2Alert"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor2ControlOutlet"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor2Enable"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor2HighThresh"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor2LowThresh"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor2Name"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor2OutletName"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor2OutletState"),
        ("EATON-EPDU-PU-SW-MIB", "tempSensor2Temp"),
        ("EATON-EPDU-PU-SW-MIB", "totalCurrent"),
        ("EATON-EPDU-PU-SW-MIB", "totalVa"),
        ("EATON-EPDU-PU-SW-MIB", "trapContactClosure1Threshold"),
        ("EATON-EPDU-PU-SW-MIB", "trapContactClosure2Threshold"),
        ("EATON-EPDU-PU-SW-MIB", "trapContactClosure3Threshold"),
        ("EATON-EPDU-PU-SW-MIB", "trapFailedLogin"),
        ("EATON-EPDU-PU-SW-MIB", "trapHumiditySensorThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "trapIpAddress"),
        ("EATON-EPDU-PU-SW-MIB", "trapOutletActivity"),
        ("EATON-EPDU-PU-SW-MIB", "trapOutletSection1Threshold"),
        ("EATON-EPDU-PU-SW-MIB", "trapOutletSection2Threshold"),
        ("EATON-EPDU-PU-SW-MIB", "trapOutletSection3Threshold"),
        ("EATON-EPDU-PU-SW-MIB", "trapSystemOnOff"),
        ("EATON-EPDU-PU-SW-MIB", "trapTemperatureSensor1Threshold"),
        ("EATON-EPDU-PU-SW-MIB", "trapTemperatureSensor2Threshold"),
        ("EATON-EPDU-PU-SW-MIB", "trapUserLoginLogout"),
        ("EATON-EPDU-PU-SW-MIB", "unitDate"),
        ("EATON-EPDU-PU-SW-MIB", "unitDayOfWeek"),
        ("EATON-EPDU-PU-SW-MIB", "unitIPAddress"),
        ("EATON-EPDU-PU-SW-MIB", "unitName"),
        ("EATON-EPDU-PU-SW-MIB", "unitTime"),
        ("EATON-EPDU-PU-SW-MIB", "userLogInLogOut"),
        ("EATON-EPDU-PU-SW-MIB", "userLogInLogOutFailed"),
        ("EATON-EPDU-PU-SW-MIB", "vaLoggingInterval"),
        ("EATON-EPDU-PU-SW-MIB", "webEnabled"),
        ("EATON-EPDU-PU-SW-MIB", "webPort"))
)
if mibBuilder.loadTexts:
    allObjects.setStatus("current")

oldObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20677, 2, 25, 5, 2)
)
oldObjects.setObjects(
      *(("EATON-EPDU-PU-SW-MIB", "outletSection1ControlOutlet"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection1OutletName"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection2ControlOutlet"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection2OutletName"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection3ControlOutlet"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection3OutletName"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection4ControlOutlet"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection4OutletName"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection5ControlOutlet"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection5OutletName"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection6ControlOutlet"),
        ("EATON-EPDU-PU-SW-MIB", "outletSection6OutletName"))
)
if mibBuilder.loadTexts:
    oldObjects.setStatus("deprecated")

obsoleteObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20677, 2, 25, 5, 3)
)
obsoleteObjects.setObjects(
    ("EATON-EPDU-PU-SW-MIB", "totalVoltage")
)
if mibBuilder.loadTexts:
    obsoleteObjects.setStatus("obsolete")


# Notification objects

notifyOutletState = NotificationType(
    (1, 3, 6, 1, 4, 1, 20677, 2, 9, 1)
)
notifyOutletState.setObjects(
      *(("EATON-EPDU-PU-SW-MIB", "infoItemIdx"),
        ("EATON-EPDU-PU-SW-MIB", "infoItemName"),
        ("EATON-EPDU-PU-SW-MIB", "infoOutletState"))
)
if mibBuilder.loadTexts:
    notifyOutletState.setStatus(
        "current"
    )

notifyCurrentThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 20677, 2, 9, 2)
)
notifyCurrentThreshold.setObjects(
      *(("EATON-EPDU-PU-SW-MIB", "infoItemIdx"),
        ("EATON-EPDU-PU-SW-MIB", "infoItemName"),
        ("EATON-EPDU-PU-SW-MIB", "infoThresholdState"),
        ("EATON-EPDU-PU-SW-MIB", "infoThresholdValue"),
        ("EATON-EPDU-PU-SW-MIB", "infoMeasuredValue"))
)
if mibBuilder.loadTexts:
    notifyCurrentThreshold.setStatus(
        "current"
    )

notifyVoltageThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 20677, 2, 9, 3)
)
notifyVoltageThreshold.setObjects(
      *(("EATON-EPDU-PU-SW-MIB", "infoItemIdx"),
        ("EATON-EPDU-PU-SW-MIB", "infoItemName"),
        ("EATON-EPDU-PU-SW-MIB", "infoThresholdState"),
        ("EATON-EPDU-PU-SW-MIB", "infoThresholdValue"),
        ("EATON-EPDU-PU-SW-MIB", "infoMeasuredValue"))
)
if mibBuilder.loadTexts:
    notifyVoltageThreshold.setStatus(
        "current"
    )

notifyTempSensorThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 20677, 2, 9, 4)
)
notifyTempSensorThreshold.setObjects(
      *(("EATON-EPDU-PU-SW-MIB", "infoItemIdx"),
        ("EATON-EPDU-PU-SW-MIB", "infoItemName"),
        ("EATON-EPDU-PU-SW-MIB", "infoThresholdState"),
        ("EATON-EPDU-PU-SW-MIB", "infoThresholdValue"),
        ("EATON-EPDU-PU-SW-MIB", "infoMeasuredValue"),
        ("EATON-EPDU-PU-SW-MIB", "fahrenheitOrCelsius"))
)
if mibBuilder.loadTexts:
    notifyTempSensorThreshold.setStatus(
        "current"
    )

notifyHumidSensorThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 20677, 2, 9, 5)
)
notifyHumidSensorThreshold.setObjects(
      *(("EATON-EPDU-PU-SW-MIB", "infoItemIdx"),
        ("EATON-EPDU-PU-SW-MIB", "infoItemName"),
        ("EATON-EPDU-PU-SW-MIB", "infoThresholdState"),
        ("EATON-EPDU-PU-SW-MIB", "infoThresholdValue"),
        ("EATON-EPDU-PU-SW-MIB", "infoMeasuredValue"))
)
if mibBuilder.loadTexts:
    notifyHumidSensorThreshold.setStatus(
        "current"
    )

notifyContactSensorThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 20677, 2, 9, 6)
)
notifyContactSensorThreshold.setObjects(
      *(("EATON-EPDU-PU-SW-MIB", "infoItemIdx"),
        ("EATON-EPDU-PU-SW-MIB", "infoItemName"),
        ("EATON-EPDU-PU-SW-MIB", "infoContactState"))
)
if mibBuilder.loadTexts:
    notifyContactSensorThreshold.setStatus(
        "current"
    )

notifyUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 20677, 2, 9, 7)
)
notifyUserLogin.setObjects(
    ("EATON-EPDU-PU-SW-MIB", "infoUserName")
)
if mibBuilder.loadTexts:
    notifyUserLogin.setStatus(
        "current"
    )

notifyUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 20677, 2, 9, 8)
)
notifyUserLogout.setObjects(
    ("EATON-EPDU-PU-SW-MIB", "infoUserName")
)
if mibBuilder.loadTexts:
    notifyUserLogout.setStatus(
        "current"
    )

notifyFailedLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 20677, 2, 9, 9)
)
notifyFailedLogin.setObjects(
    ("EATON-EPDU-PU-SW-MIB", "infoUserName")
)
if mibBuilder.loadTexts:
    notifyFailedLogin.setStatus(
        "current"
    )

notifyOutletWatchdogFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 20677, 2, 9, 10)
)
notifyOutletWatchdogFailed.setObjects(
      *(("EATON-EPDU-PU-SW-MIB", "infoItemIdx"),
        ("EATON-EPDU-PU-SW-MIB", "infoItemName"))
)
if mibBuilder.loadTexts:
    notifyOutletWatchdogFailed.setStatus(
        "current"
    )


# Notifications groups

allNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 20677, 2, 25, 5, 4)
)
allNotifications.setObjects(
      *(("EATON-EPDU-PU-SW-MIB", "notifyContactSensorThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "notifyCurrentThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "notifyFailedLogin"),
        ("EATON-EPDU-PU-SW-MIB", "notifyHumidSensorThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "notifyOutletState"),
        ("EATON-EPDU-PU-SW-MIB", "notifyOutletWatchdogFailed"),
        ("EATON-EPDU-PU-SW-MIB", "notifyTempSensorThreshold"),
        ("EATON-EPDU-PU-SW-MIB", "notifyUserLogin"),
        ("EATON-EPDU-PU-SW-MIB", "notifyUserLogout"),
        ("EATON-EPDU-PU-SW-MIB", "notifyVoltageThreshold"))
)
if mibBuilder.loadTexts:
    allNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

compliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 20677, 2, 25, 1)
)
if mibBuilder.loadTexts:
    compliances.setStatus(
        "current"
    )

oldCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 20677, 2, 25, 2)
)
if mibBuilder.loadTexts:
    oldCompliances.setStatus(
        "deprecated"
    )

obsoleteCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 20677, 2, 25, 3)
)
if mibBuilder.loadTexts:
    obsoleteCompliances.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EATON-EPDU-PU-SW-MIB",
    **{"pulizzi": pulizzi,
       "ipv3600": ipv3600,
       "unitConfig": unitConfig,
       "unitName": unitName,
       "strappingId": strappingId,
       "unitTime": unitTime,
       "unitDate": unitDate,
       "unitDayOfWeek": unitDayOfWeek,
       "vaLoggingInterval": vaLoggingInterval,
       "loginTimeout": loginTimeout,
       "invertDisplay": invertDisplay,
       "fahrenheitOrCelsius": fahrenheitOrCelsius,
       "networkSettings": networkSettings,
       "unitIPAddress": unitIPAddress,
       "subnetMask": subnetMask,
       "defaultGateway": defaultGateway,
       "webPort": webPort,
       "webEnabled": webEnabled,
       "macAddress": macAddress,
       "enablePing": enablePing,
       "pingInterval": pingInterval,
       "logManagerConfig": logManagerConfig,
       "mailServerIPAddress": mailServerIPAddress,
       "sendLogFrom": sendLogFrom,
       "sendLogToUser1Address": sendLogToUser1Address,
       "sendLogToUser2Address": sendLogToUser2Address,
       "sendAlertsToUser1Address": sendAlertsToUser1Address,
       "sendAlertsToUser2Address": sendAlertsToUser2Address,
       "sendLogFrequency": sendLogFrequency,
       "sendLogTime": sendLogTime,
       "userLogInLogOut": userLogInLogOut,
       "userLogInLogOutFailed": userLogInLogOutFailed,
       "outletActivity": outletActivity,
       "systemOnOff": systemOnOff,
       "outletSection1Alert": outletSection1Alert,
       "outletSection2Alert": outletSection2Alert,
       "outletSection3Alert": outletSection3Alert,
       "tempSensor1Alert": tempSensor1Alert,
       "tempSensor2Alert": tempSensor2Alert,
       "humSensor1Alert": humSensor1Alert,
       "contactClosure1Alert": contactClosure1Alert,
       "contactClosure2Alert": contactClosure2Alert,
       "contactClosure3Alert": contactClosure3Alert,
       "serialSettings": serialSettings,
       "baudRate": baudRate,
       "telnetSettings": telnetSettings,
       "telnetPort": telnetPort,
       "telnetEnabled": telnetEnabled,
       "outletMngt": outletMngt,
       "outletConfig": outletConfig,
       "outlet1": outlet1,
       "outlet1Name": outlet1Name,
       "outlet1PingIpAddress": outlet1PingIpAddress,
       "outlet1Link": outlet1Link,
       "outlet1SequenceTime": outlet1SequenceTime,
       "outlet1RebootTime": outlet1RebootTime,
       "outlet2": outlet2,
       "outlet2Name": outlet2Name,
       "outlet2PingIpAddress": outlet2PingIpAddress,
       "outlet2Link": outlet2Link,
       "outlet2SequenceTime": outlet2SequenceTime,
       "outlet2RebootTime": outlet2RebootTime,
       "outlet3": outlet3,
       "outlet3Name": outlet3Name,
       "outlet3PingIpAddress": outlet3PingIpAddress,
       "outlet3Link": outlet3Link,
       "outlet3SequenceTime": outlet3SequenceTime,
       "outlet3RebootTime": outlet3RebootTime,
       "outlet4": outlet4,
       "outlet4Name": outlet4Name,
       "outlet4PingIpAddress": outlet4PingIpAddress,
       "outlet4Link": outlet4Link,
       "outlet4SequenceTime": outlet4SequenceTime,
       "outlet4RebootTime": outlet4RebootTime,
       "outlet5": outlet5,
       "outlet5Name": outlet5Name,
       "outlet5PingIpAddress": outlet5PingIpAddress,
       "outlet5Link": outlet5Link,
       "outlet5SequenceTime": outlet5SequenceTime,
       "outlet5RebootTime": outlet5RebootTime,
       "outlet6": outlet6,
       "outlet6Name": outlet6Name,
       "outlet6PingIpAddress": outlet6PingIpAddress,
       "outlet6Link": outlet6Link,
       "outlet6SequenceTime": outlet6SequenceTime,
       "outlet6RebootTime": outlet6RebootTime,
       "outlet7": outlet7,
       "outlet7Name": outlet7Name,
       "outlet7PingIpAddress": outlet7PingIpAddress,
       "outlet7Link": outlet7Link,
       "outlet7SequenceTime": outlet7SequenceTime,
       "outlet7RebootTime": outlet7RebootTime,
       "outlet8": outlet8,
       "outlet8Name": outlet8Name,
       "outlet8PingIpAddress": outlet8PingIpAddress,
       "outlet8Link": outlet8Link,
       "outlet8SequenceTime": outlet8SequenceTime,
       "outlet8RebootTime": outlet8RebootTime,
       "outlet9": outlet9,
       "outlet9Name": outlet9Name,
       "outlet9PingIpAddress": outlet9PingIpAddress,
       "outlet9Link": outlet9Link,
       "outlet9SequenceTime": outlet9SequenceTime,
       "outlet9RebootTime": outlet9RebootTime,
       "outlet10": outlet10,
       "outlet10Name": outlet10Name,
       "outlet10PingIpAddress": outlet10PingIpAddress,
       "outlet10Link": outlet10Link,
       "outlet10SequenceTime": outlet10SequenceTime,
       "outlet10RebootTime": outlet10RebootTime,
       "outlet11": outlet11,
       "outlet11Name": outlet11Name,
       "outlet11PingIpAddress": outlet11PingIpAddress,
       "outlet11Link": outlet11Link,
       "outlet11SequenceTime": outlet11SequenceTime,
       "outlet11RebootTime": outlet11RebootTime,
       "outlet12": outlet12,
       "outlet12Name": outlet12Name,
       "outlet12PingIpAddress": outlet12PingIpAddress,
       "outlet12Link": outlet12Link,
       "outlet12SequenceTime": outlet12SequenceTime,
       "outlet12RebootTime": outlet12RebootTime,
       "outlet13": outlet13,
       "outlet13Name": outlet13Name,
       "outlet13PingIpAddress": outlet13PingIpAddress,
       "outlet13Link": outlet13Link,
       "outlet13SequenceTime": outlet13SequenceTime,
       "outlet13RebootTime": outlet13RebootTime,
       "outlet14": outlet14,
       "outlet14Name": outlet14Name,
       "outlet14PingIpAddress": outlet14PingIpAddress,
       "outlet14Link": outlet14Link,
       "outlet14SequenceTime": outlet14SequenceTime,
       "outlet14RebootTime": outlet14RebootTime,
       "outlet15": outlet15,
       "outlet15Name": outlet15Name,
       "outlet15PingIpAddress": outlet15PingIpAddress,
       "outlet15Link": outlet15Link,
       "outlet15SequenceTime": outlet15SequenceTime,
       "outlet15RebootTime": outlet15RebootTime,
       "outlet16": outlet16,
       "outlet16Name": outlet16Name,
       "outlet16PingIpAddress": outlet16PingIpAddress,
       "outlet16Link": outlet16Link,
       "outlet16SequenceTime": outlet16SequenceTime,
       "outlet16RebootTime": outlet16RebootTime,
       "outlet17": outlet17,
       "outlet17Name": outlet17Name,
       "outlet17PingIpAddress": outlet17PingIpAddress,
       "outlet17Link": outlet17Link,
       "outlet17SequenceTime": outlet17SequenceTime,
       "outlet17RebootTime": outlet17RebootTime,
       "outlet18": outlet18,
       "outlet18Name": outlet18Name,
       "outlet18PingIpAddress": outlet18PingIpAddress,
       "outlet18Link": outlet18Link,
       "outlet18SequenceTime": outlet18SequenceTime,
       "outlet18RebootTime": outlet18RebootTime,
       "outlet19": outlet19,
       "outlet19Name": outlet19Name,
       "outlet19PingIpAddress": outlet19PingIpAddress,
       "outlet19Link": outlet19Link,
       "outlet19SequenceTime": outlet19SequenceTime,
       "outlet19RebootTime": outlet19RebootTime,
       "outlet20": outlet20,
       "outlet20Name": outlet20Name,
       "outlet20PingIpAddress": outlet20PingIpAddress,
       "outlet20Link": outlet20Link,
       "outlet20SequenceTime": outlet20SequenceTime,
       "outlet20RebootTime": outlet20RebootTime,
       "outlet21": outlet21,
       "outlet21Name": outlet21Name,
       "outlet21PingIpAddress": outlet21PingIpAddress,
       "outlet21Link": outlet21Link,
       "outlet21SequenceTime": outlet21SequenceTime,
       "outlet21RebootTime": outlet21RebootTime,
       "outlet22": outlet22,
       "outlet22Name": outlet22Name,
       "outlet22PingIpAddress": outlet22PingIpAddress,
       "outlet22Link": outlet22Link,
       "outlet22SequenceTime": outlet22SequenceTime,
       "outlet22RebootTime": outlet22RebootTime,
       "outlet23": outlet23,
       "outlet23Name": outlet23Name,
       "outlet23PingIpAddress": outlet23PingIpAddress,
       "outlet23Link": outlet23Link,
       "outlet23SequenceTime": outlet23SequenceTime,
       "outlet23RebootTime": outlet23RebootTime,
       "outlet24": outlet24,
       "outlet24Name": outlet24Name,
       "outlet24PingIpAddress": outlet24PingIpAddress,
       "outlet24Link": outlet24Link,
       "outlet24SequenceTime": outlet24SequenceTime,
       "outlet24RebootTime": outlet24RebootTime,
       "outlet25": outlet25,
       "outlet25Name": outlet25Name,
       "outlet25PingIpAddress": outlet25PingIpAddress,
       "outlet25Link": outlet25Link,
       "outlet25SequenceTime": outlet25SequenceTime,
       "outlet25RebootTime": outlet25RebootTime,
       "outlet26": outlet26,
       "outlet26Name": outlet26Name,
       "outlet26PingIpAddress": outlet26PingIpAddress,
       "outlet26Link": outlet26Link,
       "outlet26SequenceTime": outlet26SequenceTime,
       "outlet26RebootTime": outlet26RebootTime,
       "outlet27": outlet27,
       "outlet27Name": outlet27Name,
       "outlet27PingIpAddress": outlet27PingIpAddress,
       "outlet27Link": outlet27Link,
       "outlet27SequenceTime": outlet27SequenceTime,
       "outlet27RebootTime": outlet27RebootTime,
       "outlet28": outlet28,
       "outlet28Name": outlet28Name,
       "outlet28PingIpAddress": outlet28PingIpAddress,
       "outlet28Link": outlet28Link,
       "outlet28SequenceTime": outlet28SequenceTime,
       "outlet28RebootTime": outlet28RebootTime,
       "outlet29": outlet29,
       "outlet29Name": outlet29Name,
       "outlet29PingIpAddress": outlet29PingIpAddress,
       "outlet29Link": outlet29Link,
       "outlet29SequenceTime": outlet29SequenceTime,
       "outlet29RebootTime": outlet29RebootTime,
       "outlet30": outlet30,
       "outlet30Name": outlet30Name,
       "outlet30PingIpAddress": outlet30PingIpAddress,
       "outlet30Link": outlet30Link,
       "outlet30SequenceTime": outlet30SequenceTime,
       "outlet30RebootTime": outlet30RebootTime,
       "outlet31": outlet31,
       "outlet31Name": outlet31Name,
       "outlet31PingIpAddress": outlet31PingIpAddress,
       "outlet31Link": outlet31Link,
       "outlet31SequenceTime": outlet31SequenceTime,
       "outlet31RebootTime": outlet31RebootTime,
       "outlet32": outlet32,
       "outlet32Name": outlet32Name,
       "outlet32PingIpAddress": outlet32PingIpAddress,
       "outlet32Link": outlet32Link,
       "outlet32SequenceTime": outlet32SequenceTime,
       "outlet32RebootTime": outlet32RebootTime,
       "outlet33": outlet33,
       "outlet33Name": outlet33Name,
       "outlet33PingIpAddress": outlet33PingIpAddress,
       "outlet33Link": outlet33Link,
       "outlet33SequenceTime": outlet33SequenceTime,
       "outlet33RebootTime": outlet33RebootTime,
       "outlet34": outlet34,
       "outlet34Name": outlet34Name,
       "outlet34PingIpAddress": outlet34PingIpAddress,
       "outlet34Link": outlet34Link,
       "outlet34SequenceTime": outlet34SequenceTime,
       "outlet34RebootTime": outlet34RebootTime,
       "outlet35": outlet35,
       "outlet35Name": outlet35Name,
       "outlet35PingIpAddress": outlet35PingIpAddress,
       "outlet35Link": outlet35Link,
       "outlet35SequenceTime": outlet35SequenceTime,
       "outlet35RebootTime": outlet35RebootTime,
       "outlet36": outlet36,
       "outlet36Name": outlet36Name,
       "outlet36PingIpAddress": outlet36PingIpAddress,
       "outlet36Link": outlet36Link,
       "outlet36SequenceTime": outlet36SequenceTime,
       "outlet36RebootTime": outlet36RebootTime,
       "outletControl": outletControl,
       "globalCommand": globalCommand,
       "outlet1Command": outlet1Command,
       "outlet2Command": outlet2Command,
       "outlet3Command": outlet3Command,
       "outlet4Command": outlet4Command,
       "outlet5Command": outlet5Command,
       "outlet6Command": outlet6Command,
       "outlet7Command": outlet7Command,
       "outlet8Command": outlet8Command,
       "outlet9Command": outlet9Command,
       "outlet10Command": outlet10Command,
       "outlet11Command": outlet11Command,
       "outlet12Command": outlet12Command,
       "outlet13Command": outlet13Command,
       "outlet14Command": outlet14Command,
       "outlet15Command": outlet15Command,
       "outlet16Command": outlet16Command,
       "outlet17Command": outlet17Command,
       "outlet18Command": outlet18Command,
       "outlet19Command": outlet19Command,
       "outlet20Command": outlet20Command,
       "outlet21Command": outlet21Command,
       "outlet22Command": outlet22Command,
       "outlet23Command": outlet23Command,
       "outlet24Command": outlet24Command,
       "outlet25Command": outlet25Command,
       "outlet26Command": outlet26Command,
       "outlet27Command": outlet27Command,
       "outlet28Command": outlet28Command,
       "outlet29Command": outlet29Command,
       "outlet30Command": outlet30Command,
       "outlet31Command": outlet31Command,
       "outlet32Command": outlet32Command,
       "outlet33Command": outlet33Command,
       "outlet34Command": outlet34Command,
       "outlet35Command": outlet35Command,
       "outlet36Command": outlet36Command,
       "outletStatus": outletStatus,
       "outlet1Status": outlet1Status,
       "outlet2Status": outlet2Status,
       "outlet3Status": outlet3Status,
       "outlet4Status": outlet4Status,
       "outlet5Status": outlet5Status,
       "outlet6Status": outlet6Status,
       "outlet7Status": outlet7Status,
       "outlet8Status": outlet8Status,
       "outlet9Status": outlet9Status,
       "outlet10Status": outlet10Status,
       "outlet11Status": outlet11Status,
       "outlet12Status": outlet12Status,
       "outlet13Status": outlet13Status,
       "outlet14Status": outlet14Status,
       "outlet15Status": outlet15Status,
       "outlet16Status": outlet16Status,
       "outlet17Status": outlet17Status,
       "outlet18Status": outlet18Status,
       "outlet19Status": outlet19Status,
       "outlet20Status": outlet20Status,
       "outlet21Status": outlet21Status,
       "outlet22Status": outlet22Status,
       "outlet23Status": outlet23Status,
       "outlet24Status": outlet24Status,
       "outlet25Status": outlet25Status,
       "outlet26Status": outlet26Status,
       "outlet27Status": outlet27Status,
       "outlet28Status": outlet28Status,
       "outlet29Status": outlet29Status,
       "outlet30Status": outlet30Status,
       "outlet31Status": outlet31Status,
       "outlet32Status": outlet32Status,
       "outlet33Status": outlet33Status,
       "outlet34Status": outlet34Status,
       "outlet35Status": outlet35Status,
       "outlet36Status": outlet36Status,
       "snmpSettings": snmpSettings,
       "publicCommunityName": publicCommunityName,
       "privateCommunityName": privateCommunityName,
       "trapCommunityName": trapCommunityName,
       "publicCommunityPassword": publicCommunityPassword,
       "privateCommunityPassword": privateCommunityPassword,
       "trapIpAddress": trapIpAddress,
       "snmpEnabled": snmpEnabled,
       "snmpTraps": snmpTraps,
       "trapUserLoginLogout": trapUserLoginLogout,
       "trapFailedLogin": trapFailedLogin,
       "trapOutletActivity": trapOutletActivity,
       "trapSystemOnOff": trapSystemOnOff,
       "trapOutletSection1Threshold": trapOutletSection1Threshold,
       "trapOutletSection2Threshold": trapOutletSection2Threshold,
       "trapOutletSection3Threshold": trapOutletSection3Threshold,
       "trapTemperatureSensor1Threshold": trapTemperatureSensor1Threshold,
       "trapTemperatureSensor2Threshold": trapTemperatureSensor2Threshold,
       "trapHumiditySensorThreshold": trapHumiditySensorThreshold,
       "trapContactClosure1Threshold": trapContactClosure1Threshold,
       "trapContactClosure2Threshold": trapContactClosure2Threshold,
       "trapContactClosure3Threshold": trapContactClosure3Threshold,
       "environmentalSettings": environmentalSettings,
       "temperatureSensorConfig": temperatureSensorConfig,
       "tempSensor1": tempSensor1,
       "tempSensor1Name": tempSensor1Name,
       "tempSensor1Enable": tempSensor1Enable,
       "tempSensor1HighThresh": tempSensor1HighThresh,
       "tempSensor1LowThresh": tempSensor1LowThresh,
       "tempSensor1ControlOutlet": tempSensor1ControlOutlet,
       "tempSensor1OutletName": tempSensor1OutletName,
       "tempSensor1OutletState": tempSensor1OutletState,
       "tempSensor2": tempSensor2,
       "tempSensor2Name": tempSensor2Name,
       "tempSensor2Enable": tempSensor2Enable,
       "tempSensor2HighThresh": tempSensor2HighThresh,
       "tempSensor2LowThresh": tempSensor2LowThresh,
       "tempSensor2ControlOutlet": tempSensor2ControlOutlet,
       "tempSensor2OutletName": tempSensor2OutletName,
       "tempSensor2OutletState": tempSensor2OutletState,
       "humiditySensorConfig": humiditySensorConfig,
       "humSensor1": humSensor1,
       "humSensor1Name": humSensor1Name,
       "humSensor1Enable": humSensor1Enable,
       "humSensor1HighThresh": humSensor1HighThresh,
       "humSensor1LowThresh": humSensor1LowThresh,
       "humSensor1ControlOutlet": humSensor1ControlOutlet,
       "humSensor1OutletName": humSensor1OutletName,
       "humSensor1OutletState": humSensor1OutletState,
       "contactClosureConfig": contactClosureConfig,
       "contactClosure1": contactClosure1,
       "contactClosure1Name": contactClosure1Name,
       "contactClosure1Enable": contactClosure1Enable,
       "contactClosure1ControlOutlet": contactClosure1ControlOutlet,
       "contactClosure1OutletName": contactClosure1OutletName,
       "contactClosure1OutletState": contactClosure1OutletState,
       "contactClosure2": contactClosure2,
       "contactClosure2Name": contactClosure2Name,
       "contactClosure2Enable": contactClosure2Enable,
       "contactClosure2ControlOutlet": contactClosure2ControlOutlet,
       "contactClosure2OutletName": contactClosure2OutletName,
       "contactClosure2OutletState": contactClosure2OutletState,
       "contactClosure3": contactClosure3,
       "contactClosure3Name": contactClosure3Name,
       "contactClosure3Enable": contactClosure3Enable,
       "contactClosure3ControlOutlet": contactClosure3ControlOutlet,
       "contactClosure3OutletName": contactClosure3OutletName,
       "contactClosure3OutletState": contactClosure3OutletState,
       "outletSectionConfig": outletSectionConfig,
       "outletSection1Config": outletSection1Config,
       "outletSection1VoltageHighThreshold": outletSection1VoltageHighThreshold,
       "outletSection1VoltageLowThreshold": outletSection1VoltageLowThreshold,
       "outletSection1CurrentHighThreshold": outletSection1CurrentHighThreshold,
       "outletSection1CurrentLowThreshold": outletSection1CurrentLowThreshold,
       "outletSection1ControlOutlet": outletSection1ControlOutlet,
       "outletSection1OutletName": outletSection1OutletName,
       "outletSection2Config": outletSection2Config,
       "outletSection2VoltageHighThreshold": outletSection2VoltageHighThreshold,
       "outletSection2VoltageLowThreshold": outletSection2VoltageLowThreshold,
       "outletSection2CurrentHighThreshold": outletSection2CurrentHighThreshold,
       "outletSection2CurrentLowThreshold": outletSection2CurrentLowThreshold,
       "outletSection2ControlOutlet": outletSection2ControlOutlet,
       "outletSection2OutletName": outletSection2OutletName,
       "outletSection3Config": outletSection3Config,
       "outletSection3VoltageHighThreshold": outletSection3VoltageHighThreshold,
       "outletSection3VoltageLowThreshold": outletSection3VoltageLowThreshold,
       "outletSection3CurrentHighThreshold": outletSection3CurrentHighThreshold,
       "outletSection3CurrentLowThreshold": outletSection3CurrentLowThreshold,
       "outletSection3ControlOutlet": outletSection3ControlOutlet,
       "outletSection3OutletName": outletSection3OutletName,
       "outletSection4Config": outletSection4Config,
       "outletSection4VoltageHighThreshold": outletSection4VoltageHighThreshold,
       "outletSection4VoltageLowThreshold": outletSection4VoltageLowThreshold,
       "outletSection4CurrentHighThreshold": outletSection4CurrentHighThreshold,
       "outletSection4CurrentLowThreshold": outletSection4CurrentLowThreshold,
       "outletSection4ControlOutlet": outletSection4ControlOutlet,
       "outletSection4OutletName": outletSection4OutletName,
       "outletSection5Config": outletSection5Config,
       "outletSection5VoltageHighThreshold": outletSection5VoltageHighThreshold,
       "outletSection5VoltageLowThreshold": outletSection5VoltageLowThreshold,
       "outletSection5CurrentHighThreshold": outletSection5CurrentHighThreshold,
       "outletSection5CurrentLowThreshold": outletSection5CurrentLowThreshold,
       "outletSection5ControlOutlet": outletSection5ControlOutlet,
       "outletSection5OutletName": outletSection5OutletName,
       "outletSection6Config": outletSection6Config,
       "outletSection6VoltageHighThreshold": outletSection6VoltageHighThreshold,
       "outletSection6VoltageLowThreshold": outletSection6VoltageLowThreshold,
       "outletSection6CurrentHighThreshold": outletSection6CurrentHighThreshold,
       "outletSection6CurrentLowThreshold": outletSection6CurrentLowThreshold,
       "outletSection6ControlOutlet": outletSection6ControlOutlet,
       "outletSection6OutletName": outletSection6OutletName,
       "currentSensorValues": currentSensorValues,
       "tempSensor1Temp": tempSensor1Temp,
       "tempSensor2Temp": tempSensor2Temp,
       "humSensor1Humidity": humSensor1Humidity,
       "contactClosure1State": contactClosure1State,
       "contactClosure2State": contactClosure2State,
       "contactClosure3State": contactClosure3State,
       "currentOutletSectionValues": currentOutletSectionValues,
       "outletSection1": outletSection1,
       "outletSection1Voltage": outletSection1Voltage,
       "outletSection1Current": outletSection1Current,
       "outletSection1Va": outletSection1Va,
       "outletSection2": outletSection2,
       "outletSection2Voltage": outletSection2Voltage,
       "outletSection2Current": outletSection2Current,
       "outletSection2Va": outletSection2Va,
       "outletSection3": outletSection3,
       "outletSection3Voltage": outletSection3Voltage,
       "outletSection3Current": outletSection3Current,
       "outletSection3Va": outletSection3Va,
       "total": total,
       "totalVoltage": totalVoltage,
       "totalCurrent": totalCurrent,
       "totalVa": totalVa,
       "outletSection4": outletSection4,
       "outletSection4Voltage": outletSection4Voltage,
       "outletSection4Current": outletSection4Current,
       "outletSection4Va": outletSection4Va,
       "outletSection5": outletSection5,
       "outletSection5Voltage": outletSection5Voltage,
       "outletSection5Current": outletSection5Current,
       "outletSection5Va": outletSection5Va,
       "outletSection6": outletSection6,
       "outletSection6Voltage": outletSection6Voltage,
       "outletSection6Current": outletSection6Current,
       "outletSection6Va": outletSection6Va,
       "events": events,
       "notifyOutletState": notifyOutletState,
       "notifyCurrentThreshold": notifyCurrentThreshold,
       "notifyVoltageThreshold": notifyVoltageThreshold,
       "notifyTempSensorThreshold": notifyTempSensorThreshold,
       "notifyHumidSensorThreshold": notifyHumidSensorThreshold,
       "notifyContactSensorThreshold": notifyContactSensorThreshold,
       "notifyUserLogin": notifyUserLogin,
       "notifyUserLogout": notifyUserLogout,
       "notifyFailedLogin": notifyFailedLogin,
       "notifyOutletWatchdogFailed": notifyOutletWatchdogFailed,
       "eventInfo": eventInfo,
       "infoItemIdx": infoItemIdx,
       "infoItemName": infoItemName,
       "infoOutletState": infoOutletState,
       "infoThresholdState": infoThresholdState,
       "infoThresholdValue": infoThresholdValue,
       "infoMeasuredValue": infoMeasuredValue,
       "infoContactState": infoContactState,
       "infoUserName": infoUserName,
       "conformance": conformance,
       "compliances": compliances,
       "oldCompliances": oldCompliances,
       "obsoleteCompliances": obsoleteCompliances,
       "groups": groups,
       "allObjects": allObjects,
       "oldObjects": oldObjects,
       "obsoleteObjects": obsoleteObjects,
       "allNotifications": allNotifications}
)
