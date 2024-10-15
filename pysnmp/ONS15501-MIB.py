# SNMP MIB module (ONS15501-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONS15501-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:12 2024
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ons15501MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11)
)
ons15501MIB.setRevisions(
        ("2002-08-29 16:00",
         "2002-03-18 12:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Ons15501ImageDnLoadStatus(Integer32, TextualConvention):
    status = "current"
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
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("completedSuccessfully", 7),
          ("failedAccessDenied", 5),
          ("failedFileExists", 13),
          ("failedFileNotFound", 4),
          ("failedIllegalOperation", 12),
          ("failedInDownload", 8),
          ("failedTimedOut", 6),
          ("failedTimeoutInDownload", 9),
          ("failedToConnectToServer", 10),
          ("failedUnknownErr", 3),
          ("failedUnknownTransferId", 14),
          ("failedUnknownUser", 15),
          ("failedWhileWritingToFlash", 11),
          ("inProgress", 2),
          ("notInitiated", 1))
    )



class Ons15501AdminStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )



class Ons15501NTPStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bothServersBad", 2),
          ("disabled", 1),
          ("unknown", 5),
          ("usingPrimary", 3),
          ("usingSecondary", 4))
    )



class Ons15501TenthVolt(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 0),
    )



class Ons15501TenthdB(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 500),
    )



class Ons15501TenthCentigrade(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 1000),
    )



class Ons15501AlarmStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("info", 4),
          ("major", 2),
          ("minor", 3),
          ("noAlarm", 5))
    )



class Ons15501TrapTypeEnumeration(Integer32, TextualConvention):
    status = "current"
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
              10,
              11,
              12,
              13,
              14,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("configurationChanged", 11),
          ("eEPROMBad", 14),
          ("embeddedControllerCommFailure", 5),
          ("inputSignalPowerTooLow", 3),
          ("laserPumpBad", 13),
          ("softwareRebootInitiated", 9),
          ("softwareRolledBack", 10),
          ("softwareUpgradeCompleted", 8),
          ("softwareUpgradeFailed", 7),
          ("softwareUpgradeInitiated", 6),
          ("unacceptableAmbientTemperature", 1),
          ("unacceptableElectricalPower", 2),
          ("unacceptableGain", 12),
          ("unacceptableOutputSignalPower", 4),
          ("unknown", 32767))
    )



class Ons15501TrapDirectionEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asserted", 2),
          ("cleared", 3),
          ("dontCare", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Synchronous_ObjectIdentity = ObjectIdentity
synchronous = _Synchronous_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869)
)
_SynEmbLx_ObjectIdentity = ObjectIdentity
synEmbLx = _SynEmbLx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11)
)
_Ons15501Sys_ObjectIdentity = ObjectIdentity
ons15501Sys = _Ons15501Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1)
)
_Ons15501SysDevFlash1Image_Type = DisplayString
_Ons15501SysDevFlash1Image_Object = MibScalar
ons15501SysDevFlash1Image = _Ons15501SysDevFlash1Image_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 1),
    _Ons15501SysDevFlash1Image_Type()
)
ons15501SysDevFlash1Image.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501SysDevFlash1Image.setStatus("current")
_Ons15501SysDevFlash2Image_Type = DisplayString
_Ons15501SysDevFlash2Image_Object = MibScalar
ons15501SysDevFlash2Image = _Ons15501SysDevFlash2Image_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 2),
    _Ons15501SysDevFlash2Image_Type()
)
ons15501SysDevFlash2Image.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501SysDevFlash2Image.setStatus("current")
_Ons15501SysDevFlash3Image_Type = DisplayString
_Ons15501SysDevFlash3Image_Object = MibScalar
ons15501SysDevFlash3Image = _Ons15501SysDevFlash3Image_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 3),
    _Ons15501SysDevFlash3Image_Type()
)
ons15501SysDevFlash3Image.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501SysDevFlash3Image.setStatus("current")
_Ons15501SysSwDownload_Type = DisplayString
_Ons15501SysSwDownload_Object = MibScalar
ons15501SysSwDownload = _Ons15501SysSwDownload_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 4),
    _Ons15501SysSwDownload_Type()
)
ons15501SysSwDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501SysSwDownload.setStatus("current")


class _Ons15501SysDevActiveImage_Type(Unsigned32):
    """Custom type ons15501SysDevActiveImage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Ons15501SysDevActiveImage_Type.__name__ = "Unsigned32"
_Ons15501SysDevActiveImage_Object = MibScalar
ons15501SysDevActiveImage = _Ons15501SysDevActiveImage_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 5),
    _Ons15501SysDevActiveImage_Type()
)
ons15501SysDevActiveImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501SysDevActiveImage.setStatus("current")
_Ons15501SysDeviceManagerList_Type = DisplayString
_Ons15501SysDeviceManagerList_Object = MibScalar
ons15501SysDeviceManagerList = _Ons15501SysDeviceManagerList_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 6),
    _Ons15501SysDeviceManagerList_Type()
)
ons15501SysDeviceManagerList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501SysDeviceManagerList.setStatus("current")
_Ons15501SysSwDownloadStatus_Type = Ons15501ImageDnLoadStatus
_Ons15501SysSwDownloadStatus_Object = MibScalar
ons15501SysSwDownloadStatus = _Ons15501SysSwDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 7),
    _Ons15501SysSwDownloadStatus_Type()
)
ons15501SysSwDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501SysSwDownloadStatus.setStatus("current")


class _Ons15501SysConfiguredImage_Type(Unsigned32):
    """Custom type ons15501SysConfiguredImage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Ons15501SysConfiguredImage_Type.__name__ = "Unsigned32"
