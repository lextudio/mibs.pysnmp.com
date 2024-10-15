# SNMP MIB module (PERF-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PERF-STAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:24 2024
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

(alarmFallingThreshold,
 alarmIndex,
 alarmInterval,
 alarmRisingThreshold,
 alarmValue,
 alarmVariable) = mibBuilder.importSymbols(
    "RMON-MIB",
    "alarmFallingThreshold",
    "alarmIndex",
    "alarmInterval",
    "alarmRisingThreshold",
    "alarmValue",
    "alarmVariable")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

sitaraPerfMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 2, 2, 1)
)
sitaraPerfMonMIB.setRevisions(
        ("2001-06-15 14:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FilterType(Integer32, TextualConvention):
    status = "current"
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
        *(("bothPorts", 6),
          ("destinationAddr", 4),
          ("destinationPort", 5),
          ("none", 1),
          ("sourceAddr", 2),
          ("sourcePort", 3))
    )



class FilterDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )



class PolicyName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class CbqName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 10),
    )



class PolicyType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("class", 0),
          ("group", 1),
          ("link", 2))
    )



class PolicyPathName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )



class PolicyCustomerId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )



class PolicyDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )



class SitaraOwnerString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



# MIB Managed Objects in the order of their OIDs

_Sitara_ObjectIdentity = ObjectIdentity
sitara = _Sitara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302)
)
_SitaraCfg_ObjectIdentity = ObjectIdentity
sitaraCfg = _SitaraCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1)
)
_SitaraCfgPlcy_ObjectIdentity = ObjectIdentity
sitaraCfgPlcy = _SitaraCfgPlcy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1)
)
_SitaraCfgSys_ObjectIdentity = ObjectIdentity
sitaraCfgSys = _SitaraCfgSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2)
)
_SitaraCfgSysGenlObjs_ObjectIdentity = ObjectIdentity
sitaraCfgSysGenlObjs = _SitaraCfgSysGenlObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 2)
)
_SitaraCfgSysWanSpeed_Type = Unsigned32
_SitaraCfgSysWanSpeed_Object = MibScalar
sitaraCfgSysWanSpeed = _SitaraCfgSysWanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 2, 11),
    _SitaraCfgSysWanSpeed_Type()
)
sitaraCfgSysWanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sitaraCfgSysWanSpeed.setStatus("current")
_SitaraCfgSysMon_ObjectIdentity = ObjectIdentity
sitaraCfgSysMon = _SitaraCfgSysMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 6)
)


class _SitaraCfgSysMonNextIndex_Type(Integer32):
    """Custom type sitaraCfgSysMonNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SitaraCfgSysMonNextIndex_Type.__name__ = "Integer32"
_SitaraCfgSysMonNextIndex_Object = MibScalar
sitaraCfgSysMonNextIndex = _SitaraCfgSysMonNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 6, 1),
    _SitaraCfgSysMonNextIndex_Type()
)
sitaraCfgSysMonNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgSysMonNextIndex.setStatus("current")
_SitaraCfgSysMonTable_Object = MibTable
sitaraCfgSysMonTable = _SitaraCfgSysMonTable_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    sitaraCfgSysMonTable.setStatus("current")
_SitaraCfgSysMonEntry_Object = MibTableRow
sitaraCfgSysMonEntry = _SitaraCfgSysMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 6, 2, 1)
)
sitaraCfgSysMonEntry.setIndexNames(
    (0, "PERF-STAT-MIB", "sitaraCfgSysMonIndex"),
)
if mibBuilder.loadTexts:
    sitaraCfgSysMonEntry.setStatus("current")


class _SitaraCfgSysMonIndex_Type(Integer32):
    """Custom type sitaraCfgSysMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SitaraCfgSysMonIndex_Type.__name__ = "Integer32"
_SitaraCfgSysMonIndex_Object = MibTableColumn
sitaraCfgSysMonIndex = _SitaraCfgSysMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 6, 2, 1, 1),
    _SitaraCfgSysMonIndex_Type()
)
sitaraCfgSysMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sitaraCfgSysMonIndex.setStatus("current")
_SitaraCfgSysMonName_Type = DisplayString
_SitaraCfgSysMonName_Object = MibTableColumn
sitaraCfgSysMonName = _SitaraCfgSysMonName_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 6, 2, 1, 2),
    _SitaraCfgSysMonName_Type()
)
sitaraCfgSysMonName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgSysMonName.setStatus("current")
_SitaraCfgSysMonDirection_Type = FilterDirection
_SitaraCfgSysMonDirection_Object = MibTableColumn
sitaraCfgSysMonDirection = _SitaraCfgSysMonDirection_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 6, 2, 1, 3),
    _SitaraCfgSysMonDirection_Type()
)
sitaraCfgSysMonDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgSysMonDirection.setStatus("current")


