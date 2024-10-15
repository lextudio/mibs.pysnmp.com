# SNMP MIB module (TIMETRA-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:04 2024
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

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tmnxChassisNotifyHwIndex,
 tmnxHwClass,
 tmnxHwID) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxChassisNotifyHwIndex",
    "tmnxHwClass",
    "tmnxHwID")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxLogExecRollbackOpIndex,) = mibBuilder.importSymbols(
    "TIMETRA-LOG-MIB",
    "tmnxLogExecRollbackOpIndex")

(IpAddressPrefixLength,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TTcpUdpPort,
 TmnxActionType,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "IpAddressPrefixLength",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TTcpUdpPort",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxOperState")


# MODULE-IDENTITY

timetraSysMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 1)
)
timetraSysMIBModule.setRevisions(
        ("1911-02-01 00:00",
         "1910-01-01 00:00",
         "1909-02-28 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-03-15 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1900-08-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxSsiSyncMode(Integer32, TextualConvention):
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
        *(("bootEnv", 3),
          ("config", 2),
          ("none", 1))
    )



class TmnxSsiSyncRollbackMode(Integer32, TextualConvention):
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
        *(("none", 1),
          ("rollbackAll", 3),
          ("rollbackSingle", 2))
    )



class TmnxSysMonSampleTime(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(300, 300),
    )



class TmnxSysMonUtilization(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxSysConformance_ObjectIdentity = ObjectIdentity
tmnxSysConformance = _TmnxSysConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1)
)
_TmnxSysCompliances_ObjectIdentity = ObjectIdentity
tmnxSysCompliances = _TmnxSysCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1)
)
_TmnxSysGroups_ObjectIdentity = ObjectIdentity
tmnxSysGroups = _TmnxSysGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2)
)
_TmnxSysObjs_ObjectIdentity = ObjectIdentity
tmnxSysObjs = _TmnxSysObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1)
)
_SysGenInfo_ObjectIdentity = ObjectIdentity
sysGenInfo = _SysGenInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1)
)


class _SgiCpuUsage_Type(Unsigned32):
    """Custom type sgiCpuUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SgiCpuUsage_Type.__name__ = "Unsigned32"
_SgiCpuUsage_Object = MibScalar
sgiCpuUsage = _SgiCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 1),
    _SgiCpuUsage_Type()
)
sgiCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiCpuUsage.setStatus("current")
if mibBuilder.loadTexts:
    sgiCpuUsage.setUnits("percent")
_SgiMemoryUsed_Type = Unsigned32
_SgiMemoryUsed_Object = MibScalar
sgiMemoryUsed = _SgiMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 2),
    _SgiMemoryUsed_Type()
)
sgiMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    sgiMemoryUsed.setUnits("bytes")
_SgiMemoryAvailable_Type = Unsigned32
_SgiMemoryAvailable_Object = MibScalar
sgiMemoryAvailable = _SgiMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 3),
    _SgiMemoryAvailable_Type()
)
sgiMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiMemoryAvailable.setStatus("current")
if mibBuilder.loadTexts:
    sgiMemoryAvailable.setUnits("bytes")
_SgiMemoryPoolAllocated_Type = Unsigned32
_SgiMemoryPoolAllocated_Object = MibScalar
sgiMemoryPoolAllocated = _SgiMemoryPoolAllocated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 4),
    _SgiMemoryPoolAllocated_Type()
)
sgiMemoryPoolAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiMemoryPoolAllocated.setStatus("current")
if mibBuilder.loadTexts:
    sgiMemoryPoolAllocated.setUnits("bytes")
_SgiSwMajorVersion_Type = Unsigned32
_SgiSwMajorVersion_Object = MibScalar
sgiSwMajorVersion = _SgiSwMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 5),
    _SgiSwMajorVersion_Type()
)
sgiSwMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiSwMajorVersion.setStatus("current")
_SgiSwMinorVersion_Type = Unsigned32
_SgiSwMinorVersion_Object = MibScalar
sgiSwMinorVersion = _SgiSwMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 6),
    _SgiSwMinorVersion_Type()
)
sgiSwMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiSwMinorVersion.setStatus("current")


class _SgiSwVersionModifier_Type(OctetString):
    """Custom type sgiSwVersionModifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SgiSwVersionModifier_Type.__name__ = "OctetString"
_SgiSwVersionModifier_Object = MibScalar
sgiSwVersionModifier = _SgiSwVersionModifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 7),
    _SgiSwVersionModifier_Type()
)
sgiSwVersionModifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiSwVersionModifier.setStatus("current")
_SgiSnmpInGetBulks_Type = Counter32
_SgiSnmpInGetBulks_Object = MibScalar
sgiSnmpInGetBulks = _SgiSnmpInGetBulks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 8),
    _SgiSnmpInGetBulks_Type()
)
sgiSnmpInGetBulks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiSnmpInGetBulks.setStatus("current")
_SgiKbMemoryUsed_Type = Unsigned32
_SgiKbMemoryUsed_Object = MibScalar
sgiKbMemoryUsed = _SgiKbMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 9),
    _SgiKbMemoryUsed_Type()
)
sgiKbMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiKbMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    sgiKbMemoryUsed.setUnits("kilobytes")
_SgiKbMemoryAvailable_Type = Unsigned32
_SgiKbMemoryAvailable_Object = MibScalar
sgiKbMemoryAvailable = _SgiKbMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 10),
    _SgiKbMemoryAvailable_Type()
)
sgiKbMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiKbMemoryAvailable.setStatus("current")
if mibBuilder.loadTexts:
    sgiKbMemoryAvailable.setUnits("kilobytes")
_SgiKbMemoryPoolAllocated_Type = Unsigned32
_SgiKbMemoryPoolAllocated_Object = MibScalar
sgiKbMemoryPoolAllocated = _SgiKbMemoryPoolAllocated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 11),
    _SgiKbMemoryPoolAllocated_Type()
)
sgiKbMemoryPoolAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiKbMemoryPoolAllocated.setStatus("current")
if mibBuilder.loadTexts:
    sgiKbMemoryPoolAllocated.setUnits("kilobytes")
_TmnxSysCpuMonTable_Object = MibTable
tmnxSysCpuMonTable = _TmnxSysCpuMonTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxSysCpuMonTable.setStatus("current")
_TmnxSysCpuMonEntry_Object = MibTableRow
tmnxSysCpuMonEntry = _TmnxSysCpuMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 12, 1)
)
tmnxSysCpuMonEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysCpuMonSampleTime"),
)
if mibBuilder.loadTexts:
    tmnxSysCpuMonEntry.setStatus("current")
_TmnxSysCpuMonSampleTime_Type = TmnxSysMonSampleTime
_TmnxSysCpuMonSampleTime_Object = MibTableColumn
tmnxSysCpuMonSampleTime = _TmnxSysCpuMonSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 12, 1, 1),
    _TmnxSysCpuMonSampleTime_Type()
)
tmnxSysCpuMonSampleTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysCpuMonSampleTime.setStatus("current")
_TmnxSysCpuMonCpuIdle_Type = TmnxSysMonUtilization
_TmnxSysCpuMonCpuIdle_Object = MibTableColumn
tmnxSysCpuMonCpuIdle = _TmnxSysCpuMonCpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 12, 1, 2),
    _TmnxSysCpuMonCpuIdle_Type()
)
tmnxSysCpuMonCpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpuMonCpuIdle.setStatus("current")
_TmnxSysCpuMonBusyCoreUtil_Type = TmnxSysMonUtilization
_TmnxSysCpuMonBusyCoreUtil_Object = MibTableColumn
tmnxSysCpuMonBusyCoreUtil = _TmnxSysCpuMonBusyCoreUtil_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 12, 1, 3),
    _TmnxSysCpuMonBusyCoreUtil_Type()
)
tmnxSysCpuMonBusyCoreUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpuMonBusyCoreUtil.setStatus("current")


class _TmnxSysCpuMonBusyGroupName_Type(OctetString):
    """Custom type tmnxSysCpuMonBusyGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxSysCpuMonBusyGroupName_Type.__name__ = "OctetString"
_TmnxSysCpuMonBusyGroupName_Object = MibTableColumn
tmnxSysCpuMonBusyGroupName = _TmnxSysCpuMonBusyGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 12, 1, 4),
    _TmnxSysCpuMonBusyGroupName_Type()
)
tmnxSysCpuMonBusyGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpuMonBusyGroupName.setStatus("current")
_TmnxSysCpuMonBusyGroupUtil_Type = TmnxSysMonUtilization
_TmnxSysCpuMonBusyGroupUtil_Object = MibTableColumn
tmnxSysCpuMonBusyGroupUtil = _TmnxSysCpuMonBusyGroupUtil_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 12, 1, 5),
    _TmnxSysCpuMonBusyGroupUtil_Type()
)
tmnxSysCpuMonBusyGroupUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpuMonBusyGroupUtil.setStatus("current")
_SysTimeInfo_ObjectIdentity = ObjectIdentity
sysTimeInfo = _SysTimeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2)
)


class _StiDateAndTime_Type(DateAndTime):
    """Custom type stiDateAndTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_StiDateAndTime_Type.__name__ = "DateAndTime"
_StiDateAndTime_Object = MibScalar
stiDateAndTime = _StiDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 1),
    _StiDateAndTime_Type()
)
stiDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stiDateAndTime.setStatus("current")


class _StiActiveZone_Type(OctetString):
    """Custom type stiActiveZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_StiActiveZone_Type.__name__ = "OctetString"
_StiActiveZone_Object = MibScalar
stiActiveZone = _StiActiveZone_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 2),
    _StiActiveZone_Type()
)
stiActiveZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stiActiveZone.setStatus("current")


class _StiHoursOffset_Type(Integer32):
    """Custom type stiHoursOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-11, 12),
    )


_StiHoursOffset_Type.__name__ = "Integer32"
_StiHoursOffset_Object = MibScalar
stiHoursOffset = _StiHoursOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 3),
    _StiHoursOffset_Type()
)
stiHoursOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stiHoursOffset.setStatus("current")
if mibBuilder.loadTexts:
    stiHoursOffset.setUnits("hours")


class _StiMinutesOffset_Type(Integer32):
    """Custom type stiMinutesOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_StiMinutesOffset_Type.__name__ = "Integer32"
_StiMinutesOffset_Object = MibScalar
stiMinutesOffset = _StiMinutesOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 4),
    _StiMinutesOffset_Type()
)
stiMinutesOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stiMinutesOffset.setStatus("current")
if mibBuilder.loadTexts:
    stiMinutesOffset.setUnits("minutes")


class _StiZoneType_Type(Integer32):
    """Custom type stiZoneType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("user", 2))
    )


_StiZoneType_Type.__name__ = "Integer32"
_StiZoneType_Object = MibScalar
stiZoneType = _StiZoneType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 5),
    _StiZoneType_Type()
)
stiZoneType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stiZoneType.setStatus("current")
_StiSummerZoneTable_Object = MibTable
stiSummerZoneTable = _StiSummerZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    stiSummerZoneTable.setStatus("current")
_StiSummerZoneEntry_Object = MibTableRow
stiSummerZoneEntry = _StiSummerZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1)
)
stiSummerZoneEntry.setIndexNames(
    (1, "TIMETRA-SYSTEM-MIB", "stiSummerZoneName"),
)
if mibBuilder.loadTexts:
    stiSummerZoneEntry.setStatus("current")


class _StiSummerZoneName_Type(OctetString):
    """Custom type stiSummerZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_StiSummerZoneName_Type.__name__ = "OctetString"
_StiSummerZoneName_Object = MibTableColumn
stiSummerZoneName = _StiSummerZoneName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 1),
    _StiSummerZoneName_Type()
)
stiSummerZoneName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stiSummerZoneName.setStatus("current")
_StiSummerZoneRowStatus_Type = RowStatus
_StiSummerZoneRowStatus_Object = MibTableColumn
stiSummerZoneRowStatus = _StiSummerZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 2),
    _StiSummerZoneRowStatus_Type()
)
stiSummerZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneRowStatus.setStatus("current")


class _StiSummerZoneStartDate_Type(DateAndTime):
    """Custom type stiSummerZoneStartDate based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_StiSummerZoneStartDate_Type.__name__ = "DateAndTime"
_StiSummerZoneStartDate_Object = MibTableColumn
stiSummerZoneStartDate = _StiSummerZoneStartDate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 3),
    _StiSummerZoneStartDate_Type()
)
stiSummerZoneStartDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneStartDate.setStatus("obsolete")


class _StiSummerZoneEndDate_Type(DateAndTime):
    """Custom type stiSummerZoneEndDate based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_StiSummerZoneEndDate_Type.__name__ = "DateAndTime"
_StiSummerZoneEndDate_Object = MibTableColumn
stiSummerZoneEndDate = _StiSummerZoneEndDate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 4),
    _StiSummerZoneEndDate_Type()
)
stiSummerZoneEndDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneEndDate.setStatus("obsolete")


class _StiSummerZoneOffset_Type(Unsigned32):
    """Custom type stiSummerZoneOffset based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_StiSummerZoneOffset_Type.__name__ = "Unsigned32"
_StiSummerZoneOffset_Object = MibTableColumn
stiSummerZoneOffset = _StiSummerZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 5),
    _StiSummerZoneOffset_Type()
)
stiSummerZoneOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneOffset.setStatus("current")
if mibBuilder.loadTexts:
    stiSummerZoneOffset.setUnits("minutes")


class _StiSummerZoneStartDay_Type(Integer32):
    """Custom type stiSummerZoneStartDay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_StiSummerZoneStartDay_Type.__name__ = "Integer32"
_StiSummerZoneStartDay_Object = MibTableColumn
stiSummerZoneStartDay = _StiSummerZoneStartDay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 6),
    _StiSummerZoneStartDay_Type()
)
stiSummerZoneStartDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneStartDay.setStatus("current")


class _StiSummerZoneStartWeek_Type(Integer32):
    """Custom type stiSummerZoneStartWeek based on Integer32"""
    defaultValue = 0

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
        *(("first", 0),
          ("fourth", 3),
          ("last", 4),
          ("second", 1),
          ("third", 2))
    )


_StiSummerZoneStartWeek_Type.__name__ = "Integer32"
_StiSummerZoneStartWeek_Object = MibTableColumn
stiSummerZoneStartWeek = _StiSummerZoneStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 7),
    _StiSummerZoneStartWeek_Type()
)
stiSummerZoneStartWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneStartWeek.setStatus("current")


class _StiSummerZoneStartMonth_Type(Integer32):
    """Custom type stiSummerZoneStartMonth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_StiSummerZoneStartMonth_Type.__name__ = "Integer32"
_StiSummerZoneStartMonth_Object = MibTableColumn
stiSummerZoneStartMonth = _StiSummerZoneStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 8),
    _StiSummerZoneStartMonth_Type()
)
stiSummerZoneStartMonth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneStartMonth.setStatus("current")


class _StiSummerZoneStartHour_Type(Unsigned32):
    """Custom type stiSummerZoneStartHour based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_StiSummerZoneStartHour_Type.__name__ = "Unsigned32"
_StiSummerZoneStartHour_Object = MibTableColumn
stiSummerZoneStartHour = _StiSummerZoneStartHour_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 9),
    _StiSummerZoneStartHour_Type()
)
stiSummerZoneStartHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneStartHour.setStatus("current")
if mibBuilder.loadTexts:
    stiSummerZoneStartHour.setUnits("hours")


class _StiSummerZoneStartMinute_Type(Unsigned32):
    """Custom type stiSummerZoneStartMinute based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_StiSummerZoneStartMinute_Type.__name__ = "Unsigned32"
_StiSummerZoneStartMinute_Object = MibTableColumn
stiSummerZoneStartMinute = _StiSummerZoneStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 10),
    _StiSummerZoneStartMinute_Type()
)
stiSummerZoneStartMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneStartMinute.setStatus("current")
if mibBuilder.loadTexts:
    stiSummerZoneStartMinute.setUnits("minutes")


class _StiSummerZoneEndDay_Type(Integer32):
    """Custom type stiSummerZoneEndDay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_StiSummerZoneEndDay_Type.__name__ = "Integer32"
_StiSummerZoneEndDay_Object = MibTableColumn
stiSummerZoneEndDay = _StiSummerZoneEndDay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 11),
    _StiSummerZoneEndDay_Type()
)
stiSummerZoneEndDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneEndDay.setStatus("current")


class _StiSummerZoneEndWeek_Type(Integer32):
    """Custom type stiSummerZoneEndWeek based on Integer32"""
    defaultValue = 0

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
        *(("first", 0),
          ("fourth", 3),
          ("last", 4),
          ("second", 1),
          ("third", 2))
    )


_StiSummerZoneEndWeek_Type.__name__ = "Integer32"
_StiSummerZoneEndWeek_Object = MibTableColumn
stiSummerZoneEndWeek = _StiSummerZoneEndWeek_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 12),
    _StiSummerZoneEndWeek_Type()
)
stiSummerZoneEndWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneEndWeek.setStatus("current")


class _StiSummerZoneEndMonth_Type(Integer32):
    """Custom type stiSummerZoneEndMonth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_StiSummerZoneEndMonth_Type.__name__ = "Integer32"
_StiSummerZoneEndMonth_Object = MibTableColumn
stiSummerZoneEndMonth = _StiSummerZoneEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 13),
    _StiSummerZoneEndMonth_Type()
)
stiSummerZoneEndMonth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneEndMonth.setStatus("current")


class _StiSummerZoneEndHour_Type(Unsigned32):
    """Custom type stiSummerZoneEndHour based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_StiSummerZoneEndHour_Type.__name__ = "Unsigned32"
_StiSummerZoneEndHour_Object = MibTableColumn
stiSummerZoneEndHour = _StiSummerZoneEndHour_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 14),
    _StiSummerZoneEndHour_Type()
)
stiSummerZoneEndHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneEndHour.setStatus("current")
if mibBuilder.loadTexts:
    stiSummerZoneEndHour.setUnits("hours")


class _StiSummerZoneEndMinute_Type(Unsigned32):
    """Custom type stiSummerZoneEndMinute based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_StiSummerZoneEndMinute_Type.__name__ = "Unsigned32"
_StiSummerZoneEndMinute_Object = MibTableColumn
stiSummerZoneEndMinute = _StiSummerZoneEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 15),
    _StiSummerZoneEndMinute_Type()
)
stiSummerZoneEndMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneEndMinute.setStatus("current")
if mibBuilder.loadTexts:
    stiSummerZoneEndMinute.setUnits("minutes")
_SysSntpInfo_ObjectIdentity = ObjectIdentity
sysSntpInfo = _SysSntpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3)
)


class _SntpState_Type(Integer32):
    """Custom type sntpState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("unicast", 1))
    )


_SntpState_Type.__name__ = "Integer32"
_SntpState_Object = MibScalar
sntpState = _SntpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 1),
    _SntpState_Type()
)
sntpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpState.setStatus("current")
_SntpServerTable_Object = MibTable
sntpServerTable = _SntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sntpServerTable.setStatus("current")
_SntpServerEntry_Object = MibTableRow
sntpServerEntry = _SntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 2, 1)
)
sntpServerEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "sntpServerAddress"),
)
if mibBuilder.loadTexts:
    sntpServerEntry.setStatus("current")
_SntpServerAddress_Type = IpAddress
_SntpServerAddress_Object = MibTableColumn
sntpServerAddress = _SntpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 2, 1, 1),
    _SntpServerAddress_Type()
)
sntpServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sntpServerAddress.setStatus("current")
_SntpServerRowStatus_Type = RowStatus
_SntpServerRowStatus_Object = MibTableColumn
sntpServerRowStatus = _SntpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 2, 1, 2),
    _SntpServerRowStatus_Type()
)
sntpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sntpServerRowStatus.setStatus("current")


class _SntpServerVersion_Type(Integer32):
    """Custom type sntpServerVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SntpServerVersion_Type.__name__ = "Integer32"
_SntpServerVersion_Object = MibTableColumn
sntpServerVersion = _SntpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 2, 1, 3),
    _SntpServerVersion_Type()
)
sntpServerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sntpServerVersion.setStatus("current")


class _SntpServerPreference_Type(Integer32):
    """Custom type sntpServerPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("preferred", 2))
    )


_SntpServerPreference_Type.__name__ = "Integer32"
_SntpServerPreference_Object = MibTableColumn
sntpServerPreference = _SntpServerPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 2, 1, 4),
    _SntpServerPreference_Type()
)
sntpServerPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sntpServerPreference.setStatus("current")


class _SntpServerInterval_Type(Unsigned32):
    """Custom type sntpServerInterval based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024),
    )


_SntpServerInterval_Type.__name__ = "Unsigned32"
_SntpServerInterval_Object = MibTableColumn
sntpServerInterval = _SntpServerInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 2, 1, 5),
    _SntpServerInterval_Type()
)
sntpServerInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sntpServerInterval.setStatus("current")
if mibBuilder.loadTexts:
    sntpServerInterval.setUnits("seconds")


