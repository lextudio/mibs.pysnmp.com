# SNMP MIB module (LIEBERT-GP-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIEBERT-GP-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:00 2024
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

(lgpAgentConnectedDeviceCount,
 lgpAgentDeviceIndex) = mibBuilder.importSymbols(
    "LIEBERT-GP-AGENT-MIB",
    "lgpAgentConnectedDeviceCount",
    "lgpAgentDeviceIndex")

(lgpSystem,
 liebertSystemModuleReg) = mibBuilder.importSymbols(
    "LIEBERT-GP-REGISTRATION-MIB",
    "lgpSystem",
    "liebertSystemModuleReg")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

liebertSystemModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 8, 1)
)
liebertSystemModule.setRevisions(
        ("2008-11-17 00:00",
         "2008-07-02 00:00",
         "2008-01-10 00:00",
         "2007-05-29 00:00",
         "2006-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LgpSysStatistics_ObjectIdentity = ObjectIdentity
lgpSysStatistics = _LgpSysStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 1)
)
if mibBuilder.loadTexts:
    lgpSysStatistics.setStatus("current")
_LgpSysStatisticsRunHrs_Type = Unsigned32
_LgpSysStatisticsRunHrs_Object = MibScalar
lgpSysStatisticsRunHrs = _LgpSysStatisticsRunHrs_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 1, 1),
    _LgpSysStatisticsRunHrs_Type()
)
lgpSysStatisticsRunHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysStatisticsRunHrs.setStatus("current")
if mibBuilder.loadTexts:
    lgpSysStatisticsRunHrs.setUnits("hours")
_LgpSysStatus_ObjectIdentity = ObjectIdentity
lgpSysStatus = _LgpSysStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 2)
)
if mibBuilder.loadTexts:
    lgpSysStatus.setStatus("current")


class _LgpSysSelfTestResult_Type(Integer32):
    """Custom type lgpSysSelfTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("inProgress", 4),
          ("inhibited", 6),
          ("passed", 2),
          ("sysFailure", 5),
          ("unknown", 1))
    )


_LgpSysSelfTestResult_Type.__name__ = "Integer32"
_LgpSysSelfTestResult_Object = MibScalar
lgpSysSelfTestResult = _LgpSysSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 2, 1),
    _LgpSysSelfTestResult_Type()
)
lgpSysSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysSelfTestResult.setStatus("current")


class _LgpSysState_Type(Integer32):
    """Custom type lgpSysState based on Integer32"""
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
        *(("abnormalOperation", 5),
          ("normalOperation", 1),
          ("normalWithAlarm", 4),
          ("normalWithWarning", 3),
          ("startUp", 2))
    )


_LgpSysState_Type.__name__ = "Integer32"
_LgpSysState_Object = MibScalar
lgpSysState = _LgpSysState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 2, 2),
    _LgpSysState_Type()
)
lgpSysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysState.setStatus("current")
_LgpSysSettings_ObjectIdentity = ObjectIdentity
lgpSysSettings = _LgpSysSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 3)
)
if mibBuilder.loadTexts:
    lgpSysSettings.setStatus("current")


class _LgpSysAudibleAlarm_Type(Integer32):
    """Custom type lgpSysAudibleAlarm based on Integer32"""
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


_LgpSysAudibleAlarm_Type.__name__ = "Integer32"
_LgpSysAudibleAlarm_Object = MibScalar
lgpSysAudibleAlarm = _LgpSysAudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 3, 1),
    _LgpSysAudibleAlarm_Type()
)
lgpSysAudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSysAudibleAlarm.setStatus("current")
_LgpSysControl_ObjectIdentity = ObjectIdentity
lgpSysControl = _LgpSysControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 4)
)
if mibBuilder.loadTexts:
    lgpSysControl.setStatus("current")
_LgpSysSelfTest_Type = Integer32
_LgpSysSelfTest_Object = MibScalar
lgpSysSelfTest = _LgpSysSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 4, 1),
    _LgpSysSelfTest_Type()
)
lgpSysSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSysSelfTest.setStatus("current")


class _LgpSysControlOperationOnOff_Type(Integer32):
    """Custom type lgpSysControlOperationOnOff based on Integer32"""
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


_LgpSysControlOperationOnOff_Type.__name__ = "Integer32"
_LgpSysControlOperationOnOff_Object = MibScalar
lgpSysControlOperationOnOff = _LgpSysControlOperationOnOff_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 4, 2),
    _LgpSysControlOperationOnOff_Type()
)
lgpSysControlOperationOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSysControlOperationOnOff.setStatus("current")
_LgpSysTime_ObjectIdentity = ObjectIdentity
lgpSysTime = _LgpSysTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 5)
)
if mibBuilder.loadTexts:
    lgpSysTime.setStatus("current")
_LgpSysTimeEpoch_Type = Unsigned32
_LgpSysTimeEpoch_Object = MibScalar
lgpSysTimeEpoch = _LgpSysTimeEpoch_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 5, 1),
    _LgpSysTimeEpoch_Type()
)
lgpSysTimeEpoch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSysTimeEpoch.setStatus("current")
if mibBuilder.loadTexts:
    lgpSysTimeEpoch.setUnits("seconds")
_LgpSysMaintenance_ObjectIdentity = ObjectIdentity
lgpSysMaintenance = _LgpSysMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6)
)
if mibBuilder.loadTexts:
    lgpSysMaintenance.setStatus("current")
_LgpSysMaintenanceCapacity_Type = Unsigned32
_LgpSysMaintenanceCapacity_Object = MibScalar
lgpSysMaintenanceCapacity = _LgpSysMaintenanceCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6, 1),
    _LgpSysMaintenanceCapacity_Type()
)
lgpSysMaintenanceCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysMaintenanceCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpSysMaintenanceCapacity.setUnits("percent")
_LgpSysMaintenanceYear_Type = Unsigned32
_LgpSysMaintenanceYear_Object = MibScalar
lgpSysMaintenanceYear = _LgpSysMaintenanceYear_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6, 2),
    _LgpSysMaintenanceYear_Type()
)
lgpSysMaintenanceYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysMaintenanceYear.setStatus("current")
if mibBuilder.loadTexts:
    lgpSysMaintenanceYear.setUnits("year")
_LgpSysMaintenanceMonth_Type = Unsigned32
_LgpSysMaintenanceMonth_Object = MibScalar
lgpSysMaintenanceMonth = _LgpSysMaintenanceMonth_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6, 3),
    _LgpSysMaintenanceMonth_Type()
)
lgpSysMaintenanceMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysMaintenanceMonth.setStatus("current")
if mibBuilder.loadTexts:
    lgpSysMaintenanceMonth.setUnits("month")


class _LgpSysEventDescription_Type(DisplayString):
    """Custom type lgpSysEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_LgpSysEventDescription_Type.__name__ = "DisplayString"