class _SitaraCfgSysMonProtocol_Type(Integer32):
    """Custom type sitaraCfgSysMonProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SitaraCfgSysMonProtocol_Type.__name__ = "Integer32"
_SitaraCfgSysMonProtocol_Object = MibTableColumn
sitaraCfgSysMonProtocol = _SitaraCfgSysMonProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 6, 2, 1, 4),
    _SitaraCfgSysMonProtocol_Type()
)
sitaraCfgSysMonProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgSysMonProtocol.setStatus("current")
_SitaraCfgSysMonType_Type = FilterType
_SitaraCfgSysMonType_Object = MibTableColumn
sitaraCfgSysMonType = _SitaraCfgSysMonType_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 6, 2, 1, 5),
    _SitaraCfgSysMonType_Type()
)
sitaraCfgSysMonType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgSysMonType.setStatus("current")
_SitaraCfgSysMonIPAddr_Type = IpAddress
_SitaraCfgSysMonIPAddr_Object = MibTableColumn
sitaraCfgSysMonIPAddr = _SitaraCfgSysMonIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 6, 2, 1, 6),
    _SitaraCfgSysMonIPAddr_Type()
)
sitaraCfgSysMonIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgSysMonIPAddr.setStatus("current")
_SitaraCfgSysMonIPMask_Type = IpAddress
_SitaraCfgSysMonIPMask_Object = MibTableColumn
sitaraCfgSysMonIPMask = _SitaraCfgSysMonIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 6, 2, 1, 7),
    _SitaraCfgSysMonIPMask_Type()
)
sitaraCfgSysMonIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgSysMonIPMask.setStatus("current")


class _SitaraCfgSysMonPort_Type(Integer32):
    """Custom type sitaraCfgSysMonPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SitaraCfgSysMonPort_Type.__name__ = "Integer32"
_SitaraCfgSysMonPort_Object = MibTableColumn
sitaraCfgSysMonPort = _SitaraCfgSysMonPort_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 6, 2, 1, 8),
    _SitaraCfgSysMonPort_Type()
)
sitaraCfgSysMonPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgSysMonPort.setStatus("current")
_SitaraCfgSysMonOwner_Type = SitaraOwnerString
_SitaraCfgSysMonOwner_Object = MibTableColumn
sitaraCfgSysMonOwner = _SitaraCfgSysMonOwner_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 6, 2, 1, 9),
    _SitaraCfgSysMonOwner_Type()
)
sitaraCfgSysMonOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgSysMonOwner.setStatus("current")
_SitaraCfgSysMonRowStatus_Type = RowStatus
_SitaraCfgSysMonRowStatus_Object = MibTableColumn
sitaraCfgSysMonRowStatus = _SitaraCfgSysMonRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 6, 2, 1, 10),
    _SitaraCfgSysMonRowStatus_Type()
)
sitaraCfgSysMonRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgSysMonRowStatus.setStatus("current")


class _SitaraCfgSysMonTableStatus_Type(Integer32):
    """Custom type sitaraCfgSysMonTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("none", 3),
          ("save", 1))
    )


_SitaraCfgSysMonTableStatus_Type.__name__ = "Integer32"
_SitaraCfgSysMonTableStatus_Object = MibScalar
sitaraCfgSysMonTableStatus = _SitaraCfgSysMonTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 2, 6, 3),
    _SitaraCfgSysMonTableStatus_Type()
)
sitaraCfgSysMonTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sitaraCfgSysMonTableStatus.setStatus("current")
_SitaraPerf_ObjectIdentity = ObjectIdentity
sitaraPerf = _SitaraPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 2)
)
_SitaraPerfSys_ObjectIdentity = ObjectIdentity
sitaraPerfSys = _SitaraPerfSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 2, 2)
)


class _SitaraPerfSysCPUUsage_Type(Integer32):
    """Custom type sitaraPerfSysCPUUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SitaraPerfSysCPUUsage_Type.__name__ = "Integer32"
_SitaraPerfSysCPUUsage_Object = MibScalar
sitaraPerfSysCPUUsage = _SitaraPerfSysCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 2, 2),
    _SitaraPerfSysCPUUsage_Type()
)
sitaraPerfSysCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfSysCPUUsage.setStatus("current")


class _SitaraPerfSysMemoryUsage_Type(Integer32):
    """Custom type sitaraPerfSysMemoryUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SitaraPerfSysMemoryUsage_Type.__name__ = "Integer32"
_SitaraPerfSysMemoryUsage_Object = MibScalar
sitaraPerfSysMemoryUsage = _SitaraPerfSysMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 2, 3),
    _SitaraPerfSysMemoryUsage_Type()
)
sitaraPerfSysMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfSysMemoryUsage.setStatus("current")


class _SitaraPerfSysDiskRootUtilization_Type(Integer32):
    """Custom type sitaraPerfSysDiskRootUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SitaraPerfSysDiskRootUtilization_Type.__name__ = "Integer32"
_SitaraPerfSysDiskRootUtilization_Object = MibScalar
sitaraPerfSysDiskRootUtilization = _SitaraPerfSysDiskRootUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 2, 4),
    _SitaraPerfSysDiskRootUtilization_Type()
)
sitaraPerfSysDiskRootUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfSysDiskRootUtilization.setStatus("current")


class _SitaraPerfSysDiskSyslogUtilization_Type(Integer32):
    """Custom type sitaraPerfSysDiskSyslogUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SitaraPerfSysDiskSyslogUtilization_Type.__name__ = "Integer32"
_SitaraPerfSysDiskSyslogUtilization_Object = MibScalar
sitaraPerfSysDiskSyslogUtilization = _SitaraPerfSysDiskSyslogUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 2, 5),
    _SitaraPerfSysDiskSyslogUtilization_Type()
)
sitaraPerfSysDiskSyslogUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfSysDiskSyslogUtilization.setStatus("current")


class _SitaraPerfSysDiskCacheUtilization_Type(Integer32):
    """Custom type sitaraPerfSysDiskCacheUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SitaraPerfSysDiskCacheUtilization_Type.__name__ = "Integer32"
_SitaraPerfSysDiskCacheUtilization_Object = MibScalar
sitaraPerfSysDiskCacheUtilization = _SitaraPerfSysDiskCacheUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 2, 6),
    _SitaraPerfSysDiskCacheUtilization_Type()
)
sitaraPerfSysDiskCacheUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfSysDiskCacheUtilization.setStatus("current")