class _SntpAdminState_Type(Integer32):
    """Custom type sntpAdminState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("noop", 1),
          ("outOfService", 3))
    )


_SntpAdminState_Type.__name__ = "Integer32"
_SntpAdminState_Object = MibScalar
sntpAdminState = _SntpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 3),
    _SntpAdminState_Type()
)
sntpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpAdminState.setStatus("current")
_SntpOperStatus_Type = TmnxOperState
_SntpOperStatus_Object = MibScalar
sntpOperStatus = _SntpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 4),
    _SntpOperStatus_Type()
)
sntpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpOperStatus.setStatus("current")
_SysSyncInfo_ObjectIdentity = ObjectIdentity
sysSyncInfo = _SysSyncInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4)
)


class _SsiSaveConfig_Type(TmnxActionType):
    """Custom type ssiSaveConfig based on TmnxActionType"""


_SsiSaveConfig_Object = MibScalar
ssiSaveConfig = _SsiSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 15),
    _SsiSaveConfig_Type()
)
ssiSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSaveConfig.setStatus("current")


class _SsiSyncMode_Type(TmnxSsiSyncMode):
    """Custom type ssiSyncMode based on TmnxSsiSyncMode"""


_SsiSyncMode_Object = MibScalar
ssiSyncMode = _SsiSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 16),
    _SsiSyncMode_Type()
)
ssiSyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSyncMode.setStatus("current")


class _SsiSyncForce_Type(TmnxSsiSyncMode):
    """Custom type ssiSyncForce based on TmnxSsiSyncMode"""


_SsiSyncForce_Object = MibScalar
ssiSyncForce = _SsiSyncForce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 17),
    _SsiSyncForce_Type()
)
ssiSyncForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSyncForce.setStatus("current")


class _SsiSyncStatus_Type(Integer32):
    """Custom type ssiSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bootEnv", 2),
          ("bootEnvFail", 4),
          ("bootEnvInProgress", 6),
          ("configFail", 3),
          ("configInProgress", 5),
          ("configOnly", 1),
          ("unknown", 0))
    )


_SsiSyncStatus_Type.__name__ = "Integer32"
_SsiSyncStatus_Object = MibScalar
ssiSyncStatus = _SsiSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 18),
    _SsiSyncStatus_Type()
)
ssiSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSyncStatus.setStatus("current")
_SsiSyncConfigLastTime_Type = TimeStamp
_SsiSyncConfigLastTime_Object = MibScalar
ssiSyncConfigLastTime = _SsiSyncConfigLastTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 19),
    _SsiSyncConfigLastTime_Type()
)
ssiSyncConfigLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSyncConfigLastTime.setStatus("current")
_SsiSyncBootEnvLastTime_Type = TimeStamp
_SsiSyncBootEnvLastTime_Object = MibScalar
ssiSyncBootEnvLastTime = _SsiSyncBootEnvLastTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 20),
    _SsiSyncBootEnvLastTime_Type()
)
ssiSyncBootEnvLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSyncBootEnvLastTime.setStatus("current")


class _SsiConfigMaxBackupRevisions_Type(Unsigned32):
    """Custom type ssiConfigMaxBackupRevisions based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_SsiConfigMaxBackupRevisions_Type.__name__ = "Unsigned32"
_SsiConfigMaxBackupRevisions_Object = MibScalar
ssiConfigMaxBackupRevisions = _SsiConfigMaxBackupRevisions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 21),
    _SsiConfigMaxBackupRevisions_Type()
)
ssiConfigMaxBackupRevisions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiConfigMaxBackupRevisions.setStatus("current")


class _SsiSaveConfigResult_Type(Integer32):
    """Custom type ssiSaveConfigResult based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("none", 1),
          ("success", 3))
    )


_SsiSaveConfigResult_Type.__name__ = "Integer32"
_SsiSaveConfigResult_Object = MibScalar
ssiSaveConfigResult = _SsiSaveConfigResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 22),
    _SsiSaveConfigResult_Type()
)
ssiSaveConfigResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSaveConfigResult.setStatus("current")


class _SsiSaveBof_Type(TmnxActionType):
    """Custom type ssiSaveBof based on TmnxActionType"""


_SsiSaveBof_Object = MibScalar
ssiSaveBof = _SsiSaveBof_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 23),
    _SsiSaveBof_Type()
)
ssiSaveBof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSaveBof.setStatus("current")


class _SsiSaveBofResult_Type(Integer32):
    """Custom type ssiSaveBofResult based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("none", 1),
          ("success", 3))
    )


_SsiSaveBofResult_Type.__name__ = "Integer32"
_SsiSaveBofResult_Object = MibScalar
ssiSaveBofResult = _SsiSaveBofResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 24),
    _SsiSaveBofResult_Type()
)
ssiSaveBofResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSaveBofResult.setStatus("current")


class _SsiSaveConfigDest_Type(DisplayString):
    """Custom type ssiSaveConfigDest based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_SsiSaveConfigDest_Type.__name__ = "DisplayString"
_SsiSaveConfigDest_Object = MibScalar
ssiSaveConfigDest = _SsiSaveConfigDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 25),
    _SsiSaveConfigDest_Type()
)
ssiSaveConfigDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSaveConfigDest.setStatus("current")


class _SsiSaveConfigDetail_Type(TruthValue):
    """Custom type ssiSaveConfigDetail based on TruthValue"""


_SsiSaveConfigDetail_Object = MibScalar
ssiSaveConfigDetail = _SsiSaveConfigDetail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 26),
    _SsiSaveConfigDetail_Type()
)
ssiSaveConfigDetail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSaveConfigDetail.setStatus("current")
_SsiRedFailoverTime_Type = TimeStamp
_SsiRedFailoverTime_Object = MibScalar
ssiRedFailoverTime = _SsiRedFailoverTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 27),
    _SsiRedFailoverTime_Type()
)
ssiRedFailoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiRedFailoverTime.setStatus("current")


class _SsiRedFailoverReason_Type(DisplayString):
    """Custom type ssiRedFailoverReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SsiRedFailoverReason_Type.__name__ = "DisplayString"
_SsiRedFailoverReason_Object = MibScalar
ssiRedFailoverReason = _SsiRedFailoverReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 28),
    _SsiRedFailoverReason_Type()
)
ssiRedFailoverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiRedFailoverReason.setStatus("current")
_SsiSyncRollbackLastTime_Type = TimeStamp
_SsiSyncRollbackLastTime_Object = MibScalar
ssiSyncRollbackLastTime = _SsiSyncRollbackLastTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 29),
    _SsiSyncRollbackLastTime_Type()
)
ssiSyncRollbackLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSyncRollbackLastTime.setStatus("current")


class _SsiSyncRollbackMode_Type(TmnxSsiSyncRollbackMode):
    """Custom type ssiSyncRollbackMode based on TmnxSsiSyncRollbackMode"""


_SsiSyncRollbackMode_Object = MibScalar
ssiSyncRollbackMode = _SsiSyncRollbackMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 30),
    _SsiSyncRollbackMode_Type()
)
ssiSyncRollbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSyncRollbackMode.setStatus("current")


class _SsiSyncRollbackForce_Type(TmnxSsiSyncRollbackMode):
    """Custom type ssiSyncRollbackForce based on TmnxSsiSyncRollbackMode"""


_SsiSyncRollbackForce_Object = MibScalar
ssiSyncRollbackForce = _SsiSyncRollbackForce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 31),
    _SsiSyncRollbackForce_Type()
)
ssiSyncRollbackForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSyncRollbackForce.setStatus("current")


class _SsiSyncRollbackStatus_Type(Integer32):
    """Custom type ssiSyncRollbackStatus based on Integer32"""
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
        *(("rollbackFail", 1),
          ("rollbackInProgress", 2),
          ("rollbackSuccess", 3),
          ("unknown", 0))
    )


_SsiSyncRollbackStatus_Type.__name__ = "Integer32"
_SsiSyncRollbackStatus_Object = MibScalar
ssiSyncRollbackStatus = _SsiSyncRollbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 32),
    _SsiSyncRollbackStatus_Type()
)
ssiSyncRollbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSyncRollbackStatus.setStatus("current")
_SsiSyncCertLastTime_Type = TimeStamp
_SsiSyncCertLastTime_Object = MibScalar
ssiSyncCertLastTime = _SsiSyncCertLastTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 33),
    _SsiSyncCertLastTime_Type()
)
ssiSyncCertLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSyncCertLastTime.setStatus("current")


class _SsiSyncCertMode_Type(TruthValue):
    """Custom type ssiSyncCertMode based on TruthValue"""


_SsiSyncCertMode_Object = MibScalar
ssiSyncCertMode = _SsiSyncCertMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 34),
    _SsiSyncCertMode_Type()
)
ssiSyncCertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSyncCertMode.setStatus("current")


class _SsiSyncCertForce_Type(TmnxActionType):
    """Custom type ssiSyncCertForce based on TmnxActionType"""


_SsiSyncCertForce_Object = MibScalar
ssiSyncCertForce = _SsiSyncCertForce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 35),
    _SsiSyncCertForce_Type()
)
ssiSyncCertForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSyncCertForce.setStatus("current")


class _SsiSyncCertStatus_Type(Integer32):
    """Custom type ssiSyncCertStatus based on Integer32"""
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
        *(("fail", 1),
          ("inProgress", 2),
          ("success", 3),
          ("unknown", 0))
    )


_SsiSyncCertStatus_Type.__name__ = "Integer32"
_SsiSyncCertStatus_Object = MibScalar
ssiSyncCertStatus = _SsiSyncCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 36),
    _SsiSyncCertStatus_Type()
)
ssiSyncCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSyncCertStatus.setStatus("current")
_SysBootInfo_ObjectIdentity = ObjectIdentity
sysBootInfo = _SysBootInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5)
)


class _SbiConfigStatus_Type(Integer32):
    """Custom type sbiConfigStatus based on Integer32"""
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
        *(("bootConfigFailed", 4),
          ("bootRestoreFailed", 5),
          ("configOK", 2),
          ("configRead", 1),
          ("defaultBooted", 3))
    )


_SbiConfigStatus_Type.__name__ = "Integer32"
_SbiConfigStatus_Object = MibScalar
sbiConfigStatus = _SbiConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 1),
    _SbiConfigStatus_Type()
)
sbiConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbiConfigStatus.setStatus("current")


class _SbiPersistStatus_Type(Integer32):
    """Custom type sbiPersistStatus based on Integer32"""
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
        *(("noPersistFile", 2),
          ("persistDisabled", 5),
          ("persistIndexFailure", 4),
          ("persistMismatch", 3),
          ("persistOK", 1))
    )


_SbiPersistStatus_Type.__name__ = "Integer32"
_SbiPersistStatus_Object = MibScalar
sbiPersistStatus = _SbiPersistStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 2),
    _SbiPersistStatus_Type()
)
sbiPersistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbiPersistStatus.setStatus("current")
_SbiPersistIndex_Type = TruthValue
_SbiPersistIndex_Object = MibScalar
sbiPersistIndex = _SbiPersistIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 3),
    _SbiPersistIndex_Type()
)
sbiPersistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbiPersistIndex.setStatus("current")


class _SbiSnmpdAdminStatus_Type(TmnxAdminState):
    """Custom type sbiSnmpdAdminStatus based on TmnxAdminState"""


_SbiSnmpdAdminStatus_Object = MibScalar
sbiSnmpdAdminStatus = _SbiSnmpdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 4),
    _SbiSnmpdAdminStatus_Type()
)
sbiSnmpdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSnmpdAdminStatus.setStatus("current")
_SbiSnmpdOperStatus_Type = TmnxOperState
_SbiSnmpdOperStatus_Object = MibScalar
sbiSnmpdOperStatus = _SbiSnmpdOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 5),
    _SbiSnmpdOperStatus_Type()
)
sbiSnmpdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbiSnmpdOperStatus.setStatus("current")


class _SbiSnmpdMaxPktSize_Type(Integer32):
    """Custom type sbiSnmpdMaxPktSize based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(484, 9216),
    )


_SbiSnmpdMaxPktSize_Type.__name__ = "Integer32"
_SbiSnmpdMaxPktSize_Object = MibScalar
sbiSnmpdMaxPktSize = _SbiSnmpdMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 6),
    _SbiSnmpdMaxPktSize_Type()
)
sbiSnmpdMaxPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSnmpdMaxPktSize.setStatus("current")


class _SbiSnmpdPortNum_Type(TTcpUdpPort):
    """Custom type sbiSnmpdPortNum based on TTcpUdpPort"""
    defaultValue = 161


_SbiSnmpdPortNum_Object = MibScalar
sbiSnmpdPortNum = _SbiSnmpdPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 7),
    _SbiSnmpdPortNum_Type()
)
sbiSnmpdPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSnmpdPortNum.setStatus("current")


class _SbiBootConfigOKScript_Type(DisplayString):
    """Custom type sbiBootConfigOKScript based on DisplayString"""
    defaultHexValue = ""


_SbiBootConfigOKScript_Object = MibScalar
sbiBootConfigOKScript = _SbiBootConfigOKScript_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 8),
    _SbiBootConfigOKScript_Type()
)
sbiBootConfigOKScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiBootConfigOKScript.setStatus("current")


class _SbiConfigOKScriptStatus_Type(Integer32):
    """Custom type sbiConfigOKScriptStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("notRun", 0),
          ("success", 1))
    )


_SbiConfigOKScriptStatus_Type.__name__ = "Integer32"
_SbiConfigOKScriptStatus_Object = MibScalar
sbiConfigOKScriptStatus = _SbiConfigOKScriptStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 9),
    _SbiConfigOKScriptStatus_Type()
)
sbiConfigOKScriptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbiConfigOKScriptStatus.setStatus("current")


class _SbiBootConfigFailScript_Type(DisplayString):
    """Custom type sbiBootConfigFailScript based on DisplayString"""
    defaultHexValue = ""


_SbiBootConfigFailScript_Object = MibScalar
sbiBootConfigFailScript = _SbiBootConfigFailScript_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 10),
    _SbiBootConfigFailScript_Type()
)
sbiBootConfigFailScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiBootConfigFailScript.setStatus("current")


class _SbiConfigFailScriptStatus_Type(Integer32):
    """Custom type sbiConfigFailScriptStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("notRun", 0),
          ("success", 1))
    )


_SbiConfigFailScriptStatus_Type.__name__ = "Integer32"
_SbiConfigFailScriptStatus_Object = MibScalar
sbiConfigFailScriptStatus = _SbiConfigFailScriptStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 11),
    _SbiConfigFailScriptStatus_Type()
)
sbiConfigFailScriptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbiConfigFailScriptStatus.setStatus("current")


class _SbiRedSwitchoverScript_Type(DisplayString):
    """Custom type sbiRedSwitchoverScript based on DisplayString"""
    defaultHexValue = ""


_SbiRedSwitchoverScript_Object = MibScalar
sbiRedSwitchoverScript = _SbiRedSwitchoverScript_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 12),
    _SbiRedSwitchoverScript_Type()
)
sbiRedSwitchoverScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiRedSwitchoverScript.setStatus("current")


class _SbiRedSwitchoverScriptStatus_Type(Integer32):
    """Custom type sbiRedSwitchoverScriptStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("notRun", 0),
          ("success", 1))
    )


_SbiRedSwitchoverScriptStatus_Type.__name__ = "Integer32"
_SbiRedSwitchoverScriptStatus_Object = MibScalar
sbiRedSwitchoverScriptStatus = _SbiRedSwitchoverScriptStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 13),
    _SbiRedSwitchoverScriptStatus_Type()
)
sbiRedSwitchoverScriptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbiRedSwitchoverScriptStatus.setStatus("current")
_SysRadiusInfo_ObjectIdentity = ObjectIdentity
sysRadiusInfo = _SysRadiusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6)
)


class _RadiusOperStatus_Type(Integer32):
    """Custom type radiusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_RadiusOperStatus_Type.__name__ = "Integer32"
_RadiusOperStatus_Object = MibScalar
radiusOperStatus = _RadiusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 1),
    _RadiusOperStatus_Type()
)
radiusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusOperStatus.setStatus("current")
_RadiusServerTable_Object = MibTable
radiusServerTable = _RadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    radiusServerTable.setStatus("current")
_RadiusServerEntry_Object = MibTableRow
radiusServerEntry = _RadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 2, 1)
)
radiusServerEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "radiusServerIndex"),
)
if mibBuilder.loadTexts:
    radiusServerEntry.setStatus("current")


class _RadiusServerIndex_Type(Unsigned32):
    """Custom type radiusServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RadiusServerIndex_Type.__name__ = "Unsigned32"
_RadiusServerIndex_Object = MibTableColumn
radiusServerIndex = _RadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 2, 1, 1),
    _RadiusServerIndex_Type()
)
radiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusServerIndex.setStatus("current")
_RadiusServerAddress_Type = IpAddress
_RadiusServerAddress_Object = MibTableColumn
radiusServerAddress = _RadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 2, 1, 2),
    _RadiusServerAddress_Type()
)
radiusServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerAddress.setStatus("obsolete")


class _RadiusServerOperStatus_Type(Integer32):
    """Custom type radiusServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_RadiusServerOperStatus_Type.__name__ = "Integer32"
_RadiusServerOperStatus_Object = MibTableColumn
radiusServerOperStatus = _RadiusServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 2, 1, 3),
    _RadiusServerOperStatus_Type()
)
radiusServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerOperStatus.setStatus("current")


class _RadiusServerInetAddressType_Type(InetAddressType):
    """Custom type radiusServerInetAddressType based on InetAddressType"""


_RadiusServerInetAddressType_Object = MibTableColumn
radiusServerInetAddressType = _RadiusServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 2, 1, 4),
    _RadiusServerInetAddressType_Type()
)
radiusServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerInetAddressType.setStatus("current")


class _RadiusServerInetAddress_Type(InetAddress):
    """Custom type radiusServerInetAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_RadiusServerInetAddress_Type.__name__ = "InetAddress"
_RadiusServerInetAddress_Object = MibTableColumn
radiusServerInetAddress = _RadiusServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 2, 1, 5),
    _RadiusServerInetAddress_Type()
)
radiusServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerInetAddress.setStatus("current")
_TmnxSysNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxSysNotifyObjs = _TmnxSysNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7)
)
_TmnxNotifyRow_Type = RowPointer
_TmnxNotifyRow_Object = MibScalar
tmnxNotifyRow = _TmnxNotifyRow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 1),
    _TmnxNotifyRow_Type()
)
tmnxNotifyRow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNotifyRow.setStatus("current")
_TmnxNotifyRowAdminState_Type = TmnxAdminState
_TmnxNotifyRowAdminState_Object = MibScalar
tmnxNotifyRowAdminState = _TmnxNotifyRowAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 2),
    _TmnxNotifyRowAdminState_Type()
)
tmnxNotifyRowAdminState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNotifyRowAdminState.setStatus("current")
_TmnxNotifyRowOperState_Type = TmnxOperState
_TmnxNotifyRowOperState_Object = MibScalar
tmnxNotifyRowOperState = _TmnxNotifyRowOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 3),
    _TmnxNotifyRowOperState_Type()
)
tmnxNotifyRowOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNotifyRowOperState.setStatus("current")
_TmnxMemoryModule_Type = TNamedItem
_TmnxMemoryModule_Object = MibScalar
tmnxMemoryModule = _TmnxMemoryModule_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 4),
    _TmnxMemoryModule_Type()
)
tmnxMemoryModule.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMemoryModule.setStatus("current")
_TmnxModuleMallocSize_Type = Unsigned32
_TmnxModuleMallocSize_Object = MibScalar
tmnxModuleMallocSize = _TmnxModuleMallocSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 5),
    _TmnxModuleMallocSize_Type()
)
tmnxModuleMallocSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxModuleMallocSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxModuleMallocSize.setUnits("bytes")
_TmnxDroppedTrapID_Type = ObjectIdentifier
_TmnxDroppedTrapID_Object = MibScalar
tmnxDroppedTrapID = _TmnxDroppedTrapID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 6),
    _TmnxDroppedTrapID_Type()
)
tmnxDroppedTrapID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDroppedTrapID.setStatus("current")


class _TmnxTrapDroppedReasonCode_Type(Integer32):
    """Custom type tmnxTrapDroppedReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("frequencyExceeded", 1)
    )


_TmnxTrapDroppedReasonCode_Type.__name__ = "Integer32"
_TmnxTrapDroppedReasonCode_Object = MibScalar
tmnxTrapDroppedReasonCode = _TmnxTrapDroppedReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 7),
    _TmnxTrapDroppedReasonCode_Type()
)
tmnxTrapDroppedReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTrapDroppedReasonCode.setStatus("current")
_TmnxTrapDroppedEntryID_Type = ObjectIdentifier
_TmnxTrapDroppedEntryID_Object = MibScalar
tmnxTrapDroppedEntryID = _TmnxTrapDroppedEntryID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 8),
    _TmnxTrapDroppedEntryID_Type()
)
tmnxTrapDroppedEntryID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTrapDroppedEntryID.setStatus("current")
_TmnxNotifyEntryOID_Type = ObjectIdentifier
_TmnxNotifyEntryOID_Object = MibScalar
tmnxNotifyEntryOID = _TmnxNotifyEntryOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 9),
    _TmnxNotifyEntryOID_Type()
)
tmnxNotifyEntryOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNotifyEntryOID.setStatus("current")
_TmnxSnmpdErrorMsg_Type = DisplayString
_TmnxSnmpdErrorMsg_Object = MibScalar
tmnxSnmpdErrorMsg = _TmnxSnmpdErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 10),
    _TmnxSnmpdErrorMsg_Type()
)
tmnxSnmpdErrorMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSnmpdErrorMsg.setStatus("current")
_TmnxPersistencyClient_Type = DisplayString
_TmnxPersistencyClient_Object = MibScalar
tmnxPersistencyClient = _TmnxPersistencyClient_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 11),
    _TmnxPersistencyClient_Type()
)
tmnxPersistencyClient.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPersistencyClient.setStatus("current")
_TmnxPersistencyFileLocator_Type = DisplayString
_TmnxPersistencyFileLocator_Object = MibScalar
tmnxPersistencyFileLocator = _TmnxPersistencyFileLocator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 12),
    _TmnxPersistencyFileLocator_Type()
)
tmnxPersistencyFileLocator.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPersistencyFileLocator.setStatus("current")
_TmnxPersistencyNotifyMsg_Type = DisplayString
_TmnxPersistencyNotifyMsg_Object = MibScalar
tmnxPersistencyNotifyMsg = _TmnxPersistencyNotifyMsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 13),
    _TmnxPersistencyNotifyMsg_Type()
)
tmnxPersistencyNotifyMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPersistencyNotifyMsg.setStatus("current")
_TmnxPersistenceAffectedCpm_Type = DisplayString
_TmnxPersistenceAffectedCpm_Object = MibScalar
tmnxPersistenceAffectedCpm = _TmnxPersistenceAffectedCpm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 14),
    _TmnxPersistenceAffectedCpm_Type()
)
tmnxPersistenceAffectedCpm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPersistenceAffectedCpm.setStatus("current")