_Ons15501SysConfiguredImage_Object = MibScalar
ons15501SysConfiguredImage = _Ons15501SysConfiguredImage_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 8),
    _Ons15501SysConfiguredImage_Type()
)
ons15501SysConfiguredImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501SysConfiguredImage.setStatus("current")
_Ons15501CLEICode_Type = DisplayString
_Ons15501CLEICode_Object = MibScalar
ons15501CLEICode = _Ons15501CLEICode_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 9),
    _Ons15501CLEICode_Type()
)
ons15501CLEICode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501CLEICode.setStatus("current")
_Ons15501PrimaryNTP_Type = IpAddress
_Ons15501PrimaryNTP_Object = MibScalar
ons15501PrimaryNTP = _Ons15501PrimaryNTP_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 10),
    _Ons15501PrimaryNTP_Type()
)
ons15501PrimaryNTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501PrimaryNTP.setStatus("current")
_Ons15501SecondaryNTP_Type = IpAddress
_Ons15501SecondaryNTP_Object = MibScalar
ons15501SecondaryNTP = _Ons15501SecondaryNTP_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 11),
    _Ons15501SecondaryNTP_Type()
)
ons15501SecondaryNTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501SecondaryNTP.setStatus("current")
_Ons15501NTPAdminStatus_Type = Ons15501AdminStatus
_Ons15501NTPAdminStatus_Object = MibScalar
ons15501NTPAdminStatus = _Ons15501NTPAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 12),
    _Ons15501NTPAdminStatus_Type()
)
ons15501NTPAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501NTPAdminStatus.setStatus("current")
_Ons15501NTPOperationalStatus_Type = Ons15501NTPStatus
_Ons15501NTPOperationalStatus_Object = MibScalar
ons15501NTPOperationalStatus = _Ons15501NTPOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 13),
    _Ons15501NTPOperationalStatus_Type()
)
ons15501NTPOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501NTPOperationalStatus.setStatus("current")
_Ons15501ActiveSoftwareVer_Type = DisplayString
_Ons15501ActiveSoftwareVer_Object = MibScalar
ons15501ActiveSoftwareVer = _Ons15501ActiveSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 14),
    _Ons15501ActiveSoftwareVer_Type()
)
ons15501ActiveSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501ActiveSoftwareVer.setStatus("current")
_Ons15501LastConfigChangeTime_Type = TimeStamp
_Ons15501LastConfigChangeTime_Object = MibScalar
ons15501LastConfigChangeTime = _Ons15501LastConfigChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 15),
    _Ons15501LastConfigChangeTime_Type()
)
ons15501LastConfigChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501LastConfigChangeTime.setStatus("current")
_Ons15501InRemoteInfoUpdateTime_Type = TimeStamp
_Ons15501InRemoteInfoUpdateTime_Object = MibScalar
ons15501InRemoteInfoUpdateTime = _Ons15501InRemoteInfoUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 16),
    _Ons15501InRemoteInfoUpdateTime_Type()
)
ons15501InRemoteInfoUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501InRemoteInfoUpdateTime.setStatus("current")
_Ons15501InRemoteChassisName_Type = DisplayString
_Ons15501InRemoteChassisName_Object = MibScalar
ons15501InRemoteChassisName = _Ons15501InRemoteChassisName_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 17),
    _Ons15501InRemoteChassisName_Type()
)
ons15501InRemoteChassisName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501InRemoteChassisName.setStatus("current")
_Ons15501InRemotePortName_Type = DisplayString
_Ons15501InRemotePortName_Object = MibScalar
ons15501InRemotePortName = _Ons15501InRemotePortName_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 18),
    _Ons15501InRemotePortName_Type()
)
ons15501InRemotePortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501InRemotePortName.setStatus("current")
_Ons15501InRemoteAgentIpAddr_Type = IpAddress
_Ons15501InRemoteAgentIpAddr_Object = MibScalar
ons15501InRemoteAgentIpAddr = _Ons15501InRemoteAgentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 19),
    _Ons15501InRemoteAgentIpAddr_Type()
)
ons15501InRemoteAgentIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501InRemoteAgentIpAddr.setStatus("current")
_Ons15501OutRemoteInfoUpdateTime_Type = TimeStamp
_Ons15501OutRemoteInfoUpdateTime_Object = MibScalar
ons15501OutRemoteInfoUpdateTime = _Ons15501OutRemoteInfoUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 20),
    _Ons15501OutRemoteInfoUpdateTime_Type()
)
ons15501OutRemoteInfoUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501OutRemoteInfoUpdateTime.setStatus("current")
_Ons15501OutRemoteChassisName_Type = DisplayString
_Ons15501OutRemoteChassisName_Object = MibScalar
ons15501OutRemoteChassisName = _Ons15501OutRemoteChassisName_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 21),
    _Ons15501OutRemoteChassisName_Type()
)
ons15501OutRemoteChassisName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501OutRemoteChassisName.setStatus("current")
_Ons15501OutRemotePortName_Type = DisplayString
_Ons15501OutRemotePortName_Object = MibScalar
ons15501OutRemotePortName = _Ons15501OutRemotePortName_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 22),
    _Ons15501OutRemotePortName_Type()
)
ons15501OutRemotePortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501OutRemotePortName.setStatus("current")
_Ons15501OutRemoteAgentIpAddr_Type = IpAddress
_Ons15501OutRemoteAgentIpAddr_Object = MibScalar
ons15501OutRemoteAgentIpAddr = _Ons15501OutRemoteAgentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 23),
    _Ons15501OutRemoteAgentIpAddr_Type()
)
ons15501OutRemoteAgentIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501OutRemoteAgentIpAddr.setStatus("current")
_Ons15501SysAlarmStatus_Type = Ons15501AlarmStatus
_Ons15501SysAlarmStatus_Object = MibScalar
ons15501SysAlarmStatus = _Ons15501SysAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 24),
    _Ons15501SysAlarmStatus_Type()
)
ons15501SysAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501SysAlarmStatus.setStatus("current")
_Ons15501SysDateAndTime_Type = DateAndTime
_Ons15501SysDateAndTime_Object = MibScalar
ons15501SysDateAndTime = _Ons15501SysDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 25),
    _Ons15501SysDateAndTime_Type()
)
ons15501SysDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501SysDateAndTime.setStatus("current")
_Ons15501Attr_ObjectIdentity = ObjectIdentity
ons15501Attr = _Ons15501Attr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2)
)
_Ons15501InputOpticalPower_Type = Ons15501TenthdB
_Ons15501InputOpticalPower_Object = MibScalar
ons15501InputOpticalPower = _Ons15501InputOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 1),
    _Ons15501InputOpticalPower_Type()
)
ons15501InputOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501InputOpticalPower.setStatus("current")
if mibBuilder.loadTexts:
    ons15501InputOpticalPower.setUnits("dBm")


class _Ons15501InputOpticalPowerMean_Type(Ons15501TenthdB):
    """Custom type ons15501InputOpticalPowerMean based on Ons15501TenthdB"""
    subtypeSpec = Ons15501TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_Ons15501InputOpticalPowerMean_Type.__name__ = "Ons15501TenthdB"