class _SitaraPerfAlarmStatus_Type(Integer32):
    """Custom type sitaraPerfAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("none", 3),
          ("save", 1))
    )


_SitaraPerfAlarmStatus_Type.__name__ = "Integer32"
_SitaraPerfAlarmStatus_Object = MibScalar
sitaraPerfAlarmStatus = _SitaraPerfAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 2, 7),
    _SitaraPerfAlarmStatus_Type()
)
sitaraPerfAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sitaraPerfAlarmStatus.setStatus("current")
_SitaraPerfSysQosDirectorIpAddr_Type = IpAddress
_SitaraPerfSysQosDirectorIpAddr_Object = MibScalar
sitaraPerfSysQosDirectorIpAddr = _SitaraPerfSysQosDirectorIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 2, 8),
    _SitaraPerfSysQosDirectorIpAddr_Type()
)
sitaraPerfSysQosDirectorIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sitaraPerfSysQosDirectorIpAddr.setStatus("current")


class _SitaraPerfSysQosDirectorPort_Type(Integer32):
    """Custom type sitaraPerfSysQosDirectorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SitaraPerfSysQosDirectorPort_Type.__name__ = "Integer32"
_SitaraPerfSysQosDirectorPort_Object = MibScalar
sitaraPerfSysQosDirectorPort = _SitaraPerfSysQosDirectorPort_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 2, 9),
    _SitaraPerfSysQosDirectorPort_Type()
)
sitaraPerfSysQosDirectorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sitaraPerfSysQosDirectorPort.setStatus("current")


class _SitaraPerfAlarmMasks_Type(OctetString):
    """Custom type sitaraPerfAlarmMasks based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_SitaraPerfAlarmMasks_Type.__name__ = "OctetString"
_SitaraPerfAlarmMasks_Object = MibScalar
sitaraPerfAlarmMasks = _SitaraPerfAlarmMasks_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 2, 10),
    _SitaraPerfAlarmMasks_Type()
)
sitaraPerfAlarmMasks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sitaraPerfAlarmMasks.setStatus("current")


class _SitaraPerfPlcyStatsCollection_Type(Integer32):
    """Custom type sitaraPerfPlcyStatsCollection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_SitaraPerfPlcyStatsCollection_Type.__name__ = "Integer32"
_SitaraPerfPlcyStatsCollection_Object = MibScalar
sitaraPerfPlcyStatsCollection = _SitaraPerfPlcyStatsCollection_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 2, 11),
    _SitaraPerfPlcyStatsCollection_Type()
)
sitaraPerfPlcyStatsCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sitaraPerfPlcyStatsCollection.setStatus("current")


class _SitaraPerfTrafStatsCollection_Type(Integer32):
    """Custom type sitaraPerfTrafStatsCollection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_SitaraPerfTrafStatsCollection_Type.__name__ = "Integer32"
_SitaraPerfTrafStatsCollection_Object = MibScalar
sitaraPerfTrafStatsCollection = _SitaraPerfTrafStatsCollection_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 2, 12),
    _SitaraPerfTrafStatsCollection_Type()
)
sitaraPerfTrafStatsCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sitaraPerfTrafStatsCollection.setStatus("current")
_SitaraPerfTraf_ObjectIdentity = ObjectIdentity
sitaraPerfTraf = _SitaraPerfTraf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 2, 3)
)
_SitaraPerfTrafTable_Object = MibTable
sitaraPerfTrafTable = _SitaraPerfTrafTable_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sitaraPerfTrafTable.setStatus("current")
_SitaraPerfTrafEntry_Object = MibTableRow
sitaraPerfTrafEntry = _SitaraPerfTrafEntry_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 3, 1, 1)
)
sitaraPerfTrafEntry.setIndexNames(
    (0, "PERF-STAT-MIB", "sitaraCfgSysMonIndex"),
)
if mibBuilder.loadTexts:
    sitaraPerfTrafEntry.setStatus("current")
_SitaraPerfTrafIndex_Type = Unsigned32
_SitaraPerfTrafIndex_Object = MibTableColumn
sitaraPerfTrafIndex = _SitaraPerfTrafIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 3, 1, 1, 1),
    _SitaraPerfTrafIndex_Type()
)
sitaraPerfTrafIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sitaraPerfTrafIndex.setStatus("current")
_SitaraPerfTrafName_Type = DisplayString
_SitaraPerfTrafName_Object = MibTableColumn
sitaraPerfTrafName = _SitaraPerfTrafName_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 3, 1, 1, 2),
    _SitaraPerfTrafName_Type()
)
sitaraPerfTrafName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraPerfTrafName.setStatus("current")
_SitaraPerfTrafTime_Type = TimeStamp
_SitaraPerfTrafTime_Object = MibTableColumn
sitaraPerfTrafTime = _SitaraPerfTrafTime_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 3, 1, 1, 3),
    _SitaraPerfTrafTime_Type()
)
sitaraPerfTrafTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfTrafTime.setStatus("current")


class _SitaraPerfTrafInterval_Type(Integer32):
    """Custom type sitaraPerfTrafInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SitaraPerfTrafInterval_Type.__name__ = "Integer32"