_LgpSysEventDescription_Object = MibScalar
lgpSysEventDescription = _LgpSysEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 7),
    _LgpSysEventDescription_Type()
)
lgpSysEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysEventDescription.setStatus("current")
_LgpSysEventNotifications_ObjectIdentity = ObjectIdentity
lgpSysEventNotifications = _LgpSysEventNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 8)
)
if mibBuilder.loadTexts:
    lgpSysEventNotifications.setStatus("current")
_LgpSysDeviceComponentGroup_ObjectIdentity = ObjectIdentity
lgpSysDeviceComponentGroup = _LgpSysDeviceComponentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9)
)
if mibBuilder.loadTexts:
    lgpSysDeviceComponentGroup.setStatus("current")
_LgpSysDeviceComponentTable_Object = MibTable
lgpSysDeviceComponentTable = _LgpSysDeviceComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1)
)
if mibBuilder.loadTexts:
    lgpSysDeviceComponentTable.setStatus("current")
_LgpSysDeviceComponentEntry_Object = MibTableRow
lgpSysDeviceComponentEntry = _LgpSysDeviceComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1)
)
lgpSysDeviceComponentEntry.setIndexNames(
    (0, "LIEBERT-GP-AGENT-MIB", "lgpAgentDeviceIndex"),
    (0, "LIEBERT-GP-SYSTEM-MIB", "lgpSysDeviceComponentIndex"),
)
if mibBuilder.loadTexts:
    lgpSysDeviceComponentEntry.setStatus("current")
_LgpSysDeviceComponentIndex_Type = Unsigned32
_LgpSysDeviceComponentIndex_Object = MibTableColumn
lgpSysDeviceComponentIndex = _LgpSysDeviceComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 1),
    _LgpSysDeviceComponentIndex_Type()
)
lgpSysDeviceComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpSysDeviceComponentIndex.setStatus("current")
_LgpSysDeviceComponentDescr_Type = ObjectIdentifier
_LgpSysDeviceComponentDescr_Object = MibTableColumn
lgpSysDeviceComponentDescr = _LgpSysDeviceComponentDescr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 2),
    _LgpSysDeviceComponentDescr_Type()
)
lgpSysDeviceComponentDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysDeviceComponentDescr.setStatus("current")


