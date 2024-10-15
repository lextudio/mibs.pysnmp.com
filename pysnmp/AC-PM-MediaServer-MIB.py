# SNMP MIB module (AC-PM-MediaServer-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AC-PM-MediaServer-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:34 2024
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

(acBoardMibs,
 acGeneric,
 acPerformance,
 acProducts,
 acRegistrations,
 audioCodes) = mibBuilder.importSymbols(
    "AUDIOCODES-TYPES-MIB",
    "acBoardMibs",
    "acGeneric",
    "acPerformance",
    "acProducts",
    "acRegistrations",
    "audioCodes")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

acPMMediaServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcPMMediaServerConfiguration_ObjectIdentity = ObjectIdentity
acPMMediaServerConfiguration = _AcPMMediaServerConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 1)
)


class _AcPMMediaServerConfigurationPeriodLength_Type(Unsigned32):
    """Custom type acPMMediaServerConfigurationPeriodLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 894780),
    )


_AcPMMediaServerConfigurationPeriodLength_Type.__name__ = "Unsigned32"
_AcPMMediaServerConfigurationPeriodLength_Object = MibScalar
acPMMediaServerConfigurationPeriodLength = _AcPMMediaServerConfigurationPeriodLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 1, 1),
    _AcPMMediaServerConfigurationPeriodLength_Type()
)
acPMMediaServerConfigurationPeriodLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaServerConfigurationPeriodLength.setStatus("current")


class _AcPMMediaServerConfigurationResetTotalCounters_Type(Integer32):
    """Custom type acPMMediaServerConfigurationResetTotalCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resetCountersDone", 1),
          ("resetTotalCounters", 2))
    )


_AcPMMediaServerConfigurationResetTotalCounters_Type.__name__ = "Integer32"
_AcPMMediaServerConfigurationResetTotalCounters_Object = MibScalar
acPMMediaServerConfigurationResetTotalCounters = _AcPMMediaServerConfigurationResetTotalCounters_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 1, 2),
    _AcPMMediaServerConfigurationResetTotalCounters_Type()
)
acPMMediaServerConfigurationResetTotalCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaServerConfigurationResetTotalCounters.setStatus("current")
_AcPMMediaServerData_ObjectIdentity = ObjectIdentity
acPMMediaServerData = _AcPMMediaServerData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2)
)


class _AcPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval_Type(Unsigned32):
    """Custom type acPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval_Type.__name__ = "Unsigned32"
_AcPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval_Object = MibScalar
acPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval = _AcPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 1),
    _AcPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval_Type()
)
acPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval.setStatus("current")
_AcPMMediaServerIvr_ObjectIdentity = ObjectIdentity
acPMMediaServerIvr = _AcPMMediaServerIvr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21)
)
_AcPMIvrPlayTable_Object = MibTable
acPMIvrPlayTable = _AcPMIvrPlayTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 21)
)
if mibBuilder.loadTexts:
    acPMIvrPlayTable.setStatus("current")
_AcPMIvrPlayEntry_Object = MibTableRow
acPMIvrPlayEntry = _AcPMIvrPlayEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 21, 1)
)
acPMIvrPlayEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMIvrPlayType"),
    (0, "AC-PM-MediaServer-MIB", "acPMIvrPlayInterval"),
)
if mibBuilder.loadTexts:
    acPMIvrPlayEntry.setStatus("current")


class _AcPMIvrPlayType_Type(Integer32):
    """Custom type acPMIvrPlayType based on Integer32"""
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
        *(("failedDueToLackOfResources", 2),
          ("failedDueToProvMismatch", 3),
          ("requstes", 0),
          ("successful", 1))
    )


_AcPMIvrPlayType_Type.__name__ = "Integer32"
_AcPMIvrPlayType_Object = MibTableColumn
acPMIvrPlayType = _AcPMIvrPlayType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 21, 1, 1),
    _AcPMIvrPlayType_Type()
)
acPMIvrPlayType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrPlayType.setStatus("current")


class _AcPMIvrPlayInterval_Type(Unsigned32):
    """Custom type acPMIvrPlayInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIvrPlayInterval_Type.__name__ = "Unsigned32"
_AcPMIvrPlayInterval_Object = MibTableColumn
acPMIvrPlayInterval = _AcPMIvrPlayInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 21, 1, 2),
    _AcPMIvrPlayInterval_Type()
)
acPMIvrPlayInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrPlayInterval.setStatus("current")
_AcPMIvrPlayVal_Type = Counter32
_AcPMIvrPlayVal_Object = MibTableColumn
acPMIvrPlayVal = _AcPMIvrPlayVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 21, 1, 3),
    _AcPMIvrPlayVal_Type()
)
acPMIvrPlayVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayVal.setStatus("current")
_AcPMIvrPlayInProgressTable_Object = MibTable
acPMIvrPlayInProgressTable = _AcPMIvrPlayInProgressTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 22)
)
if mibBuilder.loadTexts:
    acPMIvrPlayInProgressTable.setStatus("current")
_AcPMIvrPlayInProgressEntry_Object = MibTableRow
acPMIvrPlayInProgressEntry = _AcPMIvrPlayInProgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 22, 1)
)
acPMIvrPlayInProgressEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMIvrPlayInProgressInterval"),
)
if mibBuilder.loadTexts:
    acPMIvrPlayInProgressEntry.setStatus("current")


class _AcPMIvrPlayInProgressInterval_Type(Unsigned32):
    """Custom type acPMIvrPlayInProgressInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIvrPlayInProgressInterval_Type.__name__ = "Unsigned32"
_AcPMIvrPlayInProgressInterval_Object = MibTableColumn
acPMIvrPlayInProgressInterval = _AcPMIvrPlayInProgressInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 22, 1, 1),
    _AcPMIvrPlayInProgressInterval_Type()
)
acPMIvrPlayInProgressInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrPlayInProgressInterval.setStatus("current")
_AcPMIvrPlayInProgressVal_Type = Gauge32
_AcPMIvrPlayInProgressVal_Object = MibTableColumn
acPMIvrPlayInProgressVal = _AcPMIvrPlayInProgressVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 22, 1, 2),
    _AcPMIvrPlayInProgressVal_Type()
)
acPMIvrPlayInProgressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayInProgressVal.setStatus("current")
_AcPMIvrPlayInProgressVolume_Type = Counter32
_AcPMIvrPlayInProgressVolume_Object = MibTableColumn
acPMIvrPlayInProgressVolume = _AcPMIvrPlayInProgressVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 22, 1, 3),
    _AcPMIvrPlayInProgressVolume_Type()
)
acPMIvrPlayInProgressVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayInProgressVolume.setStatus("current")


class _AcPMIvrPlayInProgressFullDayAverage_Type(Integer32):
    """Custom type acPMIvrPlayInProgressFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIvrPlayInProgressFullDayAverage_Type.__name__ = "Integer32"
_AcPMIvrPlayInProgressFullDayAverage_Object = MibTableColumn
acPMIvrPlayInProgressFullDayAverage = _AcPMIvrPlayInProgressFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 22, 1, 4),
    _AcPMIvrPlayInProgressFullDayAverage_Type()
)
acPMIvrPlayInProgressFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayInProgressFullDayAverage.setStatus("current")
_AcPMIvrPlayDurationTable_Object = MibTable
acPMIvrPlayDurationTable = _AcPMIvrPlayDurationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 23)
)
if mibBuilder.loadTexts:
    acPMIvrPlayDurationTable.setStatus("current")