_SitaraPerfTrafInterval_Object = MibTableColumn
sitaraPerfTrafInterval = _SitaraPerfTrafInterval_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 3, 1, 1, 4),
    _SitaraPerfTrafInterval_Type()
)
sitaraPerfTrafInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfTrafInterval.setStatus("current")
_SitaraPerfTrafPktCnt_Type = Gauge32
_SitaraPerfTrafPktCnt_Object = MibTableColumn
sitaraPerfTrafPktCnt = _SitaraPerfTrafPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 3, 1, 1, 5),
    _SitaraPerfTrafPktCnt_Type()
)
sitaraPerfTrafPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfTrafPktCnt.setStatus("current")
_SitaraPerfTrafByteCnt_Type = Gauge32
_SitaraPerfTrafByteCnt_Object = MibTableColumn
sitaraPerfTrafByteCnt = _SitaraPerfTrafByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 3, 1, 1, 6),
    _SitaraPerfTrafByteCnt_Type()
)
sitaraPerfTrafByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfTrafByteCnt.setStatus("current")
_SitaraPerfPlcy_ObjectIdentity = ObjectIdentity
sitaraPerfPlcy = _SitaraPerfPlcy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4)
)
_SitaraPerfPlcyNextIndex_Type = Unsigned32
_SitaraPerfPlcyNextIndex_Object = MibScalar
sitaraPerfPlcyNextIndex = _SitaraPerfPlcyNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 1),
    _SitaraPerfPlcyNextIndex_Type()
)
sitaraPerfPlcyNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyNextIndex.setStatus("current")
_SitaraPerfPlcyTable_Object = MibTable
sitaraPerfPlcyTable = _SitaraPerfPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2)
)
if mibBuilder.loadTexts:
    sitaraPerfPlcyTable.setStatus("current")
_SitaraPerfPlcyEntry_Object = MibTableRow
sitaraPerfPlcyEntry = _SitaraPerfPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1)
)
sitaraPerfPlcyEntry.setIndexNames(
    (0, "PERF-STAT-MIB", "sitaraPerfPlcyIndex"),
)
if mibBuilder.loadTexts:
    sitaraPerfPlcyEntry.setStatus("current")
_SitaraPerfPlcyIndex_Type = Unsigned32
_SitaraPerfPlcyIndex_Object = MibTableColumn
sitaraPerfPlcyIndex = _SitaraPerfPlcyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 1),
    _SitaraPerfPlcyIndex_Type()
)
sitaraPerfPlcyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyIndex.setStatus("current")
_SitaraPerfPlcyTime_Type = TimeTicks
_SitaraPerfPlcyTime_Object = MibTableColumn
sitaraPerfPlcyTime = _SitaraPerfPlcyTime_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 2),
    _SitaraPerfPlcyTime_Type()
)
sitaraPerfPlcyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyTime.setStatus("obsolete")


class _SitaraPerfPlcyInterval_Type(Integer32):
    """Custom type sitaraPerfPlcyInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SitaraPerfPlcyInterval_Type.__name__ = "Integer32"
_SitaraPerfPlcyInterval_Object = MibTableColumn
sitaraPerfPlcyInterval = _SitaraPerfPlcyInterval_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 3),
    _SitaraPerfPlcyInterval_Type()
)
sitaraPerfPlcyInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyInterval.setStatus("obsolete")
_SitaraPerfPlcyAlias_Type = PolicyName
_SitaraPerfPlcyAlias_Object = MibTableColumn
sitaraPerfPlcyAlias = _SitaraPerfPlcyAlias_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 4),
    _SitaraPerfPlcyAlias_Type()
)
sitaraPerfPlcyAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyAlias.setStatus("obsolete")
_SitaraPerfPlcyType_Type = PolicyType
_SitaraPerfPlcyType_Object = MibTableColumn
sitaraPerfPlcyType = _SitaraPerfPlcyType_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 5),
    _SitaraPerfPlcyType_Type()
)
sitaraPerfPlcyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyType.setStatus("current")
_SitaraPerfPlcyLanBandWidth_Type = Gauge32
_SitaraPerfPlcyLanBandWidth_Object = MibTableColumn
sitaraPerfPlcyLanBandWidth = _SitaraPerfPlcyLanBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 6),
    _SitaraPerfPlcyLanBandWidth_Type()
)
sitaraPerfPlcyLanBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyLanBandWidth.setStatus("obsolete")
_SitaraPerfPlcyLanBurst_Type = Gauge32
_SitaraPerfPlcyLanBurst_Object = MibTableColumn
sitaraPerfPlcyLanBurst = _SitaraPerfPlcyLanBurst_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 7),
    _SitaraPerfPlcyLanBurst_Type()
)
sitaraPerfPlcyLanBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyLanBurst.setStatus("obsolete")
_SitaraPerfPlcyWanBandWidth_Type = Gauge32
_SitaraPerfPlcyWanBandWidth_Object = MibTableColumn
sitaraPerfPlcyWanBandWidth = _SitaraPerfPlcyWanBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 8),
    _SitaraPerfPlcyWanBandWidth_Type()
)
sitaraPerfPlcyWanBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyWanBandWidth.setStatus("obsolete")
_SitaraPerfPlcyWanBurst_Type = Gauge32
_SitaraPerfPlcyWanBurst_Object = MibTableColumn
sitaraPerfPlcyWanBurst = _SitaraPerfPlcyWanBurst_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 9),
    _SitaraPerfPlcyWanBurst_Type()
)
sitaraPerfPlcyWanBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyWanBurst.setStatus("obsolete")
_SitaraPerfPlcyPktCnt_Type = Counter32
_SitaraPerfPlcyPktCnt_Object = MibTableColumn
sitaraPerfPlcyPktCnt = _SitaraPerfPlcyPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 10),
    _SitaraPerfPlcyPktCnt_Type()
)
sitaraPerfPlcyPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyPktCnt.setStatus("current")
_SitaraPerfPlcyPktCntDrop_Type = Counter32
_SitaraPerfPlcyPktCntDrop_Object = MibTableColumn
sitaraPerfPlcyPktCntDrop = _SitaraPerfPlcyPktCntDrop_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 11),
    _SitaraPerfPlcyPktCntDrop_Type()
)
sitaraPerfPlcyPktCntDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyPktCntDrop.setStatus("current")
_SitaraPerfPlcyPktCntBurst_Type = Counter32
_SitaraPerfPlcyPktCntBurst_Object = MibTableColumn
sitaraPerfPlcyPktCntBurst = _SitaraPerfPlcyPktCntBurst_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 12),
    _SitaraPerfPlcyPktCntBurst_Type()
)
sitaraPerfPlcyPktCntBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyPktCntBurst.setStatus("current")
_SitaraPerfPlcyByteCnt_Type = Counter64
_SitaraPerfPlcyByteCnt_Object = MibTableColumn
sitaraPerfPlcyByteCnt = _SitaraPerfPlcyByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 13),
    _SitaraPerfPlcyByteCnt_Type()
)
sitaraPerfPlcyByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyByteCnt.setStatus("current")
_SitaraPerfPlcyByteCntDrop_Type = Counter64
_SitaraPerfPlcyByteCntDrop_Object = MibTableColumn
sitaraPerfPlcyByteCntDrop = _SitaraPerfPlcyByteCntDrop_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 14),
    _SitaraPerfPlcyByteCntDrop_Type()
)
sitaraPerfPlcyByteCntDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyByteCntDrop.setStatus("current")
_SitaraPerfPlcyQueuePkts_Type = Counter32
_SitaraPerfPlcyQueuePkts_Object = MibTableColumn
sitaraPerfPlcyQueuePkts = _SitaraPerfPlcyQueuePkts_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 15),
    _SitaraPerfPlcyQueuePkts_Type()
)
sitaraPerfPlcyQueuePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyQueuePkts.setStatus("obsolete")
_SitaraPerfPlcyHandle_Type = Unsigned32
_SitaraPerfPlcyHandle_Object = MibTableColumn
sitaraPerfPlcyHandle = _SitaraPerfPlcyHandle_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 16),
    _SitaraPerfPlcyHandle_Type()
)
sitaraPerfPlcyHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyHandle.setStatus("obsolete")
_SitaraPerfPlcyCbqName_Type = CbqName
_SitaraPerfPlcyCbqName_Object = MibTableColumn
sitaraPerfPlcyCbqName = _SitaraPerfPlcyCbqName_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 17),
    _SitaraPerfPlcyCbqName_Type()
)
sitaraPerfPlcyCbqName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyCbqName.setStatus("current")


class _SitaraPerfPlcyAvgIdleTime_Type(Integer32):
    """Custom type sitaraPerfPlcyAvgIdleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SitaraPerfPlcyAvgIdleTime_Type.__name__ = "Integer32"