class _LgpSysDeviceComponentSerialNum_Type(DisplayString):
    """Custom type lgpSysDeviceComponentSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_LgpSysDeviceComponentSerialNum_Type.__name__ = "DisplayString"
_LgpSysDeviceComponentSerialNum_Object = MibTableColumn
lgpSysDeviceComponentSerialNum = _LgpSysDeviceComponentSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 3),
    _LgpSysDeviceComponentSerialNum_Type()
)
lgpSysDeviceComponentSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysDeviceComponentSerialNum.setStatus("current")


class _LgpSysDeviceComponentModelNum_Type(DisplayString):
    """Custom type lgpSysDeviceComponentModelNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_LgpSysDeviceComponentModelNum_Type.__name__ = "DisplayString"
_LgpSysDeviceComponentModelNum_Object = MibTableColumn
lgpSysDeviceComponentModelNum = _LgpSysDeviceComponentModelNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 4),
    _LgpSysDeviceComponentModelNum_Type()
)
lgpSysDeviceComponentModelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysDeviceComponentModelNum.setStatus("current")
_LgpSysDeviceComponentWellknown_ObjectIdentity = ObjectIdentity
lgpSysDeviceComponentWellknown = _LgpSysDeviceComponentWellknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5)
)
if mibBuilder.loadTexts:
    lgpSysDeviceComponentWellknown.setStatus("current")
_LgpSysDeviceBatCabinet_ObjectIdentity = ObjectIdentity
lgpSysDeviceBatCabinet = _LgpSysDeviceBatCabinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5, 5)
)
if mibBuilder.loadTexts:
    lgpSysDeviceBatCabinet.setStatus("current")
_LgpSysDeviceParallelCabinet_ObjectIdentity = ObjectIdentity
lgpSysDeviceParallelCabinet = _LgpSysDeviceParallelCabinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5, 6)
)
if mibBuilder.loadTexts:
    lgpSysDeviceParallelCabinet.setStatus("current")
_LgpSysDeviceMaintBypass_ObjectIdentity = ObjectIdentity
lgpSysDeviceMaintBypass = _LgpSysDeviceMaintBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5, 7)
)
if mibBuilder.loadTexts:
    lgpSysDeviceMaintBypass.setStatus("current")

# Managed Objects groups


# Notification objects

lgpSysNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 8, 1)
)
lgpSysNotification.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-SYSTEM-MIB", "lgpSysEventDescription"))
)
if mibBuilder.loadTexts:
    lgpSysNotification.setStatus(
        "current"
    )

lgpSysNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 8, 2)
)
lgpSysNormal.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-AGENT-MIB", "lgpAgentConnectedDeviceCount"))
)
if mibBuilder.loadTexts:
    lgpSysNormal.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-GP-SYSTEM-MIB",
    **{"liebertSystemModule": liebertSystemModule,
       "lgpSysStatistics": lgpSysStatistics,
       "lgpSysStatisticsRunHrs": lgpSysStatisticsRunHrs,
       "lgpSysStatus": lgpSysStatus,
       "lgpSysSelfTestResult": lgpSysSelfTestResult,
       "lgpSysState": lgpSysState,
       "lgpSysSettings": lgpSysSettings,
       "lgpSysAudibleAlarm": lgpSysAudibleAlarm,
       "lgpSysControl": lgpSysControl,
       "lgpSysSelfTest": lgpSysSelfTest,
       "lgpSysControlOperationOnOff": lgpSysControlOperationOnOff,
       "lgpSysTime": lgpSysTime,
       "lgpSysTimeEpoch": lgpSysTimeEpoch,
       "lgpSysMaintenance": lgpSysMaintenance,
       "lgpSysMaintenanceCapacity": lgpSysMaintenanceCapacity,
       "lgpSysMaintenanceYear": lgpSysMaintenanceYear,
       "lgpSysMaintenanceMonth": lgpSysMaintenanceMonth,
       "lgpSysEventDescription": lgpSysEventDescription,
       "lgpSysEventNotifications": lgpSysEventNotifications,
       "lgpSysNotification": lgpSysNotification,
       "lgpSysNormal": lgpSysNormal,
       "lgpSysDeviceComponentGroup": lgpSysDeviceComponentGroup,
       "lgpSysDeviceComponentTable": lgpSysDeviceComponentTable,
       "lgpSysDeviceComponentEntry": lgpSysDeviceComponentEntry,
       "lgpSysDeviceComponentIndex": lgpSysDeviceComponentIndex,
       "lgpSysDeviceComponentDescr": lgpSysDeviceComponentDescr,
       "lgpSysDeviceComponentSerialNum": lgpSysDeviceComponentSerialNum,
       "lgpSysDeviceComponentModelNum": lgpSysDeviceComponentModelNum,
       "lgpSysDeviceComponentWellknown": lgpSysDeviceComponentWellknown,
       "lgpSysDeviceBatCabinet": lgpSysDeviceBatCabinet,
       "lgpSysDeviceParallelCabinet": lgpSysDeviceParallelCabinet,
       "lgpSysDeviceMaintBypass": lgpSysDeviceMaintBypass}
)