_AcPMIvrPlayDurationEntry_Object = MibTableRow
acPMIvrPlayDurationEntry = _AcPMIvrPlayDurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 23, 1)
)
acPMIvrPlayDurationEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMIvrPlayDurationInterval"),
)
if mibBuilder.loadTexts:
    acPMIvrPlayDurationEntry.setStatus("current")


class _AcPMIvrPlayDurationInterval_Type(Unsigned32):
    """Custom type acPMIvrPlayDurationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIvrPlayDurationInterval_Type.__name__ = "Unsigned32"
_AcPMIvrPlayDurationInterval_Object = MibTableColumn
acPMIvrPlayDurationInterval = _AcPMIvrPlayDurationInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 23, 1, 1),
    _AcPMIvrPlayDurationInterval_Type()
)
acPMIvrPlayDurationInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrPlayDurationInterval.setStatus("current")
_AcPMIvrPlayDurationVal_Type = Gauge32
_AcPMIvrPlayDurationVal_Object = MibTableColumn
acPMIvrPlayDurationVal = _AcPMIvrPlayDurationVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 23, 1, 2),
    _AcPMIvrPlayDurationVal_Type()
)
acPMIvrPlayDurationVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayDurationVal.setStatus("current")
_AcPMIvrPlayDurationVolume_Type = Counter32
_AcPMIvrPlayDurationVolume_Object = MibTableColumn
acPMIvrPlayDurationVolume = _AcPMIvrPlayDurationVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 23, 1, 3),
    _AcPMIvrPlayDurationVolume_Type()
)
acPMIvrPlayDurationVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayDurationVolume.setStatus("current")


class _AcPMIvrPlayDurationAverage_Type(Integer32):
    """Custom type acPMIvrPlayDurationAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIvrPlayDurationAverage_Type.__name__ = "Integer32"
_AcPMIvrPlayDurationAverage_Object = MibTableColumn
acPMIvrPlayDurationAverage = _AcPMIvrPlayDurationAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 23, 1, 4),
    _AcPMIvrPlayDurationAverage_Type()
)
acPMIvrPlayDurationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayDurationAverage.setStatus("current")
_AcPMIvrPlayCollectTable_Object = MibTable
acPMIvrPlayCollectTable = _AcPMIvrPlayCollectTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 24)
)
if mibBuilder.loadTexts:
    acPMIvrPlayCollectTable.setStatus("current")
_AcPMIvrPlayCollectEntry_Object = MibTableRow
acPMIvrPlayCollectEntry = _AcPMIvrPlayCollectEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 24, 1)
)
acPMIvrPlayCollectEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMIvrPlayCollectType"),
    (0, "AC-PM-MediaServer-MIB", "acPMIvrPlayCollectInterval"),
)
if mibBuilder.loadTexts:
    acPMIvrPlayCollectEntry.setStatus("current")


class _AcPMIvrPlayCollectType_Type(Integer32):
    """Custom type acPMIvrPlayCollectType based on Integer32"""
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
        *(("failedDueToLackOfResources", 2),
          ("failedDueToProvMismatch", 3),
          ("requstes", 0),
          ("successful", 1))
    )


_AcPMIvrPlayCollectType_Type.__name__ = "Integer32"
_AcPMIvrPlayCollectType_Object = MibTableColumn
acPMIvrPlayCollectType = _AcPMIvrPlayCollectType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 24, 1, 1),
    _AcPMIvrPlayCollectType_Type()
)
acPMIvrPlayCollectType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrPlayCollectType.setStatus("current")


class _AcPMIvrPlayCollectInterval_Type(Unsigned32):
    """Custom type acPMIvrPlayCollectInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIvrPlayCollectInterval_Type.__name__ = "Unsigned32"
_AcPMIvrPlayCollectInterval_Object = MibTableColumn
acPMIvrPlayCollectInterval = _AcPMIvrPlayCollectInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 24, 1, 2),
    _AcPMIvrPlayCollectInterval_Type()
)
acPMIvrPlayCollectInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrPlayCollectInterval.setStatus("current")
_AcPMIvrPlayCollectVal_Type = Counter32
_AcPMIvrPlayCollectVal_Object = MibTableColumn
acPMIvrPlayCollectVal = _AcPMIvrPlayCollectVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 24, 1, 3),
    _AcPMIvrPlayCollectVal_Type()
)
acPMIvrPlayCollectVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayCollectVal.setStatus("current")
_AcPMIvrPlayCollectInProgressTable_Object = MibTable
acPMIvrPlayCollectInProgressTable = _AcPMIvrPlayCollectInProgressTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 25)
)
if mibBuilder.loadTexts:
    acPMIvrPlayCollectInProgressTable.setStatus("current")
_AcPMIvrPlayCollectInProgressEntry_Object = MibTableRow
acPMIvrPlayCollectInProgressEntry = _AcPMIvrPlayCollectInProgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 25, 1)
)
acPMIvrPlayCollectInProgressEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMIvrPlayCollectInProgressInterval"),
)
if mibBuilder.loadTexts:
    acPMIvrPlayCollectInProgressEntry.setStatus("current")


class _AcPMIvrPlayCollectInProgressInterval_Type(Unsigned32):
    """Custom type acPMIvrPlayCollectInProgressInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIvrPlayCollectInProgressInterval_Type.__name__ = "Unsigned32"
_AcPMIvrPlayCollectInProgressInterval_Object = MibTableColumn
acPMIvrPlayCollectInProgressInterval = _AcPMIvrPlayCollectInProgressInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 25, 1, 1),
    _AcPMIvrPlayCollectInProgressInterval_Type()
)
acPMIvrPlayCollectInProgressInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrPlayCollectInProgressInterval.setStatus("current")
_AcPMIvrPlayCollectInProgressVal_Type = Gauge32
_AcPMIvrPlayCollectInProgressVal_Object = MibTableColumn
acPMIvrPlayCollectInProgressVal = _AcPMIvrPlayCollectInProgressVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 25, 1, 2),
    _AcPMIvrPlayCollectInProgressVal_Type()
)
acPMIvrPlayCollectInProgressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayCollectInProgressVal.setStatus("current")
_AcPMIvrPlayCollectInProgressVolume_Type = Counter32
_AcPMIvrPlayCollectInProgressVolume_Object = MibTableColumn
acPMIvrPlayCollectInProgressVolume = _AcPMIvrPlayCollectInProgressVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 25, 1, 3),
    _AcPMIvrPlayCollectInProgressVolume_Type()
)
acPMIvrPlayCollectInProgressVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayCollectInProgressVolume.setStatus("current")


class _AcPMIvrPlayCollectInProgressFullDayAverage_Type(Integer32):
    """Custom type acPMIvrPlayCollectInProgressFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIvrPlayCollectInProgressFullDayAverage_Type.__name__ = "Integer32"
_AcPMIvrPlayCollectInProgressFullDayAverage_Object = MibTableColumn
acPMIvrPlayCollectInProgressFullDayAverage = _AcPMIvrPlayCollectInProgressFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 25, 1, 4),
    _AcPMIvrPlayCollectInProgressFullDayAverage_Type()
)
acPMIvrPlayCollectInProgressFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayCollectInProgressFullDayAverage.setStatus("current")
_AcPMIvrPlayCollectDurationTable_Object = MibTable
acPMIvrPlayCollectDurationTable = _AcPMIvrPlayCollectDurationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 26)
)
if mibBuilder.loadTexts:
    acPMIvrPlayCollectDurationTable.setStatus("current")
_AcPMIvrPlayCollectDurationEntry_Object = MibTableRow
acPMIvrPlayCollectDurationEntry = _AcPMIvrPlayCollectDurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 26, 1)
)
acPMIvrPlayCollectDurationEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMIvrPlayCollectDurationInterval"),
)
if mibBuilder.loadTexts:
    acPMIvrPlayCollectDurationEntry.setStatus("current")


class _AcPMIvrPlayCollectDurationInterval_Type(Unsigned32):
    """Custom type acPMIvrPlayCollectDurationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIvrPlayCollectDurationInterval_Type.__name__ = "Unsigned32"