_SitaraPerfPlcyAvgIdleTime_Object = MibTableColumn
sitaraPerfPlcyAvgIdleTime = _SitaraPerfPlcyAvgIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 18),
    _SitaraPerfPlcyAvgIdleTime_Type()
)
sitaraPerfPlcyAvgIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyAvgIdleTime.setStatus("obsolete")
_SitaraPerfPlcyCustomerId_Type = PolicyCustomerId
_SitaraPerfPlcyCustomerId_Object = MibTableColumn
sitaraPerfPlcyCustomerId = _SitaraPerfPlcyCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 19),
    _SitaraPerfPlcyCustomerId_Type()
)
sitaraPerfPlcyCustomerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyCustomerId.setStatus("current")
_SitaraPerfPlcyOwner_Type = SitaraOwnerString
_SitaraPerfPlcyOwner_Object = MibTableColumn
sitaraPerfPlcyOwner = _SitaraPerfPlcyOwner_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 20),
    _SitaraPerfPlcyOwner_Type()
)
sitaraPerfPlcyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyOwner.setStatus("current")
_SitaraPerfPlcyPathName_Type = PolicyPathName
_SitaraPerfPlcyPathName_Object = MibTableColumn
sitaraPerfPlcyPathName = _SitaraPerfPlcyPathName_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 21),
    _SitaraPerfPlcyPathName_Type()
)
sitaraPerfPlcyPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyPathName.setStatus("current")
_SitaraPerfPlcyDirection_Type = PolicyDirection
_SitaraPerfPlcyDirection_Object = MibTableColumn
sitaraPerfPlcyDirection = _SitaraPerfPlcyDirection_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 22),
    _SitaraPerfPlcyDirection_Type()
)
sitaraPerfPlcyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyDirection.setStatus("current")


