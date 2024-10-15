# SNMP MIB module (CISCO-ITP-MSU-RATES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-MSU-RATES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:31 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

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

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoItpMsuRatesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 529)
)
ciscoItpMsuRatesMIB.setRevisions(
        ("2007-02-01 00:00",
         "2006-05-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CimrMsuThreshold(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 4294967295),
    )



class CimrMsuRateState(Integer32, TextualConvention):
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
        *(("acceptable", 1),
          ("overloaded", 3),
          ("warning", 2))
    )



class CirbhMsuTrafficDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receive", 1),
          ("transmit", 2))
    )



class CirbhMsuCurrentCount(Gauge32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoItpMsuRatesMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoItpMsuRatesMIBNotifs = _CiscoItpMsuRatesMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 0)
)
_CiscoItpMsuRatesMIBObjects_ObjectIdentity = ObjectIdentity
ciscoItpMsuRatesMIBObjects = _CiscoItpMsuRatesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1)
)
_CimrScalars_ObjectIdentity = ObjectIdentity
cimrScalars = _CimrScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 1)
)


class _CimrMsuRateSampleInterval_Type(Unsigned32):
    """Custom type cimrMsuRateSampleInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CimrMsuRateSampleInterval_Type.__name__ = "Unsigned32"
_CimrMsuRateSampleInterval_Object = MibScalar
cimrMsuRateSampleInterval = _CimrMsuRateSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 1, 4),
    _CimrMsuRateSampleInterval_Type()
)
cimrMsuRateSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimrMsuRateSampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuRateSampleInterval.setUnits("seconds")


class _CimrMsuRateNotifyInterval_Type(Unsigned32):
    """Custom type cimrMsuRateNotifyInterval based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 3600),
    )


_CimrMsuRateNotifyInterval_Type.__name__ = "Unsigned32"
_CimrMsuRateNotifyInterval_Object = MibScalar
cimrMsuRateNotifyInterval = _CimrMsuRateNotifyInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 1, 5),
    _CimrMsuRateNotifyInterval_Type()
)
cimrMsuRateNotifyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimrMsuRateNotifyInterval.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuRateNotifyInterval.setUnits("seconds")


class _CimrMsuRateNotifyEnable_Type(TruthValue):
    """Custom type cimrMsuRateNotifyEnable based on TruthValue"""


_CimrMsuRateNotifyEnable_Object = MibScalar
cimrMsuRateNotifyEnable = _CimrMsuRateNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 1, 6),
    _CimrMsuRateNotifyEnable_Type()
)
cimrMsuRateNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimrMsuRateNotifyEnable.setStatus("current")


class _CimrMsuRateAcceptableThreshold_Type(CimrMsuThreshold):
    """Custom type cimrMsuRateAcceptableThreshold based on CimrMsuThreshold"""
    defaultValue = 0


_CimrMsuRateAcceptableThreshold_Object = MibScalar
cimrMsuRateAcceptableThreshold = _CimrMsuRateAcceptableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 1, 7),
    _CimrMsuRateAcceptableThreshold_Type()
)
cimrMsuRateAcceptableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimrMsuRateAcceptableThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuRateAcceptableThreshold.setUnits("MSUs per second")


class _CimrMsuRateWarningThreshold_Type(CimrMsuThreshold):
    """Custom type cimrMsuRateWarningThreshold based on CimrMsuThreshold"""
    defaultValue = 0


_CimrMsuRateWarningThreshold_Object = MibScalar
cimrMsuRateWarningThreshold = _CimrMsuRateWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 1, 8),
    _CimrMsuRateWarningThreshold_Type()
)
cimrMsuRateWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimrMsuRateWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuRateWarningThreshold.setUnits("MSUs per second")


class _CimrMsuRateOverloadedThreshold_Type(CimrMsuThreshold):
    """Custom type cimrMsuRateOverloadedThreshold based on CimrMsuThreshold"""
    defaultValue = 0