_AcPMIvrPlayCollectDurationInterval_Object = MibTableColumn
acPMIvrPlayCollectDurationInterval = _AcPMIvrPlayCollectDurationInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 26, 1, 1),
    _AcPMIvrPlayCollectDurationInterval_Type()
)
acPMIvrPlayCollectDurationInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrPlayCollectDurationInterval.setStatus("current")
_AcPMIvrPlayCollectDurationVal_Type = Gauge32
_AcPMIvrPlayCollectDurationVal_Object = MibTableColumn
acPMIvrPlayCollectDurationVal = _AcPMIvrPlayCollectDurationVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 26, 1, 2),
    _AcPMIvrPlayCollectDurationVal_Type()
)
acPMIvrPlayCollectDurationVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayCollectDurationVal.setStatus("current")
_AcPMIvrPlayCollectDurationVolume_Type = Counter32
_AcPMIvrPlayCollectDurationVolume_Object = MibTableColumn
acPMIvrPlayCollectDurationVolume = _AcPMIvrPlayCollectDurationVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 26, 1, 3),
    _AcPMIvrPlayCollectDurationVolume_Type()
)
acPMIvrPlayCollectDurationVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayCollectDurationVolume.setStatus("current")


class _AcPMIvrPlayCollectDurationAverage_Type(Integer32):
    """Custom type acPMIvrPlayCollectDurationAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIvrPlayCollectDurationAverage_Type.__name__ = "Integer32"
_AcPMIvrPlayCollectDurationAverage_Object = MibTableColumn
acPMIvrPlayCollectDurationAverage = _AcPMIvrPlayCollectDurationAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 26, 1, 4),
    _AcPMIvrPlayCollectDurationAverage_Type()
)
acPMIvrPlayCollectDurationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayCollectDurationAverage.setStatus("current")
_AcPMIvrPlayRecordTable_Object = MibTable
acPMIvrPlayRecordTable = _AcPMIvrPlayRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 27)
)
if mibBuilder.loadTexts:
    acPMIvrPlayRecordTable.setStatus("current")
_AcPMIvrPlayRecordEntry_Object = MibTableRow
acPMIvrPlayRecordEntry = _AcPMIvrPlayRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 27, 1)
)
acPMIvrPlayRecordEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMIvrPlayRecordType"),
    (0, "AC-PM-MediaServer-MIB", "acPMIvrPlayRecordInterval"),
)
if mibBuilder.loadTexts:
    acPMIvrPlayRecordEntry.setStatus("current")


class _AcPMIvrPlayRecordType_Type(Integer32):
    """Custom type acPMIvrPlayRecordType based on Integer32"""
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
        *(("failedDueToLackOfResources", 2),
          ("failedDueToProvMismatch", 3),
          ("requstes", 0),
          ("successful", 1))
    )


_AcPMIvrPlayRecordType_Type.__name__ = "Integer32"
_AcPMIvrPlayRecordType_Object = MibTableColumn
acPMIvrPlayRecordType = _AcPMIvrPlayRecordType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 27, 1, 1),
    _AcPMIvrPlayRecordType_Type()
)
acPMIvrPlayRecordType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrPlayRecordType.setStatus("current")


class _AcPMIvrPlayRecordInterval_Type(Unsigned32):
    """Custom type acPMIvrPlayRecordInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIvrPlayRecordInterval_Type.__name__ = "Unsigned32"
_AcPMIvrPlayRecordInterval_Object = MibTableColumn
acPMIvrPlayRecordInterval = _AcPMIvrPlayRecordInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 27, 1, 2),
    _AcPMIvrPlayRecordInterval_Type()
)
acPMIvrPlayRecordInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrPlayRecordInterval.setStatus("current")
_AcPMIvrPlayRecordVal_Type = Counter32
_AcPMIvrPlayRecordVal_Object = MibTableColumn
acPMIvrPlayRecordVal = _AcPMIvrPlayRecordVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 27, 1, 3),
    _AcPMIvrPlayRecordVal_Type()
)
acPMIvrPlayRecordVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayRecordVal.setStatus("current")
_AcPMIvrPlayRecordInProgressTable_Object = MibTable
acPMIvrPlayRecordInProgressTable = _AcPMIvrPlayRecordInProgressTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 28)
)
if mibBuilder.loadTexts:
    acPMIvrPlayRecordInProgressTable.setStatus("current")
_AcPMIvrPlayRecordInProgressEntry_Object = MibTableRow
acPMIvrPlayRecordInProgressEntry = _AcPMIvrPlayRecordInProgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 28, 1)
)
acPMIvrPlayRecordInProgressEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMIvrPlayRecordInProgressInterval"),
)
if mibBuilder.loadTexts:
    acPMIvrPlayRecordInProgressEntry.setStatus("current")


class _AcPMIvrPlayRecordInProgressInterval_Type(Unsigned32):
    """Custom type acPMIvrPlayRecordInProgressInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIvrPlayRecordInProgressInterval_Type.__name__ = "Unsigned32"
_AcPMIvrPlayRecordInProgressInterval_Object = MibTableColumn
acPMIvrPlayRecordInProgressInterval = _AcPMIvrPlayRecordInProgressInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 28, 1, 1),
    _AcPMIvrPlayRecordInProgressInterval_Type()
)
acPMIvrPlayRecordInProgressInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrPlayRecordInProgressInterval.setStatus("current")
_AcPMIvrPlayRecordInProgressVal_Type = Gauge32
_AcPMIvrPlayRecordInProgressVal_Object = MibTableColumn
acPMIvrPlayRecordInProgressVal = _AcPMIvrPlayRecordInProgressVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 28, 1, 2),
    _AcPMIvrPlayRecordInProgressVal_Type()
)
acPMIvrPlayRecordInProgressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayRecordInProgressVal.setStatus("current")
_AcPMIvrPlayRecordInProgressVolume_Type = Counter32
_AcPMIvrPlayRecordInProgressVolume_Object = MibTableColumn
acPMIvrPlayRecordInProgressVolume = _AcPMIvrPlayRecordInProgressVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 28, 1, 3),
    _AcPMIvrPlayRecordInProgressVolume_Type()
)
acPMIvrPlayRecordInProgressVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayRecordInProgressVolume.setStatus("current")


class _AcPMIvrPlayRecordInProgressFullDayAverage_Type(Integer32):
    """Custom type acPMIvrPlayRecordInProgressFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIvrPlayRecordInProgressFullDayAverage_Type.__name__ = "Integer32"
_AcPMIvrPlayRecordInProgressFullDayAverage_Object = MibTableColumn
acPMIvrPlayRecordInProgressFullDayAverage = _AcPMIvrPlayRecordInProgressFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 28, 1, 4),
    _AcPMIvrPlayRecordInProgressFullDayAverage_Type()
)
acPMIvrPlayRecordInProgressFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayRecordInProgressFullDayAverage.setStatus("current")
_AcPMIvrPlayRecordDurationTable_Object = MibTable
acPMIvrPlayRecordDurationTable = _AcPMIvrPlayRecordDurationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 29)
)
if mibBuilder.loadTexts:
    acPMIvrPlayRecordDurationTable.setStatus("current")