class _TmnxSysTimeSetBy_Type(Integer32):
    """Custom type tmnxSysTimeSetBy based on Integer32"""
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
        *(("manually", 4),
          ("ntp", 1),
          ("rtc", 5),
          ("snmp", 3),
          ("sntp", 2))
    )


_TmnxSysTimeSetBy_Type.__name__ = "Integer32"
_TmnxSysTimeSetBy_Object = MibScalar
tmnxSysTimeSetBy = _TmnxSysTimeSetBy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 15),
    _TmnxSysTimeSetBy_Type()
)
tmnxSysTimeSetBy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysTimeSetBy.setStatus("current")
_TmnxFtpFailureMsg_Type = DisplayString
_TmnxFtpFailureMsg_Object = MibScalar
tmnxFtpFailureMsg = _TmnxFtpFailureMsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 16),
    _TmnxFtpFailureMsg_Type()
)
tmnxFtpFailureMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxFtpFailureMsg.setStatus("current")
_TmnxFtpFailureDestAddressType_Type = InetAddressType
_TmnxFtpFailureDestAddressType_Object = MibScalar
tmnxFtpFailureDestAddressType = _TmnxFtpFailureDestAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 17),
    _TmnxFtpFailureDestAddressType_Type()
)
tmnxFtpFailureDestAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxFtpFailureDestAddressType.setStatus("current")


class _TmnxFtpFailureDestAddress_Type(InetAddress):
    """Custom type tmnxFtpFailureDestAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxFtpFailureDestAddress_Type.__name__ = "InetAddress"
_TmnxFtpFailureDestAddress_Object = MibScalar
tmnxFtpFailureDestAddress = _TmnxFtpFailureDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 18),
    _TmnxFtpFailureDestAddress_Type()
)
tmnxFtpFailureDestAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxFtpFailureDestAddress.setStatus("current")
_TmnxNotifyObjectName_Type = DisplayString
_TmnxNotifyObjectName_Object = MibScalar
tmnxNotifyObjectName = _TmnxNotifyObjectName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 19),
    _TmnxNotifyObjectName_Type()
)
tmnxNotifyObjectName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNotifyObjectName.setStatus("current")
_TmnxSyncFailureReason_Type = DisplayString
_TmnxSyncFailureReason_Object = MibScalar
tmnxSyncFailureReason = _TmnxSyncFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 20),
    _TmnxSyncFailureReason_Type()
)
tmnxSyncFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSyncFailureReason.setStatus("current")
_TmnxSysExecScript_Type = DisplayString
_TmnxSysExecScript_Object = MibScalar
tmnxSysExecScript = _TmnxSysExecScript_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 21),
    _TmnxSysExecScript_Type()
)
tmnxSysExecScript.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysExecScript.setStatus("current")


class _TmnxSysExecResult_Type(Integer32):
    """Custom type tmnxSysExecResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("none", 0),
          ("success", 1))
    )


_TmnxSysExecResult_Type.__name__ = "Integer32"
_TmnxSysExecResult_Object = MibScalar
tmnxSysExecResult = _TmnxSysExecResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 22),
    _TmnxSysExecResult_Type()
)
tmnxSysExecResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysExecResult.setStatus("current")


class _TmnxSysRollbackFileType_Type(Integer32):
    """Custom type tmnxSysRollbackFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rescue", 2),
          ("rollback", 1))
    )


_TmnxSysRollbackFileType_Type.__name__ = "Integer32"
_TmnxSysRollbackFileType_Object = MibScalar
tmnxSysRollbackFileType = _TmnxSysRollbackFileType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 23),
    _TmnxSysRollbackFileType_Type()
)
tmnxSysRollbackFileType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileType.setStatus("current")


class _TmnxSysFileErrorType_Type(Integer32):
    """Custom type tmnxSysFileErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("write", 2))
    )


_TmnxSysFileErrorType_Type.__name__ = "Integer32"
_TmnxSysFileErrorType_Object = MibScalar
tmnxSysFileErrorType = _TmnxSysFileErrorType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 24),
    _TmnxSysFileErrorType_Type()
)
tmnxSysFileErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysFileErrorType.setStatus("current")
_SysLoginControlInfo_ObjectIdentity = ObjectIdentity
sysLoginControlInfo = _SysLoginControlInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8)
)


class _SlcFtpInboundMaxSessions_Type(Unsigned32):
    """Custom type slcFtpInboundMaxSessions based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SlcFtpInboundMaxSessions_Type.__name__ = "Unsigned32"
_SlcFtpInboundMaxSessions_Object = MibScalar
slcFtpInboundMaxSessions = _SlcFtpInboundMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 1),
    _SlcFtpInboundMaxSessions_Type()
)
slcFtpInboundMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcFtpInboundMaxSessions.setStatus("current")


class _SlcTelnetInboundMaxSessions_Type(Unsigned32):
    """Custom type slcTelnetInboundMaxSessions based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlcTelnetInboundMaxSessions_Type.__name__ = "Unsigned32"
_SlcTelnetInboundMaxSessions_Object = MibScalar
slcTelnetInboundMaxSessions = _SlcTelnetInboundMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 2),
    _SlcTelnetInboundMaxSessions_Type()
)
slcTelnetInboundMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcTelnetInboundMaxSessions.setStatus("current")


class _SlcTelnetOutboundMaxSessions_Type(Unsigned32):
    """Custom type slcTelnetOutboundMaxSessions based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlcTelnetOutboundMaxSessions_Type.__name__ = "Unsigned32"
_SlcTelnetOutboundMaxSessions_Object = MibScalar
slcTelnetOutboundMaxSessions = _SlcTelnetOutboundMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 3),
    _SlcTelnetOutboundMaxSessions_Type()
)
slcTelnetOutboundMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcTelnetOutboundMaxSessions.setStatus("current")


class _SlcPreLoginMessage_Type(OctetString):
    """Custom type slcPreLoginMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 900),
    )


_SlcPreLoginMessage_Type.__name__ = "OctetString"
_SlcPreLoginMessage_Object = MibScalar
slcPreLoginMessage = _SlcPreLoginMessage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 4),
    _SlcPreLoginMessage_Type()
)
slcPreLoginMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcPreLoginMessage.setStatus("current")
_SlcPreLoginMessageInclName_Type = TruthValue
_SlcPreLoginMessageInclName_Object = MibScalar
slcPreLoginMessageInclName = _SlcPreLoginMessageInclName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 5),
    _SlcPreLoginMessageInclName_Type()
)
slcPreLoginMessageInclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcPreLoginMessageInclName.setStatus("current")


class _SlcMessageOfTheDay_Type(OctetString):
    """Custom type slcMessageOfTheDay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 900),
    )


_SlcMessageOfTheDay_Type.__name__ = "OctetString"
_SlcMessageOfTheDay_Object = MibScalar
slcMessageOfTheDay = _SlcMessageOfTheDay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 6),
    _SlcMessageOfTheDay_Type()
)
slcMessageOfTheDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcMessageOfTheDay.setStatus("current")


class _SlcMessageOfTheDayType_Type(Integer32):
    """Custom type slcMessageOfTheDayType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("motd-type-none", 0),
          ("motd-type-text", 2),
          ("motd-type-url", 1))
    )


_SlcMessageOfTheDayType_Type.__name__ = "Integer32"
_SlcMessageOfTheDayType_Object = MibScalar
slcMessageOfTheDayType = _SlcMessageOfTheDayType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 7),
    _SlcMessageOfTheDayType_Type()
)
slcMessageOfTheDayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcMessageOfTheDayType.setStatus("current")


class _SlcLoginBanner_Type(TruthValue):
    """Custom type slcLoginBanner based on TruthValue"""


_SlcLoginBanner_Object = MibScalar
slcLoginBanner = _SlcLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 8),
    _SlcLoginBanner_Type()
)
slcLoginBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcLoginBanner.setStatus("current")


class _SlcLoginExponentialBackOff_Type(TruthValue):
    """Custom type slcLoginExponentialBackOff based on TruthValue"""


_SlcLoginExponentialBackOff_Object = MibScalar
slcLoginExponentialBackOff = _SlcLoginExponentialBackOff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 9),
    _SlcLoginExponentialBackOff_Type()
)
slcLoginExponentialBackOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcLoginExponentialBackOff.setStatus("current")


class _SlcTelnetGracefulShutdown_Type(TruthValue):
    """Custom type slcTelnetGracefulShutdown based on TruthValue"""


_SlcTelnetGracefulShutdown_Object = MibScalar
slcTelnetGracefulShutdown = _SlcTelnetGracefulShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 10),
    _SlcTelnetGracefulShutdown_Type()
)
slcTelnetGracefulShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcTelnetGracefulShutdown.setStatus("current")


class _SlcSSHGracefulShutdown_Type(TruthValue):
    """Custom type slcSSHGracefulShutdown based on TruthValue"""


_SlcSSHGracefulShutdown_Object = MibScalar
slcSSHGracefulShutdown = _SlcSSHGracefulShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 11),
    _SlcSSHGracefulShutdown_Type()
)
slcSSHGracefulShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcSSHGracefulShutdown.setStatus("current")


class _SlcTelnetMinTTLValue_Type(Unsigned32):
    """Custom type slcTelnetMinTTLValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_SlcTelnetMinTTLValue_Type.__name__ = "Unsigned32"
_SlcTelnetMinTTLValue_Object = MibScalar
slcTelnetMinTTLValue = _SlcTelnetMinTTLValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 12),
    _SlcTelnetMinTTLValue_Type()
)
slcTelnetMinTTLValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcTelnetMinTTLValue.setStatus("current")


class _SlcSSHMinTTLValue_Type(Unsigned32):
    """Custom type slcSSHMinTTLValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_SlcSSHMinTTLValue_Type.__name__ = "Unsigned32"
_SlcSSHMinTTLValue_Object = MibScalar
slcSSHMinTTLValue = _SlcSSHMinTTLValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 13),
    _SlcSSHMinTTLValue_Type()
)
slcSSHMinTTLValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcSSHMinTTLValue.setStatus("current")


class _SlcSSHInboundMaxSessions_Type(Unsigned32):
    """Custom type slcSSHInboundMaxSessions based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlcSSHInboundMaxSessions_Type.__name__ = "Unsigned32"
_SlcSSHInboundMaxSessions_Object = MibScalar
slcSSHInboundMaxSessions = _SlcSSHInboundMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 14),
    _SlcSSHInboundMaxSessions_Type()
)
slcSSHInboundMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcSSHInboundMaxSessions.setStatus("current")


class _SlcSSHOutboundMaxSessions_Type(Unsigned32):
    """Custom type slcSSHOutboundMaxSessions based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlcSSHOutboundMaxSessions_Type.__name__ = "Unsigned32"
_SlcSSHOutboundMaxSessions_Object = MibScalar
slcSSHOutboundMaxSessions = _SlcSSHOutboundMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 15),
    _SlcSSHOutboundMaxSessions_Type()
)
slcSSHOutboundMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcSSHOutboundMaxSessions.setStatus("current")
_SysLACPInfo_ObjectIdentity = ObjectIdentity
sysLACPInfo = _SysLACPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 9)
)


class _SysLACPSystemPriority_Type(Unsigned32):
    """Custom type sysLACPSystemPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysLACPSystemPriority_Type.__name__ = "Unsigned32"
_SysLACPSystemPriority_Object = MibScalar
sysLACPSystemPriority = _SysLACPSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 9, 1),
    _SysLACPSystemPriority_Type()
)
sysLACPSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLACPSystemPriority.setStatus("current")
_SysTacplusInfo_ObjectIdentity = ObjectIdentity
sysTacplusInfo = _SysTacplusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10)
)


class _TacplusOperStatus_Type(Integer32):
    """Custom type tacplusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_TacplusOperStatus_Type.__name__ = "Integer32"
_TacplusOperStatus_Object = MibScalar
tacplusOperStatus = _TacplusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 1),
    _TacplusOperStatus_Type()
)
tacplusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacplusOperStatus.setStatus("current")
_TacplusServerTable_Object = MibTable
tacplusServerTable = _TacplusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    tacplusServerTable.setStatus("current")
_TacplusServerEntry_Object = MibTableRow
tacplusServerEntry = _TacplusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 2, 1)
)
tacplusServerEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tacplusServerIndex"),
)
if mibBuilder.loadTexts:
    tacplusServerEntry.setStatus("current")


class _TacplusServerIndex_Type(Unsigned32):
    """Custom type tacplusServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TacplusServerIndex_Type.__name__ = "Unsigned32"
_TacplusServerIndex_Object = MibTableColumn
tacplusServerIndex = _TacplusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 2, 1, 1),
    _TacplusServerIndex_Type()
)
tacplusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacplusServerIndex.setStatus("current")
_TacplusServerAddress_Type = IpAddress
_TacplusServerAddress_Object = MibTableColumn
tacplusServerAddress = _TacplusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 2, 1, 2),
    _TacplusServerAddress_Type()
)
tacplusServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacplusServerAddress.setStatus("obsolete")


class _TacplusServerOperStatus_Type(Integer32):
    """Custom type tacplusServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_TacplusServerOperStatus_Type.__name__ = "Integer32"
_TacplusServerOperStatus_Object = MibTableColumn
tacplusServerOperStatus = _TacplusServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 2, 1, 3),
    _TacplusServerOperStatus_Type()
)
tacplusServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacplusServerOperStatus.setStatus("current")


class _TacPlusServerInetAddressType_Type(InetAddressType):
    """Custom type tacPlusServerInetAddressType based on InetAddressType"""


_TacPlusServerInetAddressType_Object = MibTableColumn
tacPlusServerInetAddressType = _TacPlusServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 2, 1, 4),
    _TacPlusServerInetAddressType_Type()
)
tacPlusServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacPlusServerInetAddressType.setStatus("current")


class _TacPlusServerInetAddress_Type(InetAddress):
    """Custom type tacPlusServerInetAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TacPlusServerInetAddress_Type.__name__ = "InetAddress"
_TacPlusServerInetAddress_Object = MibTableColumn
tacPlusServerInetAddress = _TacPlusServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 2, 1, 5),
    _TacPlusServerInetAddress_Type()
)
tacPlusServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacPlusServerInetAddress.setStatus("current")
_SysBofInfo_ObjectIdentity = ObjectIdentity
sysBofInfo = _SysBofInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11)
)


class _SbiActiveIpAddr_Type(IpAddress):
    """Custom type sbiActiveIpAddr based on IpAddress"""
    defaultValue = 0


_SbiActiveIpAddr_Object = MibScalar
sbiActiveIpAddr = _SbiActiveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 1),
    _SbiActiveIpAddr_Type()
)
sbiActiveIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiActiveIpAddr.setStatus("current")


class _SbiActiveIpMask_Type(IpAddressPrefixLength):
    """Custom type sbiActiveIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_SbiActiveIpMask_Object = MibScalar
sbiActiveIpMask = _SbiActiveIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 2),
    _SbiActiveIpMask_Type()
)
sbiActiveIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiActiveIpMask.setStatus("current")


class _SbiStandbyIpAddr_Type(IpAddress):
    """Custom type sbiStandbyIpAddr based on IpAddress"""
    defaultValue = 0


_SbiStandbyIpAddr_Object = MibScalar
sbiStandbyIpAddr = _SbiStandbyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 3),
    _SbiStandbyIpAddr_Type()
)
sbiStandbyIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyIpAddr.setStatus("current")


class _SbiStandbyIpMask_Type(IpAddressPrefixLength):
    """Custom type sbiStandbyIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_SbiStandbyIpMask_Object = MibScalar
sbiStandbyIpMask = _SbiStandbyIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 4),
    _SbiStandbyIpMask_Type()
)
sbiStandbyIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyIpMask.setStatus("current")


class _SbiPrimaryImage_Type(DisplayString):
    """Custom type sbiPrimaryImage based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_SbiPrimaryImage_Type.__name__ = "DisplayString"
_SbiPrimaryImage_Object = MibScalar
sbiPrimaryImage = _SbiPrimaryImage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 5),
    _SbiPrimaryImage_Type()
)
sbiPrimaryImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiPrimaryImage.setStatus("current")


class _SbiSecondaryImage_Type(DisplayString):
    """Custom type sbiSecondaryImage based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_SbiSecondaryImage_Type.__name__ = "DisplayString"
_SbiSecondaryImage_Object = MibScalar
sbiSecondaryImage = _SbiSecondaryImage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 6),
    _SbiSecondaryImage_Type()
)
sbiSecondaryImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSecondaryImage.setStatus("current")


class _SbiTertiaryImage_Type(DisplayString):
    """Custom type sbiTertiaryImage based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_SbiTertiaryImage_Type.__name__ = "DisplayString"
_SbiTertiaryImage_Object = MibScalar
sbiTertiaryImage = _SbiTertiaryImage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 7),
    _SbiTertiaryImage_Type()
)
sbiTertiaryImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiTertiaryImage.setStatus("current")


class _SbiPrimaryConfigFile_Type(DisplayString):
    """Custom type sbiPrimaryConfigFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_SbiPrimaryConfigFile_Type.__name__ = "DisplayString"
_SbiPrimaryConfigFile_Object = MibScalar
sbiPrimaryConfigFile = _SbiPrimaryConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 8),
    _SbiPrimaryConfigFile_Type()
)
sbiPrimaryConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiPrimaryConfigFile.setStatus("current")


class _SbiSecondaryConfigFile_Type(DisplayString):
    """Custom type sbiSecondaryConfigFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_SbiSecondaryConfigFile_Type.__name__ = "DisplayString"
_SbiSecondaryConfigFile_Object = MibScalar
sbiSecondaryConfigFile = _SbiSecondaryConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 9),
    _SbiSecondaryConfigFile_Type()
)
sbiSecondaryConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSecondaryConfigFile.setStatus("current")


class _SbiTertiaryConfigFile_Type(DisplayString):
    """Custom type sbiTertiaryConfigFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_SbiTertiaryConfigFile_Type.__name__ = "DisplayString"
_SbiTertiaryConfigFile_Object = MibScalar
sbiTertiaryConfigFile = _SbiTertiaryConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 10),
    _SbiTertiaryConfigFile_Type()
)
sbiTertiaryConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiTertiaryConfigFile.setStatus("current")


class _SbiPersist_Type(TruthValue):
    """Custom type sbiPersist based on TruthValue"""


_SbiPersist_Object = MibScalar
sbiPersist = _SbiPersist_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 11),
    _SbiPersist_Type()
)
sbiPersist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiPersist.setStatus("current")


class _SbiConsoleSpeed_Type(Unsigned32):
    """Custom type sbiConsoleSpeed based on Unsigned32"""
    defaultValue = 115200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 9600),
        ValueRangeConstraint(19200, 19200),
        ValueRangeConstraint(38400, 38400),
        ValueRangeConstraint(57600, 57600),
        ValueRangeConstraint(115200, 115200),
    )


_SbiConsoleSpeed_Type.__name__ = "Unsigned32"
_SbiConsoleSpeed_Object = MibScalar
sbiConsoleSpeed = _SbiConsoleSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 12),
    _SbiConsoleSpeed_Type()
)
sbiConsoleSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiConsoleSpeed.setStatus("current")
if mibBuilder.loadTexts:
    sbiConsoleSpeed.setUnits("bps")


class _SbiAutoNegotiate_Type(TruthValue):
    """Custom type sbiAutoNegotiate based on TruthValue"""


_SbiAutoNegotiate_Object = MibScalar
sbiAutoNegotiate = _SbiAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 13),
    _SbiAutoNegotiate_Type()
)
sbiAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoNegotiate.setStatus("current")


class _SbiSpeed_Type(Unsigned32):
    """Custom type sbiSpeed based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
    )


_SbiSpeed_Type.__name__ = "Unsigned32"
_SbiSpeed_Object = MibScalar
sbiSpeed = _SbiSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 14),
    _SbiSpeed_Type()
)
sbiSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSpeed.setStatus("current")
if mibBuilder.loadTexts:
    sbiSpeed.setUnits("Mbps")