_Ons15501InputOpticalPowerMean_Object = MibScalar
ons15501InputOpticalPowerMean = _Ons15501InputOpticalPowerMean_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 2),
    _Ons15501InputOpticalPowerMean_Type()
)
ons15501InputOpticalPowerMean.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501InputOpticalPowerMean.setStatus("current")
if mibBuilder.loadTexts:
    ons15501InputOpticalPowerMean.setUnits("dBm")


class _Ons15501InputOpticalPowerTrigger_Type(Ons15501TenthdB):
    """Custom type ons15501InputOpticalPowerTrigger based on Ons15501TenthdB"""
    subtypeSpec = Ons15501TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Ons15501InputOpticalPowerTrigger_Type.__name__ = "Ons15501TenthdB"
_Ons15501InputOpticalPowerTrigger_Object = MibScalar
ons15501InputOpticalPowerTrigger = _Ons15501InputOpticalPowerTrigger_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 3),
    _Ons15501InputOpticalPowerTrigger_Type()
)
ons15501InputOpticalPowerTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501InputOpticalPowerTrigger.setStatus("current")
if mibBuilder.loadTexts:
    ons15501InputOpticalPowerTrigger.setUnits("dB")
_Ons15501OutputOpticalPower_Type = Ons15501TenthdB
_Ons15501OutputOpticalPower_Object = MibScalar
ons15501OutputOpticalPower = _Ons15501OutputOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 4),
    _Ons15501OutputOpticalPower_Type()
)
ons15501OutputOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501OutputOpticalPower.setStatus("current")
if mibBuilder.loadTexts:
    ons15501OutputOpticalPower.setUnits("dBm")
_Ons15501OutputSignalPower_Type = Ons15501TenthdB
_Ons15501OutputSignalPower_Object = MibScalar
ons15501OutputSignalPower = _Ons15501OutputSignalPower_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 5),
    _Ons15501OutputSignalPower_Type()
)
ons15501OutputSignalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501OutputSignalPower.setStatus("current")
if mibBuilder.loadTexts:
    ons15501OutputSignalPower.setUnits("dBm")


class _Ons15501OutputSignalPowerMean_Type(Ons15501TenthdB):
    """Custom type ons15501OutputSignalPowerMean based on Ons15501TenthdB"""
    subtypeSpec = Ons15501TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 0),
    )


_Ons15501OutputSignalPowerMean_Type.__name__ = "Ons15501TenthdB"
_Ons15501OutputSignalPowerMean_Object = MibScalar
ons15501OutputSignalPowerMean = _Ons15501OutputSignalPowerMean_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 6),
    _Ons15501OutputSignalPowerMean_Type()
)
ons15501OutputSignalPowerMean.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501OutputSignalPowerMean.setStatus("current")
if mibBuilder.loadTexts:
    ons15501OutputSignalPowerMean.setUnits("dBm")


class _Ons15501OutputSignalPowerTrigger_Type(Ons15501TenthdB):
    """Custom type ons15501OutputSignalPowerTrigger based on Ons15501TenthdB"""
    subtypeSpec = Ons15501TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_Ons15501OutputSignalPowerTrigger_Type.__name__ = "Ons15501TenthdB"
_Ons15501OutputSignalPowerTrigger_Object = MibScalar
ons15501OutputSignalPowerTrigger = _Ons15501OutputSignalPowerTrigger_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 7),
    _Ons15501OutputSignalPowerTrigger_Type()
)
ons15501OutputSignalPowerTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501OutputSignalPowerTrigger.setStatus("current")
if mibBuilder.loadTexts:
    ons15501OutputSignalPowerTrigger.setUnits("dB")


class _Ons15501ConfigOpticalGain_Type(Ons15501TenthdB):
    """Custom type ons15501ConfigOpticalGain based on Ons15501TenthdB"""
    subtypeSpec = Ons15501TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(70, 175),
    )


_Ons15501ConfigOpticalGain_Type.__name__ = "Ons15501TenthdB"
_Ons15501ConfigOpticalGain_Object = MibScalar
ons15501ConfigOpticalGain = _Ons15501ConfigOpticalGain_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 8),
    _Ons15501ConfigOpticalGain_Type()
)
ons15501ConfigOpticalGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501ConfigOpticalGain.setStatus("current")
if mibBuilder.loadTexts:
    ons15501ConfigOpticalGain.setUnits("dB")
_Ons15501OpticalPowerGain_Type = Ons15501TenthdB
_Ons15501OpticalPowerGain_Object = MibScalar
ons15501OpticalPowerGain = _Ons15501OpticalPowerGain_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 9),
    _Ons15501OpticalPowerGain_Type()
)
ons15501OpticalPowerGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501OpticalPowerGain.setStatus("current")
if mibBuilder.loadTexts:
    ons15501OpticalPowerGain.setUnits("dB")


class _Ons15501GainTrigger_Type(Ons15501TenthdB):
    """Custom type ons15501GainTrigger based on Ons15501TenthdB"""
    subtypeSpec = Ons15501TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_Ons15501GainTrigger_Type.__name__ = "Ons15501TenthdB"
_Ons15501GainTrigger_Object = MibScalar
ons15501GainTrigger = _Ons15501GainTrigger_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 10),
    _Ons15501GainTrigger_Type()
)
ons15501GainTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501GainTrigger.setStatus("current")
if mibBuilder.loadTexts:
    ons15501GainTrigger.setUnits("dB")
_Ons15501PowerSupply1Level_Type = Ons15501TenthVolt
_Ons15501PowerSupply1Level_Object = MibScalar
ons15501PowerSupply1Level = _Ons15501PowerSupply1Level_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 11),
    _Ons15501PowerSupply1Level_Type()
)
ons15501PowerSupply1Level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501PowerSupply1Level.setStatus("current")
if mibBuilder.loadTexts:
    ons15501PowerSupply1Level.setUnits("volts")
_Ons15501PowerSupply2Level_Type = Ons15501TenthVolt
_Ons15501PowerSupply2Level_Object = MibScalar
ons15501PowerSupply2Level = _Ons15501PowerSupply2Level_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 12),
    _Ons15501PowerSupply2Level_Type()
)
ons15501PowerSupply2Level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501PowerSupply2Level.setStatus("current")
if mibBuilder.loadTexts:
    ons15501PowerSupply2Level.setUnits("volts")