_AcPMIvrPlayRecordDurationEntry_Object = MibTableRow
acPMIvrPlayRecordDurationEntry = _AcPMIvrPlayRecordDurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 29, 1)
)
acPMIvrPlayRecordDurationEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMIvrPlayRecordDurationInterval"),
)
if mibBuilder.loadTexts:
    acPMIvrPlayRecordDurationEntry.setStatus("current")


class _AcPMIvrPlayRecordDurationInterval_Type(Unsigned32):
    """Custom type acPMIvrPlayRecordDurationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIvrPlayRecordDurationInterval_Type.__name__ = "Unsigned32"
_AcPMIvrPlayRecordDurationInterval_Object = MibTableColumn
acPMIvrPlayRecordDurationInterval = _AcPMIvrPlayRecordDurationInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 29, 1, 1),
    _AcPMIvrPlayRecordDurationInterval_Type()
)
acPMIvrPlayRecordDurationInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrPlayRecordDurationInterval.setStatus("current")
_AcPMIvrPlayRecordDurationVal_Type = Gauge32
_AcPMIvrPlayRecordDurationVal_Object = MibTableColumn
acPMIvrPlayRecordDurationVal = _AcPMIvrPlayRecordDurationVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 29, 1, 2),
    _AcPMIvrPlayRecordDurationVal_Type()
)
acPMIvrPlayRecordDurationVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayRecordDurationVal.setStatus("current")
_AcPMIvrPlayRecordDurationVolume_Type = Counter32
_AcPMIvrPlayRecordDurationVolume_Object = MibTableColumn
acPMIvrPlayRecordDurationVolume = _AcPMIvrPlayRecordDurationVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 29, 1, 3),
    _AcPMIvrPlayRecordDurationVolume_Type()
)
acPMIvrPlayRecordDurationVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayRecordDurationVolume.setStatus("current")


class _AcPMIvrPlayRecordDurationAverage_Type(Integer32):
    """Custom type acPMIvrPlayRecordDurationAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIvrPlayRecordDurationAverage_Type.__name__ = "Integer32"
_AcPMIvrPlayRecordDurationAverage_Object = MibTableColumn
acPMIvrPlayRecordDurationAverage = _AcPMIvrPlayRecordDurationAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 29, 1, 4),
    _AcPMIvrPlayRecordDurationAverage_Type()
)
acPMIvrPlayRecordDurationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrPlayRecordDurationAverage.setStatus("current")
_AcPMIvrContDigitCollectTable_Object = MibTable
acPMIvrContDigitCollectTable = _AcPMIvrContDigitCollectTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 30)
)
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectTable.setStatus("current")
_AcPMIvrContDigitCollectEntry_Object = MibTableRow
acPMIvrContDigitCollectEntry = _AcPMIvrContDigitCollectEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 30, 1)
)
acPMIvrContDigitCollectEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMIvrContDigitCollectType"),
    (0, "AC-PM-MediaServer-MIB", "acPMIvrContDigitCollectInterval"),
)
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectEntry.setStatus("current")


class _AcPMIvrContDigitCollectType_Type(Integer32):
    """Custom type acPMIvrContDigitCollectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failedDueToLackOfResources", 2),
          ("requstes", 0),
          ("successful", 1))
    )


_AcPMIvrContDigitCollectType_Type.__name__ = "Integer32"
_AcPMIvrContDigitCollectType_Object = MibTableColumn
acPMIvrContDigitCollectType = _AcPMIvrContDigitCollectType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 30, 1, 1),
    _AcPMIvrContDigitCollectType_Type()
)
acPMIvrContDigitCollectType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectType.setStatus("current")


class _AcPMIvrContDigitCollectInterval_Type(Unsigned32):
    """Custom type acPMIvrContDigitCollectInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIvrContDigitCollectInterval_Type.__name__ = "Unsigned32"
_AcPMIvrContDigitCollectInterval_Object = MibTableColumn
acPMIvrContDigitCollectInterval = _AcPMIvrContDigitCollectInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 30, 1, 2),
    _AcPMIvrContDigitCollectInterval_Type()
)
acPMIvrContDigitCollectInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectInterval.setStatus("current")
_AcPMIvrContDigitCollectVal_Type = Counter32
_AcPMIvrContDigitCollectVal_Object = MibTableColumn
acPMIvrContDigitCollectVal = _AcPMIvrContDigitCollectVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 30, 1, 3),
    _AcPMIvrContDigitCollectVal_Type()
)
acPMIvrContDigitCollectVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectVal.setStatus("current")
_AcPMIvrContDigitCollectInProgressTable_Object = MibTable
acPMIvrContDigitCollectInProgressTable = _AcPMIvrContDigitCollectInProgressTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 31)
)
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectInProgressTable.setStatus("current")
_AcPMIvrContDigitCollectInProgressEntry_Object = MibTableRow
acPMIvrContDigitCollectInProgressEntry = _AcPMIvrContDigitCollectInProgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 31, 1)
)
acPMIvrContDigitCollectInProgressEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMIvrContDigitCollectInProgressInterval"),
)
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectInProgressEntry.setStatus("current")


class _AcPMIvrContDigitCollectInProgressInterval_Type(Unsigned32):
    """Custom type acPMIvrContDigitCollectInProgressInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIvrContDigitCollectInProgressInterval_Type.__name__ = "Unsigned32"
_AcPMIvrContDigitCollectInProgressInterval_Object = MibTableColumn
acPMIvrContDigitCollectInProgressInterval = _AcPMIvrContDigitCollectInProgressInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 31, 1, 1),
    _AcPMIvrContDigitCollectInProgressInterval_Type()
)
acPMIvrContDigitCollectInProgressInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectInProgressInterval.setStatus("current")
_AcPMIvrContDigitCollectInProgressVal_Type = Gauge32
_AcPMIvrContDigitCollectInProgressVal_Object = MibTableColumn
acPMIvrContDigitCollectInProgressVal = _AcPMIvrContDigitCollectInProgressVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 31, 1, 2),
    _AcPMIvrContDigitCollectInProgressVal_Type()
)
acPMIvrContDigitCollectInProgressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectInProgressVal.setStatus("current")
_AcPMIvrContDigitCollectInProgressVolume_Type = Counter32
_AcPMIvrContDigitCollectInProgressVolume_Object = MibTableColumn
acPMIvrContDigitCollectInProgressVolume = _AcPMIvrContDigitCollectInProgressVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 31, 1, 3),
    _AcPMIvrContDigitCollectInProgressVolume_Type()
)
acPMIvrContDigitCollectInProgressVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectInProgressVolume.setStatus("current")
_AcPMIvrContDigitCollectDurationTable_Object = MibTable
acPMIvrContDigitCollectDurationTable = _AcPMIvrContDigitCollectDurationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 32)
)
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectDurationTable.setStatus("current")
_AcPMIvrContDigitCollectDurationEntry_Object = MibTableRow
acPMIvrContDigitCollectDurationEntry = _AcPMIvrContDigitCollectDurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 32, 1)
)
acPMIvrContDigitCollectDurationEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMIvrContDigitCollectDurationInterval"),
)
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectDurationEntry.setStatus("current")


class _AcPMIvrContDigitCollectDurationInterval_Type(Unsigned32):
    """Custom type acPMIvrContDigitCollectDurationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIvrContDigitCollectDurationInterval_Type.__name__ = "Unsigned32"