class _SbiDuplex_Type(Integer32):
    """Custom type sbiDuplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_SbiDuplex_Type.__name__ = "Integer32"
_SbiDuplex_Object = MibScalar
sbiDuplex = _SbiDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 15),
    _SbiDuplex_Type()
)
sbiDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiDuplex.setStatus("current")


class _SbiPrimaryDns_Type(IpAddress):
    """Custom type sbiPrimaryDns based on IpAddress"""
    defaultValue = 0


_SbiPrimaryDns_Object = MibScalar
sbiPrimaryDns = _SbiPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 16),
    _SbiPrimaryDns_Type()
)
sbiPrimaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiPrimaryDns.setStatus("current")


class _SbiSecondaryDns_Type(IpAddress):
    """Custom type sbiSecondaryDns based on IpAddress"""
    defaultValue = 0


_SbiSecondaryDns_Object = MibScalar
sbiSecondaryDns = _SbiSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 17),
    _SbiSecondaryDns_Type()
)
sbiSecondaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSecondaryDns.setStatus("current")


class _SbiTertiaryDns_Type(IpAddress):
    """Custom type sbiTertiaryDns based on IpAddress"""
    defaultValue = 0


_SbiTertiaryDns_Object = MibScalar
sbiTertiaryDns = _SbiTertiaryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 18),
    _SbiTertiaryDns_Type()
)
sbiTertiaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiTertiaryDns.setStatus("current")


class _SbiDnsDomain_Type(DisplayString):
    """Custom type sbiDnsDomain based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 178),
    )


_SbiDnsDomain_Type.__name__ = "DisplayString"
_SbiDnsDomain_Object = MibScalar
sbiDnsDomain = _SbiDnsDomain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 19),
    _SbiDnsDomain_Type()
)
sbiDnsDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiDnsDomain.setStatus("current")


class _SbiWait_Type(Unsigned32):
    """Custom type sbiWait based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SbiWait_Type.__name__ = "Unsigned32"
_SbiWait_Object = MibScalar
sbiWait = _SbiWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 20),
    _SbiWait_Type()
)
sbiWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiWait.setStatus("current")
if mibBuilder.loadTexts:
    sbiWait.setUnits("seconds")
_SbiStaticRouteTable_Object = MibTable
sbiStaticRouteTable = _SbiStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 21)
)
if mibBuilder.loadTexts:
    sbiStaticRouteTable.setStatus("current")
_SbiStaticRouteEntry_Object = MibTableRow
sbiStaticRouteEntry = _SbiStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 21, 1)
)
sbiStaticRouteEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "sbiStaticRouteDest"),
    (0, "TIMETRA-SYSTEM-MIB", "sbiStaticRouteMask"),
)
if mibBuilder.loadTexts:
    sbiStaticRouteEntry.setStatus("current")
_SbiStaticRouteDest_Type = IpAddress
_SbiStaticRouteDest_Object = MibTableColumn
sbiStaticRouteDest = _SbiStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 21, 1, 1),
    _SbiStaticRouteDest_Type()
)
sbiStaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbiStaticRouteDest.setStatus("current")
_SbiStaticRouteMask_Type = IpAddressPrefixLength
_SbiStaticRouteMask_Object = MibTableColumn
sbiStaticRouteMask = _SbiStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 21, 1, 2),
    _SbiStaticRouteMask_Type()
)
sbiStaticRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbiStaticRouteMask.setStatus("current")
_SbiStaticRouteNextHop_Type = IpAddress
_SbiStaticRouteNextHop_Object = MibTableColumn
sbiStaticRouteNextHop = _SbiStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 21, 1, 3),
    _SbiStaticRouteNextHop_Type()
)
sbiStaticRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbiStaticRouteNextHop.setStatus("current")
_SbiStaticRouteRowStatus_Type = RowStatus
_SbiStaticRouteRowStatus_Object = MibTableColumn
sbiStaticRouteRowStatus = _SbiStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 21, 1, 4),
    _SbiStaticRouteRowStatus_Type()
)
sbiStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbiStaticRouteRowStatus.setStatus("current")


class _SbiActiveIPv6Addr_Type(InetAddressIPv6):
    """Custom type sbiActiveIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_SbiActiveIPv6Addr_Object = MibScalar
sbiActiveIPv6Addr = _SbiActiveIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 22),
    _SbiActiveIPv6Addr_Type()
)
sbiActiveIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiActiveIPv6Addr.setStatus("current")


class _SbiActiveIPv6PfxLen_Type(InetAddressPrefixLength):
    """Custom type sbiActiveIPv6PfxLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SbiActiveIPv6PfxLen_Type.__name__ = "InetAddressPrefixLength"
_SbiActiveIPv6PfxLen_Object = MibScalar
sbiActiveIPv6PfxLen = _SbiActiveIPv6PfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 23),
    _SbiActiveIPv6PfxLen_Type()
)
sbiActiveIPv6PfxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiActiveIPv6PfxLen.setStatus("current")


class _SbiStandbyIPv6Addr_Type(InetAddressIPv6):
    """Custom type sbiStandbyIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_SbiStandbyIPv6Addr_Object = MibScalar
sbiStandbyIPv6Addr = _SbiStandbyIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 24),
    _SbiStandbyIPv6Addr_Type()
)
sbiStandbyIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyIPv6Addr.setStatus("current")


class _SbiStandbyIPv6PfxLen_Type(InetAddressPrefixLength):
    """Custom type sbiStandbyIPv6PfxLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SbiStandbyIPv6PfxLen_Type.__name__ = "InetAddressPrefixLength"
_SbiStandbyIPv6PfxLen_Object = MibScalar
sbiStandbyIPv6PfxLen = _SbiStandbyIPv6PfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 25),
    _SbiStandbyIPv6PfxLen_Type()
)
sbiStandbyIPv6PfxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyIPv6PfxLen.setStatus("current")


class _SbiPrimaryDnsIPv6Addr_Type(InetAddressIPv6):
    """Custom type sbiPrimaryDnsIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_SbiPrimaryDnsIPv6Addr_Object = MibScalar
sbiPrimaryDnsIPv6Addr = _SbiPrimaryDnsIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 26),
    _SbiPrimaryDnsIPv6Addr_Type()
)
sbiPrimaryDnsIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiPrimaryDnsIPv6Addr.setStatus("current")


class _SbiSecondaryDnsIPv6Addr_Type(InetAddressIPv6):
    """Custom type sbiSecondaryDnsIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_SbiSecondaryDnsIPv6Addr_Object = MibScalar
sbiSecondaryDnsIPv6Addr = _SbiSecondaryDnsIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 27),
    _SbiSecondaryDnsIPv6Addr_Type()
)
sbiSecondaryDnsIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSecondaryDnsIPv6Addr.setStatus("current")


class _SbiTertiaryDnsIPv6Addr_Type(InetAddressIPv6):
    """Custom type sbiTertiaryDnsIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_SbiTertiaryDnsIPv6Addr_Object = MibScalar
sbiTertiaryDnsIPv6Addr = _SbiTertiaryDnsIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 28),
    _SbiTertiaryDnsIPv6Addr_Type()
)
sbiTertiaryDnsIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiTertiaryDnsIPv6Addr.setStatus("current")
_SbiStaticRouteIPv6Table_Object = MibTable
sbiStaticRouteIPv6Table = _SbiStaticRouteIPv6Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 29)
)
if mibBuilder.loadTexts:
    sbiStaticRouteIPv6Table.setStatus("current")
_SbiStaticRouteIPv6Entry_Object = MibTableRow
sbiStaticRouteIPv6Entry = _SbiStaticRouteIPv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 29, 1)
)
sbiStaticRouteIPv6Entry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "sbiStaticRouteIPv6Dest"),
    (0, "TIMETRA-SYSTEM-MIB", "sbiStaticRouteIPv6PfxLen"),
)
if mibBuilder.loadTexts:
    sbiStaticRouteIPv6Entry.setStatus("current")
_SbiStaticRouteIPv6Dest_Type = InetAddressIPv6
_SbiStaticRouteIPv6Dest_Object = MibTableColumn
sbiStaticRouteIPv6Dest = _SbiStaticRouteIPv6Dest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 29, 1, 1),
    _SbiStaticRouteIPv6Dest_Type()
)
sbiStaticRouteIPv6Dest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbiStaticRouteIPv6Dest.setStatus("current")


class _SbiStaticRouteIPv6PfxLen_Type(InetAddressPrefixLength):
    """Custom type sbiStaticRouteIPv6PfxLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SbiStaticRouteIPv6PfxLen_Type.__name__ = "InetAddressPrefixLength"
_SbiStaticRouteIPv6PfxLen_Object = MibTableColumn
sbiStaticRouteIPv6PfxLen = _SbiStaticRouteIPv6PfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 29, 1, 2),
    _SbiStaticRouteIPv6PfxLen_Type()
)
sbiStaticRouteIPv6PfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbiStaticRouteIPv6PfxLen.setStatus("current")
_SbiStaticRouteIPv6NextHop_Type = InetAddressIPv6
_SbiStaticRouteIPv6NextHop_Object = MibTableColumn
sbiStaticRouteIPv6NextHop = _SbiStaticRouteIPv6NextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 29, 1, 3),
    _SbiStaticRouteIPv6NextHop_Type()
)
sbiStaticRouteIPv6NextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbiStaticRouteIPv6NextHop.setStatus("current")
_SbiStaticRouteIPv6RowStatus_Type = RowStatus
_SbiStaticRouteIPv6RowStatus_Object = MibTableColumn
sbiStaticRouteIPv6RowStatus = _SbiStaticRouteIPv6RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 29, 1, 4),
    _SbiStaticRouteIPv6RowStatus_Type()
)
sbiStaticRouteIPv6RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbiStaticRouteIPv6RowStatus.setStatus("current")


class _SbiLiSeparate_Type(TruthValue):
    """Custom type sbiLiSeparate based on TruthValue"""


_SbiLiSeparate_Object = MibScalar
sbiLiSeparate = _SbiLiSeparate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 30),
    _SbiLiSeparate_Type()
)
sbiLiSeparate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiLiSeparate.setStatus("current")


class _SbiLiLocalSave_Type(TruthValue):
    """Custom type sbiLiLocalSave based on TruthValue"""


_SbiLiLocalSave_Object = MibScalar
sbiLiLocalSave = _SbiLiLocalSave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 31),
    _SbiLiLocalSave_Type()
)
sbiLiLocalSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiLiLocalSave.setStatus("current")
_SysPersistenceInfo_ObjectIdentity = ObjectIdentity
sysPersistenceInfo = _SysPersistenceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12)
)
_SysPersistenceDhcpL2Info_ObjectIdentity = ObjectIdentity
sysPersistenceDhcpL2Info = _SysPersistenceDhcpL2Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 1)
)


class _SpiDhcpL2PersistenceFileLocation_Type(Unsigned32):
    """Custom type spiDhcpL2PersistenceFileLocation based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SpiDhcpL2PersistenceFileLocation_Type.__name__ = "Unsigned32"
_SpiDhcpL2PersistenceFileLocation_Object = MibScalar
spiDhcpL2PersistenceFileLocation = _SpiDhcpL2PersistenceFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 1, 1),
    _SpiDhcpL2PersistenceFileLocation_Type()
)
spiDhcpL2PersistenceFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiDhcpL2PersistenceFileLocation.setStatus("obsolete")
_SpiDhcpL2PersistenceDescription_Type = TItemDescription
_SpiDhcpL2PersistenceDescription_Object = MibScalar
spiDhcpL2PersistenceDescription = _SpiDhcpL2PersistenceDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 1, 2),
    _SpiDhcpL2PersistenceDescription_Type()
)
spiDhcpL2PersistenceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiDhcpL2PersistenceDescription.setStatus("obsolete")
_SysPersistenceDhcpL3Info_ObjectIdentity = ObjectIdentity
sysPersistenceDhcpL3Info = _SysPersistenceDhcpL3Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 2)
)


class _SpiDhcpL3PersistenceFileLocation_Type(Unsigned32):
    """Custom type spiDhcpL3PersistenceFileLocation based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SpiDhcpL3PersistenceFileLocation_Type.__name__ = "Unsigned32"
_SpiDhcpL3PersistenceFileLocation_Object = MibScalar
spiDhcpL3PersistenceFileLocation = _SpiDhcpL3PersistenceFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 2, 1),
    _SpiDhcpL3PersistenceFileLocation_Type()
)
spiDhcpL3PersistenceFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiDhcpL3PersistenceFileLocation.setStatus("obsolete")
_SpiDhcpL3PersistenceDescription_Type = TItemDescription
_SpiDhcpL3PersistenceDescription_Object = MibScalar
spiDhcpL3PersistenceDescription = _SpiDhcpL3PersistenceDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 2, 2),
    _SpiDhcpL3PersistenceDescription_Type()
)
spiDhcpL3PersistenceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiDhcpL3PersistenceDescription.setStatus("obsolete")
_SysPersistenceSubMgmtInfo_ObjectIdentity = ObjectIdentity
sysPersistenceSubMgmtInfo = _SysPersistenceSubMgmtInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 3)
)


class _SpiSubMgmtPersistenceFileLocation_Type(Unsigned32):
    """Custom type spiSubMgmtPersistenceFileLocation based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SpiSubMgmtPersistenceFileLocation_Type.__name__ = "Unsigned32"
_SpiSubMgmtPersistenceFileLocation_Object = MibScalar
spiSubMgmtPersistenceFileLocation = _SpiSubMgmtPersistenceFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 3, 1),
    _SpiSubMgmtPersistenceFileLocation_Type()
)
spiSubMgmtPersistenceFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiSubMgmtPersistenceFileLocation.setStatus("current")
_SpiSubMgmtPersistenceDescription_Type = TItemDescription
_SpiSubMgmtPersistenceDescription_Object = MibScalar
spiSubMgmtPersistenceDescription = _SpiSubMgmtPersistenceDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 3, 2),
    _SpiSubMgmtPersistenceDescription_Type()
)
spiSubMgmtPersistenceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiSubMgmtPersistenceDescription.setStatus("current")
_SysPersistenceDhcpSrvInfo_ObjectIdentity = ObjectIdentity
sysPersistenceDhcpSrvInfo = _SysPersistenceDhcpSrvInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 4)
)


class _SpiDhcpSrvPersistenceFileLoc_Type(Unsigned32):
    """Custom type spiDhcpSrvPersistenceFileLoc based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SpiDhcpSrvPersistenceFileLoc_Type.__name__ = "Unsigned32"
_SpiDhcpSrvPersistenceFileLoc_Object = MibScalar
spiDhcpSrvPersistenceFileLoc = _SpiDhcpSrvPersistenceFileLoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 4, 1),
    _SpiDhcpSrvPersistenceFileLoc_Type()
)
spiDhcpSrvPersistenceFileLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiDhcpSrvPersistenceFileLoc.setStatus("current")
_SpiDhcpSrvPersistenceDescr_Type = TItemDescription
_SpiDhcpSrvPersistenceDescr_Object = MibScalar
spiDhcpSrvPersistenceDescr = _SpiDhcpSrvPersistenceDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 4, 2),
    _SpiDhcpSrvPersistenceDescr_Type()
)
spiDhcpSrvPersistenceDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiDhcpSrvPersistenceDescr.setStatus("current")
_SysPersistenceNatInfo_ObjectIdentity = ObjectIdentity
sysPersistenceNatInfo = _SysPersistenceNatInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 5)
)


class _SpiNatFwdPersistenceFileLoc_Type(Unsigned32):
    """Custom type spiNatFwdPersistenceFileLoc based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SpiNatFwdPersistenceFileLoc_Type.__name__ = "Unsigned32"
_SpiNatFwdPersistenceFileLoc_Object = MibScalar
spiNatFwdPersistenceFileLoc = _SpiNatFwdPersistenceFileLoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 5, 1),
    _SpiNatFwdPersistenceFileLoc_Type()
)
spiNatFwdPersistenceFileLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiNatFwdPersistenceFileLoc.setStatus("current")
_SpiNatFwdPersistenceDescr_Type = TItemDescription
_SpiNatFwdPersistenceDescr_Object = MibScalar
spiNatFwdPersistenceDescr = _SpiNatFwdPersistenceDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 5, 2),
    _SpiNatFwdPersistenceDescr_Type()
)
spiNatFwdPersistenceDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiNatFwdPersistenceDescr.setStatus("current")
_SysPersistenceAAInfo_ObjectIdentity = ObjectIdentity
sysPersistenceAAInfo = _SysPersistenceAAInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 6)
)


class _SpiAAPersistenceFileLoc_Type(Unsigned32):
    """Custom type spiAAPersistenceFileLoc based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SpiAAPersistenceFileLoc_Type.__name__ = "Unsigned32"
_SpiAAPersistenceFileLoc_Object = MibScalar
spiAAPersistenceFileLoc = _SpiAAPersistenceFileLoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 6, 1),
    _SpiAAPersistenceFileLoc_Type()
)
spiAAPersistenceFileLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiAAPersistenceFileLoc.setStatus("current")
_SpiAAPersistenceDescr_Type = TItemDescription
_SpiAAPersistenceDescr_Object = MibScalar
spiAAPersistenceDescr = _SpiAAPersistenceDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 6, 2),
    _SpiAAPersistenceDescr_Type()
)
spiAAPersistenceDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiAAPersistenceDescr.setStatus("current")
_SysLiInfo_ObjectIdentity = ObjectIdentity
sysLiInfo = _SysLiInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 13)
)


class _SliConfigStatus_Type(Integer32):
    """Custom type sliConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("notRun", 0),
          ("success", 1))
    )


_SliConfigStatus_Type.__name__ = "Integer32"
_SliConfigStatus_Object = MibScalar
sliConfigStatus = _SliConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 13, 1),
    _SliConfigStatus_Type()
)
sliConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliConfigStatus.setStatus("current")


class _SliSaveConfig_Type(TmnxActionType):
    """Custom type sliSaveConfig based on TmnxActionType"""


_SliSaveConfig_Object = MibScalar
sliSaveConfig = _SliSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 13, 2),
    _SliSaveConfig_Type()
)
sliSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sliSaveConfig.setStatus("current")


class _SliSaveConfigResult_Type(Integer32):
    """Custom type sliSaveConfigResult based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("none", 1),
          ("success", 3))
    )


_SliSaveConfigResult_Type.__name__ = "Integer32"
_SliSaveConfigResult_Object = MibScalar
sliSaveConfigResult = _SliSaveConfigResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 13, 3),
    _SliSaveConfigResult_Type()
)
sliSaveConfigResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliSaveConfigResult.setStatus("current")
_SliConfigLastModified_Type = DateAndTime
_SliConfigLastModified_Object = MibScalar
sliConfigLastModified = _SliConfigLastModified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 13, 4),
    _SliConfigLastModified_Type()
)
sliConfigLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliConfigLastModified.setStatus("current")
_SliConfigLastSaved_Type = DateAndTime
_SliConfigLastSaved_Object = MibScalar
sliConfigLastSaved = _SliConfigLastSaved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 13, 5),
    _SliConfigLastSaved_Type()
)
sliConfigLastSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliConfigLastSaved.setStatus("current")


class _SliFilterLock_Type(Integer32):
    """Custom type sliFilterLock based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlockedForAll", 2),
          ("unlockedForLiUsers", 1))
    )


_SliFilterLock_Type.__name__ = "Integer32"
_SliFilterLock_Object = MibScalar
sliFilterLock = _SliFilterLock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 13, 6),
    _SliFilterLock_Type()
)
sliFilterLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sliFilterLock.setStatus("current")
_SysDNSInfo_ObjectIdentity = ObjectIdentity
sysDNSInfo = _SysDNSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 14)
)
_SysDNSInfoLastChanged_Type = TimeStamp
_SysDNSInfoLastChanged_Object = MibScalar
sysDNSInfoLastChanged = _SysDNSInfoLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 14, 1),
    _SysDNSInfoLastChanged_Type()
)
sysDNSInfoLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDNSInfoLastChanged.setStatus("current")


class _SysDNSAddressResolvePref_Type(Integer32):
    """Custom type sysDNSAddressResolvePref based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Only", 1),
          ("ipv6First", 2))
    )


_SysDNSAddressResolvePref_Type.__name__ = "Integer32"
_SysDNSAddressResolvePref_Object = MibScalar
sysDNSAddressResolvePref = _SysDNSAddressResolvePref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 14, 2),
    _SysDNSAddressResolvePref_Type()
)
sysDNSAddressResolvePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDNSAddressResolvePref.setStatus("current")
_SysIcmpVSInfo_ObjectIdentity = ObjectIdentity
sysIcmpVSInfo = _SysIcmpVSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 15)
)


class _SysIcmpVSEnhancement_Type(TmnxEnabledDisabled):
    """Custom type sysIcmpVSEnhancement based on TmnxEnabledDisabled"""


_SysIcmpVSEnhancement_Object = MibScalar
sysIcmpVSEnhancement = _SysIcmpVSEnhancement_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 15, 1),
    _SysIcmpVSEnhancement_Type()
)
sysIcmpVSEnhancement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIcmpVSEnhancement.setStatus("current")
_SysEthInfo_ObjectIdentity = ObjectIdentity
sysEthInfo = _SysEthInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 16)
)


class _SysNewQinqUntaggedSap_Type(TruthValue):
    """Custom type sysNewQinqUntaggedSap based on TruthValue"""


_SysNewQinqUntaggedSap_Object = MibScalar
sysNewQinqUntaggedSap = _SysNewQinqUntaggedSap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 16, 1),
    _SysNewQinqUntaggedSap_Type()
)
sysNewQinqUntaggedSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNewQinqUntaggedSap.setStatus("current")
_TmnxSysRollbackInfo_ObjectIdentity = ObjectIdentity
tmnxSysRollbackInfo = _TmnxSysRollbackInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17)
)


class _TmnxSysRollbackIndex_Type(Unsigned32):
    """Custom type tmnxSysRollbackIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_TmnxSysRollbackIndex_Type.__name__ = "Unsigned32"