_Ons15501LaserStatus_Type = Ons15501AlarmStatus
_Ons15501LaserStatus_Object = MibScalar
ons15501LaserStatus = _Ons15501LaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 13),
    _Ons15501LaserStatus_Type()
)
ons15501LaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501LaserStatus.setStatus("current")
_Ons15501DevAmbTemp_Type = Ons15501TenthCentigrade
_Ons15501DevAmbTemp_Object = MibScalar
ons15501DevAmbTemp = _Ons15501DevAmbTemp_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 14),
    _Ons15501DevAmbTemp_Type()
)
ons15501DevAmbTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501DevAmbTemp.setStatus("current")
if mibBuilder.loadTexts:
    ons15501DevAmbTemp.setUnits("degrees C")


class _Ons15501DevAmbTempMean_Type(Ons15501TenthCentigrade):
    """Custom type ons15501DevAmbTempMean based on Ons15501TenthCentigrade"""
    subtypeSpec = Ons15501TenthCentigrade.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 400),
    )


_Ons15501DevAmbTempMean_Type.__name__ = "Ons15501TenthCentigrade"
_Ons15501DevAmbTempMean_Object = MibScalar
ons15501DevAmbTempMean = _Ons15501DevAmbTempMean_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 15),
    _Ons15501DevAmbTempMean_Type()
)
ons15501DevAmbTempMean.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501DevAmbTempMean.setStatus("current")
if mibBuilder.loadTexts:
    ons15501DevAmbTempMean.setUnits("degrees C")


class _Ons15501DevAmbTempTrigger_Type(Ons15501TenthCentigrade):
    """Custom type ons15501DevAmbTempTrigger based on Ons15501TenthCentigrade"""
    subtypeSpec = Ons15501TenthCentigrade.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 300),
    )


_Ons15501DevAmbTempTrigger_Type.__name__ = "Ons15501TenthCentigrade"
_Ons15501DevAmbTempTrigger_Object = MibScalar
ons15501DevAmbTempTrigger = _Ons15501DevAmbTempTrigger_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 16),
    _Ons15501DevAmbTempTrigger_Type()
)
ons15501DevAmbTempTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ons15501DevAmbTempTrigger.setStatus("current")
if mibBuilder.loadTexts:
    ons15501DevAmbTempTrigger.setUnits("degrees C")
_Ons15501PowerSupply1Status_Type = Ons15501AlarmStatus
_Ons15501PowerSupply1Status_Object = MibScalar
ons15501PowerSupply1Status = _Ons15501PowerSupply1Status_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 17),
    _Ons15501PowerSupply1Status_Type()
)
ons15501PowerSupply1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501PowerSupply1Status.setStatus("current")
_Ons15501PowerSupply2Status_Type = Ons15501AlarmStatus
_Ons15501PowerSupply2Status_Object = MibScalar
ons15501PowerSupply2Status = _Ons15501PowerSupply2Status_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 18),
    _Ons15501PowerSupply2Status_Type()
)
ons15501PowerSupply2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501PowerSupply2Status.setStatus("current")
_Ons15501Alarms_ObjectIdentity = ObjectIdentity
ons15501Alarms = _Ons15501Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3)
)


class _Ons15501LastTrapIndex_Type(Unsigned32):
    """Custom type ons15501LastTrapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Ons15501LastTrapIndex_Type.__name__ = "Unsigned32"
_Ons15501LastTrapIndex_Object = MibScalar
ons15501LastTrapIndex = _Ons15501LastTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 1),
    _Ons15501LastTrapIndex_Type()
)
ons15501LastTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501LastTrapIndex.setStatus("current")
_Ons15501TrapLogTable_Object = MibTable
ons15501TrapLogTable = _Ons15501TrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2)
)
if mibBuilder.loadTexts:
    ons15501TrapLogTable.setStatus("current")
_Ons15501TrapLogEntry_Object = MibTableRow
ons15501TrapLogEntry = _Ons15501TrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1)
)
ons15501TrapLogEntry.setIndexNames(
    (0, "ONS15501-MIB", "ons15501TrapLogEntryIndex"),
)
if mibBuilder.loadTexts:
    ons15501TrapLogEntry.setStatus("current")


class _Ons15501TrapLogEntryIndex_Type(Unsigned32):
    """Custom type ons15501TrapLogEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Ons15501TrapLogEntryIndex_Type.__name__ = "Unsigned32"
_Ons15501TrapLogEntryIndex_Object = MibTableColumn
ons15501TrapLogEntryIndex = _Ons15501TrapLogEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1, 1),
    _Ons15501TrapLogEntryIndex_Type()
)
ons15501TrapLogEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ons15501TrapLogEntryIndex.setStatus("current")
_Ons15501TrapLogEntryTrapType_Type = Ons15501TrapTypeEnumeration
_Ons15501TrapLogEntryTrapType_Object = MibTableColumn
ons15501TrapLogEntryTrapType = _Ons15501TrapLogEntryTrapType_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1, 2),
    _Ons15501TrapLogEntryTrapType_Type()
)
ons15501TrapLogEntryTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501TrapLogEntryTrapType.setStatus("current")
_Ons15501TrapLogEntryDirection_Type = Ons15501TrapDirectionEnumeration
_Ons15501TrapLogEntryDirection_Object = MibTableColumn
ons15501TrapLogEntryDirection = _Ons15501TrapLogEntryDirection_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1, 3),
    _Ons15501TrapLogEntryDirection_Type()
)
ons15501TrapLogEntryDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501TrapLogEntryDirection.setStatus("current")
_Ons15501TrapLogEntryTimeStamp_Type = TimeStamp
_Ons15501TrapLogEntryTimeStamp_Object = MibTableColumn
ons15501TrapLogEntryTimeStamp = _Ons15501TrapLogEntryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1, 4),
    _Ons15501TrapLogEntryTimeStamp_Type()
)
ons15501TrapLogEntryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501TrapLogEntryTimeStamp.setStatus("current")
_Ons15501TrapLogEntryDateAndTime_Type = DateAndTime
_Ons15501TrapLogEntryDateAndTime_Object = MibTableColumn
ons15501TrapLogEntryDateAndTime = _Ons15501TrapLogEntryDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1, 5),
    _Ons15501TrapLogEntryDateAndTime_Type()
)
ons15501TrapLogEntryDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501TrapLogEntryDateAndTime.setStatus("current")
_Ons15501TrapLogEntryPhyIndex_Type = PhysicalIndex
_Ons15501TrapLogEntryPhyIndex_Object = MibTableColumn
ons15501TrapLogEntryPhyIndex = _Ons15501TrapLogEntryPhyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1, 6),
    _Ons15501TrapLogEntryPhyIndex_Type()
)
ons15501TrapLogEntryPhyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501TrapLogEntryPhyIndex.setStatus("current")
_Ons15501TrapLogEntrySeverity_Type = Ons15501AlarmStatus
_Ons15501TrapLogEntrySeverity_Object = MibTableColumn
ons15501TrapLogEntrySeverity = _Ons15501TrapLogEntrySeverity_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1, 7),
    _Ons15501TrapLogEntrySeverity_Type()
)
ons15501TrapLogEntrySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501TrapLogEntrySeverity.setStatus("current")
_Ons15501ActiveAlarmTable_Object = MibTable
ons15501ActiveAlarmTable = _Ons15501ActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 3)
)
if mibBuilder.loadTexts:
    ons15501ActiveAlarmTable.setStatus("current")