_AcPMIvrContDigitCollectDurationInterval_Object = MibTableColumn
acPMIvrContDigitCollectDurationInterval = _AcPMIvrContDigitCollectDurationInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 32, 1, 1),
    _AcPMIvrContDigitCollectDurationInterval_Type()
)
acPMIvrContDigitCollectDurationInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectDurationInterval.setStatus("current")
_AcPMIvrContDigitCollectDurationVal_Type = Gauge32
_AcPMIvrContDigitCollectDurationVal_Object = MibTableColumn
acPMIvrContDigitCollectDurationVal = _AcPMIvrContDigitCollectDurationVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 32, 1, 2),
    _AcPMIvrContDigitCollectDurationVal_Type()
)
acPMIvrContDigitCollectDurationVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectDurationVal.setStatus("current")
_AcPMIvrContDigitCollectDurationVolume_Type = Counter32
_AcPMIvrContDigitCollectDurationVolume_Object = MibTableColumn
acPMIvrContDigitCollectDurationVolume = _AcPMIvrContDigitCollectDurationVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 32, 1, 3),
    _AcPMIvrContDigitCollectDurationVolume_Type()
)
acPMIvrContDigitCollectDurationVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectDurationVolume.setStatus("current")


class _AcPMIvrContDigitCollectDurationAverage_Type(Integer32):
    """Custom type acPMIvrContDigitCollectDurationAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIvrContDigitCollectDurationAverage_Type.__name__ = "Integer32"
_AcPMIvrContDigitCollectDurationAverage_Object = MibTableColumn
acPMIvrContDigitCollectDurationAverage = _AcPMIvrContDigitCollectDurationAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 32, 1, 4),
    _AcPMIvrContDigitCollectDurationAverage_Type()
)
acPMIvrContDigitCollectDurationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIvrContDigitCollectDurationAverage.setStatus("current")
_AcPMMediaServerBct_ObjectIdentity = ObjectIdentity
acPMMediaServerBct = _AcPMMediaServerBct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31)
)
_AcPMBctTable_Object = MibTable
acPMBctTable = _AcPMBctTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 21)
)
if mibBuilder.loadTexts:
    acPMBctTable.setStatus("current")
_AcPMBctEntry_Object = MibTableRow
acPMBctEntry = _AcPMBctEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 21, 1)
)
acPMBctEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMBctType"),
    (0, "AC-PM-MediaServer-MIB", "acPMBctInterval"),
)
if mibBuilder.loadTexts:
    acPMBctEntry.setStatus("current")


class _AcPMBctType_Type(Integer32):
    """Custom type acPMBctType based on Integer32"""
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
        *(("failedDueToLackOfResources", 2),
          ("participants", 3),
          ("requstes", 0),
          ("successful", 1))
    )


_AcPMBctType_Type.__name__ = "Integer32"
_AcPMBctType_Object = MibTableColumn
acPMBctType = _AcPMBctType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 21, 1, 1),
    _AcPMBctType_Type()
)
acPMBctType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMBctType.setStatus("current")


class _AcPMBctInterval_Type(Unsigned32):
    """Custom type acPMBctInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMBctInterval_Type.__name__ = "Unsigned32"
_AcPMBctInterval_Object = MibTableColumn
acPMBctInterval = _AcPMBctInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 21, 1, 2),
    _AcPMBctInterval_Type()
)
acPMBctInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMBctInterval.setStatus("current")
_AcPMBctVal_Type = Counter32
_AcPMBctVal_Object = MibTableColumn
acPMBctVal = _AcPMBctVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 21, 1, 3),
    _AcPMBctVal_Type()
)
acPMBctVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMBctVal.setStatus("current")
_AcPMBctInProgressTable_Object = MibTable
acPMBctInProgressTable = _AcPMBctInProgressTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 22)
)
if mibBuilder.loadTexts:
    acPMBctInProgressTable.setStatus("current")
_AcPMBctInProgressEntry_Object = MibTableRow
acPMBctInProgressEntry = _AcPMBctInProgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 22, 1)
)
acPMBctInProgressEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMBctInProgressType"),
    (0, "AC-PM-MediaServer-MIB", "acPMBctInProgressInterval"),
)
if mibBuilder.loadTexts:
    acPMBctInProgressEntry.setStatus("current")


class _AcPMBctInProgressType_Type(Integer32):
    """Custom type acPMBctInProgressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bct", 0),
          ("participants", 1))
    )


_AcPMBctInProgressType_Type.__name__ = "Integer32"
_AcPMBctInProgressType_Object = MibTableColumn
acPMBctInProgressType = _AcPMBctInProgressType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 22, 1, 1),
    _AcPMBctInProgressType_Type()
)
acPMBctInProgressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMBctInProgressType.setStatus("current")


class _AcPMBctInProgressInterval_Type(Unsigned32):
    """Custom type acPMBctInProgressInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMBctInProgressInterval_Type.__name__ = "Unsigned32"
_AcPMBctInProgressInterval_Object = MibTableColumn
acPMBctInProgressInterval = _AcPMBctInProgressInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 22, 1, 2),
    _AcPMBctInProgressInterval_Type()
)
acPMBctInProgressInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMBctInProgressInterval.setStatus("current")
_AcPMBctInProgressVal_Type = Gauge32
_AcPMBctInProgressVal_Object = MibTableColumn
acPMBctInProgressVal = _AcPMBctInProgressVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 22, 1, 3),
    _AcPMBctInProgressVal_Type()
)
acPMBctInProgressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMBctInProgressVal.setStatus("current")
_AcPMBctInProgressVolume_Type = Counter32
_AcPMBctInProgressVolume_Object = MibTableColumn
acPMBctInProgressVolume = _AcPMBctInProgressVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 22, 1, 4),
    _AcPMBctInProgressVolume_Type()
)
acPMBctInProgressVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMBctInProgressVolume.setStatus("current")
_AcPMBctDurationTable_Object = MibTable
acPMBctDurationTable = _AcPMBctDurationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 23)
)
if mibBuilder.loadTexts:
    acPMBctDurationTable.setStatus("current")
_AcPMBctDurationEntry_Object = MibTableRow
acPMBctDurationEntry = _AcPMBctDurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 23, 1)
)
acPMBctDurationEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMBctDurationInterval"),
)
if mibBuilder.loadTexts:
    acPMBctDurationEntry.setStatus("current")


class _AcPMBctDurationInterval_Type(Unsigned32):
    """Custom type acPMBctDurationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMBctDurationInterval_Type.__name__ = "Unsigned32"
_AcPMBctDurationInterval_Object = MibTableColumn
acPMBctDurationInterval = _AcPMBctDurationInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 23, 1, 1),
    _AcPMBctDurationInterval_Type()
)
acPMBctDurationInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMBctDurationInterval.setStatus("current")
_AcPMBctDurationVal_Type = Gauge32
_AcPMBctDurationVal_Object = MibTableColumn
acPMBctDurationVal = _AcPMBctDurationVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 23, 1, 2),
    _AcPMBctDurationVal_Type()
)
acPMBctDurationVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMBctDurationVal.setStatus("current")
_AcPMBctDurationVolume_Type = Counter32
_AcPMBctDurationVolume_Object = MibTableColumn
acPMBctDurationVolume = _AcPMBctDurationVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 23, 1, 3),
    _AcPMBctDurationVolume_Type()
)
acPMBctDurationVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMBctDurationVolume.setStatus("current")


class _AcPMBctDurationAverage_Type(Integer32):
    """Custom type acPMBctDurationAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMBctDurationAverage_Type.__name__ = "Integer32"
_AcPMBctDurationAverage_Object = MibTableColumn
acPMBctDurationAverage = _AcPMBctDurationAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 23, 1, 4),
    _AcPMBctDurationAverage_Type()
)
acPMBctDurationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMBctDurationAverage.setStatus("current")
_AcPMMediaServerConference_ObjectIdentity = ObjectIdentity
acPMMediaServerConference = _AcPMMediaServerConference_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41)
)
_AcPMConfTable_Object = MibTable
acPMConfTable = _AcPMConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 21)
)
if mibBuilder.loadTexts:
    acPMConfTable.setStatus("current")