_TmnxSysRollbackIndex_Object = MibScalar
tmnxSysRollbackIndex = _TmnxSysRollbackIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 1),
    _TmnxSysRollbackIndex_Type()
)
tmnxSysRollbackIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackIndex.setStatus("current")


class _TmnxSysRollbackStart_Type(TmnxActionType):
    """Custom type tmnxSysRollbackStart based on TmnxActionType"""


_TmnxSysRollbackStart_Object = MibScalar
tmnxSysRollbackStart = _TmnxSysRollbackStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 2),
    _TmnxSysRollbackStart_Type()
)
tmnxSysRollbackStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackStart.setStatus("current")


class _TmnxSysRollbackResult_Type(Integer32):
    """Custom type tmnxSysRollbackResult based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("interrupted", 5),
          ("none", 1),
          ("success", 3))
    )


_TmnxSysRollbackResult_Type.__name__ = "Integer32"
_TmnxSysRollbackResult_Object = MibScalar
tmnxSysRollbackResult = _TmnxSysRollbackResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 3),
    _TmnxSysRollbackResult_Type()
)
tmnxSysRollbackResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackResult.setStatus("current")


class _TmnxSysRollbackSave_Type(TmnxActionType):
    """Custom type tmnxSysRollbackSave based on TmnxActionType"""


_TmnxSysRollbackSave_Object = MibScalar
tmnxSysRollbackSave = _TmnxSysRollbackSave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 4),
    _TmnxSysRollbackSave_Type()
)
tmnxSysRollbackSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackSave.setStatus("current")


class _TmnxSysRollbackSaveResult_Type(Integer32):
    """Custom type tmnxSysRollbackSaveResult based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("none", 1),
          ("success", 3))
    )


_TmnxSysRollbackSaveResult_Type.__name__ = "Integer32"
_TmnxSysRollbackSaveResult_Object = MibScalar
tmnxSysRollbackSaveResult = _TmnxSysRollbackSaveResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 5),
    _TmnxSysRollbackSaveResult_Type()
)
tmnxSysRollbackSaveResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackSaveResult.setStatus("current")


class _TmnxSysRollbackLocation_Type(DisplayString):
    """Custom type tmnxSysRollbackLocation based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxSysRollbackLocation_Type.__name__ = "DisplayString"
_TmnxSysRollbackLocation_Object = MibScalar
tmnxSysRollbackLocation = _TmnxSysRollbackLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 6),
    _TmnxSysRollbackLocation_Type()
)
tmnxSysRollbackLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackLocation.setStatus("current")


class _TmnxSysRollbackRevertIndex_Type(Unsigned32):
    """Custom type tmnxSysRollbackRevertIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_TmnxSysRollbackRevertIndex_Type.__name__ = "Unsigned32"
_TmnxSysRollbackRevertIndex_Object = MibScalar
tmnxSysRollbackRevertIndex = _TmnxSysRollbackRevertIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 7),
    _TmnxSysRollbackRevertIndex_Type()
)
tmnxSysRollbackRevertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRevertIndex.setStatus("current")
_TmnxSysRollbackRevertEndTime_Type = DateAndTime
_TmnxSysRollbackRevertEndTime_Object = MibScalar
tmnxSysRollbackRevertEndTime = _TmnxSysRollbackRevertEndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 8),
    _TmnxSysRollbackRevertEndTime_Type()
)
tmnxSysRollbackRevertEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRevertEndTime.setStatus("current")
_TmnxSysRollbackSavedTime_Type = DateAndTime
_TmnxSysRollbackSavedTime_Object = MibScalar
tmnxSysRollbackSavedTime = _TmnxSysRollbackSavedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 9),
    _TmnxSysRollbackSavedTime_Type()
)
tmnxSysRollbackSavedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackSavedTime.setStatus("current")
_TmnxSysRollbackRevertStartTime_Type = DateAndTime
_TmnxSysRollbackRevertStartTime_Object = MibScalar
tmnxSysRollbackRevertStartTime = _TmnxSysRollbackRevertStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 10),
    _TmnxSysRollbackRevertStartTime_Type()
)
tmnxSysRollbackRevertStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRevertStartTime.setStatus("current")


class _TmnxSysRollbackRevertUserName_Type(TNamedItemOrEmpty):
    """Custom type tmnxSysRollbackRevertUserName based on TNamedItemOrEmpty"""
    defaultHexValue = ""

    subtypeSpec = TNamedItemOrEmpty.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxSysRollbackRevertUserName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxSysRollbackRevertUserName_Object = MibScalar
tmnxSysRollbackRevertUserName = _TmnxSysRollbackRevertUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 11),
    _TmnxSysRollbackRevertUserName_Type()
)
tmnxSysRollbackRevertUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRevertUserName.setStatus("current")


class _TmnxSysRollbackRevertFilename_Type(DisplayString):
    """Custom type tmnxSysRollbackRevertFilename based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxSysRollbackRevertFilename_Type.__name__ = "DisplayString"
_TmnxSysRollbackRevertFilename_Object = MibScalar
tmnxSysRollbackRevertFilename = _TmnxSysRollbackRevertFilename_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 12),
    _TmnxSysRollbackRevertFilename_Type()
)
tmnxSysRollbackRevertFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRevertFilename.setStatus("current")


class _TmnxSysRollbackSaveComment_Type(DisplayString):
    """Custom type tmnxSysRollbackSaveComment based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxSysRollbackSaveComment_Type.__name__ = "DisplayString"
_TmnxSysRollbackSaveComment_Object = MibScalar
tmnxSysRollbackSaveComment = _TmnxSysRollbackSaveComment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 13),
    _TmnxSysRollbackSaveComment_Type()
)
tmnxSysRollbackSaveComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackSaveComment.setStatus("current")


class _TmnxSysRollbackFileDelete_Type(TmnxActionType):
    """Custom type tmnxSysRollbackFileDelete based on TmnxActionType"""


_TmnxSysRollbackFileDelete_Object = MibScalar
tmnxSysRollbackFileDelete = _TmnxSysRollbackFileDelete_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 14),
    _TmnxSysRollbackFileDelete_Type()
)
tmnxSysRollbackFileDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileDelete.setStatus("current")


class _TmnxSysRollbackFileDeleteResult_Type(Integer32):
    """Custom type tmnxSysRollbackFileDeleteResult based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("none", 1),
          ("success", 3))
    )


_TmnxSysRollbackFileDeleteResult_Type.__name__ = "Integer32"
_TmnxSysRollbackFileDeleteResult_Object = MibScalar
tmnxSysRollbackFileDeleteResult = _TmnxSysRollbackFileDeleteResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 15),
    _TmnxSysRollbackFileDeleteResult_Type()
)
tmnxSysRollbackFileDeleteResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileDeleteResult.setStatus("current")


class _TmnxSysRollbackAbortRevert_Type(TmnxActionType):
    """Custom type tmnxSysRollbackAbortRevert based on TmnxActionType"""


_TmnxSysRollbackAbortRevert_Object = MibScalar
tmnxSysRollbackAbortRevert = _TmnxSysRollbackAbortRevert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 16),
    _TmnxSysRollbackAbortRevert_Type()
)
tmnxSysRollbackAbortRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackAbortRevert.setStatus("current")


class _TmnxSysRollbackRescueLocation_Type(DisplayString):
    """Custom type tmnxSysRollbackRescueLocation based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxSysRollbackRescueLocation_Type.__name__ = "DisplayString"
_TmnxSysRollbackRescueLocation_Object = MibScalar
tmnxSysRollbackRescueLocation = _TmnxSysRollbackRescueLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 17),
    _TmnxSysRollbackRescueLocation_Type()
)
tmnxSysRollbackRescueLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueLocation.setStatus("current")


class _TmnxSysRollbackRescueRevert_Type(TmnxActionType):
    """Custom type tmnxSysRollbackRescueRevert based on TmnxActionType"""


_TmnxSysRollbackRescueRevert_Object = MibScalar
tmnxSysRollbackRescueRevert = _TmnxSysRollbackRescueRevert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 18),
    _TmnxSysRollbackRescueRevert_Type()
)
tmnxSysRollbackRescueRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueRevert.setStatus("current")


class _TmnxSysRollbackRescueSave_Type(TmnxActionType):
    """Custom type tmnxSysRollbackRescueSave based on TmnxActionType"""


_TmnxSysRollbackRescueSave_Object = MibScalar
tmnxSysRollbackRescueSave = _TmnxSysRollbackRescueSave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 19),
    _TmnxSysRollbackRescueSave_Type()
)
tmnxSysRollbackRescueSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueSave.setStatus("current")


class _TmnxSysRollbackRescueDelete_Type(TmnxActionType):
    """Custom type tmnxSysRollbackRescueDelete based on TmnxActionType"""


_TmnxSysRollbackRescueDelete_Object = MibScalar
tmnxSysRollbackRescueDelete = _TmnxSysRollbackRescueDelete_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 20),
    _TmnxSysRollbackRescueDelete_Type()
)
tmnxSysRollbackRescueDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueDelete.setStatus("current")


class _TmnxSysRollbackRescueSaveRes_Type(Integer32):
    """Custom type tmnxSysRollbackRescueSaveRes based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("none", 1),
          ("success", 3))
    )


_TmnxSysRollbackRescueSaveRes_Type.__name__ = "Integer32"
_TmnxSysRollbackRescueSaveRes_Object = MibScalar
tmnxSysRollbackRescueSaveRes = _TmnxSysRollbackRescueSaveRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 21),
    _TmnxSysRollbackRescueSaveRes_Type()
)
tmnxSysRollbackRescueSaveRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueSaveRes.setStatus("current")


class _TmnxSysRollbackRescueRevertRes_Type(Integer32):
    """Custom type tmnxSysRollbackRescueRevertRes based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("interrupted", 5),
          ("none", 1),
          ("success", 3))
    )


_TmnxSysRollbackRescueRevertRes_Type.__name__ = "Integer32"
_TmnxSysRollbackRescueRevertRes_Object = MibScalar
tmnxSysRollbackRescueRevertRes = _TmnxSysRollbackRescueRevertRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 22),
    _TmnxSysRollbackRescueRevertRes_Type()
)
tmnxSysRollbackRescueRevertRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueRevertRes.setStatus("current")


class _TmnxSysRollbackRescueDeleteRes_Type(Integer32):
    """Custom type tmnxSysRollbackRescueDeleteRes based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("none", 1),
          ("success", 3))
    )


_TmnxSysRollbackRescueDeleteRes_Type.__name__ = "Integer32"
_TmnxSysRollbackRescueDeleteRes_Object = MibScalar
tmnxSysRollbackRescueDeleteRes = _TmnxSysRollbackRescueDeleteRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 23),
    _TmnxSysRollbackRescueDeleteRes_Type()
)
tmnxSysRollbackRescueDeleteRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueDeleteRes.setStatus("current")
_TmnxSysRollbackRescueSavedTime_Type = DateAndTime
_TmnxSysRollbackRescueSavedTime_Object = MibScalar
tmnxSysRollbackRescueSavedTime = _TmnxSysRollbackRescueSavedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 24),
    _TmnxSysRollbackRescueSavedTime_Type()
)
tmnxSysRollbackRescueSavedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueSavedTime.setStatus("current")
_TmnxSysRollbackRescueRevStTime_Type = DateAndTime
_TmnxSysRollbackRescueRevStTime_Object = MibScalar
tmnxSysRollbackRescueRevStTime = _TmnxSysRollbackRescueRevStTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 25),
    _TmnxSysRollbackRescueRevStTime_Type()
)
tmnxSysRollbackRescueRevStTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueRevStTime.setStatus("current")
_TmnxSysRollbackRescueRevEdTime_Type = DateAndTime
_TmnxSysRollbackRescueRevEdTime_Object = MibScalar
tmnxSysRollbackRescueRevEdTime = _TmnxSysRollbackRescueRevEdTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 26),
    _TmnxSysRollbackRescueRevEdTime_Type()
)
tmnxSysRollbackRescueRevEdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueRevEdTime.setStatus("current")


class _TmnxSysRollbackRescueRevUser_Type(TNamedItemOrEmpty):
    """Custom type tmnxSysRollbackRescueRevUser based on TNamedItemOrEmpty"""
    defaultHexValue = ""

    subtypeSpec = TNamedItemOrEmpty.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxSysRollbackRescueRevUser_Type.__name__ = "TNamedItemOrEmpty"
_TmnxSysRollbackRescueRevUser_Object = MibScalar
tmnxSysRollbackRescueRevUser = _TmnxSysRollbackRescueRevUser_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 27),
    _TmnxSysRollbackRescueRevUser_Type()
)
tmnxSysRollbackRescueRevUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueRevUser.setStatus("current")


class _TmnxSysRollbackRescueSaveComment_Type(DisplayString):
    """Custom type tmnxSysRollbackRescueSaveComment based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxSysRollbackRescueSaveComment_Type.__name__ = "DisplayString"
_TmnxSysRollbackRescueSaveComment_Object = MibScalar
tmnxSysRollbackRescueSaveComment = _TmnxSysRollbackRescueSaveComment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 28),
    _TmnxSysRollbackRescueSaveComment_Type()
)
tmnxSysRollbackRescueSaveComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueSaveComment.setStatus("current")


class _TmnxSysRollbackRescueAbortRevert_Type(TmnxActionType):
    """Custom type tmnxSysRollbackRescueAbortRevert based on TmnxActionType"""


_TmnxSysRollbackRescueAbortRevert_Object = MibScalar
tmnxSysRollbackRescueAbortRevert = _TmnxSysRollbackRescueAbortRevert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 29),
    _TmnxSysRollbackRescueAbortRevert_Type()
)
tmnxSysRollbackRescueAbortRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueAbortRevert.setStatus("current")


class _TmnxSysRollbackRescueFileExists_Type(TruthValue):
    """Custom type tmnxSysRollbackRescueFileExists based on TruthValue"""


_TmnxSysRollbackRescueFileExists_Object = MibScalar
tmnxSysRollbackRescueFileExists = _TmnxSysRollbackRescueFileExists_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 30),
    _TmnxSysRollbackRescueFileExists_Type()
)
tmnxSysRollbackRescueFileExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueFileExists.setStatus("current")


class _TmnxSysRollbackMaxLocalFiles_Type(Unsigned32):
    """Custom type tmnxSysRollbackMaxLocalFiles based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_TmnxSysRollbackMaxLocalFiles_Type.__name__ = "Unsigned32"
_TmnxSysRollbackMaxLocalFiles_Object = MibScalar
tmnxSysRollbackMaxLocalFiles = _TmnxSysRollbackMaxLocalFiles_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 31),
    _TmnxSysRollbackMaxLocalFiles_Type()
)
tmnxSysRollbackMaxLocalFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackMaxLocalFiles.setStatus("current")


class _TmnxSysRollbackMaxRemoteFiles_Type(Unsigned32):
    """Custom type tmnxSysRollbackMaxRemoteFiles based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_TmnxSysRollbackMaxRemoteFiles_Type.__name__ = "Unsigned32"
_TmnxSysRollbackMaxRemoteFiles_Object = MibScalar
tmnxSysRollbackMaxRemoteFiles = _TmnxSysRollbackMaxRemoteFiles_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 32),
    _TmnxSysRollbackMaxRemoteFiles_Type()
)
tmnxSysRollbackMaxRemoteFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackMaxRemoteFiles.setStatus("current")
_TmnxSysRollbackTableLastChanged_Type = TimeStamp
_TmnxSysRollbackTableLastChanged_Object = MibScalar
tmnxSysRollbackTableLastChanged = _TmnxSysRollbackTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 18),
    _TmnxSysRollbackTableLastChanged_Type()
)
tmnxSysRollbackTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackTableLastChanged.setStatus("current")
_TmnxSysRollbackFileTable_Object = MibTable
tmnxSysRollbackFileTable = _TmnxSysRollbackFileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 19)
)
if mibBuilder.loadTexts:
    tmnxSysRollbackFileTable.setStatus("current")
_TmnxSysRollbackFileEntry_Object = MibTableRow
tmnxSysRollbackFileEntry = _TmnxSysRollbackFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 19, 1)
)
tmnxSysRollbackFileEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileIndex"),
)
if mibBuilder.loadTexts:
    tmnxSysRollbackFileEntry.setStatus("current")


class _TmnxSysRollbackFileIndex_Type(Unsigned32):
    """Custom type tmnxSysRollbackFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_TmnxSysRollbackFileIndex_Type.__name__ = "Unsigned32"
_TmnxSysRollbackFileIndex_Object = MibTableColumn
tmnxSysRollbackFileIndex = _TmnxSysRollbackFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 19, 1, 1),
    _TmnxSysRollbackFileIndex_Type()
)
tmnxSysRollbackFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileIndex.setStatus("current")
_TmnxSysRollbackFileCreationTime_Type = DateAndTime
_TmnxSysRollbackFileCreationTime_Object = MibTableColumn
tmnxSysRollbackFileCreationTime = _TmnxSysRollbackFileCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 19, 1, 2),
    _TmnxSysRollbackFileCreationTime_Type()
)
tmnxSysRollbackFileCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileCreationTime.setStatus("current")


class _TmnxSysRollbackFileComment_Type(DisplayString):
    """Custom type tmnxSysRollbackFileComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxSysRollbackFileComment_Type.__name__ = "DisplayString"
_TmnxSysRollbackFileComment_Object = MibTableColumn
tmnxSysRollbackFileComment = _TmnxSysRollbackFileComment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 19, 1, 3),
    _TmnxSysRollbackFileComment_Type()
)
tmnxSysRollbackFileComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileComment.setStatus("current")


class _TmnxSysRollbackFileUserName_Type(TNamedItem):
    """Custom type tmnxSysRollbackFileUserName based on TNamedItem"""
    subtypeSpec = TNamedItem.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_TmnxSysRollbackFileUserName_Type.__name__ = "TNamedItem"
_TmnxSysRollbackFileUserName_Object = MibTableColumn
tmnxSysRollbackFileUserName = _TmnxSysRollbackFileUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 19, 1, 4),
    _TmnxSysRollbackFileUserName_Type()
)
tmnxSysRollbackFileUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileUserName.setStatus("current")