_Ons15501ActiveAlarmEntry_Object = MibTableRow
ons15501ActiveAlarmEntry = _Ons15501ActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 3, 1)
)
ons15501ActiveAlarmEntry.setIndexNames(
    (0, "ONS15501-MIB", "ons15501ActAlarmType"),
)
if mibBuilder.loadTexts:
    ons15501ActiveAlarmEntry.setStatus("current")
_Ons15501ActAlarmType_Type = Ons15501TrapTypeEnumeration
_Ons15501ActAlarmType_Object = MibTableColumn
ons15501ActAlarmType = _Ons15501ActAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 3, 1, 1),
    _Ons15501ActAlarmType_Type()
)
ons15501ActAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ons15501ActAlarmType.setStatus("current")
_Ons15501ActAlarmTimeStamp_Type = TimeStamp
_Ons15501ActAlarmTimeStamp_Object = MibTableColumn
ons15501ActAlarmTimeStamp = _Ons15501ActAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 3, 1, 2),
    _Ons15501ActAlarmTimeStamp_Type()
)
ons15501ActAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501ActAlarmTimeStamp.setStatus("current")
_Ons15501ActAlarmDateAndTime_Type = DateAndTime
_Ons15501ActAlarmDateAndTime_Object = MibTableColumn
ons15501ActAlarmDateAndTime = _Ons15501ActAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 3, 1, 3),
    _Ons15501ActAlarmDateAndTime_Type()
)
ons15501ActAlarmDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501ActAlarmDateAndTime.setStatus("current")
_Ons15501ActAlarmPhyIndex_Type = PhysicalIndex
_Ons15501ActAlarmPhyIndex_Object = MibTableColumn
ons15501ActAlarmPhyIndex = _Ons15501ActAlarmPhyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 3, 1, 4),
    _Ons15501ActAlarmPhyIndex_Type()
)
ons15501ActAlarmPhyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501ActAlarmPhyIndex.setStatus("current")
_Ons15501ActAlarmSeverity_Type = Ons15501AlarmStatus
_Ons15501ActAlarmSeverity_Object = MibTableColumn
ons15501ActAlarmSeverity = _Ons15501ActAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 3, 1, 5),
    _Ons15501ActAlarmSeverity_Type()
)
ons15501ActAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501ActAlarmSeverity.setStatus("current")
_Ons15501TrapDescriptionTable_Object = MibTable
ons15501TrapDescriptionTable = _Ons15501TrapDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 4)
)
if mibBuilder.loadTexts:
    ons15501TrapDescriptionTable.setStatus("current")
_Ons15501TrapDescriptionEntry_Object = MibTableRow
ons15501TrapDescriptionEntry = _Ons15501TrapDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 4, 1)
)
ons15501TrapDescriptionEntry.setIndexNames(
    (0, "ONS15501-MIB", "ons15501TrapTypeValue"),
)
if mibBuilder.loadTexts:
    ons15501TrapDescriptionEntry.setStatus("current")
_Ons15501TrapTypeValue_Type = Ons15501TrapTypeEnumeration
_Ons15501TrapTypeValue_Object = MibTableColumn
ons15501TrapTypeValue = _Ons15501TrapTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 4, 1, 1),
    _Ons15501TrapTypeValue_Type()
)
ons15501TrapTypeValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ons15501TrapTypeValue.setStatus("current")
_Ons15501TrapDescription_Type = DisplayString
_Ons15501TrapDescription_Object = MibTableColumn
ons15501TrapDescription = _Ons15501TrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 4, 1, 2),
    _Ons15501TrapDescription_Type()
)
ons15501TrapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501TrapDescription.setStatus("current")
_Ons15501TrapSeverity_Type = Ons15501AlarmStatus
_Ons15501TrapSeverity_Object = MibTableColumn
ons15501TrapSeverity = _Ons15501TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 4, 1, 3),
    _Ons15501TrapSeverity_Type()
)
ons15501TrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ons15501TrapSeverity.setStatus("current")
_Ons15501Notification_ObjectIdentity = ObjectIdentity
ons15501Notification = _Ons15501Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 4)
)
_Ons15501NotificationPrefix_ObjectIdentity = ObjectIdentity
ons15501NotificationPrefix = _Ons15501NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 4, 0)
)
_Ons15501OIDs_ObjectIdentity = ObjectIdentity
ons15501OIDs = _Ons15501OIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 5)
)
_Ons15501OIDSystem_ObjectIdentity = ObjectIdentity
ons15501OIDSystem = _Ons15501OIDSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 1)
)
_Ons15501OIDEntity_ObjectIdentity = ObjectIdentity
ons15501OIDEntity = _Ons15501OIDEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 2)
)
_Ons15501OIDChasiss_ObjectIdentity = ObjectIdentity
ons15501OIDChasiss = _Ons15501OIDChasiss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 2, 1)
)
_Ons15501OIDInPort_ObjectIdentity = ObjectIdentity
ons15501OIDInPort = _Ons15501OIDInPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 2, 2)
)
_Ons15501OIDOutPort_ObjectIdentity = ObjectIdentity
ons15501OIDOutPort = _Ons15501OIDOutPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 2, 3)
)
_Ons15501OIDPowerSupply_ObjectIdentity = ObjectIdentity
ons15501OIDPowerSupply = _Ons15501OIDPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 2, 4)
)
_Ons15501OIDChassisAC_ObjectIdentity = ObjectIdentity
ons15501OIDChassisAC = _Ons15501OIDChassisAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 2, 5)
)
_Ons15501OIDPowerSupplyAC_ObjectIdentity = ObjectIdentity
ons15501OIDPowerSupplyAC = _Ons15501OIDPowerSupplyAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 2, 6)
)
_Ons15501OIDSystemAC_ObjectIdentity = ObjectIdentity
ons15501OIDSystemAC = _Ons15501OIDSystemAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 3)
)
_Ons15501MIBConformance_ObjectIdentity = ObjectIdentity
ons15501MIBConformance = _Ons15501MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 6)
)
_Ons15501MIBCompliances_ObjectIdentity = ObjectIdentity
ons15501MIBCompliances = _Ons15501MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 1)
)
_Ons15501MIBGroups_ObjectIdentity = ObjectIdentity
ons15501MIBGroups = _Ons15501MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2)
)