_AcPMConfEntry_Object = MibTableRow
acPMConfEntry = _AcPMConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 21, 1)
)
acPMConfEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMConfType"),
    (0, "AC-PM-MediaServer-MIB", "acPMConfInterval"),
)
if mibBuilder.loadTexts:
    acPMConfEntry.setStatus("current")


class _AcPMConfType_Type(Integer32):
    """Custom type acPMConfType based on Integer32"""
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
        *(("failedDueToLackOfResources", 2),
          ("participants", 3),
          ("requstes", 0),
          ("successful", 1))
    )


_AcPMConfType_Type.__name__ = "Integer32"
_AcPMConfType_Object = MibTableColumn
acPMConfType = _AcPMConfType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 21, 1, 1),
    _AcPMConfType_Type()
)
acPMConfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMConfType.setStatus("current")


class _AcPMConfInterval_Type(Unsigned32):
    """Custom type acPMConfInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMConfInterval_Type.__name__ = "Unsigned32"
_AcPMConfInterval_Object = MibTableColumn
acPMConfInterval = _AcPMConfInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 21, 1, 2),
    _AcPMConfInterval_Type()
)
acPMConfInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMConfInterval.setStatus("current")
_AcPMConfVal_Type = Counter32
_AcPMConfVal_Object = MibTableColumn
acPMConfVal = _AcPMConfVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 21, 1, 3),
    _AcPMConfVal_Type()
)
acPMConfVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMConfVal.setStatus("current")
_AcPMConfInProgressTable_Object = MibTable
acPMConfInProgressTable = _AcPMConfInProgressTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 22)
)
if mibBuilder.loadTexts:
    acPMConfInProgressTable.setStatus("current")
_AcPMConfInProgressEntry_Object = MibTableRow
acPMConfInProgressEntry = _AcPMConfInProgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 22, 1)
)
acPMConfInProgressEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMConfInProgressType"),
    (0, "AC-PM-MediaServer-MIB", "acPMConfInProgressInterval"),
)
if mibBuilder.loadTexts:
    acPMConfInProgressEntry.setStatus("current")


class _AcPMConfInProgressType_Type(Integer32):
    """Custom type acPMConfInProgressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("conference", 0),
          ("participants", 1))
    )


_AcPMConfInProgressType_Type.__name__ = "Integer32"
_AcPMConfInProgressType_Object = MibTableColumn
acPMConfInProgressType = _AcPMConfInProgressType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 22, 1, 1),
    _AcPMConfInProgressType_Type()
)
acPMConfInProgressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMConfInProgressType.setStatus("current")


class _AcPMConfInProgressInterval_Type(Unsigned32):
    """Custom type acPMConfInProgressInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMConfInProgressInterval_Type.__name__ = "Unsigned32"
_AcPMConfInProgressInterval_Object = MibTableColumn
acPMConfInProgressInterval = _AcPMConfInProgressInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 22, 1, 2),
    _AcPMConfInProgressInterval_Type()
)
acPMConfInProgressInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMConfInProgressInterval.setStatus("current")
_AcPMConfInProgressVal_Type = Gauge32
_AcPMConfInProgressVal_Object = MibTableColumn
acPMConfInProgressVal = _AcPMConfInProgressVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 22, 1, 3),
    _AcPMConfInProgressVal_Type()
)
acPMConfInProgressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMConfInProgressVal.setStatus("current")
_AcPMConfInProgressVolume_Type = Counter32
_AcPMConfInProgressVolume_Object = MibTableColumn
acPMConfInProgressVolume = _AcPMConfInProgressVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 22, 1, 4),
    _AcPMConfInProgressVolume_Type()
)
acPMConfInProgressVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMConfInProgressVolume.setStatus("current")
_AcPMConfDurationTable_Object = MibTable
acPMConfDurationTable = _AcPMConfDurationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 23)
)
if mibBuilder.loadTexts:
    acPMConfDurationTable.setStatus("current")
_AcPMConfDurationEntry_Object = MibTableRow
acPMConfDurationEntry = _AcPMConfDurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 23, 1)
)
acPMConfDurationEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMConfDurationInterval"),
)
if mibBuilder.loadTexts:
    acPMConfDurationEntry.setStatus("current")


class _AcPMConfDurationInterval_Type(Unsigned32):
    """Custom type acPMConfDurationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMConfDurationInterval_Type.__name__ = "Unsigned32"
_AcPMConfDurationInterval_Object = MibTableColumn
acPMConfDurationInterval = _AcPMConfDurationInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 23, 1, 1),
    _AcPMConfDurationInterval_Type()
)
acPMConfDurationInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMConfDurationInterval.setStatus("current")
_AcPMConfDurationVal_Type = Gauge32
_AcPMConfDurationVal_Object = MibTableColumn
acPMConfDurationVal = _AcPMConfDurationVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 23, 1, 2),
    _AcPMConfDurationVal_Type()
)
acPMConfDurationVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMConfDurationVal.setStatus("current")
_AcPMConfDurationVolume_Type = Counter32
_AcPMConfDurationVolume_Object = MibTableColumn
acPMConfDurationVolume = _AcPMConfDurationVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 23, 1, 3),
    _AcPMConfDurationVolume_Type()
)
acPMConfDurationVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMConfDurationVolume.setStatus("current")


class _AcPMConfDurationAverage_Type(Integer32):
    """Custom type acPMConfDurationAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMConfDurationAverage_Type.__name__ = "Integer32"
_AcPMConfDurationAverage_Object = MibTableColumn
acPMConfDurationAverage = _AcPMConfDurationAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 23, 1, 4),
    _AcPMConfDurationAverage_Type()
)
acPMConfDurationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMConfDurationAverage.setStatus("current")
_AcPMMediaServerTrunkTest_ObjectIdentity = ObjectIdentity
acPMMediaServerTrunkTest = _AcPMMediaServerTrunkTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51)
)
_AcPMTrunkTestTable_Object = MibTable
acPMTrunkTestTable = _AcPMTrunkTestTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 21)
)
if mibBuilder.loadTexts:
    acPMTrunkTestTable.setStatus("current")
_AcPMTrunkTestEntry_Object = MibTableRow
acPMTrunkTestEntry = _AcPMTrunkTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 21, 1)
)
acPMTrunkTestEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMTrunkTestType"),
    (0, "AC-PM-MediaServer-MIB", "acPMTrunkTestInterval"),
)
if mibBuilder.loadTexts:
    acPMTrunkTestEntry.setStatus("current")


class _AcPMTrunkTestType_Type(Integer32):
    """Custom type acPMTrunkTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failedDueToLackOfResources", 2),
          ("requstes", 0),
          ("successful", 1))
    )


_AcPMTrunkTestType_Type.__name__ = "Integer32"
_AcPMTrunkTestType_Object = MibTableColumn
acPMTrunkTestType = _AcPMTrunkTestType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 21, 1, 1),
    _AcPMTrunkTestType_Type()
)
acPMTrunkTestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMTrunkTestType.setStatus("current")