class _SitaraPerfPlcyStatus_Type(Integer32):
    """Custom type sitaraPerfPlcyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inActive", 2))
    )


_SitaraPerfPlcyStatus_Type.__name__ = "Integer32"
_SitaraPerfPlcyStatus_Object = MibTableColumn
sitaraPerfPlcyStatus = _SitaraPerfPlcyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 23),
    _SitaraPerfPlcyStatus_Type()
)
sitaraPerfPlcyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyStatus.setStatus("current")
_SitaraPerfPlcyTimeStamp_Type = TimeTicks
_SitaraPerfPlcyTimeStamp_Object = MibTableColumn
sitaraPerfPlcyTimeStamp = _SitaraPerfPlcyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 24),
    _SitaraPerfPlcyTimeStamp_Type()
)
sitaraPerfPlcyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyTimeStamp.setStatus("current")
_SitaraPerfPlcyBandWidth_Type = Gauge32
_SitaraPerfPlcyBandWidth_Object = MibTableColumn
sitaraPerfPlcyBandWidth = _SitaraPerfPlcyBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 25),
    _SitaraPerfPlcyBandWidth_Type()
)
sitaraPerfPlcyBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyBandWidth.setStatus("current")
_SitaraPerfPlcyBurst_Type = Gauge32
_SitaraPerfPlcyBurst_Object = MibTableColumn
sitaraPerfPlcyBurst = _SitaraPerfPlcyBurst_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 26),
    _SitaraPerfPlcyBurst_Type()
)
sitaraPerfPlcyBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyBurst.setStatus("current")
_SitaraPerfPlcyByteCntBurst_Type = Counter64
_SitaraPerfPlcyByteCntBurst_Object = MibTableColumn
sitaraPerfPlcyByteCntBurst = _SitaraPerfPlcyByteCntBurst_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 27),
    _SitaraPerfPlcyByteCntBurst_Type()
)
sitaraPerfPlcyByteCntBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyByteCntBurst.setStatus("current")
_SitaraPerfPlcyAvgQueSize_Type = Counter32
_SitaraPerfPlcyAvgQueSize_Object = MibTableColumn
sitaraPerfPlcyAvgQueSize = _SitaraPerfPlcyAvgQueSize_Object(
    (1, 3, 6, 1, 4, 1, 2302, 2, 4, 2, 1, 28),
    _SitaraPerfPlcyAvgQueSize_Type()
)
sitaraPerfPlcyAvgQueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraPerfPlcyAvgQueSize.setStatus("current")
_SitaraPerfCach_ObjectIdentity = ObjectIdentity
sitaraPerfCach = _SitaraPerfCach_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 2, 5)
)
_SitaraPerfNotifns_ObjectIdentity = ObjectIdentity
sitaraPerfNotifns = _SitaraPerfNotifns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6)
)

# Managed Objects groups


# Notification objects

sitaraPerfNotifnsMemoryUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 1)
)
sitaraPerfNotifnsMemoryUtil.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("PERF-STAT-MIB", "sitaraPerfSysMemoryUsage"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsMemoryUtil.setStatus(
        "current"
    )

sitaraPerfNotifnsCPU = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 2)
)
sitaraPerfNotifnsCPU.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("PERF-STAT-MIB", "sitaraPerfSysCPUUsage"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsCPU.setStatus(
        "current"
    )

sitaraPerfNotifnsDiskCache = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 3)
)
sitaraPerfNotifnsDiskCache.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("PERF-STAT-MIB", "sitaraPerfSysDiskCacheUtilization"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsDiskCache.setStatus(
        "current"
    )

sitaraPerfNotifnsDiskSyslog = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 4)
)
sitaraPerfNotifnsDiskSyslog.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("PERF-STAT-MIB", "sitaraPerfSysDiskSyslogUtilization"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsDiskSyslog.setStatus(
        "current"
    )

sitaraPerfNotifnsDiskRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 5)
)
sitaraPerfNotifnsDiskRoot.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("PERF-STAT-MIB", "sitaraPerfSysDiskRootUtilization"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsDiskRoot.setStatus(
        "current"
    )

sitaraPerfNotifnsUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 6)
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsUpdate.setStatus(
        "current"
    )

sitaraPerfNotifnsMonitorReStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 7)
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsMonitorReStart.setStatus(
        "current"
    )

sitaraPerfNotifnsMonitorFailToReStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 8)
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsMonitorFailToReStart.setStatus(
        "current"
    )

sitaraPerfNotifnsPlcyPktCnt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 9)
)
sitaraPerfNotifnsPlcyPktCnt.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyAlias"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyType"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyLanBurst"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyWanBurst"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPktCnt"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPktCntBurst"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsPlcyPktCnt.setStatus(
        "obsolete"
    )

sitaraPerfNotifnsPlcyPktCnt2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 10)
)
sitaraPerfNotifnsPlcyPktCnt2.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyAlias"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyType"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyLanBurst"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyWanBurst"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPktCnt"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPktCntBurst"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsPlcyPktCnt2.setStatus(
        "obsolete"
    )

sitaraPerfNotifnsPlcyBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 11)
)
sitaraPerfNotifnsPlcyBurst.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyAlias"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyType"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyLanBurst"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyWanBurst"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPktCnt"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPktCntBurst"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsPlcyBurst.setStatus(
        "obsolete"
    )

sitaraPerfNotifnsPlcyBandWidth = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 12)
)
sitaraPerfNotifnsPlcyBandWidth.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyIndex"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyCustomerId"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyOwner"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPathName"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyDirection"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyType"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyBandWidth"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPktCnt"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPktCntDrop"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPktCntBurst"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyByteCnt"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyByteCntDrop"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyByteCntBurst"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyAvgQueSize"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsPlcyBandWidth.setStatus(
        "current"
    )

sitaraPerfNotifnsPacketDrops = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 13)
)
sitaraPerfNotifnsPacketDrops.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyIndex"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyCustomerId"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyOwner"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPathName"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyDirection"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyType"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyBandWidth"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPktCnt"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPktCntDrop"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPktCntBurst"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyByteCnt"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyByteCntDrop"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyByteCntBurst"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyAvgQueSize"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsPacketDrops.setStatus(
        "current"
    )

sitaraPerfNotifnsCachHitsRatio = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 14)
)
sitaraPerfNotifnsCachHitsRatio.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsCachHitsRatio.setStatus(
        "obsolete"
    )

sitaraPerfNotifnsPlcyMaxBandwidth = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 15)
)
sitaraPerfNotifnsPlcyMaxBandwidth.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyAlias"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyType"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyLanBandWidth"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyWanBandWidth"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsPlcyMaxBandwidth.setStatus(
        "obsolete"
    )

sitaraPerfNotifnsPlcyQueuePkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 16)
)
sitaraPerfNotifnsPlcyQueuePkts.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyAlias"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyCbqName"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyType"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyLanBandWidth"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyWanBandWidth"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyQueuePkts"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsPlcyQueuePkts.setStatus(
        "obsolete"
    )

sitaraPerfNotifnsPlcyMaxIdleTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 17)
)
sitaraPerfNotifnsPlcyMaxIdleTime.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyAlias"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyCbqName"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyType"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyLanBandWidth"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyWanBandWidth"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyAvgIdleTime"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsPlcyMaxIdleTime.setStatus(
        "obsolete"
    )

sitaraPerfNotifnsPlcyMinIdleTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 18)
)
sitaraPerfNotifnsPlcyMinIdleTime.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyAlias"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyCbqName"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyType"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyLanBandWidth"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyWanBandWidth"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyAvgIdleTime"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsPlcyMinIdleTime.setStatus(
        "obsolete"
    )

sitaraPerfNotifnsPlcyAveQueueLength = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 2, 6, 19)
)
sitaraPerfNotifnsPlcyAveQueueLength.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmInterval"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyIndex"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyCustomerId"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyOwner"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPathName"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyDirection"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyType"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyBandWidth"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPktCnt"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPktCntDrop"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyPktCntBurst"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyByteCnt"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyByteCntDrop"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyByteCntBurst"),
        ("PERF-STAT-MIB", "sitaraPerfPlcyAvgQueSize"))
)
if mibBuilder.loadTexts:
    sitaraPerfNotifnsPlcyAveQueueLength.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PERF-STAT-MIB",
    **{"FilterType": FilterType,
       "FilterDirection": FilterDirection,
       "PolicyName": PolicyName,
       "CbqName": CbqName,
       "PolicyType": PolicyType,
       "PolicyPathName": PolicyPathName,
       "PolicyCustomerId": PolicyCustomerId,
       "PolicyDirection": PolicyDirection,
       "SitaraOwnerString": SitaraOwnerString,
       "sitara": sitara,
       "sitaraCfg": sitaraCfg,
       "sitaraCfgPlcy": sitaraCfgPlcy,
       "sitaraCfgSys": sitaraCfgSys,
       "sitaraCfgSysGenlObjs": sitaraCfgSysGenlObjs,
       "sitaraCfgSysWanSpeed": sitaraCfgSysWanSpeed,
       "sitaraCfgSysMon": sitaraCfgSysMon,
       "sitaraCfgSysMonNextIndex": sitaraCfgSysMonNextIndex,
       "sitaraCfgSysMonTable": sitaraCfgSysMonTable,
       "sitaraCfgSysMonEntry": sitaraCfgSysMonEntry,
       "sitaraCfgSysMonIndex": sitaraCfgSysMonIndex,
       "sitaraCfgSysMonName": sitaraCfgSysMonName,
       "sitaraCfgSysMonDirection": sitaraCfgSysMonDirection,
       "sitaraCfgSysMonProtocol": sitaraCfgSysMonProtocol,
       "sitaraCfgSysMonType": sitaraCfgSysMonType,
       "sitaraCfgSysMonIPAddr": sitaraCfgSysMonIPAddr,
       "sitaraCfgSysMonIPMask": sitaraCfgSysMonIPMask,
       "sitaraCfgSysMonPort": sitaraCfgSysMonPort,
       "sitaraCfgSysMonOwner": sitaraCfgSysMonOwner,
       "sitaraCfgSysMonRowStatus": sitaraCfgSysMonRowStatus,
       "sitaraCfgSysMonTableStatus": sitaraCfgSysMonTableStatus,
       "sitaraPerf": sitaraPerf,
       "sitaraPerfSys": sitaraPerfSys,
       "sitaraPerfMonMIB": sitaraPerfMonMIB,
       "sitaraPerfSysCPUUsage": sitaraPerfSysCPUUsage,
       "sitaraPerfSysMemoryUsage": sitaraPerfSysMemoryUsage,
       "sitaraPerfSysDiskRootUtilization": sitaraPerfSysDiskRootUtilization,
       "sitaraPerfSysDiskSyslogUtilization": sitaraPerfSysDiskSyslogUtilization,
       "sitaraPerfSysDiskCacheUtilization": sitaraPerfSysDiskCacheUtilization,
       "sitaraPerfAlarmStatus": sitaraPerfAlarmStatus,
       "sitaraPerfSysQosDirectorIpAddr": sitaraPerfSysQosDirectorIpAddr,
       "sitaraPerfSysQosDirectorPort": sitaraPerfSysQosDirectorPort,
       "sitaraPerfAlarmMasks": sitaraPerfAlarmMasks,
       "sitaraPerfPlcyStatsCollection": sitaraPerfPlcyStatsCollection,
       "sitaraPerfTrafStatsCollection": sitaraPerfTrafStatsCollection,
       "sitaraPerfTraf": sitaraPerfTraf,
       "sitaraPerfTrafTable": sitaraPerfTrafTable,
       "sitaraPerfTrafEntry": sitaraPerfTrafEntry,
       "sitaraPerfTrafIndex": sitaraPerfTrafIndex,
       "sitaraPerfTrafName": sitaraPerfTrafName,
       "sitaraPerfTrafTime": sitaraPerfTrafTime,
       "sitaraPerfTrafInterval": sitaraPerfTrafInterval,
       "sitaraPerfTrafPktCnt": sitaraPerfTrafPktCnt,
       "sitaraPerfTrafByteCnt": sitaraPerfTrafByteCnt,
       "sitaraPerfPlcy": sitaraPerfPlcy,
       "sitaraPerfPlcyNextIndex": sitaraPerfPlcyNextIndex,
       "sitaraPerfPlcyTable": sitaraPerfPlcyTable,
       "sitaraPerfPlcyEntry": sitaraPerfPlcyEntry,
       "sitaraPerfPlcyIndex": sitaraPerfPlcyIndex,
       "sitaraPerfPlcyTime": sitaraPerfPlcyTime,
       "sitaraPerfPlcyInterval": sitaraPerfPlcyInterval,
       "sitaraPerfPlcyAlias": sitaraPerfPlcyAlias,
       "sitaraPerfPlcyType": sitaraPerfPlcyType,
       "sitaraPerfPlcyLanBandWidth": sitaraPerfPlcyLanBandWidth,
       "sitaraPerfPlcyLanBurst": sitaraPerfPlcyLanBurst,
       "sitaraPerfPlcyWanBandWidth": sitaraPerfPlcyWanBandWidth,
       "sitaraPerfPlcyWanBurst": sitaraPerfPlcyWanBurst,
       "sitaraPerfPlcyPktCnt": sitaraPerfPlcyPktCnt,
       "sitaraPerfPlcyPktCntDrop": sitaraPerfPlcyPktCntDrop,
       "sitaraPerfPlcyPktCntBurst": sitaraPerfPlcyPktCntBurst,
       "sitaraPerfPlcyByteCnt": sitaraPerfPlcyByteCnt,
       "sitaraPerfPlcyByteCntDrop": sitaraPerfPlcyByteCntDrop,
       "sitaraPerfPlcyQueuePkts": sitaraPerfPlcyQueuePkts,
       "sitaraPerfPlcyHandle": sitaraPerfPlcyHandle,
       "sitaraPerfPlcyCbqName": sitaraPerfPlcyCbqName,
       "sitaraPerfPlcyAvgIdleTime": sitaraPerfPlcyAvgIdleTime,
       "sitaraPerfPlcyCustomerId": sitaraPerfPlcyCustomerId,
       "sitaraPerfPlcyOwner": sitaraPerfPlcyOwner,
       "sitaraPerfPlcyPathName": sitaraPerfPlcyPathName,
       "sitaraPerfPlcyDirection": sitaraPerfPlcyDirection,
       "sitaraPerfPlcyStatus": sitaraPerfPlcyStatus,
       "sitaraPerfPlcyTimeStamp": sitaraPerfPlcyTimeStamp,
       "sitaraPerfPlcyBandWidth": sitaraPerfPlcyBandWidth,
       "sitaraPerfPlcyBurst": sitaraPerfPlcyBurst,
       "sitaraPerfPlcyByteCntBurst": sitaraPerfPlcyByteCntBurst,
       "sitaraPerfPlcyAvgQueSize": sitaraPerfPlcyAvgQueSize,
       "sitaraPerfCach": sitaraPerfCach,
       "sitaraPerfNotifns": sitaraPerfNotifns,
       "sitaraPerfNotifnsMemoryUtil": sitaraPerfNotifnsMemoryUtil,
       "sitaraPerfNotifnsCPU": sitaraPerfNotifnsCPU,
       "sitaraPerfNotifnsDiskCache": sitaraPerfNotifnsDiskCache,
       "sitaraPerfNotifnsDiskSyslog": sitaraPerfNotifnsDiskSyslog,
       "sitaraPerfNotifnsDiskRoot": sitaraPerfNotifnsDiskRoot,
       "sitaraPerfNotifnsUpdate": sitaraPerfNotifnsUpdate,
       "sitaraPerfNotifnsMonitorReStart": sitaraPerfNotifnsMonitorReStart,
       "sitaraPerfNotifnsMonitorFailToReStart": sitaraPerfNotifnsMonitorFailToReStart,
       "sitaraPerfNotifnsPlcyPktCnt": sitaraPerfNotifnsPlcyPktCnt,
       "sitaraPerfNotifnsPlcyPktCnt2": sitaraPerfNotifnsPlcyPktCnt2,
       "sitaraPerfNotifnsPlcyBurst": sitaraPerfNotifnsPlcyBurst,
       "sitaraPerfNotifnsPlcyBandWidth": sitaraPerfNotifnsPlcyBandWidth,
       "sitaraPerfNotifnsPacketDrops": sitaraPerfNotifnsPacketDrops,
       "sitaraPerfNotifnsCachHitsRatio": sitaraPerfNotifnsCachHitsRatio,
       "sitaraPerfNotifnsPlcyMaxBandwidth": sitaraPerfNotifnsPlcyMaxBandwidth,
       "sitaraPerfNotifnsPlcyQueuePkts": sitaraPerfNotifnsPlcyQueuePkts,
       "sitaraPerfNotifnsPlcyMaxIdleTime": sitaraPerfNotifnsPlcyMaxIdleTime,
       "sitaraPerfNotifnsPlcyMinIdleTime": sitaraPerfNotifnsPlcyMinIdleTime,
       "sitaraPerfNotifnsPlcyAveQueueLength": sitaraPerfNotifnsPlcyAveQueueLength}
)