# Managed Objects groups

ons15501SysInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 1)
)
ons15501SysInfoGroup.setObjects(
      *(("ONS15501-MIB", "ons15501SysDevFlash1Image"),
        ("ONS15501-MIB", "ons15501SysDevFlash2Image"),
        ("ONS15501-MIB", "ons15501SysDevFlash3Image"),
        ("ONS15501-MIB", "ons15501SysSwDownload"),
        ("ONS15501-MIB", "ons15501SysSwDownloadStatus"),
        ("ONS15501-MIB", "ons15501SysConfiguredImage"),
        ("ONS15501-MIB", "ons15501SysDevActiveImage"),
        ("ONS15501-MIB", "ons15501SysAlarmStatus"),
        ("ONS15501-MIB", "ons15501PrimaryNTP"),
        ("ONS15501-MIB", "ons15501SecondaryNTP"),
        ("ONS15501-MIB", "ons15501NTPAdminStatus"),
        ("ONS15501-MIB", "ons15501NTPOperationalStatus"),
        ("ONS15501-MIB", "ons15501CLEICode"),
        ("ONS15501-MIB", "ons15501InRemoteInfoUpdateTime"),
        ("ONS15501-MIB", "ons15501InRemoteChassisName"),
        ("ONS15501-MIB", "ons15501InRemotePortName"),
        ("ONS15501-MIB", "ons15501InRemoteAgentIpAddr"),
        ("ONS15501-MIB", "ons15501OutRemoteInfoUpdateTime"),
        ("ONS15501-MIB", "ons15501OutRemoteChassisName"),
        ("ONS15501-MIB", "ons15501OutRemotePortName"),
        ("ONS15501-MIB", "ons15501OutRemoteAgentIpAddr"),
        ("ONS15501-MIB", "ons15501LastConfigChangeTime"),
        ("ONS15501-MIB", "ons15501ActiveSoftwareVer"),
        ("ONS15501-MIB", "ons15501SysDeviceManagerList"))
)
if mibBuilder.loadTexts:
    ons15501SysInfoGroup.setStatus("deprecated")

ons15501TrapLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 2)
)
ons15501TrapLogGroup.setObjects(
      *(("ONS15501-MIB", "ons15501LastTrapIndex"),
        ("ONS15501-MIB", "ons15501TrapLogEntryTrapType"),
        ("ONS15501-MIB", "ons15501TrapLogEntryDirection"),
        ("ONS15501-MIB", "ons15501TrapLogEntryTimeStamp"),
        ("ONS15501-MIB", "ons15501TrapLogEntryDateAndTime"),
        ("ONS15501-MIB", "ons15501TrapLogEntryPhyIndex"),
        ("ONS15501-MIB", "ons15501TrapLogEntrySeverity"))
)
if mibBuilder.loadTexts:
    ons15501TrapLogGroup.setStatus("current")

ons15501ActiveAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 3)
)
ons15501ActiveAlarmGroup.setObjects(
      *(("ONS15501-MIB", "ons15501ActAlarmPhyIndex"),
        ("ONS15501-MIB", "ons15501ActAlarmTimeStamp"),
        ("ONS15501-MIB", "ons15501ActAlarmDateAndTime"),
        ("ONS15501-MIB", "ons15501ActAlarmSeverity"))
)
if mibBuilder.loadTexts:
    ons15501ActiveAlarmGroup.setStatus("current")

ons15501TrapDescriptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 4)
)
ons15501TrapDescriptionGroup.setObjects(
      *(("ONS15501-MIB", "ons15501TrapDescription"),
        ("ONS15501-MIB", "ons15501TrapSeverity"))
)
if mibBuilder.loadTexts:
    ons15501TrapDescriptionGroup.setStatus("current")

ons15501FinalAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 5)
)
ons15501FinalAttrGroup.setObjects(
      *(("ONS15501-MIB", "ons15501InputOpticalPower"),
        ("ONS15501-MIB", "ons15501InputOpticalPowerMean"),
        ("ONS15501-MIB", "ons15501InputOpticalPowerTrigger"),
        ("ONS15501-MIB", "ons15501OutputOpticalPower"),
        ("ONS15501-MIB", "ons15501OutputSignalPower"),
        ("ONS15501-MIB", "ons15501OutputSignalPowerMean"),
        ("ONS15501-MIB", "ons15501OutputSignalPowerTrigger"),
        ("ONS15501-MIB", "ons15501ConfigOpticalGain"),
        ("ONS15501-MIB", "ons15501OpticalPowerGain"),
        ("ONS15501-MIB", "ons15501PowerSupply1Level"),
        ("ONS15501-MIB", "ons15501PowerSupply2Level"),
        ("ONS15501-MIB", "ons15501DevAmbTemp"),
        ("ONS15501-MIB", "ons15501DevAmbTempMean"),
        ("ONS15501-MIB", "ons15501DevAmbTempTrigger"),
        ("ONS15501-MIB", "ons15501LaserStatus"),
        ("ONS15501-MIB", "ons15501GainTrigger"))
)
if mibBuilder.loadTexts:
    ons15501FinalAttrGroup.setStatus("deprecated")

ons15501CoreAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 7)
)
ons15501CoreAttrGroup.setObjects(
      *(("ONS15501-MIB", "ons15501InputOpticalPower"),
        ("ONS15501-MIB", "ons15501InputOpticalPowerMean"),
        ("ONS15501-MIB", "ons15501InputOpticalPowerTrigger"),
        ("ONS15501-MIB", "ons15501OutputOpticalPower"),
        ("ONS15501-MIB", "ons15501OutputSignalPower"),
        ("ONS15501-MIB", "ons15501OutputSignalPowerMean"),
        ("ONS15501-MIB", "ons15501OutputSignalPowerTrigger"),
        ("ONS15501-MIB", "ons15501ConfigOpticalGain"),
        ("ONS15501-MIB", "ons15501OpticalPowerGain"),
        ("ONS15501-MIB", "ons15501DevAmbTemp"),
        ("ONS15501-MIB", "ons15501DevAmbTempMean"),
        ("ONS15501-MIB", "ons15501DevAmbTempTrigger"),
        ("ONS15501-MIB", "ons15501LaserStatus"),
        ("ONS15501-MIB", "ons15501GainTrigger"))
)
if mibBuilder.loadTexts:
    ons15501CoreAttrGroup.setStatus("current")