class _TmnxSysRollbackFileVersion_Type(DisplayString):
    """Custom type tmnxSysRollbackFileVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxSysRollbackFileVersion_Type.__name__ = "DisplayString"
_TmnxSysRollbackFileVersion_Object = MibTableColumn
tmnxSysRollbackFileVersion = _TmnxSysRollbackFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 19, 1, 5),
    _TmnxSysRollbackFileVersion_Type()
)
tmnxSysRollbackFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileVersion.setStatus("current")
_SysBootedBofInfo_ObjectIdentity = ObjectIdentity
sysBootedBofInfo = _SysBootedBofInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 20)
)
_SbbiLiSeparate_Type = TruthValue
_SbbiLiSeparate_Object = MibScalar
sbbiLiSeparate = _SbbiLiSeparate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 20, 1),
    _SbbiLiSeparate_Type()
)
sbbiLiSeparate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbbiLiSeparate.setStatus("current")
_SbbiLiLocalSave_Type = TruthValue
_SbbiLiLocalSave_Object = MibScalar
sbbiLiLocalSave = _SbbiLiLocalSave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 20, 2),
    _SbbiLiLocalSave_Type()
)
sbbiLiLocalSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbbiLiLocalSave.setStatus("current")
_TmnxSysMIBNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxSysMIBNotifyPrefix = _TmnxSysMIBNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1)
)
_TmnxSysNotifications_ObjectIdentity = ObjectIdentity
tmnxSysNotifications = _TmnxSysNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0)
)

# Managed Objects groups

tmnxSysRadiusServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 4)
)
tmnxSysRadiusServerGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "radiusOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerAddress"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxSysRadiusServerGroup.setStatus("obsolete")

tmnxSysTacPlusServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 5)
)
tmnxSysTacPlusServerGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tacplusOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerAddress"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxSysTacPlusServerGroup.setStatus("obsolete")

tmnxSysBofGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 8)
)
tmnxSysBofGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiActiveIpAddr"),
        ("TIMETRA-SYSTEM-MIB", "sbiActiveIpMask"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyIpAddr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyIpMask"),
        ("TIMETRA-SYSTEM-MIB", "sbiPrimaryImage"),
        ("TIMETRA-SYSTEM-MIB", "sbiSecondaryImage"),
        ("TIMETRA-SYSTEM-MIB", "sbiTertiaryImage"),
        ("TIMETRA-SYSTEM-MIB", "sbiPrimaryConfigFile"),
        ("TIMETRA-SYSTEM-MIB", "sbiSecondaryConfigFile"),
        ("TIMETRA-SYSTEM-MIB", "sbiTertiaryConfigFile"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersist"),
        ("TIMETRA-SYSTEM-MIB", "sbiConsoleSpeed"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoNegotiate"),
        ("TIMETRA-SYSTEM-MIB", "sbiSpeed"),
        ("TIMETRA-SYSTEM-MIB", "sbiDuplex"),
        ("TIMETRA-SYSTEM-MIB", "sbiPrimaryDns"),
        ("TIMETRA-SYSTEM-MIB", "sbiSecondaryDns"),
        ("TIMETRA-SYSTEM-MIB", "sbiTertiaryDns"),
        ("TIMETRA-SYSTEM-MIB", "sbiDnsDomain"),
        ("TIMETRA-SYSTEM-MIB", "sbiWait"),
        ("TIMETRA-SYSTEM-MIB", "sbiStaticRouteNextHop"),
        ("TIMETRA-SYSTEM-MIB", "sbiStaticRouteRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxSysBofGroup.setStatus("obsolete")

tmnxSysConfigV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 12)
)
tmnxSysConfigV3v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "ssiSaveConfig"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncMode"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncForce"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncStatus"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigLastTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvLastTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiConfigMaxBackupRevisions"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigResult"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveBof"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveBofResult"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigDest"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigDetail"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedFailoverTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedFailoverReason"),
        ("TIMETRA-SYSTEM-MIB", "sbiConfigStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersistStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersistIndex"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdAdminStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdMaxPktSize"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdPortNum"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfigOKScript"),
        ("TIMETRA-SYSTEM-MIB", "sbiConfigOKScriptStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfigFailScript"),
        ("TIMETRA-SYSTEM-MIB", "sbiConfigFailScriptStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiRedSwitchoverScript"),
        ("TIMETRA-SYSTEM-MIB", "sbiRedSwitchoverScriptStatus"),
        ("TIMETRA-SYSTEM-MIB", "slcFtpInboundMaxSessions"),
        ("TIMETRA-SYSTEM-MIB", "slcTelnetInboundMaxSessions"),
        ("TIMETRA-SYSTEM-MIB", "slcTelnetOutboundMaxSessions"),
        ("TIMETRA-SYSTEM-MIB", "slcPreLoginMessage"),
        ("TIMETRA-SYSTEM-MIB", "slcPreLoginMessageInclName"),
        ("TIMETRA-SYSTEM-MIB", "slcMessageOfTheDay"),
        ("TIMETRA-SYSTEM-MIB", "slcMessageOfTheDayType"),
        ("TIMETRA-SYSTEM-MIB", "slcLoginBanner"),
        ("TIMETRA-SYSTEM-MIB", "sysLACPSystemPriority"),
        ("TIMETRA-SYSTEM-MIB", "slcLoginExponentialBackOff"))
)
if mibBuilder.loadTexts:
    tmnxSysConfigV3v0Group.setStatus("obsolete")

tmnxSysGeneralV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 15)
)
tmnxSysGeneralV3v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sgiCpuUsage"),
        ("TIMETRA-SYSTEM-MIB", "sgiMemoryUsed"),
        ("TIMETRA-SYSTEM-MIB", "sgiMemoryAvailable"),
        ("TIMETRA-SYSTEM-MIB", "sgiMemoryPoolAllocated"),
        ("TIMETRA-SYSTEM-MIB", "sgiSwMajorVersion"),
        ("TIMETRA-SYSTEM-MIB", "sgiSwMinorVersion"),
        ("TIMETRA-SYSTEM-MIB", "sgiSwVersionModifier"))
)
if mibBuilder.loadTexts:
    tmnxSysGeneralV3v0Group.setStatus("current")

tmnxSysObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 17)
)
tmnxSysObsoleteGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "stiSummerZoneStartDate"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneEndDate"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerAddress"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerAddress"))
)
if mibBuilder.loadTexts:
    tmnxSysObsoleteGroup.setStatus("obsolete")

tmnxPersistenceV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 18)
)
tmnxPersistenceV4v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "spiDhcpL2PersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpL2PersistenceDescription"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpL3PersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpL3PersistenceDescription"),
        ("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceDescription"))
)
if mibBuilder.loadTexts:
    tmnxPersistenceV4v0Group.setStatus("obsolete")

tmnxSysTimeV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 19)
)
tmnxSysTimeV4v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "stiDateAndTime"),
        ("TIMETRA-SYSTEM-MIB", "stiActiveZone"),
        ("TIMETRA-SYSTEM-MIB", "stiHoursOffset"),
        ("TIMETRA-SYSTEM-MIB", "stiMinutesOffset"),
        ("TIMETRA-SYSTEM-MIB", "stiZoneType"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneOffset"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneStartDay"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneStartWeek"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneStartMonth"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneStartHour"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneStartMinute"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneEndDay"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneEndWeek"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneEndMonth"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneEndHour"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneEndMinute"),
        ("TIMETRA-SYSTEM-MIB", "sntpState"),
        ("TIMETRA-SYSTEM-MIB", "sntpServerRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "sntpServerVersion"),
        ("TIMETRA-SYSTEM-MIB", "sntpServerPreference"),
        ("TIMETRA-SYSTEM-MIB", "sntpServerInterval"),
        ("TIMETRA-SYSTEM-MIB", "sntpAdminState"),
        ("TIMETRA-SYSTEM-MIB", "sntpOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxSysTimeV4v0Group.setStatus("current")

tmnxSysNotifyObjsR4r0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 20)
)
tmnxSysNotifyObjsR4r0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxNotifyRow"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyRowAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyRowOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxMemoryModule"),
        ("TIMETRA-SYSTEM-MIB", "tmnxModuleMallocSize"),
        ("TIMETRA-SYSTEM-MIB", "tmnxDroppedTrapID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDroppedReasonCode"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDroppedEntryID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyEntryOID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdErrorMsg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeSetBy"))
)
if mibBuilder.loadTexts:
    tmnxSysNotifyObjsR4r0Group.setStatus("obsolete")

tmnxSysNotifyObjsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 22)
)
tmnxSysNotifyObjsV5v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistencyClient"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyFileLocator"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyNotifyMsg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistenceAffectedCpm"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyRow"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyRowAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyRowOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxMemoryModule"),
        ("TIMETRA-SYSTEM-MIB", "tmnxModuleMallocSize"),
        ("TIMETRA-SYSTEM-MIB", "tmnxDroppedTrapID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDroppedReasonCode"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDroppedEntryID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyEntryOID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdErrorMsg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeSetBy"),
        ("TIMETRA-SYSTEM-MIB", "tmnxFtpFailureMsg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxFtpFailureDestAddressType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxFtpFailureDestAddress"))
)
if mibBuilder.loadTexts:
    tmnxSysNotifyObjsV5v0Group.setStatus("current")

tmnxSysTacPlusServerV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 25)
)
tmnxSysTacPlusServerV5v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tacplusOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "tacPlusServerInetAddressType"),
        ("TIMETRA-SYSTEM-MIB", "tacPlusServerInetAddress"))
)
if mibBuilder.loadTexts:
    tmnxSysTacPlusServerV5v0Group.setStatus("current")

tmnxSysRadiusServerV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 26)
)
tmnxSysRadiusServerV5v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "radiusOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerInetAddressType"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerInetAddress"))
)
if mibBuilder.loadTexts:
    tmnxSysRadiusServerV5v0Group.setStatus("current")

tmnxSysObsoleteV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 27)
)
tmnxSysObsoleteV5v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "stiSummerZoneStartDate"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneEndDate"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerAddress"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerAddress"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpL2PersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpL2PersistenceDescription"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpL3PersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpL3PersistenceDescription"))
)
if mibBuilder.loadTexts:
    tmnxSysObsoleteV5v0Group.setStatus("current")

tmnxPersistenceV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 28)
)
tmnxPersistenceV5v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceDescription"))
)
if mibBuilder.loadTexts:
    tmnxPersistenceV5v0Group.setStatus("obsolete")

tmnxSysIpv6MgmtItfV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 29)
)
tmnxSysIpv6MgmtItfV6v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiActiveIPv6Addr"),
        ("TIMETRA-SYSTEM-MIB", "sbiActiveIPv6PfxLen"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyIPv6Addr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyIPv6PfxLen"),
        ("TIMETRA-SYSTEM-MIB", "sbiPrimaryDnsIPv6Addr"),
        ("TIMETRA-SYSTEM-MIB", "sbiSecondaryDnsIPv6Addr"),
        ("TIMETRA-SYSTEM-MIB", "sbiTertiaryDnsIPv6Addr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStaticRouteIPv6NextHop"),
        ("TIMETRA-SYSTEM-MIB", "sbiStaticRouteIPv6RowStatus"),
        ("TIMETRA-SYSTEM-MIB", "sysDNSInfoLastChanged"),
        ("TIMETRA-SYSTEM-MIB", "sysDNSAddressResolvePref"))
)
if mibBuilder.loadTexts:
    tmnxSysIpv6MgmtItfV6v0Group.setStatus("current")

tmnxPersistenceV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 30)
)
tmnxPersistenceV6v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceDescription"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpSrvPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpSrvPersistenceDescr"))
)
if mibBuilder.loadTexts:
    tmnxPersistenceV6v0Group.setStatus("obsolete")

tmnxSysBofV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 31)
)
tmnxSysBofV6v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiActiveIpAddr"),
        ("TIMETRA-SYSTEM-MIB", "sbiActiveIpMask"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyIpAddr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyIpMask"),
        ("TIMETRA-SYSTEM-MIB", "sbiPrimaryImage"),
        ("TIMETRA-SYSTEM-MIB", "sbiSecondaryImage"),
        ("TIMETRA-SYSTEM-MIB", "sbiTertiaryImage"),
        ("TIMETRA-SYSTEM-MIB", "sbiPrimaryConfigFile"),
        ("TIMETRA-SYSTEM-MIB", "sbiSecondaryConfigFile"),
        ("TIMETRA-SYSTEM-MIB", "sbiTertiaryConfigFile"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersist"),
        ("TIMETRA-SYSTEM-MIB", "sbiConsoleSpeed"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoNegotiate"),
        ("TIMETRA-SYSTEM-MIB", "sbiSpeed"),
        ("TIMETRA-SYSTEM-MIB", "sbiDuplex"),
        ("TIMETRA-SYSTEM-MIB", "sbiPrimaryDns"),
        ("TIMETRA-SYSTEM-MIB", "sbiSecondaryDns"),
        ("TIMETRA-SYSTEM-MIB", "sbiTertiaryDns"),
        ("TIMETRA-SYSTEM-MIB", "sbiDnsDomain"),
        ("TIMETRA-SYSTEM-MIB", "sbiWait"),
        ("TIMETRA-SYSTEM-MIB", "sbiStaticRouteNextHop"),
        ("TIMETRA-SYSTEM-MIB", "sbiStaticRouteRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiLiSeparate"),
        ("TIMETRA-SYSTEM-MIB", "sbiLiLocalSave"))
)
if mibBuilder.loadTexts:
    tmnxSysBofV6v0Group.setStatus("current")

tmnxSysLiV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 33)
)
tmnxSysLiV6v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sliConfigStatus"),
        ("TIMETRA-SYSTEM-MIB", "sliSaveConfig"),
        ("TIMETRA-SYSTEM-MIB", "sliSaveConfigResult"),
        ("TIMETRA-SYSTEM-MIB", "sliConfigLastModified"),
        ("TIMETRA-SYSTEM-MIB", "sliConfigLastSaved"))
)
if mibBuilder.loadTexts:
    tmnxSysLiV6v0Group.setStatus("current")

tmnxSysNotifyObjsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 34)
)
tmnxSysNotifyObjsV6v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxNotifyObjectName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSyncFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxSysNotifyObjsV6v0Group.setStatus("current")

tmnxSysGeneralV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 35)
)
tmnxSysGeneralV7v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sgiSnmpInGetBulks"),
        ("TIMETRA-SYSTEM-MIB", "sgiKbMemoryUsed"),
        ("TIMETRA-SYSTEM-MIB", "sgiKbMemoryAvailable"),
        ("TIMETRA-SYSTEM-MIB", "sgiKbMemoryPoolAllocated"))
)
if mibBuilder.loadTexts:
    tmnxSysGeneralV7v0Group.setStatus("current")

tmnxSysIcmpVSV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 36)
)
tmnxSysIcmpVSV6v1Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sysIcmpVSEnhancement")
)
if mibBuilder.loadTexts:
    tmnxSysIcmpVSV6v1Group.setStatus("current")

tmnxSysConfigV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 37)
)
tmnxSysConfigV8v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "ssiSaveConfig"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncMode"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncForce"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncStatus"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigLastTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvLastTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiConfigMaxBackupRevisions"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigResult"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveBof"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveBofResult"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigDest"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigDetail"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedFailoverTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedFailoverReason"),
        ("TIMETRA-SYSTEM-MIB", "sbiConfigStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersistStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersistIndex"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdAdminStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdMaxPktSize"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdPortNum"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfigOKScript"),
        ("TIMETRA-SYSTEM-MIB", "sbiConfigOKScriptStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfigFailScript"),
        ("TIMETRA-SYSTEM-MIB", "sbiConfigFailScriptStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiRedSwitchoverScript"),
        ("TIMETRA-SYSTEM-MIB", "sbiRedSwitchoverScriptStatus"),
        ("TIMETRA-SYSTEM-MIB", "sysLACPSystemPriority"))
)
if mibBuilder.loadTexts:
    tmnxSysConfigV8v0Group.setStatus("current")

tmnxSysLoginControlV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 38)
)
tmnxSysLoginControlV8v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "slcFtpInboundMaxSessions"),
        ("TIMETRA-SYSTEM-MIB", "slcTelnetInboundMaxSessions"),
        ("TIMETRA-SYSTEM-MIB", "slcTelnetOutboundMaxSessions"),
        ("TIMETRA-SYSTEM-MIB", "slcPreLoginMessage"),
        ("TIMETRA-SYSTEM-MIB", "slcPreLoginMessageInclName"),
        ("TIMETRA-SYSTEM-MIB", "slcMessageOfTheDay"),
        ("TIMETRA-SYSTEM-MIB", "slcMessageOfTheDayType"),
        ("TIMETRA-SYSTEM-MIB", "slcLoginBanner"),
        ("TIMETRA-SYSTEM-MIB", "slcLoginExponentialBackOff"),
        ("TIMETRA-SYSTEM-MIB", "slcTelnetGracefulShutdown"),
        ("TIMETRA-SYSTEM-MIB", "slcSSHGracefulShutdown"))
)
if mibBuilder.loadTexts:
    tmnxSysLoginControlV8v0Group.setStatus("current")

tmnxSysEthInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 39)
)
tmnxSysEthInfoGroup.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sysNewQinqUntaggedSap")
)
if mibBuilder.loadTexts:
    tmnxSysEthInfoGroup.setStatus("current")

tmnxPersistenceV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 40)
)
tmnxPersistenceV9v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceDescription"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpSrvPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpSrvPersistenceDescr"),
        ("TIMETRA-SYSTEM-MIB", "spiNatFwdPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiNatFwdPersistenceDescr"),
        ("TIMETRA-SYSTEM-MIB", "spiAAPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiAAPersistenceDescr"))
)
if mibBuilder.loadTexts:
    tmnxPersistenceV9v0Group.setStatus("current")

tmnxSysLoginControlSecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 41)
)
tmnxSysLoginControlSecGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "slcTelnetMinTTLValue"),
        ("TIMETRA-SYSTEM-MIB", "slcSSHMinTTLValue"))
)
if mibBuilder.loadTexts:
    tmnxSysLoginControlSecGroup.setStatus("current")

tmnxSysLiFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 42)
)
tmnxSysLiFilterGroup.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sliFilterLock")
)
if mibBuilder.loadTexts:
    tmnxSysLiFilterGroup.setStatus("current")

tmnxSysRollbackV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 44)
)
tmnxSysRollbackV9v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackIndex"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackStart"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackResult"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackSave"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackSaveResult"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackLocation"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRevertIndex"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRevertEndTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackTableLastChanged"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileCreationTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileComment"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileUserName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackSavedTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncRollbackLastTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRevertStartTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRevertUserName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRevertFilename"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackSaveComment"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackAbortRevert"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileVersion"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileDelete"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileDeleteResult"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncRollbackMode"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncRollbackForce"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncRollbackStatus"))
)
if mibBuilder.loadTexts:
    tmnxSysRollbackV9v0Group.setStatus("current")

tmnxSysLoginControlV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 45)
)
tmnxSysLoginControlV9v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "slcSSHInboundMaxSessions"),
        ("TIMETRA-SYSTEM-MIB", "slcSSHOutboundMaxSessions"))
)
if mibBuilder.loadTexts:
    tmnxSysLoginControlV9v0Group.setStatus("current")

tmnxSystemCpuMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 46)
)
tmnxSystemCpuMonitorGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysCpuMonCpuIdle"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpuMonBusyCoreUtil"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpuMonBusyGroupName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpuMonBusyGroupUtil"))
)
if mibBuilder.loadTexts:
    tmnxSystemCpuMonitorGroup.setStatus("current")

tmnxSysCertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 47)
)
tmnxSysCertGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "ssiSyncCertForce"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncCertLastTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncCertMode"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncCertStatus"))
)
if mibBuilder.loadTexts:
    tmnxSysCertGroup.setStatus("current")

tmnxSysBootedBofGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 48)
)
tmnxSysBootedBofGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbbiLiSeparate"),
        ("TIMETRA-SYSTEM-MIB", "sbbiLiLocalSave"))
)
if mibBuilder.loadTexts:
    tmnxSysBootedBofGroup.setStatus("current")

tmnxSysRollbackRescueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 49)
)
tmnxSysRollbackRescueGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueLocation"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueSave"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueRevert"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueDelete"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueSaveRes"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueRevertRes"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueDeleteRes"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueSavedTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueRevStTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueRevEdTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueRevUser"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueSaveComment"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueAbortRevert"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueFileExists"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackMaxLocalFiles"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackMaxRemoteFiles"))
)
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueGroup.setStatus("current")

tmnxSysNotifyObjsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 51)
)
tmnxSysNotifyObjsV10v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysExecScript"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysExecResult"))
)
if mibBuilder.loadTexts:
    tmnxSysNotifyObjsV10v0Group.setStatus("current")

tmnxSysNotifyObjsGenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 53)
)
tmnxSysNotifyObjsGenGroup.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysFileErrorType")
)
if mibBuilder.loadTexts:
    tmnxSysNotifyObjsGenGroup.setStatus("current")


# Notification objects

stiDateAndTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 1)
)
stiDateAndTimeChanged.setObjects(
    ("TIMETRA-SYSTEM-MIB", "stiDateAndTime")
)
if mibBuilder.loadTexts:
    stiDateAndTimeChanged.setStatus(
        "current"
    )

ssiSaveConfigSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 2)
)
if mibBuilder.loadTexts:
    ssiSaveConfigSucceeded.setStatus(
        "current"
    )

ssiSaveConfigFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 3)
)
if mibBuilder.loadTexts:
    ssiSaveConfigFailed.setStatus(
        "current"
    )

sbiBootConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 4)
)
sbiBootConfig.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiConfigStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersistStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersistIndex"))
)
if mibBuilder.loadTexts:
    sbiBootConfig.setStatus(
        "current"
    )

sbiBootSnmpd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 5)
)
sbiBootSnmpd.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiPersistIndex"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdAdminStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdOperStatus"))
)
if mibBuilder.loadTexts:
    sbiBootSnmpd.setStatus(
        "current"
    )

radiusServerOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 6)
)
radiusServerOperStatusChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "radiusServerAddress"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerOperStatus"))
)
if mibBuilder.loadTexts:
    radiusServerOperStatusChange.setStatus(
        "obsolete"
    )

radiusOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 7)
)
radiusOperStatusChange.setObjects(
    ("TIMETRA-SYSTEM-MIB", "radiusOperStatus")
)
if mibBuilder.loadTexts:
    radiusOperStatusChange.setStatus(
        "current"
    )

tmnxConfigModify = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 8)
)
tmnxConfigModify.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxNotifyRow"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyEntryOID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyObjectName"))
)
if mibBuilder.loadTexts:
    tmnxConfigModify.setStatus(
        "current"
    )

tmnxConfigCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 9)
)
tmnxConfigCreate.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxNotifyRow"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyEntryOID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyObjectName"))
)
if mibBuilder.loadTexts:
    tmnxConfigCreate.setStatus(
        "current"
    )

tmnxConfigDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 10)
)
tmnxConfigDelete.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxNotifyRow"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyEntryOID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyObjectName"))
)
if mibBuilder.loadTexts:
    tmnxConfigDelete.setStatus(
        "current"
    )

tmnxStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 11)
)
tmnxStateChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxNotifyRow"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyRowAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyRowOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyEntryOID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyObjectName"))
)
if mibBuilder.loadTexts:
    tmnxStateChange.setStatus(
        "current"
    )

tmnxModuleMallocFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 12)
)
tmnxModuleMallocFailed.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxMemoryModule"),
        ("TIMETRA-SYSTEM-MIB", "tmnxModuleMallocSize"))
)
if mibBuilder.loadTexts:
    tmnxModuleMallocFailed.setStatus(
        "current"
    )

tmnxTrapDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 13)
)
tmnxTrapDropped.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxDroppedTrapID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDroppedReasonCode"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDroppedEntryID"))
)
if mibBuilder.loadTexts:
    tmnxTrapDropped.setStatus(
        "current"
    )

ssiSyncConfigOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 14)
)
if mibBuilder.loadTexts:
    ssiSyncConfigOK.setStatus(
        "current"
    )

ssiSyncConfigFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 15)
)
ssiSyncConfigFailed.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSyncFailureReason")
)
if mibBuilder.loadTexts:
    ssiSyncConfigFailed.setStatus(
        "current"
    )

ssiSyncBootEnvOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 16)
)
if mibBuilder.loadTexts:
    ssiSyncBootEnvOK.setStatus(
        "current"
    )

ssiSyncBootEnvFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 17)
)
ssiSyncBootEnvFailed.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSyncFailureReason")
)
if mibBuilder.loadTexts:
    ssiSyncBootEnvFailed.setStatus(
        "current"
    )

sntpTimeDiffExceedsThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 18)
)
sntpTimeDiffExceedsThreshold.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sntpAdminState")
)
if mibBuilder.loadTexts:
    sntpTimeDiffExceedsThreshold.setStatus(
        "current"
    )

tacplusServerOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 19)
)
tacplusServerOperStatusChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tacplusServerAddress"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerOperStatus"))
)
if mibBuilder.loadTexts:
    tacplusServerOperStatusChange.setStatus(
        "obsolete"
    )

tacplusOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 20)
)
tacplusOperStatusChange.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tacplusOperStatus")
)
if mibBuilder.loadTexts:
    tacplusOperStatusChange.setStatus(
        "current"
    )

tmnxSnmpdError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 21)
)
tmnxSnmpdError.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdErrorMsg")
)
if mibBuilder.loadTexts:
    tmnxSnmpdError.setStatus(
        "current"
    )

tmnxSsiMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 22)
)
tmnxSsiMismatch.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "ssiSyncMode"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersist"))
)
if mibBuilder.loadTexts:
    tmnxSsiMismatch.setStatus(
        "current"
    )

tmnxSnmpdStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 23)
)
tmnxSnmpdStateChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiSnmpdAdminStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxSnmpdStateChange.setStatus(
        "current"
    )

ssiRedStandbySyncing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 24)
)
ssiRedStandbySyncing.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    ssiRedStandbySyncing.setStatus(
        "current"
    )

ssiRedStandbyReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 25)
)
ssiRedStandbyReady.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    ssiRedStandbyReady.setStatus(
        "current"
    )

ssiRedStandbySyncLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 26)
)
ssiRedStandbySyncLost.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    ssiRedStandbySyncLost.setStatus(
        "current"
    )

ssiRedSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 27)
)
ssiRedSwitchover.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedFailoverTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedFailoverReason"))
)
if mibBuilder.loadTexts:
    ssiRedSwitchover.setStatus(
        "current"
    )

ssiRedCpmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 28)
)
ssiRedCpmActive.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    ssiRedCpmActive.setStatus(
        "current"
    )

ssiRedSingleCpm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 29)
)
ssiRedSingleCpm.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    ssiRedSingleCpm.setStatus(
        "current"
    )

persistencyClosedAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 30)
)
persistencyClosedAlarmRaised.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistenceAffectedCpm"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyClient"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyFileLocator"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyNotifyMsg"))
)
if mibBuilder.loadTexts:
    persistencyClosedAlarmRaised.setStatus(
        "current"
    )

persistencyClosedAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 31)
)
persistencyClosedAlarmCleared.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistenceAffectedCpm"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyClient"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyFileLocator"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyNotifyMsg"))
)
if mibBuilder.loadTexts:
    persistencyClosedAlarmCleared.setStatus(
        "current"
    )

tmnxSntpOperChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 32)
)
tmnxSntpOperChange.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sntpOperStatus")
)
if mibBuilder.loadTexts:
    tmnxSntpOperChange.setStatus(
        "current"
    )

tmnxSysTimeSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 33)
)
tmnxSysTimeSet.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "stiDateAndTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeSetBy"))
)
if mibBuilder.loadTexts:
    tmnxSysTimeSet.setStatus(
        "current"
    )

tmnxFtpClientFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 34)
)
tmnxFtpClientFailure.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxFtpFailureMsg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxFtpFailureDestAddressType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxFtpFailureDestAddress"))
)
if mibBuilder.loadTexts:
    tmnxFtpClientFailure.setStatus(
        "current"
    )

tacplusInetSrvrOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 35)
)
tacplusInetSrvrOperStatusChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tacPlusServerInetAddressType"),
        ("TIMETRA-SYSTEM-MIB", "tacPlusServerInetAddress"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerOperStatus"))
)
if mibBuilder.loadTexts:
    tacplusInetSrvrOperStatusChange.setStatus(
        "current"
    )

radiusInetServerOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 36)
)
radiusInetServerOperStatusChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "radiusServerInetAddressType"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerInetAddress"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerOperStatus"))
)
if mibBuilder.loadTexts:
    radiusInetServerOperStatusChange.setStatus(
        "current"
    )

persistencyEventReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 37)
)
persistencyEventReport.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyNotifyMsg")
)
if mibBuilder.loadTexts:
    persistencyEventReport.setStatus(
        "current"
    )

sbiBootConfigFailFileError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 38)
)
sbiBootConfigFailFileError.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sbiBootConfigFailScript")
)
if mibBuilder.loadTexts:
    sbiBootConfigFailFileError.setStatus(
        "current"
    )

sbiBootConfigOKFileError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 39)
)
sbiBootConfigOKFileError.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sbiBootConfigOKScript")
)
if mibBuilder.loadTexts:
    sbiBootConfigOKFileError.setStatus(
        "current"
    )

sbiBootLiConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 40)
)
sbiBootLiConfig.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sliConfigStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiLiSeparate"),
        ("TIMETRA-SYSTEM-MIB", "sbiLiLocalSave"))
)
if mibBuilder.loadTexts:
    sbiBootLiConfig.setStatus(
        "current"
    )

persistenceRestoreProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 41)
)
persistenceRestoreProblem.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistencyClient"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyNotifyMsg"))
)
if mibBuilder.loadTexts:
    persistenceRestoreProblem.setStatus(
        "current"
    )

tmnxSysRollbackStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 42)
)
tmnxSysRollbackStarted.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackIndex"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileType"),
        ("TIMETRA-LOG-MIB", "tmnxLogExecRollbackOpIndex"))
)
if mibBuilder.loadTexts:
    tmnxSysRollbackStarted.setStatus(
        "current"
    )

tmnxSysRollbackStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 43)
)
tmnxSysRollbackStatusChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackIndex"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackResult"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileType"),
        ("TIMETRA-LOG-MIB", "tmnxLogExecRollbackOpIndex"))
)
if mibBuilder.loadTexts:
    tmnxSysRollbackStatusChange.setStatus(
        "current"
    )

tmnxSysRollbackSaveStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 44)
)
tmnxSysRollbackSaveStatusChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackSaveResult"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileType"))
)
if mibBuilder.loadTexts:
    tmnxSysRollbackSaveStatusChange.setStatus(
        "current"
    )

tmnxSysRollbackFileDeleteStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 45)
)
tmnxSysRollbackFileDeleteStatus.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackIndex"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileDeleteResult"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileType"))
)
if mibBuilder.loadTexts:
    tmnxSysRollbackFileDeleteStatus.setStatus(
        "current"
    )

ssiSyncRollbackOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 46)
)
if mibBuilder.loadTexts:
    ssiSyncRollbackOK.setStatus(
        "current"
    )

ssiSyncRollbackFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 47)
)
ssiSyncRollbackFailed.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSyncFailureReason")
)
if mibBuilder.loadTexts:
    ssiSyncRollbackFailed.setStatus(
        "current"
    )

ssiSyncCertOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 48)
)
if mibBuilder.loadTexts:
    ssiSyncCertOK.setStatus(
        "current"
    )

ssiSyncCertFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 49)
)
ssiSyncCertFailed.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSyncFailureReason")
)
if mibBuilder.loadTexts:
    ssiSyncCertFailed.setStatus(
        "current"
    )

persistencyFileSysThresRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 50)
)
persistencyFileSysThresRaised.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistenceAffectedCpm"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyClient"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyFileLocator"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyNotifyMsg"))
)
if mibBuilder.loadTexts:
    persistencyFileSysThresRaised.setStatus(
        "current"
    )

persistencyFileSysThresCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 51)
)
persistencyFileSysThresCleared.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistenceAffectedCpm"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyClient"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyFileLocator"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyNotifyMsg"))
)
if mibBuilder.loadTexts:
    persistencyFileSysThresCleared.setStatus(
        "current"
    )

tmnxSysExecStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 52)
)
tmnxSysExecStarted.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysExecScript"),
        ("TIMETRA-LOG-MIB", "tmnxLogExecRollbackOpIndex"))
)
if mibBuilder.loadTexts:
    tmnxSysExecStarted.setStatus(
        "current"
    )

tmnxSysExecFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 53)
)
tmnxSysExecFinished.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysExecScript"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysExecResult"),
        ("TIMETRA-LOG-MIB", "tmnxLogExecRollbackOpIndex"))
)
if mibBuilder.loadTexts:
    tmnxSysExecFinished.setStatus(
        "current"
    )

tmnxSysRollbackSaveStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 54)
)
tmnxSysRollbackSaveStarted.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileType")
)
if mibBuilder.loadTexts:
    tmnxSysRollbackSaveStarted.setStatus(
        "current"
    )

tmnxSysRollbackDeleteStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 55)
)
tmnxSysRollbackDeleteStarted.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackIndex"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileType"))
)
if mibBuilder.loadTexts:
    tmnxSysRollbackDeleteStarted.setStatus(
        "current"
    )

tmnxSysNvsysFileError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 56)
)
tmnxSysNvsysFileError.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysFileErrorType")
)
if mibBuilder.loadTexts:
    tmnxSysNvsysFileError.setStatus(
        "current"
    )


# Notifications groups

tmnxSysNotificationV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 21)
)
tmnxSysNotificationV4v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "stiDateAndTimeChanged"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigSucceeded"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigFailed"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfig"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootSnmpd"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "radiusOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigModify"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigCreate"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigDelete"),
        ("TIMETRA-SYSTEM-MIB", "tmnxStateChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxModuleMallocFailed"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDropped"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigFailed"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvFailed"),
        ("TIMETRA-SYSTEM-MIB", "sntpTimeDiffExceedsThreshold"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tacplusOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdError"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSsiMismatch"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdStateChange"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbySyncing"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbyReady"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbySyncLost"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedSwitchover"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedCpmActive"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedSingleCpm"),
        ("TIMETRA-SYSTEM-MIB", "persistencyClosedAlarmRaised"),
        ("TIMETRA-SYSTEM-MIB", "persistencyClosedAlarmCleared"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSntpOperChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeSet"))
)
if mibBuilder.loadTexts:
    tmnxSysNotificationV4v0Group.setStatus(
        "obsolete"
    )

tmnxSysNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 23)
)
tmnxSysNotificationV5v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "stiDateAndTimeChanged"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigSucceeded"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigFailed"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfig"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootSnmpd"),
        ("TIMETRA-SYSTEM-MIB", "radiusOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigModify"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigCreate"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigDelete"),
        ("TIMETRA-SYSTEM-MIB", "tmnxStateChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxModuleMallocFailed"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDropped"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigFailed"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvFailed"),
        ("TIMETRA-SYSTEM-MIB", "sntpTimeDiffExceedsThreshold"),
        ("TIMETRA-SYSTEM-MIB", "tacplusOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdError"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSsiMismatch"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdStateChange"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbySyncing"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbyReady"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbySyncLost"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedSwitchover"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedCpmActive"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedSingleCpm"),
        ("TIMETRA-SYSTEM-MIB", "persistencyClosedAlarmRaised"),
        ("TIMETRA-SYSTEM-MIB", "persistencyClosedAlarmCleared"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSntpOperChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeSet"),
        ("TIMETRA-SYSTEM-MIB", "tmnxFtpClientFailure"),
        ("TIMETRA-SYSTEM-MIB", "tacplusInetSrvrOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "radiusInetServerOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "persistencyEventReport"))
)
if mibBuilder.loadTexts:
    tmnxSysNotificationV5v0Group.setStatus(
        "obsolete"
    )

tmnxSysObsoleteNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 24)
)
tmnxSysObsoleteNotificationV5v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tacplusServerOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerOperStatusChange"))
)
if mibBuilder.loadTexts:
    tmnxSysObsoleteNotificationV5v0Group.setStatus(
        "current"
    )

tmnxSysNotificationV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 32)
)
tmnxSysNotificationV6v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "stiDateAndTimeChanged"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigSucceeded"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigFailed"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfig"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootSnmpd"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfigFailFileError"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfigOKFileError"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootLiConfig"),
        ("TIMETRA-SYSTEM-MIB", "radiusOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigModify"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigCreate"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigDelete"),
        ("TIMETRA-SYSTEM-MIB", "tmnxStateChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxModuleMallocFailed"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDropped"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigFailed"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvFailed"),
        ("TIMETRA-SYSTEM-MIB", "sntpTimeDiffExceedsThreshold"),
        ("TIMETRA-SYSTEM-MIB", "tacplusOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdError"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSsiMismatch"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdStateChange"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbySyncing"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbyReady"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbySyncLost"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedSwitchover"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedCpmActive"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedSingleCpm"),
        ("TIMETRA-SYSTEM-MIB", "persistencyClosedAlarmRaised"),
        ("TIMETRA-SYSTEM-MIB", "persistencyClosedAlarmCleared"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSntpOperChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeSet"),
        ("TIMETRA-SYSTEM-MIB", "tmnxFtpClientFailure"),
        ("TIMETRA-SYSTEM-MIB", "tacplusInetSrvrOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "radiusInetServerOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "persistencyEventReport"))
)
if mibBuilder.loadTexts:
    tmnxSysNotificationV6v0Group.setStatus(
        "current"
    )

tmnxSysNotificationV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 43)
)
tmnxSysNotificationV9v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "persistenceRestoreProblem"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackStarted"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackSaveStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileDeleteStatus"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncRollbackOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncRollbackFailed"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncCertOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncCertFailed"))
)
if mibBuilder.loadTexts:
    tmnxSysNotificationV9v0Group.setStatus(
        "current"
    )

tmnxSysNotificationV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 50)
)
tmnxSysNotificationV10v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "persistencyFileSysThresRaised"),
        ("TIMETRA-SYSTEM-MIB", "persistencyFileSysThresCleared"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysExecStarted"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysExecFinished"))
)
if mibBuilder.loadTexts:
    tmnxSysNotificationV10v0Group.setStatus(
        "current"
    )

tmnxSysNotificationRBGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 52)
)
tmnxSysNotificationRBGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackSaveStarted"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackDeleteStarted"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNvsysFileError"))
)
if mibBuilder.loadTexts:
    tmnxSysNotificationRBGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxSysV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxSysV4v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxSysV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxSysV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxSysV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxSysV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxSysV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysBootedBofCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxSysBootedBofCompliance.setStatus(
        "current"
    )

tmnxSysV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxSysV10v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SYSTEM-MIB",
    **{"TmnxSsiSyncMode": TmnxSsiSyncMode,
       "TmnxSsiSyncRollbackMode": TmnxSsiSyncRollbackMode,
       "TmnxSysMonSampleTime": TmnxSysMonSampleTime,
       "TmnxSysMonUtilization": TmnxSysMonUtilization,
       "timetraSysMIBModule": timetraSysMIBModule,
       "tmnxSysConformance": tmnxSysConformance,
       "tmnxSysCompliances": tmnxSysCompliances,
       "tmnxSysV4v0Compliance": tmnxSysV4v0Compliance,
       "tmnxSysV5v0Compliance": tmnxSysV5v0Compliance,
       "tmnxSysV6v0Compliance": tmnxSysV6v0Compliance,
       "tmnxSysV7v0Compliance": tmnxSysV7v0Compliance,
       "tmnxSysV8v0Compliance": tmnxSysV8v0Compliance,
       "tmnxSysV9v0Compliance": tmnxSysV9v0Compliance,
       "tmnxSysBootedBofCompliance": tmnxSysBootedBofCompliance,
       "tmnxSysV10v0Compliance": tmnxSysV10v0Compliance,
       "tmnxSysGroups": tmnxSysGroups,
       "tmnxSysRadiusServerGroup": tmnxSysRadiusServerGroup,
       "tmnxSysTacPlusServerGroup": tmnxSysTacPlusServerGroup,
       "tmnxSysBofGroup": tmnxSysBofGroup,
       "tmnxSysConfigV3v0Group": tmnxSysConfigV3v0Group,
       "tmnxSysGeneralV3v0Group": tmnxSysGeneralV3v0Group,
       "tmnxSysObsoleteGroup": tmnxSysObsoleteGroup,
       "tmnxPersistenceV4v0Group": tmnxPersistenceV4v0Group,
       "tmnxSysTimeV4v0Group": tmnxSysTimeV4v0Group,
       "tmnxSysNotifyObjsR4r0Group": tmnxSysNotifyObjsR4r0Group,
       "tmnxSysNotificationV4v0Group": tmnxSysNotificationV4v0Group,
       "tmnxSysNotifyObjsV5v0Group": tmnxSysNotifyObjsV5v0Group,
       "tmnxSysNotificationV5v0Group": tmnxSysNotificationV5v0Group,
       "tmnxSysObsoleteNotificationV5v0Group": tmnxSysObsoleteNotificationV5v0Group,
       "tmnxSysTacPlusServerV5v0Group": tmnxSysTacPlusServerV5v0Group,
       "tmnxSysRadiusServerV5v0Group": tmnxSysRadiusServerV5v0Group,
       "tmnxSysObsoleteV5v0Group": tmnxSysObsoleteV5v0Group,
       "tmnxPersistenceV5v0Group": tmnxPersistenceV5v0Group,
       "tmnxSysIpv6MgmtItfV6v0Group": tmnxSysIpv6MgmtItfV6v0Group,
       "tmnxPersistenceV6v0Group": tmnxPersistenceV6v0Group,
       "tmnxSysBofV6v0Group": tmnxSysBofV6v0Group,
       "tmnxSysNotificationV6v0Group": tmnxSysNotificationV6v0Group,
       "tmnxSysLiV6v0Group": tmnxSysLiV6v0Group,
       "tmnxSysNotifyObjsV6v0Group": tmnxSysNotifyObjsV6v0Group,
       "tmnxSysGeneralV7v0Group": tmnxSysGeneralV7v0Group,
       "tmnxSysIcmpVSV6v1Group": tmnxSysIcmpVSV6v1Group,
       "tmnxSysConfigV8v0Group": tmnxSysConfigV8v0Group,
       "tmnxSysLoginControlV8v0Group": tmnxSysLoginControlV8v0Group,
       "tmnxSysEthInfoGroup": tmnxSysEthInfoGroup,
       "tmnxPersistenceV9v0Group": tmnxPersistenceV9v0Group,
       "tmnxSysLoginControlSecGroup": tmnxSysLoginControlSecGroup,
       "tmnxSysLiFilterGroup": tmnxSysLiFilterGroup,
       "tmnxSysNotificationV9v0Group": tmnxSysNotificationV9v0Group,
       "tmnxSysRollbackV9v0Group": tmnxSysRollbackV9v0Group,
       "tmnxSysLoginControlV9v0Group": tmnxSysLoginControlV9v0Group,
       "tmnxSystemCpuMonitorGroup": tmnxSystemCpuMonitorGroup,
       "tmnxSysCertGroup": tmnxSysCertGroup,
       "tmnxSysBootedBofGroup": tmnxSysBootedBofGroup,
       "tmnxSysRollbackRescueGroup": tmnxSysRollbackRescueGroup,
       "tmnxSysNotificationV10v0Group": tmnxSysNotificationV10v0Group,
       "tmnxSysNotifyObjsV10v0Group": tmnxSysNotifyObjsV10v0Group,
       "tmnxSysNotificationRBGroup": tmnxSysNotificationRBGroup,
       "tmnxSysNotifyObjsGenGroup": tmnxSysNotifyObjsGenGroup,
       "tmnxSysObjs": tmnxSysObjs,
       "sysGenInfo": sysGenInfo,
       "sgiCpuUsage": sgiCpuUsage,
       "sgiMemoryUsed": sgiMemoryUsed,
       "sgiMemoryAvailable": sgiMemoryAvailable,
       "sgiMemoryPoolAllocated": sgiMemoryPoolAllocated,
       "sgiSwMajorVersion": sgiSwMajorVersion,
       "sgiSwMinorVersion": sgiSwMinorVersion,
       "sgiSwVersionModifier": sgiSwVersionModifier,
       "sgiSnmpInGetBulks": sgiSnmpInGetBulks,
       "sgiKbMemoryUsed": sgiKbMemoryUsed,
       "sgiKbMemoryAvailable": sgiKbMemoryAvailable,
       "sgiKbMemoryPoolAllocated": sgiKbMemoryPoolAllocated,
       "tmnxSysCpuMonTable": tmnxSysCpuMonTable,
       "tmnxSysCpuMonEntry": tmnxSysCpuMonEntry,
       "tmnxSysCpuMonSampleTime": tmnxSysCpuMonSampleTime,
       "tmnxSysCpuMonCpuIdle": tmnxSysCpuMonCpuIdle,
       "tmnxSysCpuMonBusyCoreUtil": tmnxSysCpuMonBusyCoreUtil,
       "tmnxSysCpuMonBusyGroupName": tmnxSysCpuMonBusyGroupName,
       "tmnxSysCpuMonBusyGroupUtil": tmnxSysCpuMonBusyGroupUtil,
       "sysTimeInfo": sysTimeInfo,
       "stiDateAndTime": stiDateAndTime,
       "stiActiveZone": stiActiveZone,
       "stiHoursOffset": stiHoursOffset,
       "stiMinutesOffset": stiMinutesOffset,
       "stiZoneType": stiZoneType,
       "stiSummerZoneTable": stiSummerZoneTable,
       "stiSummerZoneEntry": stiSummerZoneEntry,
       "stiSummerZoneName": stiSummerZoneName,
       "stiSummerZoneRowStatus": stiSummerZoneRowStatus,
       "stiSummerZoneStartDate": stiSummerZoneStartDate,
       "stiSummerZoneEndDate": stiSummerZoneEndDate,
       "stiSummerZoneOffset": stiSummerZoneOffset,
       "stiSummerZoneStartDay": stiSummerZoneStartDay,
       "stiSummerZoneStartWeek": stiSummerZoneStartWeek,
       "stiSummerZoneStartMonth": stiSummerZoneStartMonth,
       "stiSummerZoneStartHour": stiSummerZoneStartHour,
       "stiSummerZoneStartMinute": stiSummerZoneStartMinute,
       "stiSummerZoneEndDay": stiSummerZoneEndDay,
       "stiSummerZoneEndWeek": stiSummerZoneEndWeek,
       "stiSummerZoneEndMonth": stiSummerZoneEndMonth,
       "stiSummerZoneEndHour": stiSummerZoneEndHour,
       "stiSummerZoneEndMinute": stiSummerZoneEndMinute,
       "sysSntpInfo": sysSntpInfo,
       "sntpState": sntpState,
       "sntpServerTable": sntpServerTable,
       "sntpServerEntry": sntpServerEntry,
       "sntpServerAddress": sntpServerAddress,
       "sntpServerRowStatus": sntpServerRowStatus,
       "sntpServerVersion": sntpServerVersion,
       "sntpServerPreference": sntpServerPreference,
       "sntpServerInterval": sntpServerInterval,
       "sntpAdminState": sntpAdminState,
       "sntpOperStatus": sntpOperStatus,
       "sysSyncInfo": sysSyncInfo,
       "ssiSaveConfig": ssiSaveConfig,
       "ssiSyncMode": ssiSyncMode,
       "ssiSyncForce": ssiSyncForce,
       "ssiSyncStatus": ssiSyncStatus,
       "ssiSyncConfigLastTime": ssiSyncConfigLastTime,
       "ssiSyncBootEnvLastTime": ssiSyncBootEnvLastTime,
       "ssiConfigMaxBackupRevisions": ssiConfigMaxBackupRevisions,
       "ssiSaveConfigResult": ssiSaveConfigResult,
       "ssiSaveBof": ssiSaveBof,
       "ssiSaveBofResult": ssiSaveBofResult,
       "ssiSaveConfigDest": ssiSaveConfigDest,
       "ssiSaveConfigDetail": ssiSaveConfigDetail,
       "ssiRedFailoverTime": ssiRedFailoverTime,
       "ssiRedFailoverReason": ssiRedFailoverReason,
       "ssiSyncRollbackLastTime": ssiSyncRollbackLastTime,
       "ssiSyncRollbackMode": ssiSyncRollbackMode,
       "ssiSyncRollbackForce": ssiSyncRollbackForce,
       "ssiSyncRollbackStatus": ssiSyncRollbackStatus,
       "ssiSyncCertLastTime": ssiSyncCertLastTime,
       "ssiSyncCertMode": ssiSyncCertMode,
       "ssiSyncCertForce": ssiSyncCertForce,
       "ssiSyncCertStatus": ssiSyncCertStatus,
       "sysBootInfo": sysBootInfo,
       "sbiConfigStatus": sbiConfigStatus,
       "sbiPersistStatus": sbiPersistStatus,
       "sbiPersistIndex": sbiPersistIndex,
       "sbiSnmpdAdminStatus": sbiSnmpdAdminStatus,
       "sbiSnmpdOperStatus": sbiSnmpdOperStatus,
       "sbiSnmpdMaxPktSize": sbiSnmpdMaxPktSize,
       "sbiSnmpdPortNum": sbiSnmpdPortNum,
       "sbiBootConfigOKScript": sbiBootConfigOKScript,
       "sbiConfigOKScriptStatus": sbiConfigOKScriptStatus,
       "sbiBootConfigFailScript": sbiBootConfigFailScript,
       "sbiConfigFailScriptStatus": sbiConfigFailScriptStatus,
       "sbiRedSwitchoverScript": sbiRedSwitchoverScript,
       "sbiRedSwitchoverScriptStatus": sbiRedSwitchoverScriptStatus,
       "sysRadiusInfo": sysRadiusInfo,
       "radiusOperStatus": radiusOperStatus,
       "radiusServerTable": radiusServerTable,
       "radiusServerEntry": radiusServerEntry,
       "radiusServerIndex": radiusServerIndex,
       "radiusServerAddress": radiusServerAddress,
       "radiusServerOperStatus": radiusServerOperStatus,
       "radiusServerInetAddressType": radiusServerInetAddressType,
       "radiusServerInetAddress": radiusServerInetAddress,
       "tmnxSysNotifyObjs": tmnxSysNotifyObjs,
       "tmnxNotifyRow": tmnxNotifyRow,
       "tmnxNotifyRowAdminState": tmnxNotifyRowAdminState,
       "tmnxNotifyRowOperState": tmnxNotifyRowOperState,
       "tmnxMemoryModule": tmnxMemoryModule,
       "tmnxModuleMallocSize": tmnxModuleMallocSize,
       "tmnxDroppedTrapID": tmnxDroppedTrapID,
       "tmnxTrapDroppedReasonCode": tmnxTrapDroppedReasonCode,
       "tmnxTrapDroppedEntryID": tmnxTrapDroppedEntryID,
       "tmnxNotifyEntryOID": tmnxNotifyEntryOID,
       "tmnxSnmpdErrorMsg": tmnxSnmpdErrorMsg,
       "tmnxPersistencyClient": tmnxPersistencyClient,
       "tmnxPersistencyFileLocator": tmnxPersistencyFileLocator,
       "tmnxPersistencyNotifyMsg": tmnxPersistencyNotifyMsg,
       "tmnxPersistenceAffectedCpm": tmnxPersistenceAffectedCpm,
       "tmnxSysTimeSetBy": tmnxSysTimeSetBy,
       "tmnxFtpFailureMsg": tmnxFtpFailureMsg,
       "tmnxFtpFailureDestAddressType": tmnxFtpFailureDestAddressType,
       "tmnxFtpFailureDestAddress": tmnxFtpFailureDestAddress,
       "tmnxNotifyObjectName": tmnxNotifyObjectName,
       "tmnxSyncFailureReason": tmnxSyncFailureReason,
       "tmnxSysExecScript": tmnxSysExecScript,
       "tmnxSysExecResult": tmnxSysExecResult,
       "tmnxSysRollbackFileType": tmnxSysRollbackFileType,
       "tmnxSysFileErrorType": tmnxSysFileErrorType,
       "sysLoginControlInfo": sysLoginControlInfo,
       "slcFtpInboundMaxSessions": slcFtpInboundMaxSessions,
       "slcTelnetInboundMaxSessions": slcTelnetInboundMaxSessions,
       "slcTelnetOutboundMaxSessions": slcTelnetOutboundMaxSessions,
       "slcPreLoginMessage": slcPreLoginMessage,
       "slcPreLoginMessageInclName": slcPreLoginMessageInclName,
       "slcMessageOfTheDay": slcMessageOfTheDay,
       "slcMessageOfTheDayType": slcMessageOfTheDayType,
       "slcLoginBanner": slcLoginBanner,
       "slcLoginExponentialBackOff": slcLoginExponentialBackOff,
       "slcTelnetGracefulShutdown": slcTelnetGracefulShutdown,
       "slcSSHGracefulShutdown": slcSSHGracefulShutdown,
       "slcTelnetMinTTLValue": slcTelnetMinTTLValue,
       "slcSSHMinTTLValue": slcSSHMinTTLValue,
       "slcSSHInboundMaxSessions": slcSSHInboundMaxSessions,
       "slcSSHOutboundMaxSessions": slcSSHOutboundMaxSessions,
       "sysLACPInfo": sysLACPInfo,
       "sysLACPSystemPriority": sysLACPSystemPriority,
       "sysTacplusInfo": sysTacplusInfo,
       "tacplusOperStatus": tacplusOperStatus,
       "tacplusServerTable": tacplusServerTable,
       "tacplusServerEntry": tacplusServerEntry,
       "tacplusServerIndex": tacplusServerIndex,
       "tacplusServerAddress": tacplusServerAddress,
       "tacplusServerOperStatus": tacplusServerOperStatus,
       "tacPlusServerInetAddressType": tacPlusServerInetAddressType,
       "tacPlusServerInetAddress": tacPlusServerInetAddress,
       "sysBofInfo": sysBofInfo,
       "sbiActiveIpAddr": sbiActiveIpAddr,
       "sbiActiveIpMask": sbiActiveIpMask,
       "sbiStandbyIpAddr": sbiStandbyIpAddr,
       "sbiStandbyIpMask": sbiStandbyIpMask,
       "sbiPrimaryImage": sbiPrimaryImage,
       "sbiSecondaryImage": sbiSecondaryImage,
       "sbiTertiaryImage": sbiTertiaryImage,
       "sbiPrimaryConfigFile": sbiPrimaryConfigFile,
       "sbiSecondaryConfigFile": sbiSecondaryConfigFile,
       "sbiTertiaryConfigFile": sbiTertiaryConfigFile,
       "sbiPersist": sbiPersist,
       "sbiConsoleSpeed": sbiConsoleSpeed,
       "sbiAutoNegotiate": sbiAutoNegotiate,
       "sbiSpeed": sbiSpeed,
       "sbiDuplex": sbiDuplex,
       "sbiPrimaryDns": sbiPrimaryDns,
       "sbiSecondaryDns": sbiSecondaryDns,
       "sbiTertiaryDns": sbiTertiaryDns,
       "sbiDnsDomain": sbiDnsDomain,
       "sbiWait": sbiWait,
       "sbiStaticRouteTable": sbiStaticRouteTable,
       "sbiStaticRouteEntry": sbiStaticRouteEntry,
       "sbiStaticRouteDest": sbiStaticRouteDest,
       "sbiStaticRouteMask": sbiStaticRouteMask,
       "sbiStaticRouteNextHop": sbiStaticRouteNextHop,
       "sbiStaticRouteRowStatus": sbiStaticRouteRowStatus,
       "sbiActiveIPv6Addr": sbiActiveIPv6Addr,
       "sbiActiveIPv6PfxLen": sbiActiveIPv6PfxLen,
       "sbiStandbyIPv6Addr": sbiStandbyIPv6Addr,
       "sbiStandbyIPv6PfxLen": sbiStandbyIPv6PfxLen,
       "sbiPrimaryDnsIPv6Addr": sbiPrimaryDnsIPv6Addr,
       "sbiSecondaryDnsIPv6Addr": sbiSecondaryDnsIPv6Addr,
       "sbiTertiaryDnsIPv6Addr": sbiTertiaryDnsIPv6Addr,
       "sbiStaticRouteIPv6Table": sbiStaticRouteIPv6Table,
       "sbiStaticRouteIPv6Entry": sbiStaticRouteIPv6Entry,
       "sbiStaticRouteIPv6Dest": sbiStaticRouteIPv6Dest,
       "sbiStaticRouteIPv6PfxLen": sbiStaticRouteIPv6PfxLen,
       "sbiStaticRouteIPv6NextHop": sbiStaticRouteIPv6NextHop,
       "sbiStaticRouteIPv6RowStatus": sbiStaticRouteIPv6RowStatus,
       "sbiLiSeparate": sbiLiSeparate,
       "sbiLiLocalSave": sbiLiLocalSave,
       "sysPersistenceInfo": sysPersistenceInfo,
       "sysPersistenceDhcpL2Info": sysPersistenceDhcpL2Info,
       "spiDhcpL2PersistenceFileLocation": spiDhcpL2PersistenceFileLocation,
       "spiDhcpL2PersistenceDescription": spiDhcpL2PersistenceDescription,
       "sysPersistenceDhcpL3Info": sysPersistenceDhcpL3Info,
       "spiDhcpL3PersistenceFileLocation": spiDhcpL3PersistenceFileLocation,
       "spiDhcpL3PersistenceDescription": spiDhcpL3PersistenceDescription,
       "sysPersistenceSubMgmtInfo": sysPersistenceSubMgmtInfo,
       "spiSubMgmtPersistenceFileLocation": spiSubMgmtPersistenceFileLocation,
       "spiSubMgmtPersistenceDescription": spiSubMgmtPersistenceDescription,
       "sysPersistenceDhcpSrvInfo": sysPersistenceDhcpSrvInfo,
       "spiDhcpSrvPersistenceFileLoc": spiDhcpSrvPersistenceFileLoc,
       "spiDhcpSrvPersistenceDescr": spiDhcpSrvPersistenceDescr,
       "sysPersistenceNatInfo": sysPersistenceNatInfo,
       "spiNatFwdPersistenceFileLoc": spiNatFwdPersistenceFileLoc,
       "spiNatFwdPersistenceDescr": spiNatFwdPersistenceDescr,
       "sysPersistenceAAInfo": sysPersistenceAAInfo,
       "spiAAPersistenceFileLoc": spiAAPersistenceFileLoc,
       "spiAAPersistenceDescr": spiAAPersistenceDescr,
       "sysLiInfo": sysLiInfo,
       "sliConfigStatus": sliConfigStatus,
       "sliSaveConfig": sliSaveConfig,
       "sliSaveConfigResult": sliSaveConfigResult,
       "sliConfigLastModified": sliConfigLastModified,
       "sliConfigLastSaved": sliConfigLastSaved,
       "sliFilterLock": sliFilterLock,
       "sysDNSInfo": sysDNSInfo,
       "sysDNSInfoLastChanged": sysDNSInfoLastChanged,
       "sysDNSAddressResolvePref": sysDNSAddressResolvePref,
       "sysIcmpVSInfo": sysIcmpVSInfo,
       "sysIcmpVSEnhancement": sysIcmpVSEnhancement,
       "sysEthInfo": sysEthInfo,
       "sysNewQinqUntaggedSap": sysNewQinqUntaggedSap,
       "tmnxSysRollbackInfo": tmnxSysRollbackInfo,
       "tmnxSysRollbackIndex": tmnxSysRollbackIndex,
       "tmnxSysRollbackStart": tmnxSysRollbackStart,
       "tmnxSysRollbackResult": tmnxSysRollbackResult,
       "tmnxSysRollbackSave": tmnxSysRollbackSave,
       "tmnxSysRollbackSaveResult": tmnxSysRollbackSaveResult,
       "tmnxSysRollbackLocation": tmnxSysRollbackLocation,
       "tmnxSysRollbackRevertIndex": tmnxSysRollbackRevertIndex,
       "tmnxSysRollbackRevertEndTime": tmnxSysRollbackRevertEndTime,
       "tmnxSysRollbackSavedTime": tmnxSysRollbackSavedTime,
       "tmnxSysRollbackRevertStartTime": tmnxSysRollbackRevertStartTime,
       "tmnxSysRollbackRevertUserName": tmnxSysRollbackRevertUserName,
       "tmnxSysRollbackRevertFilename": tmnxSysRollbackRevertFilename,
       "tmnxSysRollbackSaveComment": tmnxSysRollbackSaveComment,
       "tmnxSysRollbackFileDelete": tmnxSysRollbackFileDelete,
       "tmnxSysRollbackFileDeleteResult": tmnxSysRollbackFileDeleteResult,
       "tmnxSysRollbackAbortRevert": tmnxSysRollbackAbortRevert,
       "tmnxSysRollbackRescueLocation": tmnxSysRollbackRescueLocation,
       "tmnxSysRollbackRescueRevert": tmnxSysRollbackRescueRevert,
       "tmnxSysRollbackRescueSave": tmnxSysRollbackRescueSave,
       "tmnxSysRollbackRescueDelete": tmnxSysRollbackRescueDelete,
       "tmnxSysRollbackRescueSaveRes": tmnxSysRollbackRescueSaveRes,
       "tmnxSysRollbackRescueRevertRes": tmnxSysRollbackRescueRevertRes,
       "tmnxSysRollbackRescueDeleteRes": tmnxSysRollbackRescueDeleteRes,
       "tmnxSysRollbackRescueSavedTime": tmnxSysRollbackRescueSavedTime,
       "tmnxSysRollbackRescueRevStTime": tmnxSysRollbackRescueRevStTime,
       "tmnxSysRollbackRescueRevEdTime": tmnxSysRollbackRescueRevEdTime,
       "tmnxSysRollbackRescueRevUser": tmnxSysRollbackRescueRevUser,
       "tmnxSysRollbackRescueSaveComment": tmnxSysRollbackRescueSaveComment,
       "tmnxSysRollbackRescueAbortRevert": tmnxSysRollbackRescueAbortRevert,
       "tmnxSysRollbackRescueFileExists": tmnxSysRollbackRescueFileExists,
       "tmnxSysRollbackMaxLocalFiles": tmnxSysRollbackMaxLocalFiles,
       "tmnxSysRollbackMaxRemoteFiles": tmnxSysRollbackMaxRemoteFiles,
       "tmnxSysRollbackTableLastChanged": tmnxSysRollbackTableLastChanged,
       "tmnxSysRollbackFileTable": tmnxSysRollbackFileTable,
       "tmnxSysRollbackFileEntry": tmnxSysRollbackFileEntry,
       "tmnxSysRollbackFileIndex": tmnxSysRollbackFileIndex,
       "tmnxSysRollbackFileCreationTime": tmnxSysRollbackFileCreationTime,
       "tmnxSysRollbackFileComment": tmnxSysRollbackFileComment,
       "tmnxSysRollbackFileUserName": tmnxSysRollbackFileUserName,
       "tmnxSysRollbackFileVersion": tmnxSysRollbackFileVersion,
       "sysBootedBofInfo": sysBootedBofInfo,
       "sbbiLiSeparate": sbbiLiSeparate,
       "sbbiLiLocalSave": sbbiLiLocalSave,
       "tmnxSysMIBNotifyPrefix": tmnxSysMIBNotifyPrefix,
       "tmnxSysNotifications": tmnxSysNotifications,
       "stiDateAndTimeChanged": stiDateAndTimeChanged,
       "ssiSaveConfigSucceeded": ssiSaveConfigSucceeded,
       "ssiSaveConfigFailed": ssiSaveConfigFailed,
       "sbiBootConfig": sbiBootConfig,
       "sbiBootSnmpd": sbiBootSnmpd,
       "radiusServerOperStatusChange": radiusServerOperStatusChange,
       "radiusOperStatusChange": radiusOperStatusChange,
       "tmnxConfigModify": tmnxConfigModify,
       "tmnxConfigCreate": tmnxConfigCreate,
       "tmnxConfigDelete": tmnxConfigDelete,
       "tmnxStateChange": tmnxStateChange,
       "tmnxModuleMallocFailed": tmnxModuleMallocFailed,
       "tmnxTrapDropped": tmnxTrapDropped,
       "ssiSyncConfigOK": ssiSyncConfigOK,
       "ssiSyncConfigFailed": ssiSyncConfigFailed,
       "ssiSyncBootEnvOK": ssiSyncBootEnvOK,
       "ssiSyncBootEnvFailed": ssiSyncBootEnvFailed,
       "sntpTimeDiffExceedsThreshold": sntpTimeDiffExceedsThreshold,
       "tacplusServerOperStatusChange": tacplusServerOperStatusChange,
       "tacplusOperStatusChange": tacplusOperStatusChange,
       "tmnxSnmpdError": tmnxSnmpdError,
       "tmnxSsiMismatch": tmnxSsiMismatch,
       "tmnxSnmpdStateChange": tmnxSnmpdStateChange,
       "ssiRedStandbySyncing": ssiRedStandbySyncing,
       "ssiRedStandbyReady": ssiRedStandbyReady,
       "ssiRedStandbySyncLost": ssiRedStandbySyncLost,
       "ssiRedSwitchover": ssiRedSwitchover,
       "ssiRedCpmActive": ssiRedCpmActive,
       "ssiRedSingleCpm": ssiRedSingleCpm,
       "persistencyClosedAlarmRaised": persistencyClosedAlarmRaised,
       "persistencyClosedAlarmCleared": persistencyClosedAlarmCleared,
       "tmnxSntpOperChange": tmnxSntpOperChange,
       "tmnxSysTimeSet": tmnxSysTimeSet,
       "tmnxFtpClientFailure": tmnxFtpClientFailure,
       "tacplusInetSrvrOperStatusChange": tacplusInetSrvrOperStatusChange,
       "radiusInetServerOperStatusChange": radiusInetServerOperStatusChange,
       "persistencyEventReport": persistencyEventReport,
       "sbiBootConfigFailFileError": sbiBootConfigFailFileError,
       "sbiBootConfigOKFileError": sbiBootConfigOKFileError,
       "sbiBootLiConfig": sbiBootLiConfig,
       "persistenceRestoreProblem": persistenceRestoreProblem,
       "tmnxSysRollbackStarted": tmnxSysRollbackStarted,
       "tmnxSysRollbackStatusChange": tmnxSysRollbackStatusChange,
       "tmnxSysRollbackSaveStatusChange": tmnxSysRollbackSaveStatusChange,
       "tmnxSysRollbackFileDeleteStatus": tmnxSysRollbackFileDeleteStatus,
       "ssiSyncRollbackOK": ssiSyncRollbackOK,
       "ssiSyncRollbackFailed": ssiSyncRollbackFailed,
       "ssiSyncCertOK": ssiSyncCertOK,
       "ssiSyncCertFailed": ssiSyncCertFailed,
       "persistencyFileSysThresRaised": persistencyFileSysThresRaised,
       "persistencyFileSysThresCleared": persistencyFileSysThresCleared,
       "tmnxSysExecStarted": tmnxSysExecStarted,
       "tmnxSysExecFinished": tmnxSysExecFinished,
       "tmnxSysRollbackSaveStarted": tmnxSysRollbackSaveStarted,
       "tmnxSysRollbackDeleteStarted": tmnxSysRollbackDeleteStarted,
       "tmnxSysNvsysFileError": tmnxSysNvsysFileError}
)