class _AcPMTrunkTestInterval_Type(Unsigned32):
    """Custom type acPMTrunkTestInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMTrunkTestInterval_Type.__name__ = "Unsigned32"
_AcPMTrunkTestInterval_Object = MibTableColumn
acPMTrunkTestInterval = _AcPMTrunkTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 21, 1, 2),
    _AcPMTrunkTestInterval_Type()
)
acPMTrunkTestInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMTrunkTestInterval.setStatus("current")
_AcPMTrunkTestVal_Type = Counter32
_AcPMTrunkTestVal_Object = MibTableColumn
acPMTrunkTestVal = _AcPMTrunkTestVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 21, 1, 3),
    _AcPMTrunkTestVal_Type()
)
acPMTrunkTestVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkTestVal.setStatus("current")
_AcPMTrunkTestInProgressTable_Object = MibTable
acPMTrunkTestInProgressTable = _AcPMTrunkTestInProgressTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 22)
)
if mibBuilder.loadTexts:
    acPMTrunkTestInProgressTable.setStatus("current")
_AcPMTrunkTestInProgressEntry_Object = MibTableRow
acPMTrunkTestInProgressEntry = _AcPMTrunkTestInProgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 22, 1)
)
acPMTrunkTestInProgressEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMTrunkTestInProgressInterval"),
)
if mibBuilder.loadTexts:
    acPMTrunkTestInProgressEntry.setStatus("current")


class _AcPMTrunkTestInProgressInterval_Type(Unsigned32):
    """Custom type acPMTrunkTestInProgressInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMTrunkTestInProgressInterval_Type.__name__ = "Unsigned32"
_AcPMTrunkTestInProgressInterval_Object = MibTableColumn
acPMTrunkTestInProgressInterval = _AcPMTrunkTestInProgressInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 22, 1, 1),
    _AcPMTrunkTestInProgressInterval_Type()
)
acPMTrunkTestInProgressInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMTrunkTestInProgressInterval.setStatus("current")
_AcPMTrunkTestInProgressVal_Type = Gauge32
_AcPMTrunkTestInProgressVal_Object = MibTableColumn
acPMTrunkTestInProgressVal = _AcPMTrunkTestInProgressVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 22, 1, 2),
    _AcPMTrunkTestInProgressVal_Type()
)
acPMTrunkTestInProgressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkTestInProgressVal.setStatus("current")
_AcPMTrunkTestInProgressVolume_Type = Counter32
_AcPMTrunkTestInProgressVolume_Object = MibTableColumn
acPMTrunkTestInProgressVolume = _AcPMTrunkTestInProgressVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 22, 1, 3),
    _AcPMTrunkTestInProgressVolume_Type()
)
acPMTrunkTestInProgressVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkTestInProgressVolume.setStatus("current")
_AcPMTrunkTestDurationTable_Object = MibTable
acPMTrunkTestDurationTable = _AcPMTrunkTestDurationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 23)
)
if mibBuilder.loadTexts:
    acPMTrunkTestDurationTable.setStatus("current")
_AcPMTrunkTestDurationEntry_Object = MibTableRow
acPMTrunkTestDurationEntry = _AcPMTrunkTestDurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 23, 1)
)
acPMTrunkTestDurationEntry.setIndexNames(
    (0, "AC-PM-MediaServer-MIB", "acPMTrunkTestDurationInterval"),
)
if mibBuilder.loadTexts:
    acPMTrunkTestDurationEntry.setStatus("current")


class _AcPMTrunkTestDurationInterval_Type(Unsigned32):
    """Custom type acPMTrunkTestDurationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMTrunkTestDurationInterval_Type.__name__ = "Unsigned32"
_AcPMTrunkTestDurationInterval_Object = MibTableColumn
acPMTrunkTestDurationInterval = _AcPMTrunkTestDurationInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 23, 1, 1),
    _AcPMTrunkTestDurationInterval_Type()
)
acPMTrunkTestDurationInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMTrunkTestDurationInterval.setStatus("current")
_AcPMTrunkTestDurationVal_Type = Gauge32
_AcPMTrunkTestDurationVal_Object = MibTableColumn
acPMTrunkTestDurationVal = _AcPMTrunkTestDurationVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 23, 1, 2),
    _AcPMTrunkTestDurationVal_Type()
)
acPMTrunkTestDurationVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkTestDurationVal.setStatus("current")
_AcPMTrunkTestDurationVolume_Type = Counter32
_AcPMTrunkTestDurationVolume_Object = MibTableColumn
acPMTrunkTestDurationVolume = _AcPMTrunkTestDurationVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 23, 1, 3),
    _AcPMTrunkTestDurationVolume_Type()
)
acPMTrunkTestDurationVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkTestDurationVolume.setStatus("current")


class _AcPMTrunkTestDurationAverage_Type(Integer32):
    """Custom type acPMTrunkTestDurationAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTrunkTestDurationAverage_Type.__name__ = "Integer32"