ons15501PowerSupplyStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 8)
)
ons15501PowerSupplyStatusGroup.setObjects(
      *(("ONS15501-MIB", "ons15501PowerSupply1Status"),
        ("ONS15501-MIB", "ons15501PowerSupply2Status"))
)
if mibBuilder.loadTexts:
    ons15501PowerSupplyStatusGroup.setStatus("current")

ons15501PowerSupplyLevelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 9)
)
ons15501PowerSupplyLevelGroup.setObjects(
      *(("ONS15501-MIB", "ons15501PowerSupply1Level"),
        ("ONS15501-MIB", "ons15501PowerSupply2Level"))
)
if mibBuilder.loadTexts:
    ons15501PowerSupplyLevelGroup.setStatus("current")

ons15501SysInfoGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 10)
)
ons15501SysInfoGroup2.setObjects(
      *(("ONS15501-MIB", "ons15501SysDevFlash1Image"),
        ("ONS15501-MIB", "ons15501SysDevFlash2Image"),
        ("ONS15501-MIB", "ons15501SysDevFlash3Image"),
        ("ONS15501-MIB", "ons15501SysSwDownload"),
        ("ONS15501-MIB", "ons15501SysSwDownloadStatus"),
        ("ONS15501-MIB", "ons15501SysConfiguredImage"),
        ("ONS15501-MIB", "ons15501SysDevActiveImage"),
        ("ONS15501-MIB", "ons15501SysAlarmStatus"),
        ("ONS15501-MIB", "ons15501PrimaryNTP"),
        ("ONS15501-MIB", "ons15501SecondaryNTP"),
        ("ONS15501-MIB", "ons15501NTPAdminStatus"),
        ("ONS15501-MIB", "ons15501NTPOperationalStatus"),
        ("ONS15501-MIB", "ons15501CLEICode"),
        ("ONS15501-MIB", "ons15501InRemoteInfoUpdateTime"),
        ("ONS15501-MIB", "ons15501InRemoteChassisName"),
        ("ONS15501-MIB", "ons15501InRemotePortName"),
        ("ONS15501-MIB", "ons15501InRemoteAgentIpAddr"),
        ("ONS15501-MIB", "ons15501OutRemoteInfoUpdateTime"),
        ("ONS15501-MIB", "ons15501OutRemoteChassisName"),
        ("ONS15501-MIB", "ons15501OutRemotePortName"),
        ("ONS15501-MIB", "ons15501OutRemoteAgentIpAddr"),
        ("ONS15501-MIB", "ons15501LastConfigChangeTime"),
        ("ONS15501-MIB", "ons15501ActiveSoftwareVer"),
        ("ONS15501-MIB", "ons15501SysDeviceManagerList"),
        ("ONS15501-MIB", "ons15501SysDateAndTime"))
)
if mibBuilder.loadTexts:
    ons15501SysInfoGroup2.setStatus("current")


# Notification objects

ons15501GenericNotificationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 4, 0, 1)
)
ons15501GenericNotificationTrap.setObjects(
      *(("ONS15501-MIB", "ons15501LastTrapIndex"),
        ("ONS15501-MIB", "ons15501TrapLogEntryTrapType"),
        ("ONS15501-MIB", "ons15501TrapLogEntryDirection"),
        ("ONS15501-MIB", "ons15501TrapLogEntryPhyIndex"),
        ("ONS15501-MIB", "ons15501TrapLogEntrySeverity"))
)
if mibBuilder.loadTexts:
    ons15501GenericNotificationTrap.setStatus(
        "current"
    )


# Notifications groups

ons15501FinalNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 6)
)
ons15501FinalNotificationsGroup.setObjects(
    ("ONS15501-MIB", "ons15501GenericNotificationTrap")
)
if mibBuilder.loadTexts:
    ons15501FinalNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ons15501FinalCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 1, 1)
)
if mibBuilder.loadTexts:
    ons15501FinalCompliance.setStatus(
        "deprecated"
    )