_CimrMsuRateOverloadedThreshold_Object = MibScalar
cimrMsuRateOverloadedThreshold = _CimrMsuRateOverloadedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 1, 9),
    _CimrMsuRateOverloadedThreshold_Type()
)
cimrMsuRateOverloadedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimrMsuRateOverloadedThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuRateOverloadedThreshold.setUnits("MSUs per second")
_CimrTables_ObjectIdentity = ObjectIdentity
cimrTables = _CimrTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2)
)
_CimrMsuProcTable_Object = MibTable
cimrMsuProcTable = _CimrMsuProcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cimrMsuProcTable.setStatus("current")
_CimrMsuProcEntry_Object = MibTableRow
cimrMsuProcEntry = _CimrMsuProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 1, 1)
)
cimrMsuProcEntry.setIndexNames(
    (0, "CISCO-ITP-MSU-RATES-MIB", "cimrMsuProcIndex"),
)
if mibBuilder.loadTexts:
    cimrMsuProcEntry.setStatus("current")


class _CimrMsuProcIndex_Type(Unsigned32):
    """Custom type cimrMsuProcIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CimrMsuProcIndex_Type.__name__ = "Unsigned32"
_CimrMsuProcIndex_Object = MibTableColumn
cimrMsuProcIndex = _CimrMsuProcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 1, 1, 1),
    _CimrMsuProcIndex_Type()
)
cimrMsuProcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cimrMsuProcIndex.setStatus("current")
_CimrMsuProcPhysicalIndex_Type = EntPhysicalIndexOrZero
_CimrMsuProcPhysicalIndex_Object = MibTableColumn
cimrMsuProcPhysicalIndex = _CimrMsuProcPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 1, 1, 2),
    _CimrMsuProcPhysicalIndex_Type()
)
cimrMsuProcPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuProcPhysicalIndex.setStatus("current")


class _CimrMsuProcAcceptableThreshold_Type(CimrMsuThreshold):
    """Custom type cimrMsuProcAcceptableThreshold based on CimrMsuThreshold"""
    defaultValue = 0


_CimrMsuProcAcceptableThreshold_Object = MibTableColumn
cimrMsuProcAcceptableThreshold = _CimrMsuProcAcceptableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 1, 1, 3),
    _CimrMsuProcAcceptableThreshold_Type()
)
cimrMsuProcAcceptableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimrMsuProcAcceptableThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuProcAcceptableThreshold.setUnits("MSUs per second")


class _CimrMsuProcWarningThreshold_Type(CimrMsuThreshold):
    """Custom type cimrMsuProcWarningThreshold based on CimrMsuThreshold"""
    defaultValue = 0


_CimrMsuProcWarningThreshold_Object = MibTableColumn
cimrMsuProcWarningThreshold = _CimrMsuProcWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 1, 1, 4),
    _CimrMsuProcWarningThreshold_Type()
)
cimrMsuProcWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimrMsuProcWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuProcWarningThreshold.setUnits("MSUs per second")


class _CimrMsuProcOverloadedThreshold_Type(CimrMsuThreshold):
    """Custom type cimrMsuProcOverloadedThreshold based on CimrMsuThreshold"""
    defaultValue = 0


_CimrMsuProcOverloadedThreshold_Object = MibTableColumn
cimrMsuProcOverloadedThreshold = _CimrMsuProcOverloadedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 1, 1, 5),
    _CimrMsuProcOverloadedThreshold_Type()
)
cimrMsuProcOverloadedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimrMsuProcOverloadedThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuProcOverloadedThreshold.setUnits("MSUs per second")
_CimrMsuProcReset_Type = TruthValue
_CimrMsuProcReset_Object = MibTableColumn
cimrMsuProcReset = _CimrMsuProcReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 1, 1, 6),
    _CimrMsuProcReset_Type()
)
cimrMsuProcReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimrMsuProcReset.setStatus("current")
_CimrMsuProcResetTimestamp_Type = TimeStamp
_CimrMsuProcResetTimestamp_Object = MibTableColumn
cimrMsuProcResetTimestamp = _CimrMsuProcResetTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 1, 1, 7),
    _CimrMsuProcResetTimestamp_Type()
)
cimrMsuProcResetTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuProcResetTimestamp.setStatus("current")
_CimrMsuProcSlotNumber_Type = Integer32
_CimrMsuProcSlotNumber_Object = MibTableColumn
cimrMsuProcSlotNumber = _CimrMsuProcSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 1, 1, 8),
    _CimrMsuProcSlotNumber_Type()
)
cimrMsuProcSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuProcSlotNumber.setStatus("current")
_CimrMsuProcBayNumber_Type = Integer32
_CimrMsuProcBayNumber_Object = MibTableColumn
cimrMsuProcBayNumber = _CimrMsuProcBayNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 1, 1, 9),
    _CimrMsuProcBayNumber_Type()
)
cimrMsuProcBayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuProcBayNumber.setStatus("current")
_CimrMsuTrafficTable_Object = MibTable
cimrMsuTrafficTable = _CimrMsuTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cimrMsuTrafficTable.setStatus("current")
_CimrMsuTrafficEntry_Object = MibTableRow
cimrMsuTrafficEntry = _CimrMsuTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 2, 1)
)
cimrMsuTrafficEntry.setIndexNames(
    (0, "CISCO-ITP-MSU-RATES-MIB", "cimrMsuProcIndex"),
    (0, "CISCO-ITP-MSU-RATES-MIB", "cimrMsuTrafficDirection"),
)
if mibBuilder.loadTexts:
    cimrMsuTrafficEntry.setStatus("current")
_CimrMsuTrafficDirection_Type = CirbhMsuTrafficDirection
_CimrMsuTrafficDirection_Object = MibTableColumn
cimrMsuTrafficDirection = _CimrMsuTrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 2, 1, 1),
    _CimrMsuTrafficDirection_Type()
)
cimrMsuTrafficDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cimrMsuTrafficDirection.setStatus("current")
_CimrMsuTrafficRateState_Type = CimrMsuRateState
_CimrMsuTrafficRateState_Object = MibTableColumn
cimrMsuTrafficRateState = _CimrMsuTrafficRateState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 2, 1, 2),
    _CimrMsuTrafficRateState_Type()
)
cimrMsuTrafficRateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuTrafficRateState.setStatus("current")
_CimrMsuTrafficRate_Type = Gauge32
_CimrMsuTrafficRate_Object = MibTableColumn
cimrMsuTrafficRate = _CimrMsuTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 2, 1, 3),
    _CimrMsuTrafficRate_Type()
)
cimrMsuTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuTrafficRate.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuTrafficRate.setUnits("MSUs per seconds")
_CimrMsuTrafficSize_Type = Gauge32
_CimrMsuTrafficSize_Object = MibTableColumn
cimrMsuTrafficSize = _CimrMsuTrafficSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 2, 1, 4),
    _CimrMsuTrafficSize_Type()
)
cimrMsuTrafficSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuTrafficSize.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuTrafficSize.setUnits("Average bytes per MSU")
_CimrMsuTrafficDurWarning_Type = CirbhMsuCurrentCount
_CimrMsuTrafficDurWarning_Object = MibTableColumn
cimrMsuTrafficDurWarning = _CimrMsuTrafficDurWarning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 2, 1, 5),
    _CimrMsuTrafficDurWarning_Type()
)
cimrMsuTrafficDurWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuTrafficDurWarning.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuTrafficDurWarning.setUnits("seconds")
_CimrMsuTrafficDurOverloaded_Type = CirbhMsuCurrentCount
_CimrMsuTrafficDurOverloaded_Object = MibTableColumn
cimrMsuTrafficDurOverloaded = _CimrMsuTrafficDurOverloaded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 2, 1, 6),
    _CimrMsuTrafficDurOverloaded_Type()
)
cimrMsuTrafficDurOverloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuTrafficDurOverloaded.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuTrafficDurOverloaded.setUnits("seconds")
_CimrMsuTrafficMaxRate_Type = Gauge32
_CimrMsuTrafficMaxRate_Object = MibTableColumn
cimrMsuTrafficMaxRate = _CimrMsuTrafficMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 2, 1, 7),
    _CimrMsuTrafficMaxRate_Type()
)
cimrMsuTrafficMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuTrafficMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuTrafficMaxRate.setUnits("MSUs per second")
_CimrMsuTrafficMaxTimestamp_Type = TimeStamp
_CimrMsuTrafficMaxTimestamp_Object = MibTableColumn
cimrMsuTrafficMaxTimestamp = _CimrMsuTrafficMaxTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 2, 1, 8),
    _CimrMsuTrafficMaxTimestamp_Type()
)
cimrMsuTrafficMaxTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuTrafficMaxTimestamp.setStatus("current")
_CimrMsuTrafficMSUs_Type = Counter32
_CimrMsuTrafficMSUs_Object = MibTableColumn
cimrMsuTrafficMSUs = _CimrMsuTrafficMSUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 2, 1, 9),
    _CimrMsuTrafficMSUs_Type()
)
cimrMsuTrafficMSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuTrafficMSUs.setStatus("current")
_CimrMsuDistTable_Object = MibTable
cimrMsuDistTable = _CimrMsuDistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cimrMsuDistTable.setStatus("current")
_CimrMsuDistEntry_Object = MibTableRow
cimrMsuDistEntry = _CimrMsuDistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 3, 1)
)
cimrMsuDistEntry.setIndexNames(
    (0, "CISCO-ITP-MSU-RATES-MIB", "cimrMsuProcIndex"),
    (0, "CISCO-ITP-MSU-RATES-MIB", "cimrMsuTrafficDirection"),
)
if mibBuilder.loadTexts:
    cimrMsuDistEntry.setStatus("current")
_CimrMsuDist000to009Seconds_Type = CirbhMsuCurrentCount
_CimrMsuDist000to009Seconds_Object = MibTableColumn
cimrMsuDist000to009Seconds = _CimrMsuDist000to009Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 3, 1, 1),
    _CimrMsuDist000to009Seconds_Type()
)
cimrMsuDist000to009Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuDist000to009Seconds.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuDist000to009Seconds.setUnits("seconds")
_CimrMsuDist010to019Seconds_Type = CirbhMsuCurrentCount
_CimrMsuDist010to019Seconds_Object = MibTableColumn
cimrMsuDist010to019Seconds = _CimrMsuDist010to019Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 3, 1, 2),
    _CimrMsuDist010to019Seconds_Type()
)
cimrMsuDist010to019Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuDist010to019Seconds.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuDist010to019Seconds.setUnits("seconds")
_CimrMsuDist020to029Seconds_Type = CirbhMsuCurrentCount
_CimrMsuDist020to029Seconds_Object = MibTableColumn
cimrMsuDist020to029Seconds = _CimrMsuDist020to029Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 3, 1, 3),
    _CimrMsuDist020to029Seconds_Type()
)
cimrMsuDist020to029Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuDist020to029Seconds.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuDist020to029Seconds.setUnits("seconds")
_CimrMsuDist030to039Seconds_Type = CirbhMsuCurrentCount
_CimrMsuDist030to039Seconds_Object = MibTableColumn
cimrMsuDist030to039Seconds = _CimrMsuDist030to039Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 3, 1, 4),
    _CimrMsuDist030to039Seconds_Type()
)
cimrMsuDist030to039Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuDist030to039Seconds.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuDist030to039Seconds.setUnits("seconds")
_CimrMsuDist040to049Seconds_Type = CirbhMsuCurrentCount
_CimrMsuDist040to049Seconds_Object = MibTableColumn
cimrMsuDist040to049Seconds = _CimrMsuDist040to049Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 3, 1, 5),
    _CimrMsuDist040to049Seconds_Type()
)
cimrMsuDist040to049Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuDist040to049Seconds.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuDist040to049Seconds.setUnits("seconds")
_CimrMsuDist050to059Seconds_Type = CirbhMsuCurrentCount
_CimrMsuDist050to059Seconds_Object = MibTableColumn
cimrMsuDist050to059Seconds = _CimrMsuDist050to059Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 3, 1, 6),
    _CimrMsuDist050to059Seconds_Type()
)
cimrMsuDist050to059Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuDist050to059Seconds.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuDist050to059Seconds.setUnits("seconds")
_CimrMsuDist060to069Seconds_Type = CirbhMsuCurrentCount
_CimrMsuDist060to069Seconds_Object = MibTableColumn
cimrMsuDist060to069Seconds = _CimrMsuDist060to069Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 3, 1, 7),
    _CimrMsuDist060to069Seconds_Type()
)
cimrMsuDist060to069Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuDist060to069Seconds.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuDist060to069Seconds.setUnits("seconds")
_CimrMsuDist070to079Seconds_Type = CirbhMsuCurrentCount
_CimrMsuDist070to079Seconds_Object = MibTableColumn
cimrMsuDist070to079Seconds = _CimrMsuDist070to079Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 3, 1, 8),
    _CimrMsuDist070to079Seconds_Type()
)
cimrMsuDist070to079Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuDist070to079Seconds.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuDist070to079Seconds.setUnits("seconds")
_CimrMsuDist080to089Seconds_Type = CirbhMsuCurrentCount
_CimrMsuDist080to089Seconds_Object = MibTableColumn
cimrMsuDist080to089Seconds = _CimrMsuDist080to089Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 3, 1, 9),
    _CimrMsuDist080to089Seconds_Type()
)
cimrMsuDist080to089Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuDist080to089Seconds.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuDist080to089Seconds.setUnits("seconds")
_CimrMsuDist090orAbove_Type = CirbhMsuCurrentCount
_CimrMsuDist090orAbove_Object = MibTableColumn
cimrMsuDist090orAbove = _CimrMsuDist090orAbove_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 1, 2, 3, 1, 10),
    _CimrMsuDist090orAbove_Type()
)
cimrMsuDist090orAbove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimrMsuDist090orAbove.setStatus("current")
if mibBuilder.loadTexts:
    cimrMsuDist090orAbove.setUnits("seconds")
_CiscoItpMsuRatesMIBConform_ObjectIdentity = ObjectIdentity
ciscoItpMsuRatesMIBConform = _CiscoItpMsuRatesMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 2)
)
_CiscoItpMsuRatesMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoItpMsuRatesMIBCompliances = _CiscoItpMsuRatesMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 2, 1)
)
_CiscoItpMsuRatesMIBGroups_ObjectIdentity = ObjectIdentity
ciscoItpMsuRatesMIBGroups = _CiscoItpMsuRatesMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 2, 2)
)

# Managed Objects groups

ciscoItpMsuRatesScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 2, 2, 1)
)
ciscoItpMsuRatesScalarsGroup.setObjects(
      *(("CISCO-ITP-MSU-RATES-MIB", "cimrMsuRateSampleInterval"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuRateNotifyInterval"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuRateNotifyEnable"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuRateAcceptableThreshold"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuRateWarningThreshold"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuRateOverloadedThreshold"))
)
if mibBuilder.loadTexts:
    ciscoItpMsuRatesScalarsGroup.setStatus("current")

ciscoItpMsuRatesObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 2, 2, 2)
)
ciscoItpMsuRatesObjects.setObjects(
      *(("CISCO-ITP-MSU-RATES-MIB", "cimrMsuProcPhysicalIndex"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuProcAcceptableThreshold"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuProcWarningThreshold"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuProcOverloadedThreshold"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuProcReset"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuProcResetTimestamp"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuProcSlotNumber"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuProcBayNumber"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuTrafficRateState"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuTrafficRate"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuTrafficSize"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuTrafficDurWarning"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuTrafficDurOverloaded"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuTrafficMaxRate"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuTrafficMaxTimestamp"))
)
if mibBuilder.loadTexts:
    ciscoItpMsuRatesObjects.setStatus("current")

ciscoItpMsuDistObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 2, 2, 3)
)
ciscoItpMsuDistObjects.setObjects(
      *(("CISCO-ITP-MSU-RATES-MIB", "cimrMsuDist000to009Seconds"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuDist010to019Seconds"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuDist020to029Seconds"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuDist030to039Seconds"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuDist040to049Seconds"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuDist050to059Seconds"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuDist060to069Seconds"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuDist070to079Seconds"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuDist080to089Seconds"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuDist090orAbove"))
)
if mibBuilder.loadTexts:
    ciscoItpMsuDistObjects.setStatus("current")

ciscoItpMsuRatesObjectsRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 2, 2, 5)
)
ciscoItpMsuRatesObjectsRev1.setObjects(
    ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuTrafficMSUs")
)
if mibBuilder.loadTexts:
    ciscoItpMsuRatesObjectsRev1.setStatus("current")


# Notification objects

ciscoItpMsuRateState = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 0, 1)
)
ciscoItpMsuRateState.setObjects(
      *(("CISCO-ITP-MSU-RATES-MIB", "cimrMsuTrafficRateState"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuTrafficRate"),
        ("CISCO-ITP-MSU-RATES-MIB", "cimrMsuTrafficSize"))
)
if mibBuilder.loadTexts:
    ciscoItpMsuRateState.setStatus(
        "current"
    )


# Notifications groups

ciscoItpMsuRatesNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 2, 2, 4)
)
ciscoItpMsuRatesNotifyGroup.setObjects(
    ("CISCO-ITP-MSU-RATES-MIB", "ciscoItpMsuRateState")
)
if mibBuilder.loadTexts:
    ciscoItpMsuRatesNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoItpMsuRatesMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoItpMsuRatesMIBCompliance.setStatus(
        "deprecated"
    )

ciscoItpMsuRatesMIBCompliancesRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 529, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoItpMsuRatesMIBCompliancesRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-MSU-RATES-MIB",
    **{"CimrMsuThreshold": CimrMsuThreshold,
       "CimrMsuRateState": CimrMsuRateState,
       "CirbhMsuTrafficDirection": CirbhMsuTrafficDirection,
       "CirbhMsuCurrentCount": CirbhMsuCurrentCount,
       "ciscoItpMsuRatesMIB": ciscoItpMsuRatesMIB,
       "ciscoItpMsuRatesMIBNotifs": ciscoItpMsuRatesMIBNotifs,
       "ciscoItpMsuRateState": ciscoItpMsuRateState,
       "ciscoItpMsuRatesMIBObjects": ciscoItpMsuRatesMIBObjects,
       "cimrScalars": cimrScalars,
       "cimrMsuRateSampleInterval": cimrMsuRateSampleInterval,
       "cimrMsuRateNotifyInterval": cimrMsuRateNotifyInterval,
       "cimrMsuRateNotifyEnable": cimrMsuRateNotifyEnable,
       "cimrMsuRateAcceptableThreshold": cimrMsuRateAcceptableThreshold,
       "cimrMsuRateWarningThreshold": cimrMsuRateWarningThreshold,
       "cimrMsuRateOverloadedThreshold": cimrMsuRateOverloadedThreshold,
       "cimrTables": cimrTables,
       "cimrMsuProcTable": cimrMsuProcTable,
       "cimrMsuProcEntry": cimrMsuProcEntry,
       "cimrMsuProcIndex": cimrMsuProcIndex,
       "cimrMsuProcPhysicalIndex": cimrMsuProcPhysicalIndex,
       "cimrMsuProcAcceptableThreshold": cimrMsuProcAcceptableThreshold,
       "cimrMsuProcWarningThreshold": cimrMsuProcWarningThreshold,
       "cimrMsuProcOverloadedThreshold": cimrMsuProcOverloadedThreshold,
       "cimrMsuProcReset": cimrMsuProcReset,
       "cimrMsuProcResetTimestamp": cimrMsuProcResetTimestamp,
       "cimrMsuProcSlotNumber": cimrMsuProcSlotNumber,
       "cimrMsuProcBayNumber": cimrMsuProcBayNumber,
       "cimrMsuTrafficTable": cimrMsuTrafficTable,
       "cimrMsuTrafficEntry": cimrMsuTrafficEntry,
       "cimrMsuTrafficDirection": cimrMsuTrafficDirection,
       "cimrMsuTrafficRateState": cimrMsuTrafficRateState,
       "cimrMsuTrafficRate": cimrMsuTrafficRate,
       "cimrMsuTrafficSize": cimrMsuTrafficSize,
       "cimrMsuTrafficDurWarning": cimrMsuTrafficDurWarning,
       "cimrMsuTrafficDurOverloaded": cimrMsuTrafficDurOverloaded,
       "cimrMsuTrafficMaxRate": cimrMsuTrafficMaxRate,
       "cimrMsuTrafficMaxTimestamp": cimrMsuTrafficMaxTimestamp,
       "cimrMsuTrafficMSUs": cimrMsuTrafficMSUs,
       "cimrMsuDistTable": cimrMsuDistTable,
       "cimrMsuDistEntry": cimrMsuDistEntry,
       "cimrMsuDist000to009Seconds": cimrMsuDist000to009Seconds,
       "cimrMsuDist010to019Seconds": cimrMsuDist010to019Seconds,
       "cimrMsuDist020to029Seconds": cimrMsuDist020to029Seconds,
       "cimrMsuDist030to039Seconds": cimrMsuDist030to039Seconds,
       "cimrMsuDist040to049Seconds": cimrMsuDist040to049Seconds,
       "cimrMsuDist050to059Seconds": cimrMsuDist050to059Seconds,
       "cimrMsuDist060to069Seconds": cimrMsuDist060to069Seconds,
       "cimrMsuDist070to079Seconds": cimrMsuDist070to079Seconds,
       "cimrMsuDist080to089Seconds": cimrMsuDist080to089Seconds,
       "cimrMsuDist090orAbove": cimrMsuDist090orAbove,
       "ciscoItpMsuRatesMIBConform": ciscoItpMsuRatesMIBConform,
       "ciscoItpMsuRatesMIBCompliances": ciscoItpMsuRatesMIBCompliances,
       "ciscoItpMsuRatesMIBCompliance": ciscoItpMsuRatesMIBCompliance,
       "ciscoItpMsuRatesMIBCompliancesRev1": ciscoItpMsuRatesMIBCompliancesRev1,
       "ciscoItpMsuRatesMIBGroups": ciscoItpMsuRatesMIBGroups,
       "ciscoItpMsuRatesScalarsGroup": ciscoItpMsuRatesScalarsGroup,
       "ciscoItpMsuRatesObjects": ciscoItpMsuRatesObjects,
       "ciscoItpMsuDistObjects": ciscoItpMsuDistObjects,
       "ciscoItpMsuRatesNotifyGroup": ciscoItpMsuRatesNotifyGroup,
       "ciscoItpMsuRatesObjectsRev1": ciscoItpMsuRatesObjectsRev1}
)