_AcPMTrunkTestDurationAverage_Object = MibTableColumn
acPMTrunkTestDurationAverage = _AcPMTrunkTestDurationAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 23, 1, 4),
    _AcPMTrunkTestDurationAverage_Type()
)
acPMTrunkTestDurationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkTestDurationAverage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-PM-MediaServer-MIB",
    **{"acPMMediaServer": acPMMediaServer,
       "acPMMediaServerConfiguration": acPMMediaServerConfiguration,
       "acPMMediaServerConfigurationPeriodLength": acPMMediaServerConfigurationPeriodLength,
       "acPMMediaServerConfigurationResetTotalCounters": acPMMediaServerConfigurationResetTotalCounters,
       "acPMMediaServerData": acPMMediaServerData,
       "acPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval": acPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval,
       "acPMMediaServerIvr": acPMMediaServerIvr,
       "acPMIvrPlayTable": acPMIvrPlayTable,
       "acPMIvrPlayEntry": acPMIvrPlayEntry,
       "acPMIvrPlayType": acPMIvrPlayType,
       "acPMIvrPlayInterval": acPMIvrPlayInterval,
       "acPMIvrPlayVal": acPMIvrPlayVal,
       "acPMIvrPlayInProgressTable": acPMIvrPlayInProgressTable,
       "acPMIvrPlayInProgressEntry": acPMIvrPlayInProgressEntry,
       "acPMIvrPlayInProgressInterval": acPMIvrPlayInProgressInterval,
       "acPMIvrPlayInProgressVal": acPMIvrPlayInProgressVal,
       "acPMIvrPlayInProgressVolume": acPMIvrPlayInProgressVolume,
       "acPMIvrPlayInProgressFullDayAverage": acPMIvrPlayInProgressFullDayAverage,
       "acPMIvrPlayDurationTable": acPMIvrPlayDurationTable,
       "acPMIvrPlayDurationEntry": acPMIvrPlayDurationEntry,
       "acPMIvrPlayDurationInterval": acPMIvrPlayDurationInterval,
       "acPMIvrPlayDurationVal": acPMIvrPlayDurationVal,
       "acPMIvrPlayDurationVolume": acPMIvrPlayDurationVolume,
       "acPMIvrPlayDurationAverage": acPMIvrPlayDurationAverage,
       "acPMIvrPlayCollectTable": acPMIvrPlayCollectTable,
       "acPMIvrPlayCollectEntry": acPMIvrPlayCollectEntry,
       "acPMIvrPlayCollectType": acPMIvrPlayCollectType,
       "acPMIvrPlayCollectInterval": acPMIvrPlayCollectInterval,
       "acPMIvrPlayCollectVal": acPMIvrPlayCollectVal,
       "acPMIvrPlayCollectInProgressTable": acPMIvrPlayCollectInProgressTable,
       "acPMIvrPlayCollectInProgressEntry": acPMIvrPlayCollectInProgressEntry,
       "acPMIvrPlayCollectInProgressInterval": acPMIvrPlayCollectInProgressInterval,
       "acPMIvrPlayCollectInProgressVal": acPMIvrPlayCollectInProgressVal,
       "acPMIvrPlayCollectInProgressVolume": acPMIvrPlayCollectInProgressVolume,
       "acPMIvrPlayCollectInProgressFullDayAverage": acPMIvrPlayCollectInProgressFullDayAverage,
       "acPMIvrPlayCollectDurationTable": acPMIvrPlayCollectDurationTable,
       "acPMIvrPlayCollectDurationEntry": acPMIvrPlayCollectDurationEntry,
       "acPMIvrPlayCollectDurationInterval": acPMIvrPlayCollectDurationInterval,
       "acPMIvrPlayCollectDurationVal": acPMIvrPlayCollectDurationVal,
       "acPMIvrPlayCollectDurationVolume": acPMIvrPlayCollectDurationVolume,
       "acPMIvrPlayCollectDurationAverage": acPMIvrPlayCollectDurationAverage,
       "acPMIvrPlayRecordTable": acPMIvrPlayRecordTable,
       "acPMIvrPlayRecordEntry": acPMIvrPlayRecordEntry,
       "acPMIvrPlayRecordType": acPMIvrPlayRecordType,
       "acPMIvrPlayRecordInterval": acPMIvrPlayRecordInterval,
       "acPMIvrPlayRecordVal": acPMIvrPlayRecordVal,
       "acPMIvrPlayRecordInProgressTable": acPMIvrPlayRecordInProgressTable,
       "acPMIvrPlayRecordInProgressEntry": acPMIvrPlayRecordInProgressEntry,
       "acPMIvrPlayRecordInProgressInterval": acPMIvrPlayRecordInProgressInterval,
       "acPMIvrPlayRecordInProgressVal": acPMIvrPlayRecordInProgressVal,
       "acPMIvrPlayRecordInProgressVolume": acPMIvrPlayRecordInProgressVolume,
       "acPMIvrPlayRecordInProgressFullDayAverage": acPMIvrPlayRecordInProgressFullDayAverage,
       "acPMIvrPlayRecordDurationTable": acPMIvrPlayRecordDurationTable,
       "acPMIvrPlayRecordDurationEntry": acPMIvrPlayRecordDurationEntry,
       "acPMIvrPlayRecordDurationInterval": acPMIvrPlayRecordDurationInterval,
       "acPMIvrPlayRecordDurationVal": acPMIvrPlayRecordDurationVal,
       "acPMIvrPlayRecordDurationVolume": acPMIvrPlayRecordDurationVolume,
       "acPMIvrPlayRecordDurationAverage": acPMIvrPlayRecordDurationAverage,
       "acPMIvrContDigitCollectTable": acPMIvrContDigitCollectTable,
       "acPMIvrContDigitCollectEntry": acPMIvrContDigitCollectEntry,
       "acPMIvrContDigitCollectType": acPMIvrContDigitCollectType,
       "acPMIvrContDigitCollectInterval": acPMIvrContDigitCollectInterval,
       "acPMIvrContDigitCollectVal": acPMIvrContDigitCollectVal,
       "acPMIvrContDigitCollectInProgressTable": acPMIvrContDigitCollectInProgressTable,
       "acPMIvrContDigitCollectInProgressEntry": acPMIvrContDigitCollectInProgressEntry,
       "acPMIvrContDigitCollectInProgressInterval": acPMIvrContDigitCollectInProgressInterval,
       "acPMIvrContDigitCollectInProgressVal": acPMIvrContDigitCollectInProgressVal,
       "acPMIvrContDigitCollectInProgressVolume": acPMIvrContDigitCollectInProgressVolume,
       "acPMIvrContDigitCollectDurationTable": acPMIvrContDigitCollectDurationTable,
       "acPMIvrContDigitCollectDurationEntry": acPMIvrContDigitCollectDurationEntry,
       "acPMIvrContDigitCollectDurationInterval": acPMIvrContDigitCollectDurationInterval,
       "acPMIvrContDigitCollectDurationVal": acPMIvrContDigitCollectDurationVal,
       "acPMIvrContDigitCollectDurationVolume": acPMIvrContDigitCollectDurationVolume,
       "acPMIvrContDigitCollectDurationAverage": acPMIvrContDigitCollectDurationAverage,
       "acPMMediaServerBct": acPMMediaServerBct,
       "acPMBctTable": acPMBctTable,
       "acPMBctEntry": acPMBctEntry,
       "acPMBctType": acPMBctType,
       "acPMBctInterval": acPMBctInterval,
       "acPMBctVal": acPMBctVal,
       "acPMBctInProgressTable": acPMBctInProgressTable,
       "acPMBctInProgressEntry": acPMBctInProgressEntry,
       "acPMBctInProgressType": acPMBctInProgressType,
       "acPMBctInProgressInterval": acPMBctInProgressInterval,
       "acPMBctInProgressVal": acPMBctInProgressVal,
       "acPMBctInProgressVolume": acPMBctInProgressVolume,
       "acPMBctDurationTable": acPMBctDurationTable,
       "acPMBctDurationEntry": acPMBctDurationEntry,
       "acPMBctDurationInterval": acPMBctDurationInterval,
       "acPMBctDurationVal": acPMBctDurationVal,
       "acPMBctDurationVolume": acPMBctDurationVolume,
       "acPMBctDurationAverage": acPMBctDurationAverage,
       "acPMMediaServerConference": acPMMediaServerConference,
       "acPMConfTable": acPMConfTable,
       "acPMConfEntry": acPMConfEntry,
       "acPMConfType": acPMConfType,
       "acPMConfInterval": acPMConfInterval,
       "acPMConfVal": acPMConfVal,
       "acPMConfInProgressTable": acPMConfInProgressTable,
       "acPMConfInProgressEntry": acPMConfInProgressEntry,
       "acPMConfInProgressType": acPMConfInProgressType,
       "acPMConfInProgressInterval": acPMConfInProgressInterval,
       "acPMConfInProgressVal": acPMConfInProgressVal,
       "acPMConfInProgressVolume": acPMConfInProgressVolume,
       "acPMConfDurationTable": acPMConfDurationTable,
       "acPMConfDurationEntry": acPMConfDurationEntry,
       "acPMConfDurationInterval": acPMConfDurationInterval,
       "acPMConfDurationVal": acPMConfDurationVal,
       "acPMConfDurationVolume": acPMConfDurationVolume,
       "acPMConfDurationAverage": acPMConfDurationAverage,
       "acPMMediaServerTrunkTest": acPMMediaServerTrunkTest,
       "acPMTrunkTestTable": acPMTrunkTestTable,
       "acPMTrunkTestEntry": acPMTrunkTestEntry,
       "acPMTrunkTestType": acPMTrunkTestType,
       "acPMTrunkTestInterval": acPMTrunkTestInterval,
       "acPMTrunkTestVal": acPMTrunkTestVal,
       "acPMTrunkTestInProgressTable": acPMTrunkTestInProgressTable,
       "acPMTrunkTestInProgressEntry": acPMTrunkTestInProgressEntry,
       "acPMTrunkTestInProgressInterval": acPMTrunkTestInProgressInterval,
       "acPMTrunkTestInProgressVal": acPMTrunkTestInProgressVal,
       "acPMTrunkTestInProgressVolume": acPMTrunkTestInProgressVolume,
       "acPMTrunkTestDurationTable": acPMTrunkTestDurationTable,
       "acPMTrunkTestDurationEntry": acPMTrunkTestDurationEntry,
       "acPMTrunkTestDurationInterval": acPMTrunkTestDurationInterval,
       "acPMTrunkTestDurationVal": acPMTrunkTestDurationVal,
       "acPMTrunkTestDurationVolume": acPMTrunkTestDurationVolume,
       "acPMTrunkTestDurationAverage": acPMTrunkTestDurationAverage}
)