ons15501Rel4Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 1, 2)
)
if mibBuilder.loadTexts:
    ons15501Rel4Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONS15501-MIB",
    **{"Ons15501ImageDnLoadStatus": Ons15501ImageDnLoadStatus,
       "Ons15501AdminStatus": Ons15501AdminStatus,
       "Ons15501NTPStatus": Ons15501NTPStatus,
       "Ons15501TenthVolt": Ons15501TenthVolt,
       "Ons15501TenthdB": Ons15501TenthdB,
       "Ons15501TenthCentigrade": Ons15501TenthCentigrade,
       "Ons15501AlarmStatus": Ons15501AlarmStatus,
       "Ons15501TrapTypeEnumeration": Ons15501TrapTypeEnumeration,
       "Ons15501TrapDirectionEnumeration": Ons15501TrapDirectionEnumeration,
       "synchronous": synchronous,
       "synEmbLx": synEmbLx,
       "ons15501MIB": ons15501MIB,
       "ons15501Sys": ons15501Sys,
       "ons15501SysDevFlash1Image": ons15501SysDevFlash1Image,
       "ons15501SysDevFlash2Image": ons15501SysDevFlash2Image,
       "ons15501SysDevFlash3Image": ons15501SysDevFlash3Image,
       "ons15501SysSwDownload": ons15501SysSwDownload,
       "ons15501SysDevActiveImage": ons15501SysDevActiveImage,
       "ons15501SysDeviceManagerList": ons15501SysDeviceManagerList,
       "ons15501SysSwDownloadStatus": ons15501SysSwDownloadStatus,
       "ons15501SysConfiguredImage": ons15501SysConfiguredImage,
       "ons15501CLEICode": ons15501CLEICode,
       "ons15501PrimaryNTP": ons15501PrimaryNTP,
       "ons15501SecondaryNTP": ons15501SecondaryNTP,
       "ons15501NTPAdminStatus": ons15501NTPAdminStatus,
       "ons15501NTPOperationalStatus": ons15501NTPOperationalStatus,
       "ons15501ActiveSoftwareVer": ons15501ActiveSoftwareVer,
       "ons15501LastConfigChangeTime": ons15501LastConfigChangeTime,
       "ons15501InRemoteInfoUpdateTime": ons15501InRemoteInfoUpdateTime,
       "ons15501InRemoteChassisName": ons15501InRemoteChassisName,
       "ons15501InRemotePortName": ons15501InRemotePortName,
       "ons15501InRemoteAgentIpAddr": ons15501InRemoteAgentIpAddr,
       "ons15501OutRemoteInfoUpdateTime": ons15501OutRemoteInfoUpdateTime,
       "ons15501OutRemoteChassisName": ons15501OutRemoteChassisName,
       "ons15501OutRemotePortName": ons15501OutRemotePortName,
       "ons15501OutRemoteAgentIpAddr": ons15501OutRemoteAgentIpAddr,
       "ons15501SysAlarmStatus": ons15501SysAlarmStatus,
       "ons15501SysDateAndTime": ons15501SysDateAndTime,
       "ons15501Attr": ons15501Attr,
       "ons15501InputOpticalPower": ons15501InputOpticalPower,
       "ons15501InputOpticalPowerMean": ons15501InputOpticalPowerMean,
       "ons15501InputOpticalPowerTrigger": ons15501InputOpticalPowerTrigger,
       "ons15501OutputOpticalPower": ons15501OutputOpticalPower,
       "ons15501OutputSignalPower": ons15501OutputSignalPower,
       "ons15501OutputSignalPowerMean": ons15501OutputSignalPowerMean,
       "ons15501OutputSignalPowerTrigger": ons15501OutputSignalPowerTrigger,
       "ons15501ConfigOpticalGain": ons15501ConfigOpticalGain,
       "ons15501OpticalPowerGain": ons15501OpticalPowerGain,
       "ons15501GainTrigger": ons15501GainTrigger,
       "ons15501PowerSupply1Level": ons15501PowerSupply1Level,
       "ons15501PowerSupply2Level": ons15501PowerSupply2Level,
       "ons15501LaserStatus": ons15501LaserStatus,
       "ons15501DevAmbTemp": ons15501DevAmbTemp,
       "ons15501DevAmbTempMean": ons15501DevAmbTempMean,
       "ons15501DevAmbTempTrigger": ons15501DevAmbTempTrigger,
       "ons15501PowerSupply1Status": ons15501PowerSupply1Status,
       "ons15501PowerSupply2Status": ons15501PowerSupply2Status,
       "ons15501Alarms": ons15501Alarms,
       "ons15501LastTrapIndex": ons15501LastTrapIndex,
       "ons15501TrapLogTable": ons15501TrapLogTable,
       "ons15501TrapLogEntry": ons15501TrapLogEntry,
       "ons15501TrapLogEntryIndex": ons15501TrapLogEntryIndex,
       "ons15501TrapLogEntryTrapType": ons15501TrapLogEntryTrapType,
       "ons15501TrapLogEntryDirection": ons15501TrapLogEntryDirection,
       "ons15501TrapLogEntryTimeStamp": ons15501TrapLogEntryTimeStamp,
       "ons15501TrapLogEntryDateAndTime": ons15501TrapLogEntryDateAndTime,
       "ons15501TrapLogEntryPhyIndex": ons15501TrapLogEntryPhyIndex,
       "ons15501TrapLogEntrySeverity": ons15501TrapLogEntrySeverity,
       "ons15501ActiveAlarmTable": ons15501ActiveAlarmTable,
       "ons15501ActiveAlarmEntry": ons15501ActiveAlarmEntry,
       "ons15501ActAlarmType": ons15501ActAlarmType,
       "ons15501ActAlarmTimeStamp": ons15501ActAlarmTimeStamp,
       "ons15501ActAlarmDateAndTime": ons15501ActAlarmDateAndTime,
       "ons15501ActAlarmPhyIndex": ons15501ActAlarmPhyIndex,
       "ons15501ActAlarmSeverity": ons15501ActAlarmSeverity,
       "ons15501TrapDescriptionTable": ons15501TrapDescriptionTable,
       "ons15501TrapDescriptionEntry": ons15501TrapDescriptionEntry,
       "ons15501TrapTypeValue": ons15501TrapTypeValue,
       "ons15501TrapDescription": ons15501TrapDescription,
       "ons15501TrapSeverity": ons15501TrapSeverity,
       "ons15501Notification": ons15501Notification,
       "ons15501NotificationPrefix": ons15501NotificationPrefix,
       "ons15501GenericNotificationTrap": ons15501GenericNotificationTrap,
       "ons15501OIDs": ons15501OIDs,
       "ons15501OIDSystem": ons15501OIDSystem,
       "ons15501OIDEntity": ons15501OIDEntity,
       "ons15501OIDChasiss": ons15501OIDChasiss,
       "ons15501OIDInPort": ons15501OIDInPort,
       "ons15501OIDOutPort": ons15501OIDOutPort,
       "ons15501OIDPowerSupply": ons15501OIDPowerSupply,
       "ons15501OIDChassisAC": ons15501OIDChassisAC,
       "ons15501OIDPowerSupplyAC": ons15501OIDPowerSupplyAC,
       "ons15501OIDSystemAC": ons15501OIDSystemAC,
       "ons15501MIBConformance": ons15501MIBConformance,
       "ons15501MIBCompliances": ons15501MIBCompliances,
       "ons15501FinalCompliance": ons15501FinalCompliance,
       "ons15501Rel4Compliance": ons15501Rel4Compliance,
       "ons15501MIBGroups": ons15501MIBGroups,
       "ons15501SysInfoGroup": ons15501SysInfoGroup,
       "ons15501TrapLogGroup": ons15501TrapLogGroup,
       "ons15501ActiveAlarmGroup": ons15501ActiveAlarmGroup,
       "ons15501TrapDescriptionGroup": ons15501TrapDescriptionGroup,
       "ons15501FinalAttrGroup": ons15501FinalAttrGroup,
       "ons15501FinalNotificationsGroup": ons15501FinalNotificationsGroup,
       "ons15501CoreAttrGroup": ons15501CoreAttrGroup,
       "ons15501PowerSupplyStatusGroup": ons15501PowerSupplyStatusGroup,
       "ons15501PowerSupplyLevelGroup": ons15501PowerSupplyLevelGroup,
       "ons15501SysInfoGroup2": ons15501SysInfoGroup2}
)
