# SNMP MIB module (IEEE-802DOT17-RPR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE-802DOT17-RPR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:46 2024
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

(HCPerfCurrentCount,
 HCPerfIntervalCount,
 HCPerfTotalCount) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount",
    "HCPerfIntervalCount",
    "HCPerfTotalCount")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ieee802dot17rprMIB = ModuleIdentity(
    (1, 0, 8802, 17, 1, 1)
)
ieee802dot17rprMIB.setRevisions(
        ("2004-04-21 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RprSpan(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("east", 1),
          ("west", 2))
    )



class RprProtectionStatus(Bits, TextualConvention):
    status = "current"


class RprOamRinglet(Integer32, TextualConvention):
    status = "current"
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
        *(("default", 1),
          ("reverseRinglet", 4),
          ("ringlet0", 2),
          ("ringlet1", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RprObjects_ObjectIdentity = ObjectIdentity
rprObjects = _RprObjects_ObjectIdentity(
    (1, 0, 8802, 17, 1, 1, 1)
)
_RprGeneral_ObjectIdentity = ObjectIdentity
rprGeneral = _RprGeneral_ObjectIdentity(
    (1, 0, 8802, 17, 1, 1, 1, 1)
)
_RprIfTable_Object = MibTable
rprIfTable = _RprIfTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rprIfTable.setStatus("current")
_RprIfEntry_Object = MibTableRow
rprIfEntry = _RprIfEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1)
)
rprIfEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprIfIndex"),
)
if mibBuilder.loadTexts:
    rprIfEntry.setStatus("current")
_RprIfIndex_Type = InterfaceIndex
_RprIfIndex_Object = MibTableColumn
rprIfIndex = _RprIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 1),
    _RprIfIndex_Type()
)
rprIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprIfIndex.setStatus("current")


class _RprIfStationsOnRing_Type(Unsigned32):
    """Custom type rprIfStationsOnRing based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RprIfStationsOnRing_Type.__name__ = "Unsigned32"
_RprIfStationsOnRing_Object = MibTableColumn
rprIfStationsOnRing = _RprIfStationsOnRing_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 2),
    _RprIfStationsOnRing_Type()
)
rprIfStationsOnRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfStationsOnRing.setStatus("current")


class _RprIfReversionMode_Type(TruthValue):
    """Custom type rprIfReversionMode based on TruthValue"""


_RprIfReversionMode_Object = MibTableColumn
rprIfReversionMode = _RprIfReversionMode_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 3),
    _RprIfReversionMode_Type()
)
rprIfReversionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfReversionMode.setStatus("current")


class _RprIfProtectionWTR_Type(Unsigned32):
    """Custom type rprIfProtectionWTR based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_RprIfProtectionWTR_Type.__name__ = "Unsigned32"
_RprIfProtectionWTR_Object = MibTableColumn
rprIfProtectionWTR = _RprIfProtectionWTR_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 4),
    _RprIfProtectionWTR_Type()
)
rprIfProtectionWTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfProtectionWTR.setStatus("current")
if mibBuilder.loadTexts:
    rprIfProtectionWTR.setUnits("Seconds")


class _RprIfProtectionFastTimer_Type(Unsigned32):
    """Custom type rprIfProtectionFastTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RprIfProtectionFastTimer_Type.__name__ = "Unsigned32"
_RprIfProtectionFastTimer_Object = MibTableColumn
rprIfProtectionFastTimer = _RprIfProtectionFastTimer_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 5),
    _RprIfProtectionFastTimer_Type()
)
rprIfProtectionFastTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfProtectionFastTimer.setStatus("current")
if mibBuilder.loadTexts:
    rprIfProtectionFastTimer.setUnits("milliseconds")


class _RprIfProtectionSlowTimer_Type(Unsigned32):
    """Custom type rprIfProtectionSlowTimer based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_RprIfProtectionSlowTimer_Type.__name__ = "Unsigned32"
_RprIfProtectionSlowTimer_Object = MibTableColumn
rprIfProtectionSlowTimer = _RprIfProtectionSlowTimer_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 6),
    _RprIfProtectionSlowTimer_Type()
)
rprIfProtectionSlowTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfProtectionSlowTimer.setStatus("current")
if mibBuilder.loadTexts:
    rprIfProtectionSlowTimer.setUnits("50 milliseconds")


class _RprIfAtdTimer_Type(Unsigned32):
    """Custom type rprIfAtdTimer based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_RprIfAtdTimer_Type.__name__ = "Unsigned32"
_RprIfAtdTimer_Object = MibTableColumn
rprIfAtdTimer = _RprIfAtdTimer_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 7),
    _RprIfAtdTimer_Type()
)
rprIfAtdTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfAtdTimer.setStatus("current")
if mibBuilder.loadTexts:
    rprIfAtdTimer.setUnits("50 milliseconds")


class _RprIfKeepaliveTimeout_Type(Unsigned32):
    """Custom type rprIfKeepaliveTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 50),
    )


_RprIfKeepaliveTimeout_Type.__name__ = "Unsigned32"
_RprIfKeepaliveTimeout_Object = MibTableColumn
rprIfKeepaliveTimeout = _RprIfKeepaliveTimeout_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 8),
    _RprIfKeepaliveTimeout_Type()
)
rprIfKeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfKeepaliveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rprIfKeepaliveTimeout.setUnits("milliseconds")


class _RprIfFairnessAggressive_Type(TruthValue):
    """Custom type rprIfFairnessAggressive based on TruthValue"""


_RprIfFairnessAggressive_Object = MibTableColumn
rprIfFairnessAggressive = _RprIfFairnessAggressive_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 9),
    _RprIfFairnessAggressive_Type()
)
rprIfFairnessAggressive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfFairnessAggressive.setStatus("current")
_RprIfPtqSize_Type = Unsigned32
_RprIfPtqSize_Object = MibTableColumn
rprIfPtqSize = _RprIfPtqSize_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 10),
    _RprIfPtqSize_Type()
)
rprIfPtqSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfPtqSize.setStatus("current")
if mibBuilder.loadTexts:
    rprIfPtqSize.setUnits("Bytes")
_RprIfStqSize_Type = Unsigned32
_RprIfStqSize_Object = MibTableColumn
rprIfStqSize = _RprIfStqSize_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 11),
    _RprIfStqSize_Type()
)
rprIfStqSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfStqSize.setStatus("current")
if mibBuilder.loadTexts:
    rprIfStqSize.setUnits("Bytes")


class _RprIfSTQFullThreshold_Type(Unsigned32):
    """Custom type rprIfSTQFullThreshold based on Unsigned32"""
    defaultValue = 2


_RprIfSTQFullThreshold_Object = MibTableColumn
rprIfSTQFullThreshold = _RprIfSTQFullThreshold_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 12),
    _RprIfSTQFullThreshold_Type()
)
rprIfSTQFullThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfSTQFullThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rprIfSTQFullThreshold.setUnits("MTUs")


class _RprIfIdleThreshold_Type(Unsigned32):
    """Custom type rprIfIdleThreshold based on Unsigned32"""
    defaultValue = 1


_RprIfIdleThreshold_Object = MibTableColumn
rprIfIdleThreshold = _RprIfIdleThreshold_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 13),
    _RprIfIdleThreshold_Type()
)
rprIfIdleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfIdleThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rprIfIdleThreshold.setUnits("MTUs")


class _RprIfSesThreshold_Type(Unsigned32):
    """Custom type rprIfSesThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_RprIfSesThreshold_Type.__name__ = "Unsigned32"
_RprIfSesThreshold_Object = MibTableColumn
rprIfSesThreshold = _RprIfSesThreshold_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 14),
    _RprIfSesThreshold_Type()
)
rprIfSesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfSesThreshold.setStatus("current")
_RprIfWrapConfig_Type = TruthValue
_RprIfWrapConfig_Object = MibTableColumn
rprIfWrapConfig = _RprIfWrapConfig_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 15),
    _RprIfWrapConfig_Type()
)
rprIfWrapConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfWrapConfig.setStatus("current")


class _RprIfJumboFramePreferred_Type(TruthValue):
    """Custom type rprIfJumboFramePreferred based on TruthValue"""


_RprIfJumboFramePreferred_Object = MibTableColumn
rprIfJumboFramePreferred = _RprIfJumboFramePreferred_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 16),
    _RprIfJumboFramePreferred_Type()
)
rprIfJumboFramePreferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfJumboFramePreferred.setStatus("current")


class _RprIfMacOperModes_Type(Bits):
    """Custom type rprIfMacOperModes based on Bits"""
    namedValues = NamedValues(
        *(("dropBadFcs", 1),
          ("strictOrder", 0))
    )

_RprIfMacOperModes_Type.__name__ = "Bits"
_RprIfMacOperModes_Object = MibTableColumn
rprIfMacOperModes = _RprIfMacOperModes_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 17),
    _RprIfMacOperModes_Type()
)
rprIfMacOperModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfMacOperModes.setStatus("current")


class _RprIfRingOperModes_Type(Bits):
    """Custom type rprIfRingOperModes based on Bits"""
    namedValues = NamedValues(
        *(("jumboFrames", 0),
          ("openRing", 2),
          ("wrapProtection", 1))
    )

_RprIfRingOperModes_Type.__name__ = "Bits"
_RprIfRingOperModes_Object = MibTableColumn
rprIfRingOperModes = _RprIfRingOperModes_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 18),
    _RprIfRingOperModes_Type()
)
rprIfRingOperModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfRingOperModes.setStatus("current")


class _RprIfCurrentStatus_Type(Bits):
    """Custom type rprIfCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("duplicateMac", 1),
          ("exceedMaxStations", 2),
          ("neighborInconsistency", 0))
    )

_RprIfCurrentStatus_Type.__name__ = "Bits"
_RprIfCurrentStatus_Object = MibTableColumn
rprIfCurrentStatus = _RprIfCurrentStatus_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 19),
    _RprIfCurrentStatus_Type()
)
rprIfCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfCurrentStatus.setStatus("current")
_RprIfLastChange_Type = TimeStamp
_RprIfLastChange_Object = MibTableColumn
rprIfLastChange = _RprIfLastChange_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 20),
    _RprIfLastChange_Type()
)
rprIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfLastChange.setStatus("current")
_RprIfChanges_Type = Counter32
_RprIfChanges_Object = MibTableColumn
rprIfChanges = _RprIfChanges_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 1, 1, 21),
    _RprIfChanges_Type()
)
rprIfChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfChanges.setStatus("current")
_RprIfStatsControlTable_Object = MibTable
rprIfStatsControlTable = _RprIfStatsControlTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rprIfStatsControlTable.setStatus("current")
_RprIfStatsControlEntry_Object = MibTableRow
rprIfStatsControlEntry = _RprIfStatsControlEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 2, 1)
)
rprIfStatsControlEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprIfStatsControlIfIndex"),
)
if mibBuilder.loadTexts:
    rprIfStatsControlEntry.setStatus("current")
_RprIfStatsControlIfIndex_Type = InterfaceIndex
_RprIfStatsControlIfIndex_Object = MibTableColumn
rprIfStatsControlIfIndex = _RprIfStatsControlIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 2, 1, 1),
    _RprIfStatsControlIfIndex_Type()
)
rprIfStatsControlIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprIfStatsControlIfIndex.setStatus("current")


class _RprIfStatsControlPeriodClear_Type(Integer32):
    """Custom type rprIfStatsControlPeriodClear based on Integer32"""
    defaultValue = 1

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
        *(("clearAllIntervals", 2),
          ("clearCurrent", 3),
          ("clearIntervals", 4),
          ("clearSpecificInterval", 5),
          ("idle", 1))
    )


_RprIfStatsControlPeriodClear_Type.__name__ = "Integer32"
_RprIfStatsControlPeriodClear_Object = MibTableColumn
rprIfStatsControlPeriodClear = _RprIfStatsControlPeriodClear_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 2, 1, 2),
    _RprIfStatsControlPeriodClear_Type()
)
rprIfStatsControlPeriodClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfStatsControlPeriodClear.setStatus("current")


class _RprIfStatsControlCountPointClear_Type(Integer32):
    """Custom type rprIfStatsControlCountPointClear based on Integer32"""
    defaultValue = 1

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
        *(("clearAll", 1),
          ("clearClient", 4),
          ("clearEast", 3),
          ("clearWest", 2))
    )


_RprIfStatsControlCountPointClear_Type.__name__ = "Integer32"
_RprIfStatsControlCountPointClear_Object = MibTableColumn
rprIfStatsControlCountPointClear = _RprIfStatsControlCountPointClear_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 2, 1, 3),
    _RprIfStatsControlCountPointClear_Type()
)
rprIfStatsControlCountPointClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfStatsControlCountPointClear.setStatus("current")


class _RprIfStatsControlIntervalClear_Type(Unsigned32):
    """Custom type rprIfStatsControlIntervalClear based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_RprIfStatsControlIntervalClear_Type.__name__ = "Unsigned32"
_RprIfStatsControlIntervalClear_Object = MibTableColumn
rprIfStatsControlIntervalClear = _RprIfStatsControlIntervalClear_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 2, 1, 4),
    _RprIfStatsControlIntervalClear_Type()
)
rprIfStatsControlIntervalClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfStatsControlIntervalClear.setStatus("current")


class _RprIfStatsControlCommitClear_Type(Integer32):
    """Custom type rprIfStatsControlCommitClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commit", 1),
          ("commitDone", 2),
          ("commitFailed", 3))
    )


_RprIfStatsControlCommitClear_Type.__name__ = "Integer32"
_RprIfStatsControlCommitClear_Object = MibTableColumn
rprIfStatsControlCommitClear = _RprIfStatsControlCommitClear_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 2, 1, 5),
    _RprIfStatsControlCommitClear_Type()
)
rprIfStatsControlCommitClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprIfStatsControlCommitClear.setStatus("current")


class _RprIfStatsControlTimeElapsed_Type(Unsigned32):
    """Custom type rprIfStatsControlTimeElapsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_RprIfStatsControlTimeElapsed_Type.__name__ = "Unsigned32"
_RprIfStatsControlTimeElapsed_Object = MibTableColumn
rprIfStatsControlTimeElapsed = _RprIfStatsControlTimeElapsed_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 2, 1, 6),
    _RprIfStatsControlTimeElapsed_Type()
)
rprIfStatsControlTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfStatsControlTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    rprIfStatsControlTimeElapsed.setUnits("Seconds")


class _RprIfStatsControlValidIntervals_Type(Unsigned32):
    """Custom type rprIfStatsControlValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_RprIfStatsControlValidIntervals_Type.__name__ = "Unsigned32"
_RprIfStatsControlValidIntervals_Object = MibTableColumn
rprIfStatsControlValidIntervals = _RprIfStatsControlValidIntervals_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 2, 1, 7),
    _RprIfStatsControlValidIntervals_Type()
)
rprIfStatsControlValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfStatsControlValidIntervals.setStatus("current")
_RprSpanTable_Object = MibTable
rprSpanTable = _RprSpanTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rprSpanTable.setStatus("current")
_RprSpanEntry_Object = MibTableRow
rprSpanEntry = _RprSpanEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 3, 1)
)
rprSpanEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanIfIndex"),
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanId"),
)
if mibBuilder.loadTexts:
    rprSpanEntry.setStatus("current")
_RprSpanIfIndex_Type = InterfaceIndex
_RprSpanIfIndex_Object = MibTableColumn
rprSpanIfIndex = _RprSpanIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 3, 1, 1),
    _RprSpanIfIndex_Type()
)
rprSpanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanIfIndex.setStatus("current")
_RprSpanId_Type = RprSpan
_RprSpanId_Object = MibTableColumn
rprSpanId = _RprSpanId_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 3, 1, 2),
    _RprSpanId_Type()
)
rprSpanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanId.setStatus("current")
_RprSpanLowerLayerIfIndex_Type = InterfaceIndexOrZero
_RprSpanLowerLayerIfIndex_Object = MibTableColumn
rprSpanLowerLayerIfIndex = _RprSpanLowerLayerIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 3, 1, 3),
    _RprSpanLowerLayerIfIndex_Type()
)
rprSpanLowerLayerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanLowerLayerIfIndex.setStatus("current")
_RprSpanTotalRingletReservedRate_Type = Unsigned32
_RprSpanTotalRingletReservedRate_Object = MibTableColumn
rprSpanTotalRingletReservedRate = _RprSpanTotalRingletReservedRate_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 3, 1, 4),
    _RprSpanTotalRingletReservedRate_Type()
)
rprSpanTotalRingletReservedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanTotalRingletReservedRate.setStatus("current")
if mibBuilder.loadTexts:
    rprSpanTotalRingletReservedRate.setUnits("Mb/s")


class _RprSpanCurrentStatus_Type(Bits):
    """Custom type rprSpanCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("keepAliveTimeout", 0),
          ("miscabling", 1),
          ("phyLinkDegrade", 2),
          ("phyLinkFail", 3))
    )

_RprSpanCurrentStatus_Type.__name__ = "Bits"
_RprSpanCurrentStatus_Object = MibTableColumn
rprSpanCurrentStatus = _RprSpanCurrentStatus_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 3, 1, 5),
    _RprSpanCurrentStatus_Type()
)
rprSpanCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentStatus.setStatus("current")
_RprSpanLastChange_Type = TimeStamp
_RprSpanLastChange_Object = MibTableColumn
rprSpanLastChange = _RprSpanLastChange_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 3, 1, 6),
    _RprSpanLastChange_Type()
)
rprSpanLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanLastChange.setStatus("current")
_RprSpanChanges_Type = Counter32
_RprSpanChanges_Object = MibTableColumn
rprSpanChanges = _RprSpanChanges_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 3, 1, 7),
    _RprSpanChanges_Type()
)
rprSpanChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanChanges.setStatus("current")
_RprSpanProtectionTable_Object = MibTable
rprSpanProtectionTable = _RprSpanProtectionTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rprSpanProtectionTable.setStatus("current")
_RprSpanProtectionEntry_Object = MibTableRow
rprSpanProtectionEntry = _RprSpanProtectionEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 4, 1)
)
rprSpanProtectionEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanProtectionIfIndex"),
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanProtectionSpan"),
)
if mibBuilder.loadTexts:
    rprSpanProtectionEntry.setStatus("current")
_RprSpanProtectionIfIndex_Type = InterfaceIndex
_RprSpanProtectionIfIndex_Object = MibTableColumn
rprSpanProtectionIfIndex = _RprSpanProtectionIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 4, 1, 1),
    _RprSpanProtectionIfIndex_Type()
)
rprSpanProtectionIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanProtectionIfIndex.setStatus("current")
_RprSpanProtectionSpan_Type = RprSpan
_RprSpanProtectionSpan_Object = MibTableColumn
rprSpanProtectionSpan = _RprSpanProtectionSpan_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 4, 1, 2),
    _RprSpanProtectionSpan_Type()
)
rprSpanProtectionSpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanProtectionSpan.setStatus("current")
_RprSpanProtectionNeighborValid_Type = TruthValue
_RprSpanProtectionNeighborValid_Object = MibTableColumn
rprSpanProtectionNeighborValid = _RprSpanProtectionNeighborValid_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 4, 1, 3),
    _RprSpanProtectionNeighborValid_Type()
)
rprSpanProtectionNeighborValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanProtectionNeighborValid.setStatus("current")


class _RprSpanProtectionHoldOffTimer_Type(Unsigned32):
    """Custom type rprSpanProtectionHoldOffTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_RprSpanProtectionHoldOffTimer_Type.__name__ = "Unsigned32"
_RprSpanProtectionHoldOffTimer_Object = MibTableColumn
rprSpanProtectionHoldOffTimer = _RprSpanProtectionHoldOffTimer_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 4, 1, 4),
    _RprSpanProtectionHoldOffTimer_Type()
)
rprSpanProtectionHoldOffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprSpanProtectionHoldOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    rprSpanProtectionHoldOffTimer.setUnits("milliseconds")


class _RprSpanProtectionCommand_Type(Integer32):
    """Custom type rprSpanProtectionCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forcedSwitch", 3),
          ("idle", 1),
          ("manualSwitch", 2))
    )


_RprSpanProtectionCommand_Type.__name__ = "Integer32"
_RprSpanProtectionCommand_Object = MibTableColumn
rprSpanProtectionCommand = _RprSpanProtectionCommand_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 4, 1, 5),
    _RprSpanProtectionCommand_Type()
)
rprSpanProtectionCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprSpanProtectionCommand.setStatus("current")
_RprSpanProtectionCount_Type = Counter32
_RprSpanProtectionCount_Object = MibTableColumn
rprSpanProtectionCount = _RprSpanProtectionCount_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 4, 1, 6),
    _RprSpanProtectionCount_Type()
)
rprSpanProtectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanProtectionCount.setStatus("current")
_RprSpanProtectionDuration_Type = Counter32
_RprSpanProtectionDuration_Object = MibTableColumn
rprSpanProtectionDuration = _RprSpanProtectionDuration_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 4, 1, 7),
    _RprSpanProtectionDuration_Type()
)
rprSpanProtectionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanProtectionDuration.setStatus("current")
if mibBuilder.loadTexts:
    rprSpanProtectionDuration.setUnits("seconds")
_RprSpanProtectionLastActivationTime_Type = TimeStamp
_RprSpanProtectionLastActivationTime_Object = MibTableColumn
rprSpanProtectionLastActivationTime = _RprSpanProtectionLastActivationTime_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 4, 1, 8),
    _RprSpanProtectionLastActivationTime_Type()
)
rprSpanProtectionLastActivationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanProtectionLastActivationTime.setStatus("current")
_RprIfChangeSummaryObject_ObjectIdentity = ObjectIdentity
rprIfChangeSummaryObject = _RprIfChangeSummaryObject_ObjectIdentity(
    (1, 0, 8802, 17, 1, 1, 1, 1, 5)
)
_RprIfChangeSummaryNumInterfaces_Type = Unsigned32
_RprIfChangeSummaryNumInterfaces_Object = MibScalar
rprIfChangeSummaryNumInterfaces = _RprIfChangeSummaryNumInterfaces_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 5, 1),
    _RprIfChangeSummaryNumInterfaces_Type()
)
rprIfChangeSummaryNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfChangeSummaryNumInterfaces.setStatus("current")
_RprIfChangeSummaryIfLastChange_Type = TimeStamp
_RprIfChangeSummaryIfLastChange_Object = MibScalar
rprIfChangeSummaryIfLastChange = _RprIfChangeSummaryIfLastChange_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 5, 2),
    _RprIfChangeSummaryIfLastChange_Type()
)
rprIfChangeSummaryIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfChangeSummaryIfLastChange.setStatus("current")
_RprIfChangeSummaryIfChanges_Type = Counter32
_RprIfChangeSummaryIfChanges_Object = MibScalar
rprIfChangeSummaryIfChanges = _RprIfChangeSummaryIfChanges_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 5, 3),
    _RprIfChangeSummaryIfChanges_Type()
)
rprIfChangeSummaryIfChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfChangeSummaryIfChanges.setStatus("current")
_RprIfChangeSummarySpanLastChange_Type = TimeStamp
_RprIfChangeSummarySpanLastChange_Object = MibScalar
rprIfChangeSummarySpanLastChange = _RprIfChangeSummarySpanLastChange_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 5, 4),
    _RprIfChangeSummarySpanLastChange_Type()
)
rprIfChangeSummarySpanLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfChangeSummarySpanLastChange.setStatus("current")
_RprIfChangeSummarySpanChanges_Type = Counter32
_RprIfChangeSummarySpanChanges_Object = MibScalar
rprIfChangeSummarySpanChanges = _RprIfChangeSummarySpanChanges_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 5, 5),
    _RprIfChangeSummarySpanChanges_Type()
)
rprIfChangeSummarySpanChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfChangeSummarySpanChanges.setStatus("current")
_RprIfChangeSummaryFairnessLastChange_Type = TimeStamp
_RprIfChangeSummaryFairnessLastChange_Object = MibScalar
rprIfChangeSummaryFairnessLastChange = _RprIfChangeSummaryFairnessLastChange_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 5, 6),
    _RprIfChangeSummaryFairnessLastChange_Type()
)
rprIfChangeSummaryFairnessLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfChangeSummaryFairnessLastChange.setStatus("current")
_RprIfChangeSummaryFairnessChanges_Type = Counter32
_RprIfChangeSummaryFairnessChanges_Object = MibScalar
rprIfChangeSummaryFairnessChanges = _RprIfChangeSummaryFairnessChanges_Object(
    (1, 0, 8802, 17, 1, 1, 1, 1, 5, 7),
    _RprIfChangeSummaryFairnessChanges_Type()
)
rprIfChangeSummaryFairnessChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprIfChangeSummaryFairnessChanges.setStatus("current")
_RprProtocols_ObjectIdentity = ObjectIdentity
rprProtocols = _RprProtocols_ObjectIdentity(
    (1, 0, 8802, 17, 1, 1, 1, 2)
)
_RprTopoImageTable_Object = MibTable
rprTopoImageTable = _RprTopoImageTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rprTopoImageTable.setStatus("current")
_RprTopoImageEntry_Object = MibTableRow
rprTopoImageEntry = _RprTopoImageEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1)
)
rprTopoImageEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprTopoImageIfIndex"),
    (0, "IEEE-802DOT17-RPR-MIB", "rprTopoImageMacAddress"),
)
if mibBuilder.loadTexts:
    rprTopoImageEntry.setStatus("current")
_RprTopoImageIfIndex_Type = InterfaceIndex
_RprTopoImageIfIndex_Object = MibTableColumn
rprTopoImageIfIndex = _RprTopoImageIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 1),
    _RprTopoImageIfIndex_Type()
)
rprTopoImageIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprTopoImageIfIndex.setStatus("current")
_RprTopoImageMacAddress_Type = MacAddress
_RprTopoImageMacAddress_Object = MibTableColumn
rprTopoImageMacAddress = _RprTopoImageMacAddress_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 2),
    _RprTopoImageMacAddress_Type()
)
rprTopoImageMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprTopoImageMacAddress.setStatus("current")
_RprTopoImageSecMacAddress1_Type = MacAddress
_RprTopoImageSecMacAddress1_Object = MibTableColumn
rprTopoImageSecMacAddress1 = _RprTopoImageSecMacAddress1_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 3),
    _RprTopoImageSecMacAddress1_Type()
)
rprTopoImageSecMacAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageSecMacAddress1.setStatus("current")
_RprTopoImageSecMacAddress2_Type = MacAddress
_RprTopoImageSecMacAddress2_Object = MibTableColumn
rprTopoImageSecMacAddress2 = _RprTopoImageSecMacAddress2_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 4),
    _RprTopoImageSecMacAddress2_Type()
)
rprTopoImageSecMacAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageSecMacAddress2.setStatus("current")
_RprTopoImageStationIfIndex_Type = InterfaceIndex
_RprTopoImageStationIfIndex_Object = MibTableColumn
rprTopoImageStationIfIndex = _RprTopoImageStationIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 5),
    _RprTopoImageStationIfIndex_Type()
)
rprTopoImageStationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageStationIfIndex.setStatus("current")
_RprTopoImageStationName_Type = SnmpAdminString
_RprTopoImageStationName_Object = MibTableColumn
rprTopoImageStationName = _RprTopoImageStationName_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 6),
    _RprTopoImageStationName_Type()
)
rprTopoImageStationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageStationName.setStatus("current")
_RprTopoImageInetAddressType_Type = InetAddressType
_RprTopoImageInetAddressType_Object = MibTableColumn
rprTopoImageInetAddressType = _RprTopoImageInetAddressType_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 7),
    _RprTopoImageInetAddressType_Type()
)
rprTopoImageInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageInetAddressType.setStatus("current")
_RprTopoImageInetAddress_Type = InetAddress
_RprTopoImageInetAddress_Object = MibTableColumn
rprTopoImageInetAddress = _RprTopoImageInetAddress_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 8),
    _RprTopoImageInetAddress_Type()
)
rprTopoImageInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageInetAddress.setStatus("current")


class _RprTopoImageCapability_Type(Bits):
    """Custom type rprTopoImageCapability based on Bits"""
    namedValues = NamedValues(
        *(("jumboFrames", 0),
          ("supportsConservativeFairness", 2),
          ("wrapProtection", 1))
    )

_RprTopoImageCapability_Type.__name__ = "Bits"
_RprTopoImageCapability_Object = MibTableColumn
rprTopoImageCapability = _RprTopoImageCapability_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 9),
    _RprTopoImageCapability_Type()
)
rprTopoImageCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageCapability.setStatus("current")
_RprTopoImageRinglet0Hops_Type = Integer32
_RprTopoImageRinglet0Hops_Object = MibTableColumn
rprTopoImageRinglet0Hops = _RprTopoImageRinglet0Hops_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 10),
    _RprTopoImageRinglet0Hops_Type()
)
rprTopoImageRinglet0Hops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageRinglet0Hops.setStatus("current")
_RprTopoImageRinglet0ReservedRate_Type = Unsigned32
_RprTopoImageRinglet0ReservedRate_Object = MibTableColumn
rprTopoImageRinglet0ReservedRate = _RprTopoImageRinglet0ReservedRate_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 11),
    _RprTopoImageRinglet0ReservedRate_Type()
)
rprTopoImageRinglet0ReservedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageRinglet0ReservedRate.setStatus("current")
if mibBuilder.loadTexts:
    rprTopoImageRinglet0ReservedRate.setUnits("Mb/s")
_RprTopoImageRinglet1Hops_Type = Integer32
_RprTopoImageRinglet1Hops_Object = MibTableColumn
rprTopoImageRinglet1Hops = _RprTopoImageRinglet1Hops_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 12),
    _RprTopoImageRinglet1Hops_Type()
)
rprTopoImageRinglet1Hops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageRinglet1Hops.setStatus("current")
_RprTopoImageRinglet1ReservedRate_Type = Unsigned32
_RprTopoImageRinglet1ReservedRate_Object = MibTableColumn
rprTopoImageRinglet1ReservedRate = _RprTopoImageRinglet1ReservedRate_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 13),
    _RprTopoImageRinglet1ReservedRate_Type()
)
rprTopoImageRinglet1ReservedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageRinglet1ReservedRate.setStatus("current")
if mibBuilder.loadTexts:
    rprTopoImageRinglet1ReservedRate.setUnits("Mb/s")
_RprTopoImageWestProtectionStatus_Type = RprProtectionStatus
_RprTopoImageWestProtectionStatus_Object = MibTableColumn
rprTopoImageWestProtectionStatus = _RprTopoImageWestProtectionStatus_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 14),
    _RprTopoImageWestProtectionStatus_Type()
)
rprTopoImageWestProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageWestProtectionStatus.setStatus("current")


class _RprTopoImageWestWeight_Type(Unsigned32):
    """Custom type rprTopoImageWestWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RprTopoImageWestWeight_Type.__name__ = "Unsigned32"
_RprTopoImageWestWeight_Object = MibTableColumn
rprTopoImageWestWeight = _RprTopoImageWestWeight_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 15),
    _RprTopoImageWestWeight_Type()
)
rprTopoImageWestWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageWestWeight.setStatus("current")
_RprTopoImageEastProtectionStatus_Type = RprProtectionStatus
_RprTopoImageEastProtectionStatus_Object = MibTableColumn
rprTopoImageEastProtectionStatus = _RprTopoImageEastProtectionStatus_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 16),
    _RprTopoImageEastProtectionStatus_Type()
)
rprTopoImageEastProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageEastProtectionStatus.setStatus("current")


class _RprTopoImageEastWeight_Type(Unsigned32):
    """Custom type rprTopoImageEastWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RprTopoImageEastWeight_Type.__name__ = "Unsigned32"
_RprTopoImageEastWeight_Object = MibTableColumn
rprTopoImageEastWeight = _RprTopoImageEastWeight_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 17),
    _RprTopoImageEastWeight_Type()
)
rprTopoImageEastWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageEastWeight.setStatus("current")


class _RprTopoImageStatus_Type(Bits):
    """Custom type rprTopoImageStatus based on Bits"""
    namedValues = NamedValues(
        *(("reachableRinglet0", 0),
          ("reachableRinglet1", 1),
          ("receivedBadFcs", 4),
          ("receivedMultichokeFairness", 5),
          ("wrapActiveEast", 3),
          ("wrapActiveWest", 2))
    )

_RprTopoImageStatus_Type.__name__ = "Bits"
_RprTopoImageStatus_Object = MibTableColumn
rprTopoImageStatus = _RprTopoImageStatus_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 1, 1, 18),
    _RprTopoImageStatus_Type()
)
rprTopoImageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprTopoImageStatus.setStatus("current")
_RprFairnessTable_Object = MibTable
rprFairnessTable = _RprFairnessTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rprFairnessTable.setStatus("current")
_RprFairnessEntry_Object = MibTableRow
rprFairnessEntry = _RprFairnessEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1)
)
rprFairnessEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprFairnessIfIndex"),
    (0, "IEEE-802DOT17-RPR-MIB", "rprFairnessRinglet"),
)
if mibBuilder.loadTexts:
    rprFairnessEntry.setStatus("current")
_RprFairnessIfIndex_Type = InterfaceIndex
_RprFairnessIfIndex_Object = MibTableColumn
rprFairnessIfIndex = _RprFairnessIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 1),
    _RprFairnessIfIndex_Type()
)
rprFairnessIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprFairnessIfIndex.setStatus("current")


class _RprFairnessRinglet_Type(Integer32):
    """Custom type rprFairnessRinglet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ringlet0", 1),
          ("ringlet1", 2))
    )


_RprFairnessRinglet_Type.__name__ = "Integer32"
_RprFairnessRinglet_Object = MibTableColumn
rprFairnessRinglet = _RprFairnessRinglet_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 2),
    _RprFairnessRinglet_Type()
)
rprFairnessRinglet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprFairnessRinglet.setStatus("current")


class _RprFairnessRingletWeight_Type(Unsigned32):
    """Custom type rprFairnessRingletWeight based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RprFairnessRingletWeight_Type.__name__ = "Unsigned32"
_RprFairnessRingletWeight_Object = MibTableColumn
rprFairnessRingletWeight = _RprFairnessRingletWeight_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 3),
    _RprFairnessRingletWeight_Type()
)
rprFairnessRingletWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprFairnessRingletWeight.setStatus("current")


class _RprFairnessReservedRate_Type(Unsigned32):
    """Custom type rprFairnessReservedRate based on Unsigned32"""
    defaultValue = 0


_RprFairnessReservedRate_Object = MibTableColumn
rprFairnessReservedRate = _RprFairnessReservedRate_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 4),
    _RprFairnessReservedRate_Type()
)
rprFairnessReservedRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprFairnessReservedRate.setStatus("current")
if mibBuilder.loadTexts:
    rprFairnessReservedRate.setUnits("Mb/s")
_RprFairnessMaxAllowed_Type = Unsigned32
_RprFairnessMaxAllowed_Object = MibTableColumn
rprFairnessMaxAllowed = _RprFairnessMaxAllowed_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 5),
    _RprFairnessMaxAllowed_Type()
)
rprFairnessMaxAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprFairnessMaxAllowed.setStatus("current")
if mibBuilder.loadTexts:
    rprFairnessMaxAllowed.setUnits("Mb/s")


class _RprFairnessAgeCoef_Type(Unsigned32):
    """Custom type rprFairnessAgeCoef based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_RprFairnessAgeCoef_Type.__name__ = "Unsigned32"
_RprFairnessAgeCoef_Object = MibTableColumn
rprFairnessAgeCoef = _RprFairnessAgeCoef_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 6),
    _RprFairnessAgeCoef_Type()
)
rprFairnessAgeCoef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprFairnessAgeCoef.setStatus("current")


class _RprFairnessRampCoef_Type(Unsigned32):
    """Custom type rprFairnessRampCoef based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 9),
    )


_RprFairnessRampCoef_Type.__name__ = "Unsigned32"
_RprFairnessRampCoef_Object = MibTableColumn
rprFairnessRampCoef = _RprFairnessRampCoef_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 7),
    _RprFairnessRampCoef_Type()
)
rprFairnessRampCoef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprFairnessRampCoef.setStatus("current")


class _RprFairnessLpCoef_Type(Unsigned32):
    """Custom type rprFairnessLpCoef based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 9),
    )


_RprFairnessLpCoef_Type.__name__ = "Unsigned32"
_RprFairnessLpCoef_Object = MibTableColumn
rprFairnessLpCoef = _RprFairnessLpCoef_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 8),
    _RprFairnessLpCoef_Type()
)
rprFairnessLpCoef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprFairnessLpCoef.setStatus("current")


class _RprFairnessAdvertisementRatio_Type(Unsigned32):
    """Custom type rprFairnessAdvertisementRatio based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_RprFairnessAdvertisementRatio_Type.__name__ = "Unsigned32"
_RprFairnessAdvertisementRatio_Object = MibTableColumn
rprFairnessAdvertisementRatio = _RprFairnessAdvertisementRatio_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 9),
    _RprFairnessAdvertisementRatio_Type()
)
rprFairnessAdvertisementRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprFairnessAdvertisementRatio.setStatus("current")
if mibBuilder.loadTexts:
    rprFairnessAdvertisementRatio.setUnits("0.00025")


class _RprFairnessMcffReportCoef_Type(Unsigned32):
    """Custom type rprFairnessMcffReportCoef based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 512),
    )


_RprFairnessMcffReportCoef_Type.__name__ = "Unsigned32"
_RprFairnessMcffReportCoef_Object = MibTableColumn
rprFairnessMcffReportCoef = _RprFairnessMcffReportCoef_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 10),
    _RprFairnessMcffReportCoef_Type()
)
rprFairnessMcffReportCoef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprFairnessMcffReportCoef.setStatus("current")


class _RprFairnessActiveWeightsCoef_Type(Unsigned32):
    """Custom type rprFairnessActiveWeightsCoef based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 512),
    )


_RprFairnessActiveWeightsCoef_Type.__name__ = "Unsigned32"
_RprFairnessActiveWeightsCoef_Object = MibTableColumn
rprFairnessActiveWeightsCoef = _RprFairnessActiveWeightsCoef_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 11),
    _RprFairnessActiveWeightsCoef_Type()
)
rprFairnessActiveWeightsCoef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprFairnessActiveWeightsCoef.setStatus("current")


class _RprFairnessSTQHighThreshold_Type(Unsigned32):
    """Custom type rprFairnessSTQHighThreshold based on Unsigned32"""
    defaultValue = 250

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RprFairnessSTQHighThreshold_Type.__name__ = "Unsigned32"
_RprFairnessSTQHighThreshold_Object = MibTableColumn
rprFairnessSTQHighThreshold = _RprFairnessSTQHighThreshold_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 12),
    _RprFairnessSTQHighThreshold_Type()
)
rprFairnessSTQHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprFairnessSTQHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rprFairnessSTQHighThreshold.setUnits("Tenth of percent")


class _RprFairnessSTQMedThreshold_Type(Unsigned32):
    """Custom type rprFairnessSTQMedThreshold based on Unsigned32"""
    defaultValue = 187

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RprFairnessSTQMedThreshold_Type.__name__ = "Unsigned32"
_RprFairnessSTQMedThreshold_Object = MibTableColumn
rprFairnessSTQMedThreshold = _RprFairnessSTQMedThreshold_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 13),
    _RprFairnessSTQMedThreshold_Type()
)
rprFairnessSTQMedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprFairnessSTQMedThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rprFairnessSTQMedThreshold.setUnits("Tenth of percent")


class _RprFairnessSTQLowThreshold_Type(Unsigned32):
    """Custom type rprFairnessSTQLowThreshold based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RprFairnessSTQLowThreshold_Type.__name__ = "Unsigned32"
_RprFairnessSTQLowThreshold_Object = MibTableColumn
rprFairnessSTQLowThreshold = _RprFairnessSTQLowThreshold_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 14),
    _RprFairnessSTQLowThreshold_Type()
)
rprFairnessSTQLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprFairnessSTQLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rprFairnessSTQLowThreshold.setUnits("Tenth of percent")


class _RprFairnessRateHighThreshold_Type(Unsigned32):
    """Custom type rprFairnessRateHighThreshold based on Unsigned32"""
    defaultValue = 950

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 990),
    )


_RprFairnessRateHighThreshold_Type.__name__ = "Unsigned32"
_RprFairnessRateHighThreshold_Object = MibTableColumn
rprFairnessRateHighThreshold = _RprFairnessRateHighThreshold_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 15),
    _RprFairnessRateHighThreshold_Type()
)
rprFairnessRateHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprFairnessRateHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rprFairnessRateHighThreshold.setUnits("Tenth of percent")


class _RprFairnessRateLowThreshold_Type(Unsigned32):
    """Custom type rprFairnessRateLowThreshold based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 990),
    )


_RprFairnessRateLowThreshold_Type.__name__ = "Unsigned32"
_RprFairnessRateLowThreshold_Object = MibTableColumn
rprFairnessRateLowThreshold = _RprFairnessRateLowThreshold_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 16),
    _RprFairnessRateLowThreshold_Type()
)
rprFairnessRateLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprFairnessRateLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rprFairnessRateLowThreshold.setUnits("Tenth of percent")


class _RprFairnessResetWaterMarks_Type(Integer32):
    """Custom type rprFairnessResetWaterMarks based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("resetWaterMarks", 2))
    )


_RprFairnessResetWaterMarks_Type.__name__ = "Integer32"
_RprFairnessResetWaterMarks_Object = MibTableColumn
rprFairnessResetWaterMarks = _RprFairnessResetWaterMarks_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 17),
    _RprFairnessResetWaterMarks_Type()
)
rprFairnessResetWaterMarks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprFairnessResetWaterMarks.setStatus("current")


class _RprFairnessSTQHighWaterMark_Type(Unsigned32):
    """Custom type rprFairnessSTQHighWaterMark based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RprFairnessSTQHighWaterMark_Type.__name__ = "Unsigned32"
_RprFairnessSTQHighWaterMark_Object = MibTableColumn
rprFairnessSTQHighWaterMark = _RprFairnessSTQHighWaterMark_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 18),
    _RprFairnessSTQHighWaterMark_Type()
)
rprFairnessSTQHighWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprFairnessSTQHighWaterMark.setStatus("current")
if mibBuilder.loadTexts:
    rprFairnessSTQHighWaterMark.setUnits("Tenth of percent")


class _RprFairnessSTQLowWaterMark_Type(Unsigned32):
    """Custom type rprFairnessSTQLowWaterMark based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RprFairnessSTQLowWaterMark_Type.__name__ = "Unsigned32"
_RprFairnessSTQLowWaterMark_Object = MibTableColumn
rprFairnessSTQLowWaterMark = _RprFairnessSTQLowWaterMark_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 19),
    _RprFairnessSTQLowWaterMark_Type()
)
rprFairnessSTQLowWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprFairnessSTQLowWaterMark.setStatus("current")
if mibBuilder.loadTexts:
    rprFairnessSTQLowWaterMark.setUnits("Tenth of percent")
_RprFairnessLastChange_Type = TimeStamp
_RprFairnessLastChange_Object = MibTableColumn
rprFairnessLastChange = _RprFairnessLastChange_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 20),
    _RprFairnessLastChange_Type()
)
rprFairnessLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprFairnessLastChange.setStatus("current")
_RprFairnessChanges_Type = Counter32
_RprFairnessChanges_Object = MibTableColumn
rprFairnessChanges = _RprFairnessChanges_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 2, 1, 21),
    _RprFairnessChanges_Type()
)
rprFairnessChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprFairnessChanges.setStatus("current")
_RprOamTable_Object = MibTable
rprOamTable = _RprOamTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    rprOamTable.setStatus("current")
_RprOamEntry_Object = MibTableRow
rprOamEntry = _RprOamEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3, 1)
)
rprOamEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprOamIfIndex"),
)
if mibBuilder.loadTexts:
    rprOamEntry.setStatus("current")
_RprOamIfIndex_Type = InterfaceIndex
_RprOamIfIndex_Object = MibTableColumn
rprOamIfIndex = _RprOamIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3, 1, 1),
    _RprOamIfIndex_Type()
)
rprOamIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprOamIfIndex.setStatus("current")


class _RprOamActionType_Type(Integer32):
    """Custom type rprOamActionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("echo", 1),
          ("flush", 2))
    )


_RprOamActionType_Type.__name__ = "Integer32"
_RprOamActionType_Object = MibTableColumn
rprOamActionType = _RprOamActionType_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3, 1, 2),
    _RprOamActionType_Type()
)
rprOamActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprOamActionType.setStatus("current")
_RprOamDestAddress_Type = MacAddress
_RprOamDestAddress_Object = MibTableColumn
rprOamDestAddress = _RprOamDestAddress_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3, 1, 3),
    _RprOamDestAddress_Type()
)
rprOamDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprOamDestAddress.setStatus("current")


class _RprOamRequestRinglet_Type(RprOamRinglet):
    """Custom type rprOamRequestRinglet based on RprOamRinglet"""


_RprOamRequestRinglet_Object = MibTableColumn
rprOamRequestRinglet = _RprOamRequestRinglet_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3, 1, 4),
    _RprOamRequestRinglet_Type()
)
rprOamRequestRinglet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprOamRequestRinglet.setStatus("current")


class _RprOamResponseRinglet_Type(RprOamRinglet):
    """Custom type rprOamResponseRinglet based on RprOamRinglet"""


_RprOamResponseRinglet_Object = MibTableColumn
rprOamResponseRinglet = _RprOamResponseRinglet_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3, 1, 5),
    _RprOamResponseRinglet_Type()
)
rprOamResponseRinglet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprOamResponseRinglet.setStatus("current")


class _RprOamClassOfService_Type(Integer32):
    """Custom type rprOamClassOfService based on Integer32"""
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
        *(("classA", 1),
          ("classB", 2),
          ("classC", 3))
    )


_RprOamClassOfService_Type.__name__ = "Integer32"
_RprOamClassOfService_Object = MibTableColumn
rprOamClassOfService = _RprOamClassOfService_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3, 1, 6),
    _RprOamClassOfService_Type()
)
rprOamClassOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprOamClassOfService.setStatus("current")


class _RprOamUserData_Type(OctetString):
    """Custom type rprOamUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_RprOamUserData_Type.__name__ = "OctetString"
_RprOamUserData_Object = MibTableColumn
rprOamUserData = _RprOamUserData_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3, 1, 7),
    _RprOamUserData_Type()
)
rprOamUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprOamUserData.setStatus("current")


class _RprOamProtected_Type(TruthValue):
    """Custom type rprOamProtected based on TruthValue"""


_RprOamProtected_Object = MibTableColumn
rprOamProtected = _RprOamProtected_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3, 1, 8),
    _RprOamProtected_Type()
)
rprOamProtected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprOamProtected.setStatus("current")


class _RprOamRequestCount_Type(Unsigned32):
    """Custom type rprOamRequestCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RprOamRequestCount_Type.__name__ = "Unsigned32"
_RprOamRequestCount_Object = MibTableColumn
rprOamRequestCount = _RprOamRequestCount_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3, 1, 9),
    _RprOamRequestCount_Type()
)
rprOamRequestCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprOamRequestCount.setStatus("current")


class _RprOamTimeout_Type(Unsigned32):
    """Custom type rprOamTimeout based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_RprOamTimeout_Type.__name__ = "Unsigned32"
_RprOamTimeout_Object = MibTableColumn
rprOamTimeout = _RprOamTimeout_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3, 1, 10),
    _RprOamTimeout_Type()
)
rprOamTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprOamTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rprOamTimeout.setUnits("10usec")


class _RprOamControl_Type(Integer32):
    """Custom type rprOamControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abort", 3),
          ("active", 2),
          ("idle", 1))
    )


_RprOamControl_Type.__name__ = "Integer32"
_RprOamControl_Object = MibTableColumn
rprOamControl = _RprOamControl_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3, 1, 11),
    _RprOamControl_Type()
)
rprOamControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rprOamControl.setStatus("current")


class _RprOamResponseCount_Type(Unsigned32):
    """Custom type rprOamResponseCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RprOamResponseCount_Type.__name__ = "Unsigned32"
_RprOamResponseCount_Object = MibTableColumn
rprOamResponseCount = _RprOamResponseCount_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3, 1, 12),
    _RprOamResponseCount_Type()
)
rprOamResponseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprOamResponseCount.setStatus("current")


class _RprOamAvResponseTime_Type(Unsigned32):
    """Custom type rprOamAvResponseTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RprOamAvResponseTime_Type.__name__ = "Unsigned32"
_RprOamAvResponseTime_Object = MibTableColumn
rprOamAvResponseTime = _RprOamAvResponseTime_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3, 1, 13),
    _RprOamAvResponseTime_Type()
)
rprOamAvResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprOamAvResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    rprOamAvResponseTime.setUnits("10usec")


class _RprOamResponseStatus_Type(Integer32):
    """Custom type rprOamResponseStatus based on Integer32"""
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
        *(("error", 3),
          ("inProcess", 2),
          ("success", 4),
          ("unknown", 1))
    )


_RprOamResponseStatus_Type.__name__ = "Integer32"
_RprOamResponseStatus_Object = MibTableColumn
rprOamResponseStatus = _RprOamResponseStatus_Object(
    (1, 0, 8802, 17, 1, 1, 1, 2, 3, 1, 14),
    _RprOamResponseStatus_Type()
)
rprOamResponseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprOamResponseStatus.setStatus("current")
_RprSpanCounters_ObjectIdentity = ObjectIdentity
rprSpanCounters = _RprSpanCounters_ObjectIdentity(
    (1, 0, 8802, 17, 1, 1, 1, 3)
)
_RprSpanCountersCurrentTable_Object = MibTable
rprSpanCountersCurrentTable = _RprSpanCountersCurrentTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rprSpanCountersCurrentTable.setStatus("current")
_RprSpanCountersCurrentEntry_Object = MibTableRow
rprSpanCountersCurrentEntry = _RprSpanCountersCurrentEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1)
)
rprSpanCountersCurrentEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanCurrentIfIndex"),
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanCurrentSpan"),
)
if mibBuilder.loadTexts:
    rprSpanCountersCurrentEntry.setStatus("current")
_RprSpanCurrentIfIndex_Type = InterfaceIndex
_RprSpanCurrentIfIndex_Object = MibTableColumn
rprSpanCurrentIfIndex = _RprSpanCurrentIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 1),
    _RprSpanCurrentIfIndex_Type()
)
rprSpanCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanCurrentIfIndex.setStatus("current")
_RprSpanCurrentSpan_Type = RprSpan
_RprSpanCurrentSpan_Object = MibTableColumn
rprSpanCurrentSpan = _RprSpanCurrentSpan_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 2),
    _RprSpanCurrentSpan_Type()
)
rprSpanCurrentSpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanCurrentSpan.setStatus("current")
_RprSpanCurrentInUcastClassAFrames_Type = HCPerfCurrentCount
_RprSpanCurrentInUcastClassAFrames_Object = MibTableColumn
rprSpanCurrentInUcastClassAFrames = _RprSpanCurrentInUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 3),
    _RprSpanCurrentInUcastClassAFrames_Type()
)
rprSpanCurrentInUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInUcastClassAFrames.setStatus("current")
_RprSpanCurrentInUcastClassAOctets_Type = HCPerfCurrentCount
_RprSpanCurrentInUcastClassAOctets_Object = MibTableColumn
rprSpanCurrentInUcastClassAOctets = _RprSpanCurrentInUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 4),
    _RprSpanCurrentInUcastClassAOctets_Type()
)
rprSpanCurrentInUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInUcastClassAOctets.setStatus("current")
_RprSpanCurrentInUcastClassBCirFrames_Type = HCPerfCurrentCount
_RprSpanCurrentInUcastClassBCirFrames_Object = MibTableColumn
rprSpanCurrentInUcastClassBCirFrames = _RprSpanCurrentInUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 5),
    _RprSpanCurrentInUcastClassBCirFrames_Type()
)
rprSpanCurrentInUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInUcastClassBCirFrames.setStatus("current")
_RprSpanCurrentInUcastClassBCirOctets_Type = HCPerfCurrentCount
_RprSpanCurrentInUcastClassBCirOctets_Object = MibTableColumn
rprSpanCurrentInUcastClassBCirOctets = _RprSpanCurrentInUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 6),
    _RprSpanCurrentInUcastClassBCirOctets_Type()
)
rprSpanCurrentInUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInUcastClassBCirOctets.setStatus("current")
_RprSpanCurrentInUcastClassBEirFrames_Type = HCPerfCurrentCount
_RprSpanCurrentInUcastClassBEirFrames_Object = MibTableColumn
rprSpanCurrentInUcastClassBEirFrames = _RprSpanCurrentInUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 7),
    _RprSpanCurrentInUcastClassBEirFrames_Type()
)
rprSpanCurrentInUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInUcastClassBEirFrames.setStatus("current")
_RprSpanCurrentInUcastClassBEirOctets_Type = HCPerfCurrentCount
_RprSpanCurrentInUcastClassBEirOctets_Object = MibTableColumn
rprSpanCurrentInUcastClassBEirOctets = _RprSpanCurrentInUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 8),
    _RprSpanCurrentInUcastClassBEirOctets_Type()
)
rprSpanCurrentInUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInUcastClassBEirOctets.setStatus("current")
_RprSpanCurrentInUcastClassCFrames_Type = HCPerfCurrentCount
_RprSpanCurrentInUcastClassCFrames_Object = MibTableColumn
rprSpanCurrentInUcastClassCFrames = _RprSpanCurrentInUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 9),
    _RprSpanCurrentInUcastClassCFrames_Type()
)
rprSpanCurrentInUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInUcastClassCFrames.setStatus("current")
_RprSpanCurrentInUcastClassCOctets_Type = HCPerfCurrentCount
_RprSpanCurrentInUcastClassCOctets_Object = MibTableColumn
rprSpanCurrentInUcastClassCOctets = _RprSpanCurrentInUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 10),
    _RprSpanCurrentInUcastClassCOctets_Type()
)
rprSpanCurrentInUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInUcastClassCOctets.setStatus("current")
_RprSpanCurrentInMcastClassAFrames_Type = HCPerfCurrentCount
_RprSpanCurrentInMcastClassAFrames_Object = MibTableColumn
rprSpanCurrentInMcastClassAFrames = _RprSpanCurrentInMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 11),
    _RprSpanCurrentInMcastClassAFrames_Type()
)
rprSpanCurrentInMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInMcastClassAFrames.setStatus("current")
_RprSpanCurrentInMcastClassAOctets_Type = HCPerfCurrentCount
_RprSpanCurrentInMcastClassAOctets_Object = MibTableColumn
rprSpanCurrentInMcastClassAOctets = _RprSpanCurrentInMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 12),
    _RprSpanCurrentInMcastClassAOctets_Type()
)
rprSpanCurrentInMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInMcastClassAOctets.setStatus("current")
_RprSpanCurrentInMcastClassBCirFrames_Type = HCPerfCurrentCount
_RprSpanCurrentInMcastClassBCirFrames_Object = MibTableColumn
rprSpanCurrentInMcastClassBCirFrames = _RprSpanCurrentInMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 13),
    _RprSpanCurrentInMcastClassBCirFrames_Type()
)
rprSpanCurrentInMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInMcastClassBCirFrames.setStatus("current")
_RprSpanCurrentInMcastClassBCirOctets_Type = HCPerfCurrentCount
_RprSpanCurrentInMcastClassBCirOctets_Object = MibTableColumn
rprSpanCurrentInMcastClassBCirOctets = _RprSpanCurrentInMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 14),
    _RprSpanCurrentInMcastClassBCirOctets_Type()
)
rprSpanCurrentInMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInMcastClassBCirOctets.setStatus("current")
_RprSpanCurrentInMcastClassBEirFrames_Type = HCPerfCurrentCount
_RprSpanCurrentInMcastClassBEirFrames_Object = MibTableColumn
rprSpanCurrentInMcastClassBEirFrames = _RprSpanCurrentInMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 15),
    _RprSpanCurrentInMcastClassBEirFrames_Type()
)
rprSpanCurrentInMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInMcastClassBEirFrames.setStatus("current")
_RprSpanCurrentInMcastClassBEirOctets_Type = HCPerfCurrentCount
_RprSpanCurrentInMcastClassBEirOctets_Object = MibTableColumn
rprSpanCurrentInMcastClassBEirOctets = _RprSpanCurrentInMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 16),
    _RprSpanCurrentInMcastClassBEirOctets_Type()
)
rprSpanCurrentInMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInMcastClassBEirOctets.setStatus("current")
_RprSpanCurrentInMcastClassCFrames_Type = HCPerfCurrentCount
_RprSpanCurrentInMcastClassCFrames_Object = MibTableColumn
rprSpanCurrentInMcastClassCFrames = _RprSpanCurrentInMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 17),
    _RprSpanCurrentInMcastClassCFrames_Type()
)
rprSpanCurrentInMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInMcastClassCFrames.setStatus("current")
_RprSpanCurrentInMcastClassCOctets_Type = HCPerfCurrentCount
_RprSpanCurrentInMcastClassCOctets_Object = MibTableColumn
rprSpanCurrentInMcastClassCOctets = _RprSpanCurrentInMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 18),
    _RprSpanCurrentInMcastClassCOctets_Type()
)
rprSpanCurrentInMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentInMcastClassCOctets.setStatus("current")
_RprSpanCurrentOutUcastClassAFrames_Type = HCPerfCurrentCount
_RprSpanCurrentOutUcastClassAFrames_Object = MibTableColumn
rprSpanCurrentOutUcastClassAFrames = _RprSpanCurrentOutUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 19),
    _RprSpanCurrentOutUcastClassAFrames_Type()
)
rprSpanCurrentOutUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutUcastClassAFrames.setStatus("current")
_RprSpanCurrentOutUcastClassAOctets_Type = HCPerfCurrentCount
_RprSpanCurrentOutUcastClassAOctets_Object = MibTableColumn
rprSpanCurrentOutUcastClassAOctets = _RprSpanCurrentOutUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 20),
    _RprSpanCurrentOutUcastClassAOctets_Type()
)
rprSpanCurrentOutUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutUcastClassAOctets.setStatus("current")
_RprSpanCurrentOutUcastClassBCirFrames_Type = HCPerfCurrentCount
_RprSpanCurrentOutUcastClassBCirFrames_Object = MibTableColumn
rprSpanCurrentOutUcastClassBCirFrames = _RprSpanCurrentOutUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 21),
    _RprSpanCurrentOutUcastClassBCirFrames_Type()
)
rprSpanCurrentOutUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutUcastClassBCirFrames.setStatus("current")
_RprSpanCurrentOutUcastClassBCirOctets_Type = HCPerfCurrentCount
_RprSpanCurrentOutUcastClassBCirOctets_Object = MibTableColumn
rprSpanCurrentOutUcastClassBCirOctets = _RprSpanCurrentOutUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 22),
    _RprSpanCurrentOutUcastClassBCirOctets_Type()
)
rprSpanCurrentOutUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutUcastClassBCirOctets.setStatus("current")
_RprSpanCurrentOutUcastClassBEirFrames_Type = HCPerfCurrentCount
_RprSpanCurrentOutUcastClassBEirFrames_Object = MibTableColumn
rprSpanCurrentOutUcastClassBEirFrames = _RprSpanCurrentOutUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 23),
    _RprSpanCurrentOutUcastClassBEirFrames_Type()
)
rprSpanCurrentOutUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutUcastClassBEirFrames.setStatus("current")
_RprSpanCurrentOutUcastClassBEirOctets_Type = HCPerfCurrentCount
_RprSpanCurrentOutUcastClassBEirOctets_Object = MibTableColumn
rprSpanCurrentOutUcastClassBEirOctets = _RprSpanCurrentOutUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 24),
    _RprSpanCurrentOutUcastClassBEirOctets_Type()
)
rprSpanCurrentOutUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutUcastClassBEirOctets.setStatus("current")
_RprSpanCurrentOutUcastClassCFrames_Type = HCPerfCurrentCount
_RprSpanCurrentOutUcastClassCFrames_Object = MibTableColumn
rprSpanCurrentOutUcastClassCFrames = _RprSpanCurrentOutUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 25),
    _RprSpanCurrentOutUcastClassCFrames_Type()
)
rprSpanCurrentOutUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutUcastClassCFrames.setStatus("current")
_RprSpanCurrentOutUcastClassCOctets_Type = HCPerfCurrentCount
_RprSpanCurrentOutUcastClassCOctets_Object = MibTableColumn
rprSpanCurrentOutUcastClassCOctets = _RprSpanCurrentOutUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 26),
    _RprSpanCurrentOutUcastClassCOctets_Type()
)
rprSpanCurrentOutUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutUcastClassCOctets.setStatus("current")
_RprSpanCurrentOutMcastClassAFrames_Type = HCPerfCurrentCount
_RprSpanCurrentOutMcastClassAFrames_Object = MibTableColumn
rprSpanCurrentOutMcastClassAFrames = _RprSpanCurrentOutMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 27),
    _RprSpanCurrentOutMcastClassAFrames_Type()
)
rprSpanCurrentOutMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutMcastClassAFrames.setStatus("current")
_RprSpanCurrentOutMcastClassAOctets_Type = HCPerfCurrentCount
_RprSpanCurrentOutMcastClassAOctets_Object = MibTableColumn
rprSpanCurrentOutMcastClassAOctets = _RprSpanCurrentOutMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 28),
    _RprSpanCurrentOutMcastClassAOctets_Type()
)
rprSpanCurrentOutMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutMcastClassAOctets.setStatus("current")
_RprSpanCurrentOutMcastClassBCirFrames_Type = HCPerfCurrentCount
_RprSpanCurrentOutMcastClassBCirFrames_Object = MibTableColumn
rprSpanCurrentOutMcastClassBCirFrames = _RprSpanCurrentOutMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 29),
    _RprSpanCurrentOutMcastClassBCirFrames_Type()
)
rprSpanCurrentOutMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutMcastClassBCirFrames.setStatus("current")
_RprSpanCurrentOutMcastClassBCirOctets_Type = HCPerfCurrentCount
_RprSpanCurrentOutMcastClassBCirOctets_Object = MibTableColumn
rprSpanCurrentOutMcastClassBCirOctets = _RprSpanCurrentOutMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 30),
    _RprSpanCurrentOutMcastClassBCirOctets_Type()
)
rprSpanCurrentOutMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutMcastClassBCirOctets.setStatus("current")
_RprSpanCurrentOutMcastClassBEirFrames_Type = HCPerfCurrentCount
_RprSpanCurrentOutMcastClassBEirFrames_Object = MibTableColumn
rprSpanCurrentOutMcastClassBEirFrames = _RprSpanCurrentOutMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 31),
    _RprSpanCurrentOutMcastClassBEirFrames_Type()
)
rprSpanCurrentOutMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutMcastClassBEirFrames.setStatus("current")
_RprSpanCurrentOutMcastClassBEirOctets_Type = HCPerfCurrentCount
_RprSpanCurrentOutMcastClassBEirOctets_Object = MibTableColumn
rprSpanCurrentOutMcastClassBEirOctets = _RprSpanCurrentOutMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 32),
    _RprSpanCurrentOutMcastClassBEirOctets_Type()
)
rprSpanCurrentOutMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutMcastClassBEirOctets.setStatus("current")
_RprSpanCurrentOutMcastClassCFrames_Type = HCPerfCurrentCount
_RprSpanCurrentOutMcastClassCFrames_Object = MibTableColumn
rprSpanCurrentOutMcastClassCFrames = _RprSpanCurrentOutMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 33),
    _RprSpanCurrentOutMcastClassCFrames_Type()
)
rprSpanCurrentOutMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutMcastClassCFrames.setStatus("current")
_RprSpanCurrentOutMcastClassCOctets_Type = HCPerfCurrentCount
_RprSpanCurrentOutMcastClassCOctets_Object = MibTableColumn
rprSpanCurrentOutMcastClassCOctets = _RprSpanCurrentOutMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 1, 1, 34),
    _RprSpanCurrentOutMcastClassCOctets_Type()
)
rprSpanCurrentOutMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanCurrentOutMcastClassCOctets.setStatus("current")
_RprSpanCountersIntervalTable_Object = MibTable
rprSpanCountersIntervalTable = _RprSpanCountersIntervalTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    rprSpanCountersIntervalTable.setStatus("current")
_RprSpanCountersIntervalEntry_Object = MibTableRow
rprSpanCountersIntervalEntry = _RprSpanCountersIntervalEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1)
)
rprSpanCountersIntervalEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanIntervalIfIndex"),
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanIntervalSpan"),
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanIntervalNumber"),
)
if mibBuilder.loadTexts:
    rprSpanCountersIntervalEntry.setStatus("current")
_RprSpanIntervalIfIndex_Type = InterfaceIndex
_RprSpanIntervalIfIndex_Object = MibTableColumn
rprSpanIntervalIfIndex = _RprSpanIntervalIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 1),
    _RprSpanIntervalIfIndex_Type()
)
rprSpanIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanIntervalIfIndex.setStatus("current")
_RprSpanIntervalSpan_Type = RprSpan
_RprSpanIntervalSpan_Object = MibTableColumn
rprSpanIntervalSpan = _RprSpanIntervalSpan_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 2),
    _RprSpanIntervalSpan_Type()
)
rprSpanIntervalSpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanIntervalSpan.setStatus("current")


class _RprSpanIntervalNumber_Type(Unsigned32):
    """Custom type rprSpanIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_RprSpanIntervalNumber_Type.__name__ = "Unsigned32"
_RprSpanIntervalNumber_Object = MibTableColumn
rprSpanIntervalNumber = _RprSpanIntervalNumber_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 3),
    _RprSpanIntervalNumber_Type()
)
rprSpanIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanIntervalNumber.setStatus("current")
_RprSpanIntervalValidData_Type = TruthValue
_RprSpanIntervalValidData_Object = MibTableColumn
rprSpanIntervalValidData = _RprSpanIntervalValidData_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 4),
    _RprSpanIntervalValidData_Type()
)
rprSpanIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalValidData.setStatus("current")


class _RprSpanIntervalTimeElapsed_Type(Unsigned32):
    """Custom type rprSpanIntervalTimeElapsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_RprSpanIntervalTimeElapsed_Type.__name__ = "Unsigned32"
_RprSpanIntervalTimeElapsed_Object = MibTableColumn
rprSpanIntervalTimeElapsed = _RprSpanIntervalTimeElapsed_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 5),
    _RprSpanIntervalTimeElapsed_Type()
)
rprSpanIntervalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    rprSpanIntervalTimeElapsed.setUnits("Seconds")
_RprSpanIntervalStartTime_Type = DateAndTime
_RprSpanIntervalStartTime_Object = MibTableColumn
rprSpanIntervalStartTime = _RprSpanIntervalStartTime_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 6),
    _RprSpanIntervalStartTime_Type()
)
rprSpanIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalStartTime.setStatus("current")
_RprSpanIntervalInUcastClassAFrames_Type = HCPerfIntervalCount
_RprSpanIntervalInUcastClassAFrames_Object = MibTableColumn
rprSpanIntervalInUcastClassAFrames = _RprSpanIntervalInUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 7),
    _RprSpanIntervalInUcastClassAFrames_Type()
)
rprSpanIntervalInUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInUcastClassAFrames.setStatus("current")
_RprSpanIntervalInUcastClassAOctets_Type = HCPerfIntervalCount
_RprSpanIntervalInUcastClassAOctets_Object = MibTableColumn
rprSpanIntervalInUcastClassAOctets = _RprSpanIntervalInUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 8),
    _RprSpanIntervalInUcastClassAOctets_Type()
)
rprSpanIntervalInUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInUcastClassAOctets.setStatus("current")
_RprSpanIntervalInUcastClassBCirFrames_Type = HCPerfIntervalCount
_RprSpanIntervalInUcastClassBCirFrames_Object = MibTableColumn
rprSpanIntervalInUcastClassBCirFrames = _RprSpanIntervalInUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 9),
    _RprSpanIntervalInUcastClassBCirFrames_Type()
)
rprSpanIntervalInUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInUcastClassBCirFrames.setStatus("current")
_RprSpanIntervalInUcastClassBCirOctets_Type = HCPerfIntervalCount
_RprSpanIntervalInUcastClassBCirOctets_Object = MibTableColumn
rprSpanIntervalInUcastClassBCirOctets = _RprSpanIntervalInUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 10),
    _RprSpanIntervalInUcastClassBCirOctets_Type()
)
rprSpanIntervalInUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInUcastClassBCirOctets.setStatus("current")
_RprSpanIntervalInUcastClassBEirFrames_Type = HCPerfIntervalCount
_RprSpanIntervalInUcastClassBEirFrames_Object = MibTableColumn
rprSpanIntervalInUcastClassBEirFrames = _RprSpanIntervalInUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 11),
    _RprSpanIntervalInUcastClassBEirFrames_Type()
)
rprSpanIntervalInUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInUcastClassBEirFrames.setStatus("current")
_RprSpanIntervalInUcastClassBEirOctets_Type = HCPerfIntervalCount
_RprSpanIntervalInUcastClassBEirOctets_Object = MibTableColumn
rprSpanIntervalInUcastClassBEirOctets = _RprSpanIntervalInUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 12),
    _RprSpanIntervalInUcastClassBEirOctets_Type()
)
rprSpanIntervalInUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInUcastClassBEirOctets.setStatus("current")
_RprSpanIntervalInUcastClassCFrames_Type = HCPerfIntervalCount
_RprSpanIntervalInUcastClassCFrames_Object = MibTableColumn
rprSpanIntervalInUcastClassCFrames = _RprSpanIntervalInUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 13),
    _RprSpanIntervalInUcastClassCFrames_Type()
)
rprSpanIntervalInUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInUcastClassCFrames.setStatus("current")
_RprSpanIntervalInUcastClassCOctets_Type = HCPerfIntervalCount
_RprSpanIntervalInUcastClassCOctets_Object = MibTableColumn
rprSpanIntervalInUcastClassCOctets = _RprSpanIntervalInUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 14),
    _RprSpanIntervalInUcastClassCOctets_Type()
)
rprSpanIntervalInUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInUcastClassCOctets.setStatus("current")
_RprSpanIntervalInMcastClassAFrames_Type = HCPerfIntervalCount
_RprSpanIntervalInMcastClassAFrames_Object = MibTableColumn
rprSpanIntervalInMcastClassAFrames = _RprSpanIntervalInMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 15),
    _RprSpanIntervalInMcastClassAFrames_Type()
)
rprSpanIntervalInMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInMcastClassAFrames.setStatus("current")
_RprSpanIntervalInMcastClassAOctets_Type = HCPerfIntervalCount
_RprSpanIntervalInMcastClassAOctets_Object = MibTableColumn
rprSpanIntervalInMcastClassAOctets = _RprSpanIntervalInMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 16),
    _RprSpanIntervalInMcastClassAOctets_Type()
)
rprSpanIntervalInMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInMcastClassAOctets.setStatus("current")
_RprSpanIntervalInMcastClassBCirFrames_Type = HCPerfIntervalCount
_RprSpanIntervalInMcastClassBCirFrames_Object = MibTableColumn
rprSpanIntervalInMcastClassBCirFrames = _RprSpanIntervalInMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 17),
    _RprSpanIntervalInMcastClassBCirFrames_Type()
)
rprSpanIntervalInMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInMcastClassBCirFrames.setStatus("current")
_RprSpanIntervalInMcastClassBCirOctets_Type = HCPerfIntervalCount
_RprSpanIntervalInMcastClassBCirOctets_Object = MibTableColumn
rprSpanIntervalInMcastClassBCirOctets = _RprSpanIntervalInMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 18),
    _RprSpanIntervalInMcastClassBCirOctets_Type()
)
rprSpanIntervalInMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInMcastClassBCirOctets.setStatus("current")
_RprSpanIntervalInMcastClassBEirFrames_Type = HCPerfIntervalCount
_RprSpanIntervalInMcastClassBEirFrames_Object = MibTableColumn
rprSpanIntervalInMcastClassBEirFrames = _RprSpanIntervalInMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 19),
    _RprSpanIntervalInMcastClassBEirFrames_Type()
)
rprSpanIntervalInMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInMcastClassBEirFrames.setStatus("current")
_RprSpanIntervalInMcastClassBEirOctets_Type = HCPerfIntervalCount
_RprSpanIntervalInMcastClassBEirOctets_Object = MibTableColumn
rprSpanIntervalInMcastClassBEirOctets = _RprSpanIntervalInMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 20),
    _RprSpanIntervalInMcastClassBEirOctets_Type()
)
rprSpanIntervalInMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInMcastClassBEirOctets.setStatus("current")
_RprSpanIntervalInMcastClassCFrames_Type = HCPerfIntervalCount
_RprSpanIntervalInMcastClassCFrames_Object = MibTableColumn
rprSpanIntervalInMcastClassCFrames = _RprSpanIntervalInMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 21),
    _RprSpanIntervalInMcastClassCFrames_Type()
)
rprSpanIntervalInMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInMcastClassCFrames.setStatus("current")
_RprSpanIntervalInMcastClassCOctets_Type = HCPerfIntervalCount
_RprSpanIntervalInMcastClassCOctets_Object = MibTableColumn
rprSpanIntervalInMcastClassCOctets = _RprSpanIntervalInMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 22),
    _RprSpanIntervalInMcastClassCOctets_Type()
)
rprSpanIntervalInMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalInMcastClassCOctets.setStatus("current")
_RprSpanIntervalOutUcastClassAFrames_Type = HCPerfIntervalCount
_RprSpanIntervalOutUcastClassAFrames_Object = MibTableColumn
rprSpanIntervalOutUcastClassAFrames = _RprSpanIntervalOutUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 23),
    _RprSpanIntervalOutUcastClassAFrames_Type()
)
rprSpanIntervalOutUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutUcastClassAFrames.setStatus("current")
_RprSpanIntervalOutUcastClassAOctets_Type = HCPerfIntervalCount
_RprSpanIntervalOutUcastClassAOctets_Object = MibTableColumn
rprSpanIntervalOutUcastClassAOctets = _RprSpanIntervalOutUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 24),
    _RprSpanIntervalOutUcastClassAOctets_Type()
)
rprSpanIntervalOutUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutUcastClassAOctets.setStatus("current")
_RprSpanIntervalOutUcastClassBCirFrames_Type = HCPerfIntervalCount
_RprSpanIntervalOutUcastClassBCirFrames_Object = MibTableColumn
rprSpanIntervalOutUcastClassBCirFrames = _RprSpanIntervalOutUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 25),
    _RprSpanIntervalOutUcastClassBCirFrames_Type()
)
rprSpanIntervalOutUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutUcastClassBCirFrames.setStatus("current")
_RprSpanIntervalOutUcastClassBCirOctets_Type = HCPerfIntervalCount
_RprSpanIntervalOutUcastClassBCirOctets_Object = MibTableColumn
rprSpanIntervalOutUcastClassBCirOctets = _RprSpanIntervalOutUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 26),
    _RprSpanIntervalOutUcastClassBCirOctets_Type()
)
rprSpanIntervalOutUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutUcastClassBCirOctets.setStatus("current")
_RprSpanIntervalOutUcastClassBEirFrames_Type = HCPerfIntervalCount
_RprSpanIntervalOutUcastClassBEirFrames_Object = MibTableColumn
rprSpanIntervalOutUcastClassBEirFrames = _RprSpanIntervalOutUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 27),
    _RprSpanIntervalOutUcastClassBEirFrames_Type()
)
rprSpanIntervalOutUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutUcastClassBEirFrames.setStatus("current")
_RprSpanIntervalOutUcastClassBEirOctets_Type = HCPerfIntervalCount
_RprSpanIntervalOutUcastClassBEirOctets_Object = MibTableColumn
rprSpanIntervalOutUcastClassBEirOctets = _RprSpanIntervalOutUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 28),
    _RprSpanIntervalOutUcastClassBEirOctets_Type()
)
rprSpanIntervalOutUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutUcastClassBEirOctets.setStatus("current")
_RprSpanIntervalOutUcastClassCFrames_Type = HCPerfIntervalCount
_RprSpanIntervalOutUcastClassCFrames_Object = MibTableColumn
rprSpanIntervalOutUcastClassCFrames = _RprSpanIntervalOutUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 29),
    _RprSpanIntervalOutUcastClassCFrames_Type()
)
rprSpanIntervalOutUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutUcastClassCFrames.setStatus("current")
_RprSpanIntervalOutUcastClassCOctets_Type = HCPerfIntervalCount
_RprSpanIntervalOutUcastClassCOctets_Object = MibTableColumn
rprSpanIntervalOutUcastClassCOctets = _RprSpanIntervalOutUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 30),
    _RprSpanIntervalOutUcastClassCOctets_Type()
)
rprSpanIntervalOutUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutUcastClassCOctets.setStatus("current")
_RprSpanIntervalOutMcastClassAFrames_Type = HCPerfIntervalCount
_RprSpanIntervalOutMcastClassAFrames_Object = MibTableColumn
rprSpanIntervalOutMcastClassAFrames = _RprSpanIntervalOutMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 31),
    _RprSpanIntervalOutMcastClassAFrames_Type()
)
rprSpanIntervalOutMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutMcastClassAFrames.setStatus("current")
_RprSpanIntervalOutMcastClassAOctets_Type = HCPerfIntervalCount
_RprSpanIntervalOutMcastClassAOctets_Object = MibTableColumn
rprSpanIntervalOutMcastClassAOctets = _RprSpanIntervalOutMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 32),
    _RprSpanIntervalOutMcastClassAOctets_Type()
)
rprSpanIntervalOutMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutMcastClassAOctets.setStatus("current")
_RprSpanIntervalOutMcastClassBCirFrames_Type = HCPerfIntervalCount
_RprSpanIntervalOutMcastClassBCirFrames_Object = MibTableColumn
rprSpanIntervalOutMcastClassBCirFrames = _RprSpanIntervalOutMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 33),
    _RprSpanIntervalOutMcastClassBCirFrames_Type()
)
rprSpanIntervalOutMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutMcastClassBCirFrames.setStatus("current")
_RprSpanIntervalOutMcastClassBCirOctets_Type = HCPerfIntervalCount
_RprSpanIntervalOutMcastClassBCirOctets_Object = MibTableColumn
rprSpanIntervalOutMcastClassBCirOctets = _RprSpanIntervalOutMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 34),
    _RprSpanIntervalOutMcastClassBCirOctets_Type()
)
rprSpanIntervalOutMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutMcastClassBCirOctets.setStatus("current")
_RprSpanIntervalOutMcastClassBEirFrames_Type = HCPerfIntervalCount
_RprSpanIntervalOutMcastClassBEirFrames_Object = MibTableColumn
rprSpanIntervalOutMcastClassBEirFrames = _RprSpanIntervalOutMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 35),
    _RprSpanIntervalOutMcastClassBEirFrames_Type()
)
rprSpanIntervalOutMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutMcastClassBEirFrames.setStatus("current")
_RprSpanIntervalOutMcastClassBEirOctets_Type = HCPerfIntervalCount
_RprSpanIntervalOutMcastClassBEirOctets_Object = MibTableColumn
rprSpanIntervalOutMcastClassBEirOctets = _RprSpanIntervalOutMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 36),
    _RprSpanIntervalOutMcastClassBEirOctets_Type()
)
rprSpanIntervalOutMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutMcastClassBEirOctets.setStatus("current")
_RprSpanIntervalOutMcastClassCFrames_Type = HCPerfIntervalCount
_RprSpanIntervalOutMcastClassCFrames_Object = MibTableColumn
rprSpanIntervalOutMcastClassCFrames = _RprSpanIntervalOutMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 37),
    _RprSpanIntervalOutMcastClassCFrames_Type()
)
rprSpanIntervalOutMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutMcastClassCFrames.setStatus("current")
_RprSpanIntervalOutMcastClassCOctets_Type = HCPerfIntervalCount
_RprSpanIntervalOutMcastClassCOctets_Object = MibTableColumn
rprSpanIntervalOutMcastClassCOctets = _RprSpanIntervalOutMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 2, 1, 38),
    _RprSpanIntervalOutMcastClassCOctets_Type()
)
rprSpanIntervalOutMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanIntervalOutMcastClassCOctets.setStatus("current")
_RprSpanCountersDayTable_Object = MibTable
rprSpanCountersDayTable = _RprSpanCountersDayTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    rprSpanCountersDayTable.setStatus("current")
_RprSpanCountersDayEntry_Object = MibTableRow
rprSpanCountersDayEntry = _RprSpanCountersDayEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1)
)
rprSpanCountersDayEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanDayIfIndex"),
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanDaySpan"),
)
if mibBuilder.loadTexts:
    rprSpanCountersDayEntry.setStatus("current")
_RprSpanDayIfIndex_Type = InterfaceIndex
_RprSpanDayIfIndex_Object = MibTableColumn
rprSpanDayIfIndex = _RprSpanDayIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 1),
    _RprSpanDayIfIndex_Type()
)
rprSpanDayIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanDayIfIndex.setStatus("current")
_RprSpanDaySpan_Type = RprSpan
_RprSpanDaySpan_Object = MibTableColumn
rprSpanDaySpan = _RprSpanDaySpan_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 2),
    _RprSpanDaySpan_Type()
)
rprSpanDaySpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanDaySpan.setStatus("current")
_RprSpanDayInUcastClassAFrames_Type = HCPerfTotalCount
_RprSpanDayInUcastClassAFrames_Object = MibTableColumn
rprSpanDayInUcastClassAFrames = _RprSpanDayInUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 3),
    _RprSpanDayInUcastClassAFrames_Type()
)
rprSpanDayInUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInUcastClassAFrames.setStatus("current")
_RprSpanDayInUcastClassAOctets_Type = HCPerfTotalCount
_RprSpanDayInUcastClassAOctets_Object = MibTableColumn
rprSpanDayInUcastClassAOctets = _RprSpanDayInUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 4),
    _RprSpanDayInUcastClassAOctets_Type()
)
rprSpanDayInUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInUcastClassAOctets.setStatus("current")
_RprSpanDayInUcastClassBCirFrames_Type = HCPerfTotalCount
_RprSpanDayInUcastClassBCirFrames_Object = MibTableColumn
rprSpanDayInUcastClassBCirFrames = _RprSpanDayInUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 5),
    _RprSpanDayInUcastClassBCirFrames_Type()
)
rprSpanDayInUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInUcastClassBCirFrames.setStatus("current")
_RprSpanDayInUcastClassBCirOctets_Type = HCPerfTotalCount
_RprSpanDayInUcastClassBCirOctets_Object = MibTableColumn
rprSpanDayInUcastClassBCirOctets = _RprSpanDayInUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 6),
    _RprSpanDayInUcastClassBCirOctets_Type()
)
rprSpanDayInUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInUcastClassBCirOctets.setStatus("current")
_RprSpanDayInUcastClassBEirFrames_Type = HCPerfTotalCount
_RprSpanDayInUcastClassBEirFrames_Object = MibTableColumn
rprSpanDayInUcastClassBEirFrames = _RprSpanDayInUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 7),
    _RprSpanDayInUcastClassBEirFrames_Type()
)
rprSpanDayInUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInUcastClassBEirFrames.setStatus("current")
_RprSpanDayInUcastClassBEirOctets_Type = HCPerfTotalCount
_RprSpanDayInUcastClassBEirOctets_Object = MibTableColumn
rprSpanDayInUcastClassBEirOctets = _RprSpanDayInUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 8),
    _RprSpanDayInUcastClassBEirOctets_Type()
)
rprSpanDayInUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInUcastClassBEirOctets.setStatus("current")
_RprSpanDayInUcastClassCFrames_Type = HCPerfTotalCount
_RprSpanDayInUcastClassCFrames_Object = MibTableColumn
rprSpanDayInUcastClassCFrames = _RprSpanDayInUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 9),
    _RprSpanDayInUcastClassCFrames_Type()
)
rprSpanDayInUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInUcastClassCFrames.setStatus("current")
_RprSpanDayInUcastClassCOctets_Type = HCPerfTotalCount
_RprSpanDayInUcastClassCOctets_Object = MibTableColumn
rprSpanDayInUcastClassCOctets = _RprSpanDayInUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 10),
    _RprSpanDayInUcastClassCOctets_Type()
)
rprSpanDayInUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInUcastClassCOctets.setStatus("current")
_RprSpanDayInMcastClassAFrames_Type = HCPerfTotalCount
_RprSpanDayInMcastClassAFrames_Object = MibTableColumn
rprSpanDayInMcastClassAFrames = _RprSpanDayInMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 11),
    _RprSpanDayInMcastClassAFrames_Type()
)
rprSpanDayInMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInMcastClassAFrames.setStatus("current")
_RprSpanDayInMcastClassAOctets_Type = HCPerfTotalCount
_RprSpanDayInMcastClassAOctets_Object = MibTableColumn
rprSpanDayInMcastClassAOctets = _RprSpanDayInMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 12),
    _RprSpanDayInMcastClassAOctets_Type()
)
rprSpanDayInMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInMcastClassAOctets.setStatus("current")
_RprSpanDayInMcastClassBCirFrames_Type = HCPerfTotalCount
_RprSpanDayInMcastClassBCirFrames_Object = MibTableColumn
rprSpanDayInMcastClassBCirFrames = _RprSpanDayInMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 13),
    _RprSpanDayInMcastClassBCirFrames_Type()
)
rprSpanDayInMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInMcastClassBCirFrames.setStatus("current")
_RprSpanDayInMcastClassBCirOctets_Type = HCPerfTotalCount
_RprSpanDayInMcastClassBCirOctets_Object = MibTableColumn
rprSpanDayInMcastClassBCirOctets = _RprSpanDayInMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 14),
    _RprSpanDayInMcastClassBCirOctets_Type()
)
rprSpanDayInMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInMcastClassBCirOctets.setStatus("current")
_RprSpanDayInMcastClassBEirFrames_Type = HCPerfTotalCount
_RprSpanDayInMcastClassBEirFrames_Object = MibTableColumn
rprSpanDayInMcastClassBEirFrames = _RprSpanDayInMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 15),
    _RprSpanDayInMcastClassBEirFrames_Type()
)
rprSpanDayInMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInMcastClassBEirFrames.setStatus("current")
_RprSpanDayInMcastClassBEirOctets_Type = HCPerfTotalCount
_RprSpanDayInMcastClassBEirOctets_Object = MibTableColumn
rprSpanDayInMcastClassBEirOctets = _RprSpanDayInMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 16),
    _RprSpanDayInMcastClassBEirOctets_Type()
)
rprSpanDayInMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInMcastClassBEirOctets.setStatus("current")
_RprSpanDayInMcastClassCFrames_Type = HCPerfTotalCount
_RprSpanDayInMcastClassCFrames_Object = MibTableColumn
rprSpanDayInMcastClassCFrames = _RprSpanDayInMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 17),
    _RprSpanDayInMcastClassCFrames_Type()
)
rprSpanDayInMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInMcastClassCFrames.setStatus("current")
_RprSpanDayInMcastClassCOctets_Type = HCPerfTotalCount
_RprSpanDayInMcastClassCOctets_Object = MibTableColumn
rprSpanDayInMcastClassCOctets = _RprSpanDayInMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 18),
    _RprSpanDayInMcastClassCOctets_Type()
)
rprSpanDayInMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayInMcastClassCOctets.setStatus("current")
_RprSpanDayOutUcastClassAFrames_Type = HCPerfTotalCount
_RprSpanDayOutUcastClassAFrames_Object = MibTableColumn
rprSpanDayOutUcastClassAFrames = _RprSpanDayOutUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 19),
    _RprSpanDayOutUcastClassAFrames_Type()
)
rprSpanDayOutUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutUcastClassAFrames.setStatus("current")
_RprSpanDayOutUcastClassAOctets_Type = HCPerfTotalCount
_RprSpanDayOutUcastClassAOctets_Object = MibTableColumn
rprSpanDayOutUcastClassAOctets = _RprSpanDayOutUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 20),
    _RprSpanDayOutUcastClassAOctets_Type()
)
rprSpanDayOutUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutUcastClassAOctets.setStatus("current")
_RprSpanDayOutUcastClassBCirFrames_Type = HCPerfTotalCount
_RprSpanDayOutUcastClassBCirFrames_Object = MibTableColumn
rprSpanDayOutUcastClassBCirFrames = _RprSpanDayOutUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 21),
    _RprSpanDayOutUcastClassBCirFrames_Type()
)
rprSpanDayOutUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutUcastClassBCirFrames.setStatus("current")
_RprSpanDayOutUcastClassBCirOctets_Type = HCPerfTotalCount
_RprSpanDayOutUcastClassBCirOctets_Object = MibTableColumn
rprSpanDayOutUcastClassBCirOctets = _RprSpanDayOutUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 22),
    _RprSpanDayOutUcastClassBCirOctets_Type()
)
rprSpanDayOutUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutUcastClassBCirOctets.setStatus("current")
_RprSpanDayOutUcastClassBEirFrames_Type = HCPerfTotalCount
_RprSpanDayOutUcastClassBEirFrames_Object = MibTableColumn
rprSpanDayOutUcastClassBEirFrames = _RprSpanDayOutUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 23),
    _RprSpanDayOutUcastClassBEirFrames_Type()
)
rprSpanDayOutUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutUcastClassBEirFrames.setStatus("current")
_RprSpanDayOutUcastClassBEirOctets_Type = HCPerfTotalCount
_RprSpanDayOutUcastClassBEirOctets_Object = MibTableColumn
rprSpanDayOutUcastClassBEirOctets = _RprSpanDayOutUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 24),
    _RprSpanDayOutUcastClassBEirOctets_Type()
)
rprSpanDayOutUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutUcastClassBEirOctets.setStatus("current")
_RprSpanDayOutUcastClassCFrames_Type = HCPerfTotalCount
_RprSpanDayOutUcastClassCFrames_Object = MibTableColumn
rprSpanDayOutUcastClassCFrames = _RprSpanDayOutUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 25),
    _RprSpanDayOutUcastClassCFrames_Type()
)
rprSpanDayOutUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutUcastClassCFrames.setStatus("current")
_RprSpanDayOutUcastClassCOctets_Type = HCPerfTotalCount
_RprSpanDayOutUcastClassCOctets_Object = MibTableColumn
rprSpanDayOutUcastClassCOctets = _RprSpanDayOutUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 26),
    _RprSpanDayOutUcastClassCOctets_Type()
)
rprSpanDayOutUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutUcastClassCOctets.setStatus("current")
_RprSpanDayOutMcastClassAFrames_Type = HCPerfTotalCount
_RprSpanDayOutMcastClassAFrames_Object = MibTableColumn
rprSpanDayOutMcastClassAFrames = _RprSpanDayOutMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 27),
    _RprSpanDayOutMcastClassAFrames_Type()
)
rprSpanDayOutMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutMcastClassAFrames.setStatus("current")
_RprSpanDayOutMcastClassAOctets_Type = HCPerfTotalCount
_RprSpanDayOutMcastClassAOctets_Object = MibTableColumn
rprSpanDayOutMcastClassAOctets = _RprSpanDayOutMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 28),
    _RprSpanDayOutMcastClassAOctets_Type()
)
rprSpanDayOutMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutMcastClassAOctets.setStatus("current")
_RprSpanDayOutMcastClassBCirFrames_Type = HCPerfTotalCount
_RprSpanDayOutMcastClassBCirFrames_Object = MibTableColumn
rprSpanDayOutMcastClassBCirFrames = _RprSpanDayOutMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 29),
    _RprSpanDayOutMcastClassBCirFrames_Type()
)
rprSpanDayOutMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutMcastClassBCirFrames.setStatus("current")
_RprSpanDayOutMcastClassBCirOctets_Type = HCPerfTotalCount
_RprSpanDayOutMcastClassBCirOctets_Object = MibTableColumn
rprSpanDayOutMcastClassBCirOctets = _RprSpanDayOutMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 30),
    _RprSpanDayOutMcastClassBCirOctets_Type()
)
rprSpanDayOutMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutMcastClassBCirOctets.setStatus("current")
_RprSpanDayOutMcastClassBEirFrames_Type = HCPerfTotalCount
_RprSpanDayOutMcastClassBEirFrames_Object = MibTableColumn
rprSpanDayOutMcastClassBEirFrames = _RprSpanDayOutMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 31),
    _RprSpanDayOutMcastClassBEirFrames_Type()
)
rprSpanDayOutMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutMcastClassBEirFrames.setStatus("current")
_RprSpanDayOutMcastClassBEirOctets_Type = HCPerfTotalCount
_RprSpanDayOutMcastClassBEirOctets_Object = MibTableColumn
rprSpanDayOutMcastClassBEirOctets = _RprSpanDayOutMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 32),
    _RprSpanDayOutMcastClassBEirOctets_Type()
)
rprSpanDayOutMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutMcastClassBEirOctets.setStatus("current")
_RprSpanDayOutMcastClassCFrames_Type = HCPerfTotalCount
_RprSpanDayOutMcastClassCFrames_Object = MibTableColumn
rprSpanDayOutMcastClassCFrames = _RprSpanDayOutMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 33),
    _RprSpanDayOutMcastClassCFrames_Type()
)
rprSpanDayOutMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutMcastClassCFrames.setStatus("current")
_RprSpanDayOutMcastClassCOctets_Type = HCPerfTotalCount
_RprSpanDayOutMcastClassCOctets_Object = MibTableColumn
rprSpanDayOutMcastClassCOctets = _RprSpanDayOutMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 3, 1, 34),
    _RprSpanDayOutMcastClassCOctets_Type()
)
rprSpanDayOutMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanDayOutMcastClassCOctets.setStatus("current")
_RprSpanCountersStatsTable_Object = MibTable
rprSpanCountersStatsTable = _RprSpanCountersStatsTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    rprSpanCountersStatsTable.setStatus("current")
_RprSpanCountersStatsEntry_Object = MibTableRow
rprSpanCountersStatsEntry = _RprSpanCountersStatsEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1)
)
rprSpanCountersStatsEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanStatsIfIndex"),
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanStatsSpan"),
)
if mibBuilder.loadTexts:
    rprSpanCountersStatsEntry.setStatus("current")
_RprSpanStatsIfIndex_Type = InterfaceIndex
_RprSpanStatsIfIndex_Object = MibTableColumn
rprSpanStatsIfIndex = _RprSpanStatsIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 1),
    _RprSpanStatsIfIndex_Type()
)
rprSpanStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanStatsIfIndex.setStatus("current")
_RprSpanStatsSpan_Type = RprSpan
_RprSpanStatsSpan_Object = MibTableColumn
rprSpanStatsSpan = _RprSpanStatsSpan_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 2),
    _RprSpanStatsSpan_Type()
)
rprSpanStatsSpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanStatsSpan.setStatus("current")
_RprSpanStatsInUcastClassAFrames_Type = Counter64
_RprSpanStatsInUcastClassAFrames_Object = MibTableColumn
rprSpanStatsInUcastClassAFrames = _RprSpanStatsInUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 3),
    _RprSpanStatsInUcastClassAFrames_Type()
)
rprSpanStatsInUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInUcastClassAFrames.setStatus("current")
_RprSpanStatsInUcastClassAOctets_Type = Counter64
_RprSpanStatsInUcastClassAOctets_Object = MibTableColumn
rprSpanStatsInUcastClassAOctets = _RprSpanStatsInUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 4),
    _RprSpanStatsInUcastClassAOctets_Type()
)
rprSpanStatsInUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInUcastClassAOctets.setStatus("current")
_RprSpanStatsInUcastClassBCirFrames_Type = Counter64
_RprSpanStatsInUcastClassBCirFrames_Object = MibTableColumn
rprSpanStatsInUcastClassBCirFrames = _RprSpanStatsInUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 5),
    _RprSpanStatsInUcastClassBCirFrames_Type()
)
rprSpanStatsInUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInUcastClassBCirFrames.setStatus("current")
_RprSpanStatsInUcastClassBCirOctets_Type = Counter64
_RprSpanStatsInUcastClassBCirOctets_Object = MibTableColumn
rprSpanStatsInUcastClassBCirOctets = _RprSpanStatsInUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 6),
    _RprSpanStatsInUcastClassBCirOctets_Type()
)
rprSpanStatsInUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInUcastClassBCirOctets.setStatus("current")
_RprSpanStatsInUcastClassBEirFrames_Type = Counter64
_RprSpanStatsInUcastClassBEirFrames_Object = MibTableColumn
rprSpanStatsInUcastClassBEirFrames = _RprSpanStatsInUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 7),
    _RprSpanStatsInUcastClassBEirFrames_Type()
)
rprSpanStatsInUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInUcastClassBEirFrames.setStatus("current")
_RprSpanStatsInUcastClassBEirOctets_Type = Counter64
_RprSpanStatsInUcastClassBEirOctets_Object = MibTableColumn
rprSpanStatsInUcastClassBEirOctets = _RprSpanStatsInUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 8),
    _RprSpanStatsInUcastClassBEirOctets_Type()
)
rprSpanStatsInUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInUcastClassBEirOctets.setStatus("current")
_RprSpanStatsInUcastClassCFrames_Type = Counter64
_RprSpanStatsInUcastClassCFrames_Object = MibTableColumn
rprSpanStatsInUcastClassCFrames = _RprSpanStatsInUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 9),
    _RprSpanStatsInUcastClassCFrames_Type()
)
rprSpanStatsInUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInUcastClassCFrames.setStatus("current")
_RprSpanStatsInUcastClassCOctets_Type = Counter64
_RprSpanStatsInUcastClassCOctets_Object = MibTableColumn
rprSpanStatsInUcastClassCOctets = _RprSpanStatsInUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 10),
    _RprSpanStatsInUcastClassCOctets_Type()
)
rprSpanStatsInUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInUcastClassCOctets.setStatus("current")
_RprSpanStatsInMcastClassAFrames_Type = Counter64
_RprSpanStatsInMcastClassAFrames_Object = MibTableColumn
rprSpanStatsInMcastClassAFrames = _RprSpanStatsInMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 11),
    _RprSpanStatsInMcastClassAFrames_Type()
)
rprSpanStatsInMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInMcastClassAFrames.setStatus("current")
_RprSpanStatsInMcastClassAOctets_Type = Counter64
_RprSpanStatsInMcastClassAOctets_Object = MibTableColumn
rprSpanStatsInMcastClassAOctets = _RprSpanStatsInMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 12),
    _RprSpanStatsInMcastClassAOctets_Type()
)
rprSpanStatsInMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInMcastClassAOctets.setStatus("current")
_RprSpanStatsInMcastClassBCirFrames_Type = Counter64
_RprSpanStatsInMcastClassBCirFrames_Object = MibTableColumn
rprSpanStatsInMcastClassBCirFrames = _RprSpanStatsInMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 13),
    _RprSpanStatsInMcastClassBCirFrames_Type()
)
rprSpanStatsInMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInMcastClassBCirFrames.setStatus("current")
_RprSpanStatsInMcastClassBCirOctets_Type = Counter64
_RprSpanStatsInMcastClassBCirOctets_Object = MibTableColumn
rprSpanStatsInMcastClassBCirOctets = _RprSpanStatsInMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 14),
    _RprSpanStatsInMcastClassBCirOctets_Type()
)
rprSpanStatsInMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInMcastClassBCirOctets.setStatus("current")
_RprSpanStatsInMcastClassBEirFrames_Type = Counter64
_RprSpanStatsInMcastClassBEirFrames_Object = MibTableColumn
rprSpanStatsInMcastClassBEirFrames = _RprSpanStatsInMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 15),
    _RprSpanStatsInMcastClassBEirFrames_Type()
)
rprSpanStatsInMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInMcastClassBEirFrames.setStatus("current")
_RprSpanStatsInMcastClassBEirOctets_Type = Counter64
_RprSpanStatsInMcastClassBEirOctets_Object = MibTableColumn
rprSpanStatsInMcastClassBEirOctets = _RprSpanStatsInMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 16),
    _RprSpanStatsInMcastClassBEirOctets_Type()
)
rprSpanStatsInMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInMcastClassBEirOctets.setStatus("current")
_RprSpanStatsInMcastClassCFrames_Type = Counter64
_RprSpanStatsInMcastClassCFrames_Object = MibTableColumn
rprSpanStatsInMcastClassCFrames = _RprSpanStatsInMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 17),
    _RprSpanStatsInMcastClassCFrames_Type()
)
rprSpanStatsInMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInMcastClassCFrames.setStatus("current")
_RprSpanStatsInMcastClassCOctets_Type = Counter64
_RprSpanStatsInMcastClassCOctets_Object = MibTableColumn
rprSpanStatsInMcastClassCOctets = _RprSpanStatsInMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 18),
    _RprSpanStatsInMcastClassCOctets_Type()
)
rprSpanStatsInMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInMcastClassCOctets.setStatus("current")
_RprSpanStatsInCtrlFrames_Type = Counter64
_RprSpanStatsInCtrlFrames_Object = MibTableColumn
rprSpanStatsInCtrlFrames = _RprSpanStatsInCtrlFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 19),
    _RprSpanStatsInCtrlFrames_Type()
)
rprSpanStatsInCtrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInCtrlFrames.setStatus("current")
_RprSpanStatsInOamEchoFrames_Type = Counter64
_RprSpanStatsInOamEchoFrames_Object = MibTableColumn
rprSpanStatsInOamEchoFrames = _RprSpanStatsInOamEchoFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 20),
    _RprSpanStatsInOamEchoFrames_Type()
)
rprSpanStatsInOamEchoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInOamEchoFrames.setStatus("current")
_RprSpanStatsInOamFlushFrames_Type = Counter64
_RprSpanStatsInOamFlushFrames_Object = MibTableColumn
rprSpanStatsInOamFlushFrames = _RprSpanStatsInOamFlushFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 21),
    _RprSpanStatsInOamFlushFrames_Type()
)
rprSpanStatsInOamFlushFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInOamFlushFrames.setStatus("current")
_RprSpanStatsInOamOrgFrames_Type = Counter64
_RprSpanStatsInOamOrgFrames_Object = MibTableColumn
rprSpanStatsInOamOrgFrames = _RprSpanStatsInOamOrgFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 22),
    _RprSpanStatsInOamOrgFrames_Type()
)
rprSpanStatsInOamOrgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInOamOrgFrames.setStatus("current")
_RprSpanStatsInTopoAtdFrames_Type = Counter64
_RprSpanStatsInTopoAtdFrames_Object = MibTableColumn
rprSpanStatsInTopoAtdFrames = _RprSpanStatsInTopoAtdFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 23),
    _RprSpanStatsInTopoAtdFrames_Type()
)
rprSpanStatsInTopoAtdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInTopoAtdFrames.setStatus("current")
_RprSpanStatsInTopoChkSumFrames_Type = Counter64
_RprSpanStatsInTopoChkSumFrames_Object = MibTableColumn
rprSpanStatsInTopoChkSumFrames = _RprSpanStatsInTopoChkSumFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 24),
    _RprSpanStatsInTopoChkSumFrames_Type()
)
rprSpanStatsInTopoChkSumFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInTopoChkSumFrames.setStatus("current")
_RprSpanStatsInTopoTpFrames_Type = Counter64
_RprSpanStatsInTopoTpFrames_Object = MibTableColumn
rprSpanStatsInTopoTpFrames = _RprSpanStatsInTopoTpFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 25),
    _RprSpanStatsInTopoTpFrames_Type()
)
rprSpanStatsInTopoTpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsInTopoTpFrames.setStatus("current")
_RprSpanStatsOutUcastClassAFrames_Type = Counter64
_RprSpanStatsOutUcastClassAFrames_Object = MibTableColumn
rprSpanStatsOutUcastClassAFrames = _RprSpanStatsOutUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 26),
    _RprSpanStatsOutUcastClassAFrames_Type()
)
rprSpanStatsOutUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutUcastClassAFrames.setStatus("current")
_RprSpanStatsOutUcastClassAOctets_Type = Counter64
_RprSpanStatsOutUcastClassAOctets_Object = MibTableColumn
rprSpanStatsOutUcastClassAOctets = _RprSpanStatsOutUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 27),
    _RprSpanStatsOutUcastClassAOctets_Type()
)
rprSpanStatsOutUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutUcastClassAOctets.setStatus("current")
_RprSpanStatsOutUcastClassBCirFrames_Type = Counter64
_RprSpanStatsOutUcastClassBCirFrames_Object = MibTableColumn
rprSpanStatsOutUcastClassBCirFrames = _RprSpanStatsOutUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 28),
    _RprSpanStatsOutUcastClassBCirFrames_Type()
)
rprSpanStatsOutUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutUcastClassBCirFrames.setStatus("current")
_RprSpanStatsOutUcastClassBCirOctets_Type = Counter64
_RprSpanStatsOutUcastClassBCirOctets_Object = MibTableColumn
rprSpanStatsOutUcastClassBCirOctets = _RprSpanStatsOutUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 29),
    _RprSpanStatsOutUcastClassBCirOctets_Type()
)
rprSpanStatsOutUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutUcastClassBCirOctets.setStatus("current")
_RprSpanStatsOutUcastClassBEirFrames_Type = Counter64
_RprSpanStatsOutUcastClassBEirFrames_Object = MibTableColumn
rprSpanStatsOutUcastClassBEirFrames = _RprSpanStatsOutUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 30),
    _RprSpanStatsOutUcastClassBEirFrames_Type()
)
rprSpanStatsOutUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutUcastClassBEirFrames.setStatus("current")
_RprSpanStatsOutUcastClassBEirOctets_Type = Counter64
_RprSpanStatsOutUcastClassBEirOctets_Object = MibTableColumn
rprSpanStatsOutUcastClassBEirOctets = _RprSpanStatsOutUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 31),
    _RprSpanStatsOutUcastClassBEirOctets_Type()
)
rprSpanStatsOutUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutUcastClassBEirOctets.setStatus("current")
_RprSpanStatsOutUcastClassCFrames_Type = Counter64
_RprSpanStatsOutUcastClassCFrames_Object = MibTableColumn
rprSpanStatsOutUcastClassCFrames = _RprSpanStatsOutUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 32),
    _RprSpanStatsOutUcastClassCFrames_Type()
)
rprSpanStatsOutUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutUcastClassCFrames.setStatus("current")
_RprSpanStatsOutUcastClassCOctets_Type = Counter64
_RprSpanStatsOutUcastClassCOctets_Object = MibTableColumn
rprSpanStatsOutUcastClassCOctets = _RprSpanStatsOutUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 33),
    _RprSpanStatsOutUcastClassCOctets_Type()
)
rprSpanStatsOutUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutUcastClassCOctets.setStatus("current")
_RprSpanStatsOutMcastClassAFrames_Type = Counter64
_RprSpanStatsOutMcastClassAFrames_Object = MibTableColumn
rprSpanStatsOutMcastClassAFrames = _RprSpanStatsOutMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 34),
    _RprSpanStatsOutMcastClassAFrames_Type()
)
rprSpanStatsOutMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutMcastClassAFrames.setStatus("current")
_RprSpanStatsOutMcastClassAOctets_Type = Counter64
_RprSpanStatsOutMcastClassAOctets_Object = MibTableColumn
rprSpanStatsOutMcastClassAOctets = _RprSpanStatsOutMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 35),
    _RprSpanStatsOutMcastClassAOctets_Type()
)
rprSpanStatsOutMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutMcastClassAOctets.setStatus("current")
_RprSpanStatsOutMcastClassBCirFrames_Type = Counter64
_RprSpanStatsOutMcastClassBCirFrames_Object = MibTableColumn
rprSpanStatsOutMcastClassBCirFrames = _RprSpanStatsOutMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 36),
    _RprSpanStatsOutMcastClassBCirFrames_Type()
)
rprSpanStatsOutMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutMcastClassBCirFrames.setStatus("current")
_RprSpanStatsOutMcastClassBCirOctets_Type = Counter64
_RprSpanStatsOutMcastClassBCirOctets_Object = MibTableColumn
rprSpanStatsOutMcastClassBCirOctets = _RprSpanStatsOutMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 37),
    _RprSpanStatsOutMcastClassBCirOctets_Type()
)
rprSpanStatsOutMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutMcastClassBCirOctets.setStatus("current")
_RprSpanStatsOutMcastClassBEirFrames_Type = Counter64
_RprSpanStatsOutMcastClassBEirFrames_Object = MibTableColumn
rprSpanStatsOutMcastClassBEirFrames = _RprSpanStatsOutMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 38),
    _RprSpanStatsOutMcastClassBEirFrames_Type()
)
rprSpanStatsOutMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutMcastClassBEirFrames.setStatus("current")
_RprSpanStatsOutMcastClassBEirOctets_Type = Counter64
_RprSpanStatsOutMcastClassBEirOctets_Object = MibTableColumn
rprSpanStatsOutMcastClassBEirOctets = _RprSpanStatsOutMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 39),
    _RprSpanStatsOutMcastClassBEirOctets_Type()
)
rprSpanStatsOutMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutMcastClassBEirOctets.setStatus("current")
_RprSpanStatsOutMcastClassCFrames_Type = Counter64
_RprSpanStatsOutMcastClassCFrames_Object = MibTableColumn
rprSpanStatsOutMcastClassCFrames = _RprSpanStatsOutMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 40),
    _RprSpanStatsOutMcastClassCFrames_Type()
)
rprSpanStatsOutMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutMcastClassCFrames.setStatus("current")
_RprSpanStatsOutMcastClassCOctets_Type = Counter64
_RprSpanStatsOutMcastClassCOctets_Object = MibTableColumn
rprSpanStatsOutMcastClassCOctets = _RprSpanStatsOutMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 41),
    _RprSpanStatsOutMcastClassCOctets_Type()
)
rprSpanStatsOutMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutMcastClassCOctets.setStatus("current")
_RprSpanStatsOutCtrlFrames_Type = Counter64
_RprSpanStatsOutCtrlFrames_Object = MibTableColumn
rprSpanStatsOutCtrlFrames = _RprSpanStatsOutCtrlFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 42),
    _RprSpanStatsOutCtrlFrames_Type()
)
rprSpanStatsOutCtrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutCtrlFrames.setStatus("current")
_RprSpanStatsOutOamEchoFrames_Type = Counter64
_RprSpanStatsOutOamEchoFrames_Object = MibTableColumn
rprSpanStatsOutOamEchoFrames = _RprSpanStatsOutOamEchoFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 43),
    _RprSpanStatsOutOamEchoFrames_Type()
)
rprSpanStatsOutOamEchoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutOamEchoFrames.setStatus("current")
_RprSpanStatsOutOamFlushFrames_Type = Counter64
_RprSpanStatsOutOamFlushFrames_Object = MibTableColumn
rprSpanStatsOutOamFlushFrames = _RprSpanStatsOutOamFlushFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 44),
    _RprSpanStatsOutOamFlushFrames_Type()
)
rprSpanStatsOutOamFlushFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutOamFlushFrames.setStatus("current")
_RprSpanStatsOutOamOrgFrames_Type = Counter64
_RprSpanStatsOutOamOrgFrames_Object = MibTableColumn
rprSpanStatsOutOamOrgFrames = _RprSpanStatsOutOamOrgFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 45),
    _RprSpanStatsOutOamOrgFrames_Type()
)
rprSpanStatsOutOamOrgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutOamOrgFrames.setStatus("current")
_RprSpanStatsOutTopoAtdFrames_Type = Counter64
_RprSpanStatsOutTopoAtdFrames_Object = MibTableColumn
rprSpanStatsOutTopoAtdFrames = _RprSpanStatsOutTopoAtdFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 46),
    _RprSpanStatsOutTopoAtdFrames_Type()
)
rprSpanStatsOutTopoAtdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutTopoAtdFrames.setStatus("current")
_RprSpanStatsOutTopoChkSumFrames_Type = Counter64
_RprSpanStatsOutTopoChkSumFrames_Object = MibTableColumn
rprSpanStatsOutTopoChkSumFrames = _RprSpanStatsOutTopoChkSumFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 47),
    _RprSpanStatsOutTopoChkSumFrames_Type()
)
rprSpanStatsOutTopoChkSumFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutTopoChkSumFrames.setStatus("current")
_RprSpanStatsOutTopoTpFrames_Type = Counter64
_RprSpanStatsOutTopoTpFrames_Object = MibTableColumn
rprSpanStatsOutTopoTpFrames = _RprSpanStatsOutTopoTpFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 3, 4, 1, 48),
    _RprSpanStatsOutTopoTpFrames_Type()
)
rprSpanStatsOutTopoTpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanStatsOutTopoTpFrames.setStatus("current")
_RprClientCounters_ObjectIdentity = ObjectIdentity
rprClientCounters = _RprClientCounters_ObjectIdentity(
    (1, 0, 8802, 17, 1, 1, 1, 4)
)
_RprClientCountersCurrentTable_Object = MibTable
rprClientCountersCurrentTable = _RprClientCountersCurrentTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rprClientCountersCurrentTable.setStatus("current")
_RprClientCountersCurrentEntry_Object = MibTableRow
rprClientCountersCurrentEntry = _RprClientCountersCurrentEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1)
)
rprClientCountersCurrentEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprClientCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    rprClientCountersCurrentEntry.setStatus("current")
_RprClientCurrentIfIndex_Type = InterfaceIndex
_RprClientCurrentIfIndex_Object = MibTableColumn
rprClientCurrentIfIndex = _RprClientCurrentIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 1),
    _RprClientCurrentIfIndex_Type()
)
rprClientCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprClientCurrentIfIndex.setStatus("current")
_RprClientCurrentInUcastClassAFrames_Type = HCPerfCurrentCount
_RprClientCurrentInUcastClassAFrames_Object = MibTableColumn
rprClientCurrentInUcastClassAFrames = _RprClientCurrentInUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 2),
    _RprClientCurrentInUcastClassAFrames_Type()
)
rprClientCurrentInUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInUcastClassAFrames.setStatus("current")
_RprClientCurrentInUcastClassAOctets_Type = HCPerfCurrentCount
_RprClientCurrentInUcastClassAOctets_Object = MibTableColumn
rprClientCurrentInUcastClassAOctets = _RprClientCurrentInUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 3),
    _RprClientCurrentInUcastClassAOctets_Type()
)
rprClientCurrentInUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInUcastClassAOctets.setStatus("current")
_RprClientCurrentInUcastClassBCirFrames_Type = HCPerfCurrentCount
_RprClientCurrentInUcastClassBCirFrames_Object = MibTableColumn
rprClientCurrentInUcastClassBCirFrames = _RprClientCurrentInUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 4),
    _RprClientCurrentInUcastClassBCirFrames_Type()
)
rprClientCurrentInUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInUcastClassBCirFrames.setStatus("current")
_RprClientCurrentInUcastClassBCirOctets_Type = HCPerfCurrentCount
_RprClientCurrentInUcastClassBCirOctets_Object = MibTableColumn
rprClientCurrentInUcastClassBCirOctets = _RprClientCurrentInUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 5),
    _RprClientCurrentInUcastClassBCirOctets_Type()
)
rprClientCurrentInUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInUcastClassBCirOctets.setStatus("current")
_RprClientCurrentInUcastClassBEirFrames_Type = HCPerfCurrentCount
_RprClientCurrentInUcastClassBEirFrames_Object = MibTableColumn
rprClientCurrentInUcastClassBEirFrames = _RprClientCurrentInUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 6),
    _RprClientCurrentInUcastClassBEirFrames_Type()
)
rprClientCurrentInUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInUcastClassBEirFrames.setStatus("current")
_RprClientCurrentInUcastClassBEirOctets_Type = HCPerfCurrentCount
_RprClientCurrentInUcastClassBEirOctets_Object = MibTableColumn
rprClientCurrentInUcastClassBEirOctets = _RprClientCurrentInUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 7),
    _RprClientCurrentInUcastClassBEirOctets_Type()
)
rprClientCurrentInUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInUcastClassBEirOctets.setStatus("current")
_RprClientCurrentInUcastClassCFrames_Type = HCPerfCurrentCount
_RprClientCurrentInUcastClassCFrames_Object = MibTableColumn
rprClientCurrentInUcastClassCFrames = _RprClientCurrentInUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 8),
    _RprClientCurrentInUcastClassCFrames_Type()
)
rprClientCurrentInUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInUcastClassCFrames.setStatus("current")
_RprClientCurrentInUcastClassCOctets_Type = HCPerfCurrentCount
_RprClientCurrentInUcastClassCOctets_Object = MibTableColumn
rprClientCurrentInUcastClassCOctets = _RprClientCurrentInUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 9),
    _RprClientCurrentInUcastClassCOctets_Type()
)
rprClientCurrentInUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInUcastClassCOctets.setStatus("current")
_RprClientCurrentInMcastClassAFrames_Type = HCPerfCurrentCount
_RprClientCurrentInMcastClassAFrames_Object = MibTableColumn
rprClientCurrentInMcastClassAFrames = _RprClientCurrentInMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 10),
    _RprClientCurrentInMcastClassAFrames_Type()
)
rprClientCurrentInMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInMcastClassAFrames.setStatus("current")
_RprClientCurrentInMcastClassAOctets_Type = HCPerfCurrentCount
_RprClientCurrentInMcastClassAOctets_Object = MibTableColumn
rprClientCurrentInMcastClassAOctets = _RprClientCurrentInMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 11),
    _RprClientCurrentInMcastClassAOctets_Type()
)
rprClientCurrentInMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInMcastClassAOctets.setStatus("current")
_RprClientCurrentInMcastClassBCirFrames_Type = HCPerfCurrentCount
_RprClientCurrentInMcastClassBCirFrames_Object = MibTableColumn
rprClientCurrentInMcastClassBCirFrames = _RprClientCurrentInMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 12),
    _RprClientCurrentInMcastClassBCirFrames_Type()
)
rprClientCurrentInMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInMcastClassBCirFrames.setStatus("current")
_RprClientCurrentInMcastClassBCirOctets_Type = HCPerfCurrentCount
_RprClientCurrentInMcastClassBCirOctets_Object = MibTableColumn
rprClientCurrentInMcastClassBCirOctets = _RprClientCurrentInMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 13),
    _RprClientCurrentInMcastClassBCirOctets_Type()
)
rprClientCurrentInMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInMcastClassBCirOctets.setStatus("current")
_RprClientCurrentInMcastClassBEirFrames_Type = HCPerfCurrentCount
_RprClientCurrentInMcastClassBEirFrames_Object = MibTableColumn
rprClientCurrentInMcastClassBEirFrames = _RprClientCurrentInMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 14),
    _RprClientCurrentInMcastClassBEirFrames_Type()
)
rprClientCurrentInMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInMcastClassBEirFrames.setStatus("current")
_RprClientCurrentInMcastClassBEirOctets_Type = HCPerfCurrentCount
_RprClientCurrentInMcastClassBEirOctets_Object = MibTableColumn
rprClientCurrentInMcastClassBEirOctets = _RprClientCurrentInMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 15),
    _RprClientCurrentInMcastClassBEirOctets_Type()
)
rprClientCurrentInMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInMcastClassBEirOctets.setStatus("current")
_RprClientCurrentInMcastClassCFrames_Type = HCPerfCurrentCount
_RprClientCurrentInMcastClassCFrames_Object = MibTableColumn
rprClientCurrentInMcastClassCFrames = _RprClientCurrentInMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 16),
    _RprClientCurrentInMcastClassCFrames_Type()
)
rprClientCurrentInMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInMcastClassCFrames.setStatus("current")
_RprClientCurrentInMcastClassCOctets_Type = HCPerfCurrentCount
_RprClientCurrentInMcastClassCOctets_Object = MibTableColumn
rprClientCurrentInMcastClassCOctets = _RprClientCurrentInMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 17),
    _RprClientCurrentInMcastClassCOctets_Type()
)
rprClientCurrentInMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentInMcastClassCOctets.setStatus("current")
_RprClientCurrentOutUcastClassAFrames_Type = HCPerfCurrentCount
_RprClientCurrentOutUcastClassAFrames_Object = MibTableColumn
rprClientCurrentOutUcastClassAFrames = _RprClientCurrentOutUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 18),
    _RprClientCurrentOutUcastClassAFrames_Type()
)
rprClientCurrentOutUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutUcastClassAFrames.setStatus("current")
_RprClientCurrentOutUcastClassAOctets_Type = HCPerfCurrentCount
_RprClientCurrentOutUcastClassAOctets_Object = MibTableColumn
rprClientCurrentOutUcastClassAOctets = _RprClientCurrentOutUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 19),
    _RprClientCurrentOutUcastClassAOctets_Type()
)
rprClientCurrentOutUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutUcastClassAOctets.setStatus("current")
_RprClientCurrentOutUcastClassBCirFrames_Type = HCPerfCurrentCount
_RprClientCurrentOutUcastClassBCirFrames_Object = MibTableColumn
rprClientCurrentOutUcastClassBCirFrames = _RprClientCurrentOutUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 20),
    _RprClientCurrentOutUcastClassBCirFrames_Type()
)
rprClientCurrentOutUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutUcastClassBCirFrames.setStatus("current")
_RprClientCurrentOutUcastClassBCirOctets_Type = HCPerfCurrentCount
_RprClientCurrentOutUcastClassBCirOctets_Object = MibTableColumn
rprClientCurrentOutUcastClassBCirOctets = _RprClientCurrentOutUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 21),
    _RprClientCurrentOutUcastClassBCirOctets_Type()
)
rprClientCurrentOutUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutUcastClassBCirOctets.setStatus("current")
_RprClientCurrentOutUcastClassBEirFrames_Type = HCPerfCurrentCount
_RprClientCurrentOutUcastClassBEirFrames_Object = MibTableColumn
rprClientCurrentOutUcastClassBEirFrames = _RprClientCurrentOutUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 22),
    _RprClientCurrentOutUcastClassBEirFrames_Type()
)
rprClientCurrentOutUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutUcastClassBEirFrames.setStatus("current")
_RprClientCurrentOutUcastClassBEirOctets_Type = HCPerfCurrentCount
_RprClientCurrentOutUcastClassBEirOctets_Object = MibTableColumn
rprClientCurrentOutUcastClassBEirOctets = _RprClientCurrentOutUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 23),
    _RprClientCurrentOutUcastClassBEirOctets_Type()
)
rprClientCurrentOutUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutUcastClassBEirOctets.setStatus("current")
_RprClientCurrentOutUcastClassCFrames_Type = HCPerfCurrentCount
_RprClientCurrentOutUcastClassCFrames_Object = MibTableColumn
rprClientCurrentOutUcastClassCFrames = _RprClientCurrentOutUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 24),
    _RprClientCurrentOutUcastClassCFrames_Type()
)
rprClientCurrentOutUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutUcastClassCFrames.setStatus("current")
_RprClientCurrentOutUcastClassCOctets_Type = HCPerfCurrentCount
_RprClientCurrentOutUcastClassCOctets_Object = MibTableColumn
rprClientCurrentOutUcastClassCOctets = _RprClientCurrentOutUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 25),
    _RprClientCurrentOutUcastClassCOctets_Type()
)
rprClientCurrentOutUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutUcastClassCOctets.setStatus("current")
_RprClientCurrentOutMcastClassAFrames_Type = HCPerfCurrentCount
_RprClientCurrentOutMcastClassAFrames_Object = MibTableColumn
rprClientCurrentOutMcastClassAFrames = _RprClientCurrentOutMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 26),
    _RprClientCurrentOutMcastClassAFrames_Type()
)
rprClientCurrentOutMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutMcastClassAFrames.setStatus("current")
_RprClientCurrentOutMcastClassAOctets_Type = HCPerfCurrentCount
_RprClientCurrentOutMcastClassAOctets_Object = MibTableColumn
rprClientCurrentOutMcastClassAOctets = _RprClientCurrentOutMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 27),
    _RprClientCurrentOutMcastClassAOctets_Type()
)
rprClientCurrentOutMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutMcastClassAOctets.setStatus("current")
_RprClientCurrentOutMcastClassBCirFrames_Type = HCPerfCurrentCount
_RprClientCurrentOutMcastClassBCirFrames_Object = MibTableColumn
rprClientCurrentOutMcastClassBCirFrames = _RprClientCurrentOutMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 28),
    _RprClientCurrentOutMcastClassBCirFrames_Type()
)
rprClientCurrentOutMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutMcastClassBCirFrames.setStatus("current")
_RprClientCurrentOutMcastClassBCirOctets_Type = HCPerfCurrentCount
_RprClientCurrentOutMcastClassBCirOctets_Object = MibTableColumn
rprClientCurrentOutMcastClassBCirOctets = _RprClientCurrentOutMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 29),
    _RprClientCurrentOutMcastClassBCirOctets_Type()
)
rprClientCurrentOutMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutMcastClassBCirOctets.setStatus("current")
_RprClientCurrentOutMcastClassBEirFrames_Type = HCPerfCurrentCount
_RprClientCurrentOutMcastClassBEirFrames_Object = MibTableColumn
rprClientCurrentOutMcastClassBEirFrames = _RprClientCurrentOutMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 30),
    _RprClientCurrentOutMcastClassBEirFrames_Type()
)
rprClientCurrentOutMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutMcastClassBEirFrames.setStatus("current")
_RprClientCurrentOutMcastClassBEirOctets_Type = HCPerfCurrentCount
_RprClientCurrentOutMcastClassBEirOctets_Object = MibTableColumn
rprClientCurrentOutMcastClassBEirOctets = _RprClientCurrentOutMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 31),
    _RprClientCurrentOutMcastClassBEirOctets_Type()
)
rprClientCurrentOutMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutMcastClassBEirOctets.setStatus("current")
_RprClientCurrentOutMcastClassCFrames_Type = HCPerfCurrentCount
_RprClientCurrentOutMcastClassCFrames_Object = MibTableColumn
rprClientCurrentOutMcastClassCFrames = _RprClientCurrentOutMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 32),
    _RprClientCurrentOutMcastClassCFrames_Type()
)
rprClientCurrentOutMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutMcastClassCFrames.setStatus("current")
_RprClientCurrentOutMcastClassCOctets_Type = HCPerfCurrentCount
_RprClientCurrentOutMcastClassCOctets_Object = MibTableColumn
rprClientCurrentOutMcastClassCOctets = _RprClientCurrentOutMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 1, 1, 33),
    _RprClientCurrentOutMcastClassCOctets_Type()
)
rprClientCurrentOutMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientCurrentOutMcastClassCOctets.setStatus("current")
_RprClientCountersIntervalTable_Object = MibTable
rprClientCountersIntervalTable = _RprClientCountersIntervalTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    rprClientCountersIntervalTable.setStatus("current")
_RprClientCountersIntervalEntry_Object = MibTableRow
rprClientCountersIntervalEntry = _RprClientCountersIntervalEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1)
)
rprClientCountersIntervalEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprClientIntervalIfIndex"),
    (0, "IEEE-802DOT17-RPR-MIB", "rprClientIntervalNumber"),
)
if mibBuilder.loadTexts:
    rprClientCountersIntervalEntry.setStatus("current")
_RprClientIntervalIfIndex_Type = InterfaceIndex
_RprClientIntervalIfIndex_Object = MibTableColumn
rprClientIntervalIfIndex = _RprClientIntervalIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 1),
    _RprClientIntervalIfIndex_Type()
)
rprClientIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprClientIntervalIfIndex.setStatus("current")


class _RprClientIntervalNumber_Type(Unsigned32):
    """Custom type rprClientIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_RprClientIntervalNumber_Type.__name__ = "Unsigned32"
_RprClientIntervalNumber_Object = MibTableColumn
rprClientIntervalNumber = _RprClientIntervalNumber_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 2),
    _RprClientIntervalNumber_Type()
)
rprClientIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprClientIntervalNumber.setStatus("current")
_RprClientIntervalValidData_Type = TruthValue
_RprClientIntervalValidData_Object = MibTableColumn
rprClientIntervalValidData = _RprClientIntervalValidData_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 3),
    _RprClientIntervalValidData_Type()
)
rprClientIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalValidData.setStatus("current")


class _RprClientIntervalTimeElapsed_Type(Unsigned32):
    """Custom type rprClientIntervalTimeElapsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_RprClientIntervalTimeElapsed_Type.__name__ = "Unsigned32"
_RprClientIntervalTimeElapsed_Object = MibTableColumn
rprClientIntervalTimeElapsed = _RprClientIntervalTimeElapsed_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 4),
    _RprClientIntervalTimeElapsed_Type()
)
rprClientIntervalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    rprClientIntervalTimeElapsed.setUnits("Seconds")
_RprClientIntervalInUcastClassAFrames_Type = HCPerfIntervalCount
_RprClientIntervalInUcastClassAFrames_Object = MibTableColumn
rprClientIntervalInUcastClassAFrames = _RprClientIntervalInUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 5),
    _RprClientIntervalInUcastClassAFrames_Type()
)
rprClientIntervalInUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInUcastClassAFrames.setStatus("current")
_RprClientIntervalInUcastClassAOctets_Type = HCPerfIntervalCount
_RprClientIntervalInUcastClassAOctets_Object = MibTableColumn
rprClientIntervalInUcastClassAOctets = _RprClientIntervalInUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 6),
    _RprClientIntervalInUcastClassAOctets_Type()
)
rprClientIntervalInUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInUcastClassAOctets.setStatus("current")
_RprClientIntervalInUcastClassBCirFrames_Type = HCPerfIntervalCount
_RprClientIntervalInUcastClassBCirFrames_Object = MibTableColumn
rprClientIntervalInUcastClassBCirFrames = _RprClientIntervalInUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 7),
    _RprClientIntervalInUcastClassBCirFrames_Type()
)
rprClientIntervalInUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInUcastClassBCirFrames.setStatus("current")
_RprClientIntervalInUcastClassBCirOctets_Type = HCPerfIntervalCount
_RprClientIntervalInUcastClassBCirOctets_Object = MibTableColumn
rprClientIntervalInUcastClassBCirOctets = _RprClientIntervalInUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 8),
    _RprClientIntervalInUcastClassBCirOctets_Type()
)
rprClientIntervalInUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInUcastClassBCirOctets.setStatus("current")
_RprClientIntervalInUcastClassBEirFrames_Type = HCPerfIntervalCount
_RprClientIntervalInUcastClassBEirFrames_Object = MibTableColumn
rprClientIntervalInUcastClassBEirFrames = _RprClientIntervalInUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 9),
    _RprClientIntervalInUcastClassBEirFrames_Type()
)
rprClientIntervalInUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInUcastClassBEirFrames.setStatus("current")
_RprClientIntervalInUcastClassBEirOctets_Type = HCPerfIntervalCount
_RprClientIntervalInUcastClassBEirOctets_Object = MibTableColumn
rprClientIntervalInUcastClassBEirOctets = _RprClientIntervalInUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 10),
    _RprClientIntervalInUcastClassBEirOctets_Type()
)
rprClientIntervalInUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInUcastClassBEirOctets.setStatus("current")
_RprClientIntervalInUcastClassCFrames_Type = HCPerfIntervalCount
_RprClientIntervalInUcastClassCFrames_Object = MibTableColumn
rprClientIntervalInUcastClassCFrames = _RprClientIntervalInUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 11),
    _RprClientIntervalInUcastClassCFrames_Type()
)
rprClientIntervalInUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInUcastClassCFrames.setStatus("current")
_RprClientIntervalInUcastClassCOctets_Type = HCPerfIntervalCount
_RprClientIntervalInUcastClassCOctets_Object = MibTableColumn
rprClientIntervalInUcastClassCOctets = _RprClientIntervalInUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 12),
    _RprClientIntervalInUcastClassCOctets_Type()
)
rprClientIntervalInUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInUcastClassCOctets.setStatus("current")
_RprClientIntervalInMcastClassAFrames_Type = HCPerfIntervalCount
_RprClientIntervalInMcastClassAFrames_Object = MibTableColumn
rprClientIntervalInMcastClassAFrames = _RprClientIntervalInMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 13),
    _RprClientIntervalInMcastClassAFrames_Type()
)
rprClientIntervalInMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInMcastClassAFrames.setStatus("current")
_RprClientIntervalInMcastClassAOctets_Type = HCPerfIntervalCount
_RprClientIntervalInMcastClassAOctets_Object = MibTableColumn
rprClientIntervalInMcastClassAOctets = _RprClientIntervalInMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 14),
    _RprClientIntervalInMcastClassAOctets_Type()
)
rprClientIntervalInMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInMcastClassAOctets.setStatus("current")
_RprClientIntervalInMcastClassBCirFrames_Type = HCPerfIntervalCount
_RprClientIntervalInMcastClassBCirFrames_Object = MibTableColumn
rprClientIntervalInMcastClassBCirFrames = _RprClientIntervalInMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 15),
    _RprClientIntervalInMcastClassBCirFrames_Type()
)
rprClientIntervalInMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInMcastClassBCirFrames.setStatus("current")
_RprClientIntervalInMcastClassBCirOctets_Type = HCPerfIntervalCount
_RprClientIntervalInMcastClassBCirOctets_Object = MibTableColumn
rprClientIntervalInMcastClassBCirOctets = _RprClientIntervalInMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 16),
    _RprClientIntervalInMcastClassBCirOctets_Type()
)
rprClientIntervalInMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInMcastClassBCirOctets.setStatus("current")
_RprClientIntervalInMcastClassBEirFrames_Type = HCPerfIntervalCount
_RprClientIntervalInMcastClassBEirFrames_Object = MibTableColumn
rprClientIntervalInMcastClassBEirFrames = _RprClientIntervalInMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 17),
    _RprClientIntervalInMcastClassBEirFrames_Type()
)
rprClientIntervalInMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInMcastClassBEirFrames.setStatus("current")
_RprClientIntervalInMcastClassBEirOctets_Type = HCPerfIntervalCount
_RprClientIntervalInMcastClassBEirOctets_Object = MibTableColumn
rprClientIntervalInMcastClassBEirOctets = _RprClientIntervalInMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 18),
    _RprClientIntervalInMcastClassBEirOctets_Type()
)
rprClientIntervalInMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInMcastClassBEirOctets.setStatus("current")
_RprClientIntervalInMcastClassCFrames_Type = HCPerfIntervalCount
_RprClientIntervalInMcastClassCFrames_Object = MibTableColumn
rprClientIntervalInMcastClassCFrames = _RprClientIntervalInMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 19),
    _RprClientIntervalInMcastClassCFrames_Type()
)
rprClientIntervalInMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInMcastClassCFrames.setStatus("current")
_RprClientIntervalInMcastClassCOctets_Type = HCPerfIntervalCount
_RprClientIntervalInMcastClassCOctets_Object = MibTableColumn
rprClientIntervalInMcastClassCOctets = _RprClientIntervalInMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 20),
    _RprClientIntervalInMcastClassCOctets_Type()
)
rprClientIntervalInMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalInMcastClassCOctets.setStatus("current")
_RprClientIntervalOutUcastClassAFrames_Type = HCPerfIntervalCount
_RprClientIntervalOutUcastClassAFrames_Object = MibTableColumn
rprClientIntervalOutUcastClassAFrames = _RprClientIntervalOutUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 21),
    _RprClientIntervalOutUcastClassAFrames_Type()
)
rprClientIntervalOutUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutUcastClassAFrames.setStatus("current")
_RprClientIntervalOutUcastClassAOctets_Type = HCPerfIntervalCount
_RprClientIntervalOutUcastClassAOctets_Object = MibTableColumn
rprClientIntervalOutUcastClassAOctets = _RprClientIntervalOutUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 22),
    _RprClientIntervalOutUcastClassAOctets_Type()
)
rprClientIntervalOutUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutUcastClassAOctets.setStatus("current")
_RprClientIntervalOutUcastClassBCirFrames_Type = HCPerfIntervalCount
_RprClientIntervalOutUcastClassBCirFrames_Object = MibTableColumn
rprClientIntervalOutUcastClassBCirFrames = _RprClientIntervalOutUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 23),
    _RprClientIntervalOutUcastClassBCirFrames_Type()
)
rprClientIntervalOutUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutUcastClassBCirFrames.setStatus("current")
_RprClientIntervalOutUcastClassBCirOctets_Type = HCPerfIntervalCount
_RprClientIntervalOutUcastClassBCirOctets_Object = MibTableColumn
rprClientIntervalOutUcastClassBCirOctets = _RprClientIntervalOutUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 24),
    _RprClientIntervalOutUcastClassBCirOctets_Type()
)
rprClientIntervalOutUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutUcastClassBCirOctets.setStatus("current")
_RprClientIntervalOutUcastClassBEirFrames_Type = HCPerfIntervalCount
_RprClientIntervalOutUcastClassBEirFrames_Object = MibTableColumn
rprClientIntervalOutUcastClassBEirFrames = _RprClientIntervalOutUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 25),
    _RprClientIntervalOutUcastClassBEirFrames_Type()
)
rprClientIntervalOutUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutUcastClassBEirFrames.setStatus("current")
_RprClientIntervalOutUcastClassBEirOctets_Type = HCPerfIntervalCount
_RprClientIntervalOutUcastClassBEirOctets_Object = MibTableColumn
rprClientIntervalOutUcastClassBEirOctets = _RprClientIntervalOutUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 26),
    _RprClientIntervalOutUcastClassBEirOctets_Type()
)
rprClientIntervalOutUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutUcastClassBEirOctets.setStatus("current")
_RprClientIntervalOutUcastClassCFrames_Type = HCPerfIntervalCount
_RprClientIntervalOutUcastClassCFrames_Object = MibTableColumn
rprClientIntervalOutUcastClassCFrames = _RprClientIntervalOutUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 27),
    _RprClientIntervalOutUcastClassCFrames_Type()
)
rprClientIntervalOutUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutUcastClassCFrames.setStatus("current")
_RprClientIntervalOutUcastClassCOctets_Type = HCPerfIntervalCount
_RprClientIntervalOutUcastClassCOctets_Object = MibTableColumn
rprClientIntervalOutUcastClassCOctets = _RprClientIntervalOutUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 28),
    _RprClientIntervalOutUcastClassCOctets_Type()
)
rprClientIntervalOutUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutUcastClassCOctets.setStatus("current")
_RprClientIntervalOutMcastClassAFrames_Type = HCPerfIntervalCount
_RprClientIntervalOutMcastClassAFrames_Object = MibTableColumn
rprClientIntervalOutMcastClassAFrames = _RprClientIntervalOutMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 29),
    _RprClientIntervalOutMcastClassAFrames_Type()
)
rprClientIntervalOutMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutMcastClassAFrames.setStatus("current")
_RprClientIntervalOutMcastClassAOctets_Type = HCPerfIntervalCount
_RprClientIntervalOutMcastClassAOctets_Object = MibTableColumn
rprClientIntervalOutMcastClassAOctets = _RprClientIntervalOutMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 30),
    _RprClientIntervalOutMcastClassAOctets_Type()
)
rprClientIntervalOutMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutMcastClassAOctets.setStatus("current")
_RprClientIntervalOutMcastClassBCirFrames_Type = HCPerfIntervalCount
_RprClientIntervalOutMcastClassBCirFrames_Object = MibTableColumn
rprClientIntervalOutMcastClassBCirFrames = _RprClientIntervalOutMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 31),
    _RprClientIntervalOutMcastClassBCirFrames_Type()
)
rprClientIntervalOutMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutMcastClassBCirFrames.setStatus("current")
_RprClientIntervalOutMcastClassBCirOctets_Type = HCPerfIntervalCount
_RprClientIntervalOutMcastClassBCirOctets_Object = MibTableColumn
rprClientIntervalOutMcastClassBCirOctets = _RprClientIntervalOutMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 32),
    _RprClientIntervalOutMcastClassBCirOctets_Type()
)
rprClientIntervalOutMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutMcastClassBCirOctets.setStatus("current")
_RprClientIntervalOutMcastClassBEirFrames_Type = HCPerfIntervalCount
_RprClientIntervalOutMcastClassBEirFrames_Object = MibTableColumn
rprClientIntervalOutMcastClassBEirFrames = _RprClientIntervalOutMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 33),
    _RprClientIntervalOutMcastClassBEirFrames_Type()
)
rprClientIntervalOutMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutMcastClassBEirFrames.setStatus("current")
_RprClientIntervalOutMcastClassBEirOctets_Type = HCPerfIntervalCount
_RprClientIntervalOutMcastClassBEirOctets_Object = MibTableColumn
rprClientIntervalOutMcastClassBEirOctets = _RprClientIntervalOutMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 34),
    _RprClientIntervalOutMcastClassBEirOctets_Type()
)
rprClientIntervalOutMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutMcastClassBEirOctets.setStatus("current")
_RprClientIntervalOutMcastClassCFrames_Type = HCPerfIntervalCount
_RprClientIntervalOutMcastClassCFrames_Object = MibTableColumn
rprClientIntervalOutMcastClassCFrames = _RprClientIntervalOutMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 35),
    _RprClientIntervalOutMcastClassCFrames_Type()
)
rprClientIntervalOutMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutMcastClassCFrames.setStatus("current")
_RprClientIntervalOutMcastClassCOctets_Type = HCPerfIntervalCount
_RprClientIntervalOutMcastClassCOctets_Object = MibTableColumn
rprClientIntervalOutMcastClassCOctets = _RprClientIntervalOutMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 2, 1, 36),
    _RprClientIntervalOutMcastClassCOctets_Type()
)
rprClientIntervalOutMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientIntervalOutMcastClassCOctets.setStatus("current")
_RprClientCountersDayTable_Object = MibTable
rprClientCountersDayTable = _RprClientCountersDayTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    rprClientCountersDayTable.setStatus("current")
_RprClientCountersDayEntry_Object = MibTableRow
rprClientCountersDayEntry = _RprClientCountersDayEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1)
)
rprClientCountersDayEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprClientDayIfIndex"),
)
if mibBuilder.loadTexts:
    rprClientCountersDayEntry.setStatus("current")
_RprClientDayIfIndex_Type = InterfaceIndex
_RprClientDayIfIndex_Object = MibTableColumn
rprClientDayIfIndex = _RprClientDayIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 1),
    _RprClientDayIfIndex_Type()
)
rprClientDayIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprClientDayIfIndex.setStatus("current")
_RprClientDayInUcastClassAFrames_Type = HCPerfTotalCount
_RprClientDayInUcastClassAFrames_Object = MibTableColumn
rprClientDayInUcastClassAFrames = _RprClientDayInUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 2),
    _RprClientDayInUcastClassAFrames_Type()
)
rprClientDayInUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInUcastClassAFrames.setStatus("current")
_RprClientDayInUcastClassAOctets_Type = HCPerfTotalCount
_RprClientDayInUcastClassAOctets_Object = MibTableColumn
rprClientDayInUcastClassAOctets = _RprClientDayInUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 3),
    _RprClientDayInUcastClassAOctets_Type()
)
rprClientDayInUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInUcastClassAOctets.setStatus("current")
_RprClientDayInUcastClassBCirFrames_Type = HCPerfTotalCount
_RprClientDayInUcastClassBCirFrames_Object = MibTableColumn
rprClientDayInUcastClassBCirFrames = _RprClientDayInUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 4),
    _RprClientDayInUcastClassBCirFrames_Type()
)
rprClientDayInUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInUcastClassBCirFrames.setStatus("current")
_RprClientDayInUcastClassBCirOctets_Type = HCPerfTotalCount
_RprClientDayInUcastClassBCirOctets_Object = MibTableColumn
rprClientDayInUcastClassBCirOctets = _RprClientDayInUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 5),
    _RprClientDayInUcastClassBCirOctets_Type()
)
rprClientDayInUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInUcastClassBCirOctets.setStatus("current")
_RprClientDayInUcastClassBEirFrames_Type = HCPerfTotalCount
_RprClientDayInUcastClassBEirFrames_Object = MibTableColumn
rprClientDayInUcastClassBEirFrames = _RprClientDayInUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 6),
    _RprClientDayInUcastClassBEirFrames_Type()
)
rprClientDayInUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInUcastClassBEirFrames.setStatus("current")
_RprClientDayInUcastClassBEirOctets_Type = HCPerfTotalCount
_RprClientDayInUcastClassBEirOctets_Object = MibTableColumn
rprClientDayInUcastClassBEirOctets = _RprClientDayInUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 7),
    _RprClientDayInUcastClassBEirOctets_Type()
)
rprClientDayInUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInUcastClassBEirOctets.setStatus("current")
_RprClientDayInUcastClassCFrames_Type = HCPerfTotalCount
_RprClientDayInUcastClassCFrames_Object = MibTableColumn
rprClientDayInUcastClassCFrames = _RprClientDayInUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 8),
    _RprClientDayInUcastClassCFrames_Type()
)
rprClientDayInUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInUcastClassCFrames.setStatus("current")
_RprClientDayInUcastClassCOctets_Type = HCPerfTotalCount
_RprClientDayInUcastClassCOctets_Object = MibTableColumn
rprClientDayInUcastClassCOctets = _RprClientDayInUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 9),
    _RprClientDayInUcastClassCOctets_Type()
)
rprClientDayInUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInUcastClassCOctets.setStatus("current")
_RprClientDayInMcastClassAFrames_Type = HCPerfTotalCount
_RprClientDayInMcastClassAFrames_Object = MibTableColumn
rprClientDayInMcastClassAFrames = _RprClientDayInMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 10),
    _RprClientDayInMcastClassAFrames_Type()
)
rprClientDayInMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInMcastClassAFrames.setStatus("current")
_RprClientDayInMcastClassAOctets_Type = HCPerfTotalCount
_RprClientDayInMcastClassAOctets_Object = MibTableColumn
rprClientDayInMcastClassAOctets = _RprClientDayInMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 11),
    _RprClientDayInMcastClassAOctets_Type()
)
rprClientDayInMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInMcastClassAOctets.setStatus("current")
_RprClientDayInMcastClassBCirFrames_Type = HCPerfTotalCount
_RprClientDayInMcastClassBCirFrames_Object = MibTableColumn
rprClientDayInMcastClassBCirFrames = _RprClientDayInMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 12),
    _RprClientDayInMcastClassBCirFrames_Type()
)
rprClientDayInMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInMcastClassBCirFrames.setStatus("current")
_RprClientDayInMcastClassBCirOctets_Type = HCPerfTotalCount
_RprClientDayInMcastClassBCirOctets_Object = MibTableColumn
rprClientDayInMcastClassBCirOctets = _RprClientDayInMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 13),
    _RprClientDayInMcastClassBCirOctets_Type()
)
rprClientDayInMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInMcastClassBCirOctets.setStatus("current")
_RprClientDayInMcastClassBEirFrames_Type = HCPerfTotalCount
_RprClientDayInMcastClassBEirFrames_Object = MibTableColumn
rprClientDayInMcastClassBEirFrames = _RprClientDayInMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 14),
    _RprClientDayInMcastClassBEirFrames_Type()
)
rprClientDayInMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInMcastClassBEirFrames.setStatus("current")
_RprClientDayInMcastClassBEirOctets_Type = HCPerfTotalCount
_RprClientDayInMcastClassBEirOctets_Object = MibTableColumn
rprClientDayInMcastClassBEirOctets = _RprClientDayInMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 15),
    _RprClientDayInMcastClassBEirOctets_Type()
)
rprClientDayInMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInMcastClassBEirOctets.setStatus("current")
_RprClientDayInMcastClassCFrames_Type = HCPerfTotalCount
_RprClientDayInMcastClassCFrames_Object = MibTableColumn
rprClientDayInMcastClassCFrames = _RprClientDayInMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 16),
    _RprClientDayInMcastClassCFrames_Type()
)
rprClientDayInMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInMcastClassCFrames.setStatus("current")
_RprClientDayInMcastClassCOctets_Type = HCPerfTotalCount
_RprClientDayInMcastClassCOctets_Object = MibTableColumn
rprClientDayInMcastClassCOctets = _RprClientDayInMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 17),
    _RprClientDayInMcastClassCOctets_Type()
)
rprClientDayInMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayInMcastClassCOctets.setStatus("current")
_RprClientDayOutUcastClassAFrames_Type = HCPerfTotalCount
_RprClientDayOutUcastClassAFrames_Object = MibTableColumn
rprClientDayOutUcastClassAFrames = _RprClientDayOutUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 18),
    _RprClientDayOutUcastClassAFrames_Type()
)
rprClientDayOutUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutUcastClassAFrames.setStatus("current")
_RprClientDayOutUcastClassAOctets_Type = HCPerfTotalCount
_RprClientDayOutUcastClassAOctets_Object = MibTableColumn
rprClientDayOutUcastClassAOctets = _RprClientDayOutUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 19),
    _RprClientDayOutUcastClassAOctets_Type()
)
rprClientDayOutUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutUcastClassAOctets.setStatus("current")
_RprClientDayOutUcastClassBCirFrames_Type = HCPerfTotalCount
_RprClientDayOutUcastClassBCirFrames_Object = MibTableColumn
rprClientDayOutUcastClassBCirFrames = _RprClientDayOutUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 20),
    _RprClientDayOutUcastClassBCirFrames_Type()
)
rprClientDayOutUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutUcastClassBCirFrames.setStatus("current")
_RprClientDayOutUcastClassBCirOctets_Type = HCPerfTotalCount
_RprClientDayOutUcastClassBCirOctets_Object = MibTableColumn
rprClientDayOutUcastClassBCirOctets = _RprClientDayOutUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 21),
    _RprClientDayOutUcastClassBCirOctets_Type()
)
rprClientDayOutUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutUcastClassBCirOctets.setStatus("current")
_RprClientDayOutUcastClassBEirFrames_Type = HCPerfTotalCount
_RprClientDayOutUcastClassBEirFrames_Object = MibTableColumn
rprClientDayOutUcastClassBEirFrames = _RprClientDayOutUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 22),
    _RprClientDayOutUcastClassBEirFrames_Type()
)
rprClientDayOutUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutUcastClassBEirFrames.setStatus("current")
_RprClientDayOutUcastClassBEirOctets_Type = HCPerfTotalCount
_RprClientDayOutUcastClassBEirOctets_Object = MibTableColumn
rprClientDayOutUcastClassBEirOctets = _RprClientDayOutUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 23),
    _RprClientDayOutUcastClassBEirOctets_Type()
)
rprClientDayOutUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutUcastClassBEirOctets.setStatus("current")
_RprClientDayOutUcastClassCFrames_Type = HCPerfTotalCount
_RprClientDayOutUcastClassCFrames_Object = MibTableColumn
rprClientDayOutUcastClassCFrames = _RprClientDayOutUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 24),
    _RprClientDayOutUcastClassCFrames_Type()
)
rprClientDayOutUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutUcastClassCFrames.setStatus("current")
_RprClientDayOutUcastClassCOctets_Type = HCPerfTotalCount
_RprClientDayOutUcastClassCOctets_Object = MibTableColumn
rprClientDayOutUcastClassCOctets = _RprClientDayOutUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 25),
    _RprClientDayOutUcastClassCOctets_Type()
)
rprClientDayOutUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutUcastClassCOctets.setStatus("current")
_RprClientDayOutMcastClassAFrames_Type = HCPerfTotalCount
_RprClientDayOutMcastClassAFrames_Object = MibTableColumn
rprClientDayOutMcastClassAFrames = _RprClientDayOutMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 26),
    _RprClientDayOutMcastClassAFrames_Type()
)
rprClientDayOutMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutMcastClassAFrames.setStatus("current")
_RprClientDayOutMcastClassAOctets_Type = HCPerfTotalCount
_RprClientDayOutMcastClassAOctets_Object = MibTableColumn
rprClientDayOutMcastClassAOctets = _RprClientDayOutMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 27),
    _RprClientDayOutMcastClassAOctets_Type()
)
rprClientDayOutMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutMcastClassAOctets.setStatus("current")
_RprClientDayOutMcastClassBCirFrames_Type = HCPerfTotalCount
_RprClientDayOutMcastClassBCirFrames_Object = MibTableColumn
rprClientDayOutMcastClassBCirFrames = _RprClientDayOutMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 28),
    _RprClientDayOutMcastClassBCirFrames_Type()
)
rprClientDayOutMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutMcastClassBCirFrames.setStatus("current")
_RprClientDayOutMcastClassBCirOctets_Type = HCPerfTotalCount
_RprClientDayOutMcastClassBCirOctets_Object = MibTableColumn
rprClientDayOutMcastClassBCirOctets = _RprClientDayOutMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 29),
    _RprClientDayOutMcastClassBCirOctets_Type()
)
rprClientDayOutMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutMcastClassBCirOctets.setStatus("current")
_RprClientDayOutMcastClassBEirFrames_Type = HCPerfTotalCount
_RprClientDayOutMcastClassBEirFrames_Object = MibTableColumn
rprClientDayOutMcastClassBEirFrames = _RprClientDayOutMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 30),
    _RprClientDayOutMcastClassBEirFrames_Type()
)
rprClientDayOutMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutMcastClassBEirFrames.setStatus("current")
_RprClientDayOutMcastClassBEirOctets_Type = HCPerfTotalCount
_RprClientDayOutMcastClassBEirOctets_Object = MibTableColumn
rprClientDayOutMcastClassBEirOctets = _RprClientDayOutMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 31),
    _RprClientDayOutMcastClassBEirOctets_Type()
)
rprClientDayOutMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutMcastClassBEirOctets.setStatus("current")
_RprClientDayOutMcastClassCFrames_Type = HCPerfTotalCount
_RprClientDayOutMcastClassCFrames_Object = MibTableColumn
rprClientDayOutMcastClassCFrames = _RprClientDayOutMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 32),
    _RprClientDayOutMcastClassCFrames_Type()
)
rprClientDayOutMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutMcastClassCFrames.setStatus("current")
_RprClientDayOutMcastClassCOctets_Type = HCPerfTotalCount
_RprClientDayOutMcastClassCOctets_Object = MibTableColumn
rprClientDayOutMcastClassCOctets = _RprClientDayOutMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 3, 1, 33),
    _RprClientDayOutMcastClassCOctets_Type()
)
rprClientDayOutMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientDayOutMcastClassCOctets.setStatus("current")
_RprClientCountersStatsTable_Object = MibTable
rprClientCountersStatsTable = _RprClientCountersStatsTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    rprClientCountersStatsTable.setStatus("current")
_RprClientCountersStatsEntry_Object = MibTableRow
rprClientCountersStatsEntry = _RprClientCountersStatsEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1)
)
rprClientCountersStatsEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprClientStatsIfIndex"),
)
if mibBuilder.loadTexts:
    rprClientCountersStatsEntry.setStatus("current")
_RprClientStatsIfIndex_Type = InterfaceIndex
_RprClientStatsIfIndex_Object = MibTableColumn
rprClientStatsIfIndex = _RprClientStatsIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 1),
    _RprClientStatsIfIndex_Type()
)
rprClientStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprClientStatsIfIndex.setStatus("current")
_RprClientStatsInUcastClassAFrames_Type = Counter64
_RprClientStatsInUcastClassAFrames_Object = MibTableColumn
rprClientStatsInUcastClassAFrames = _RprClientStatsInUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 2),
    _RprClientStatsInUcastClassAFrames_Type()
)
rprClientStatsInUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInUcastClassAFrames.setStatus("current")
_RprClientStatsInUcastClassAOctets_Type = Counter64
_RprClientStatsInUcastClassAOctets_Object = MibTableColumn
rprClientStatsInUcastClassAOctets = _RprClientStatsInUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 3),
    _RprClientStatsInUcastClassAOctets_Type()
)
rprClientStatsInUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInUcastClassAOctets.setStatus("current")
_RprClientStatsInUcastClassBCirFrames_Type = Counter64
_RprClientStatsInUcastClassBCirFrames_Object = MibTableColumn
rprClientStatsInUcastClassBCirFrames = _RprClientStatsInUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 4),
    _RprClientStatsInUcastClassBCirFrames_Type()
)
rprClientStatsInUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInUcastClassBCirFrames.setStatus("current")
_RprClientStatsInUcastClassBCirOctets_Type = Counter64
_RprClientStatsInUcastClassBCirOctets_Object = MibTableColumn
rprClientStatsInUcastClassBCirOctets = _RprClientStatsInUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 5),
    _RprClientStatsInUcastClassBCirOctets_Type()
)
rprClientStatsInUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInUcastClassBCirOctets.setStatus("current")
_RprClientStatsInUcastClassBEirFrames_Type = Counter64
_RprClientStatsInUcastClassBEirFrames_Object = MibTableColumn
rprClientStatsInUcastClassBEirFrames = _RprClientStatsInUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 6),
    _RprClientStatsInUcastClassBEirFrames_Type()
)
rprClientStatsInUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInUcastClassBEirFrames.setStatus("current")
_RprClientStatsInUcastClassBEirOctets_Type = Counter64
_RprClientStatsInUcastClassBEirOctets_Object = MibTableColumn
rprClientStatsInUcastClassBEirOctets = _RprClientStatsInUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 7),
    _RprClientStatsInUcastClassBEirOctets_Type()
)
rprClientStatsInUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInUcastClassBEirOctets.setStatus("current")
_RprClientStatsInUcastClassCFrames_Type = Counter64
_RprClientStatsInUcastClassCFrames_Object = MibTableColumn
rprClientStatsInUcastClassCFrames = _RprClientStatsInUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 8),
    _RprClientStatsInUcastClassCFrames_Type()
)
rprClientStatsInUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInUcastClassCFrames.setStatus("current")
_RprClientStatsInUcastClassCOctets_Type = Counter64
_RprClientStatsInUcastClassCOctets_Object = MibTableColumn
rprClientStatsInUcastClassCOctets = _RprClientStatsInUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 9),
    _RprClientStatsInUcastClassCOctets_Type()
)
rprClientStatsInUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInUcastClassCOctets.setStatus("current")
_RprClientStatsInMcastClassAFrames_Type = Counter64
_RprClientStatsInMcastClassAFrames_Object = MibTableColumn
rprClientStatsInMcastClassAFrames = _RprClientStatsInMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 10),
    _RprClientStatsInMcastClassAFrames_Type()
)
rprClientStatsInMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInMcastClassAFrames.setStatus("current")
_RprClientStatsInMcastClassAOctets_Type = Counter64
_RprClientStatsInMcastClassAOctets_Object = MibTableColumn
rprClientStatsInMcastClassAOctets = _RprClientStatsInMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 11),
    _RprClientStatsInMcastClassAOctets_Type()
)
rprClientStatsInMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInMcastClassAOctets.setStatus("current")
_RprClientStatsInMcastClassBCirFrames_Type = Counter64
_RprClientStatsInMcastClassBCirFrames_Object = MibTableColumn
rprClientStatsInMcastClassBCirFrames = _RprClientStatsInMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 12),
    _RprClientStatsInMcastClassBCirFrames_Type()
)
rprClientStatsInMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInMcastClassBCirFrames.setStatus("current")
_RprClientStatsInMcastClassBCirOctets_Type = Counter64
_RprClientStatsInMcastClassBCirOctets_Object = MibTableColumn
rprClientStatsInMcastClassBCirOctets = _RprClientStatsInMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 13),
    _RprClientStatsInMcastClassBCirOctets_Type()
)
rprClientStatsInMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInMcastClassBCirOctets.setStatus("current")
_RprClientStatsInMcastClassBEirFrames_Type = Counter64
_RprClientStatsInMcastClassBEirFrames_Object = MibTableColumn
rprClientStatsInMcastClassBEirFrames = _RprClientStatsInMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 14),
    _RprClientStatsInMcastClassBEirFrames_Type()
)
rprClientStatsInMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInMcastClassBEirFrames.setStatus("current")
_RprClientStatsInMcastClassBEirOctets_Type = Counter64
_RprClientStatsInMcastClassBEirOctets_Object = MibTableColumn
rprClientStatsInMcastClassBEirOctets = _RprClientStatsInMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 15),
    _RprClientStatsInMcastClassBEirOctets_Type()
)
rprClientStatsInMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInMcastClassBEirOctets.setStatus("current")
_RprClientStatsInMcastClassCFrames_Type = Counter64
_RprClientStatsInMcastClassCFrames_Object = MibTableColumn
rprClientStatsInMcastClassCFrames = _RprClientStatsInMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 16),
    _RprClientStatsInMcastClassCFrames_Type()
)
rprClientStatsInMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInMcastClassCFrames.setStatus("current")
_RprClientStatsInMcastClassCOctets_Type = Counter64
_RprClientStatsInMcastClassCOctets_Object = MibTableColumn
rprClientStatsInMcastClassCOctets = _RprClientStatsInMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 17),
    _RprClientStatsInMcastClassCOctets_Type()
)
rprClientStatsInMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInMcastClassCOctets.setStatus("current")
_RprClientStatsInBcastFrames_Type = Counter64
_RprClientStatsInBcastFrames_Object = MibTableColumn
rprClientStatsInBcastFrames = _RprClientStatsInBcastFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 18),
    _RprClientStatsInBcastFrames_Type()
)
rprClientStatsInBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsInBcastFrames.setStatus("current")
_RprClientStatsOutUcastClassAFrames_Type = Counter64
_RprClientStatsOutUcastClassAFrames_Object = MibTableColumn
rprClientStatsOutUcastClassAFrames = _RprClientStatsOutUcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 19),
    _RprClientStatsOutUcastClassAFrames_Type()
)
rprClientStatsOutUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutUcastClassAFrames.setStatus("current")
_RprClientStatsOutUcastClassAOctets_Type = Counter64
_RprClientStatsOutUcastClassAOctets_Object = MibTableColumn
rprClientStatsOutUcastClassAOctets = _RprClientStatsOutUcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 20),
    _RprClientStatsOutUcastClassAOctets_Type()
)
rprClientStatsOutUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutUcastClassAOctets.setStatus("current")
_RprClientStatsOutUcastClassBCirFrames_Type = Counter64
_RprClientStatsOutUcastClassBCirFrames_Object = MibTableColumn
rprClientStatsOutUcastClassBCirFrames = _RprClientStatsOutUcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 21),
    _RprClientStatsOutUcastClassBCirFrames_Type()
)
rprClientStatsOutUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutUcastClassBCirFrames.setStatus("current")
_RprClientStatsOutUcastClassBCirOctets_Type = Counter64
_RprClientStatsOutUcastClassBCirOctets_Object = MibTableColumn
rprClientStatsOutUcastClassBCirOctets = _RprClientStatsOutUcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 22),
    _RprClientStatsOutUcastClassBCirOctets_Type()
)
rprClientStatsOutUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutUcastClassBCirOctets.setStatus("current")
_RprClientStatsOutUcastClassBEirFrames_Type = Counter64
_RprClientStatsOutUcastClassBEirFrames_Object = MibTableColumn
rprClientStatsOutUcastClassBEirFrames = _RprClientStatsOutUcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 23),
    _RprClientStatsOutUcastClassBEirFrames_Type()
)
rprClientStatsOutUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutUcastClassBEirFrames.setStatus("current")
_RprClientStatsOutUcastClassBEirOctets_Type = Counter64
_RprClientStatsOutUcastClassBEirOctets_Object = MibTableColumn
rprClientStatsOutUcastClassBEirOctets = _RprClientStatsOutUcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 24),
    _RprClientStatsOutUcastClassBEirOctets_Type()
)
rprClientStatsOutUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutUcastClassBEirOctets.setStatus("current")
_RprClientStatsOutUcastClassCFrames_Type = Counter64
_RprClientStatsOutUcastClassCFrames_Object = MibTableColumn
rprClientStatsOutUcastClassCFrames = _RprClientStatsOutUcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 25),
    _RprClientStatsOutUcastClassCFrames_Type()
)
rprClientStatsOutUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutUcastClassCFrames.setStatus("current")
_RprClientStatsOutUcastClassCOctets_Type = Counter64
_RprClientStatsOutUcastClassCOctets_Object = MibTableColumn
rprClientStatsOutUcastClassCOctets = _RprClientStatsOutUcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 26),
    _RprClientStatsOutUcastClassCOctets_Type()
)
rprClientStatsOutUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutUcastClassCOctets.setStatus("current")
_RprClientStatsOutMcastClassAFrames_Type = Counter64
_RprClientStatsOutMcastClassAFrames_Object = MibTableColumn
rprClientStatsOutMcastClassAFrames = _RprClientStatsOutMcastClassAFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 27),
    _RprClientStatsOutMcastClassAFrames_Type()
)
rprClientStatsOutMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutMcastClassAFrames.setStatus("current")
_RprClientStatsOutMcastClassAOctets_Type = Counter64
_RprClientStatsOutMcastClassAOctets_Object = MibTableColumn
rprClientStatsOutMcastClassAOctets = _RprClientStatsOutMcastClassAOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 28),
    _RprClientStatsOutMcastClassAOctets_Type()
)
rprClientStatsOutMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutMcastClassAOctets.setStatus("current")
_RprClientStatsOutMcastClassBCirFrames_Type = Counter64
_RprClientStatsOutMcastClassBCirFrames_Object = MibTableColumn
rprClientStatsOutMcastClassBCirFrames = _RprClientStatsOutMcastClassBCirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 29),
    _RprClientStatsOutMcastClassBCirFrames_Type()
)
rprClientStatsOutMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutMcastClassBCirFrames.setStatus("current")
_RprClientStatsOutMcastClassBCirOctets_Type = Counter64
_RprClientStatsOutMcastClassBCirOctets_Object = MibTableColumn
rprClientStatsOutMcastClassBCirOctets = _RprClientStatsOutMcastClassBCirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 30),
    _RprClientStatsOutMcastClassBCirOctets_Type()
)
rprClientStatsOutMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutMcastClassBCirOctets.setStatus("current")
_RprClientStatsOutMcastClassBEirFrames_Type = Counter64
_RprClientStatsOutMcastClassBEirFrames_Object = MibTableColumn
rprClientStatsOutMcastClassBEirFrames = _RprClientStatsOutMcastClassBEirFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 31),
    _RprClientStatsOutMcastClassBEirFrames_Type()
)
rprClientStatsOutMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutMcastClassBEirFrames.setStatus("current")
_RprClientStatsOutMcastClassBEirOctets_Type = Counter64
_RprClientStatsOutMcastClassBEirOctets_Object = MibTableColumn
rprClientStatsOutMcastClassBEirOctets = _RprClientStatsOutMcastClassBEirOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 32),
    _RprClientStatsOutMcastClassBEirOctets_Type()
)
rprClientStatsOutMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutMcastClassBEirOctets.setStatus("current")
_RprClientStatsOutMcastClassCFrames_Type = Counter64
_RprClientStatsOutMcastClassCFrames_Object = MibTableColumn
rprClientStatsOutMcastClassCFrames = _RprClientStatsOutMcastClassCFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 33),
    _RprClientStatsOutMcastClassCFrames_Type()
)
rprClientStatsOutMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutMcastClassCFrames.setStatus("current")
_RprClientStatsOutMcastClassCOctets_Type = Counter64
_RprClientStatsOutMcastClassCOctets_Object = MibTableColumn
rprClientStatsOutMcastClassCOctets = _RprClientStatsOutMcastClassCOctets_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 34),
    _RprClientStatsOutMcastClassCOctets_Type()
)
rprClientStatsOutMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutMcastClassCOctets.setStatus("current")
_RprClientStatsOutBcastFrames_Type = Counter64
_RprClientStatsOutBcastFrames_Object = MibTableColumn
rprClientStatsOutBcastFrames = _RprClientStatsOutBcastFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 4, 4, 1, 35),
    _RprClientStatsOutBcastFrames_Type()
)
rprClientStatsOutBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprClientStatsOutBcastFrames.setStatus("current")
_RprSpanErrorCounters_ObjectIdentity = ObjectIdentity
rprSpanErrorCounters = _RprSpanErrorCounters_ObjectIdentity(
    (1, 0, 8802, 17, 1, 1, 1, 5)
)
_RprSpanErrorCountersCurrentTable_Object = MibTable
rprSpanErrorCountersCurrentTable = _RprSpanErrorCountersCurrentTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rprSpanErrorCountersCurrentTable.setStatus("current")
_RprSpanErrorCountersCurrentEntry_Object = MibTableRow
rprSpanErrorCountersCurrentEntry = _RprSpanErrorCountersCurrentEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1)
)
rprSpanErrorCountersCurrentEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentIfIndex"),
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentSpan"),
)
if mibBuilder.loadTexts:
    rprSpanErrorCountersCurrentEntry.setStatus("current")
_RprSpanErrorCurrentIfIndex_Type = InterfaceIndex
_RprSpanErrorCurrentIfIndex_Object = MibTableColumn
rprSpanErrorCurrentIfIndex = _RprSpanErrorCurrentIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 1),
    _RprSpanErrorCurrentIfIndex_Type()
)
rprSpanErrorCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentIfIndex.setStatus("current")
_RprSpanErrorCurrentSpan_Type = RprSpan
_RprSpanErrorCurrentSpan_Object = MibTableColumn
rprSpanErrorCurrentSpan = _RprSpanErrorCurrentSpan_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 2),
    _RprSpanErrorCurrentSpan_Type()
)
rprSpanErrorCurrentSpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentSpan.setStatus("current")
_RprSpanErrorCurrentTtlExpFrames_Type = HCPerfCurrentCount
_RprSpanErrorCurrentTtlExpFrames_Object = MibTableColumn
rprSpanErrorCurrentTtlExpFrames = _RprSpanErrorCurrentTtlExpFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 3),
    _RprSpanErrorCurrentTtlExpFrames_Type()
)
rprSpanErrorCurrentTtlExpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentTtlExpFrames.setStatus("current")
_RprSpanErrorCurrentTooLongFrames_Type = HCPerfCurrentCount
_RprSpanErrorCurrentTooLongFrames_Object = MibTableColumn
rprSpanErrorCurrentTooLongFrames = _RprSpanErrorCurrentTooLongFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 4),
    _RprSpanErrorCurrentTooLongFrames_Type()
)
rprSpanErrorCurrentTooLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentTooLongFrames.setStatus("current")
_RprSpanErrorCurrentTooShortFrames_Type = HCPerfCurrentCount
_RprSpanErrorCurrentTooShortFrames_Object = MibTableColumn
rprSpanErrorCurrentTooShortFrames = _RprSpanErrorCurrentTooShortFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 5),
    _RprSpanErrorCurrentTooShortFrames_Type()
)
rprSpanErrorCurrentTooShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentTooShortFrames.setStatus("current")
_RprSpanErrorCurrentBadHecFrames_Type = HCPerfCurrentCount
_RprSpanErrorCurrentBadHecFrames_Object = MibTableColumn
rprSpanErrorCurrentBadHecFrames = _RprSpanErrorCurrentBadHecFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 6),
    _RprSpanErrorCurrentBadHecFrames_Type()
)
rprSpanErrorCurrentBadHecFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentBadHecFrames.setStatus("current")
_RprSpanErrorCurrentBadFcsFrames_Type = HCPerfCurrentCount
_RprSpanErrorCurrentBadFcsFrames_Object = MibTableColumn
rprSpanErrorCurrentBadFcsFrames = _RprSpanErrorCurrentBadFcsFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 7),
    _RprSpanErrorCurrentBadFcsFrames_Type()
)
rprSpanErrorCurrentBadFcsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentBadFcsFrames.setStatus("current")
_RprSpanErrorCurrentSelfSrcUcastFrames_Type = HCPerfCurrentCount
_RprSpanErrorCurrentSelfSrcUcastFrames_Object = MibTableColumn
rprSpanErrorCurrentSelfSrcUcastFrames = _RprSpanErrorCurrentSelfSrcUcastFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 8),
    _RprSpanErrorCurrentSelfSrcUcastFrames_Type()
)
rprSpanErrorCurrentSelfSrcUcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentSelfSrcUcastFrames.setStatus("current")
_RprSpanErrorCurrentPmdAbortFrames_Type = HCPerfCurrentCount
_RprSpanErrorCurrentPmdAbortFrames_Object = MibTableColumn
rprSpanErrorCurrentPmdAbortFrames = _RprSpanErrorCurrentPmdAbortFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 9),
    _RprSpanErrorCurrentPmdAbortFrames_Type()
)
rprSpanErrorCurrentPmdAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentPmdAbortFrames.setStatus("current")
_RprSpanErrorCurrentBadAddrFrames_Type = HCPerfCurrentCount
_RprSpanErrorCurrentBadAddrFrames_Object = MibTableColumn
rprSpanErrorCurrentBadAddrFrames = _RprSpanErrorCurrentBadAddrFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 10),
    _RprSpanErrorCurrentBadAddrFrames_Type()
)
rprSpanErrorCurrentBadAddrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentBadAddrFrames.setStatus("current")
_RprSpanErrorCurrentBadParityFrames_Type = HCPerfCurrentCount
_RprSpanErrorCurrentBadParityFrames_Object = MibTableColumn
rprSpanErrorCurrentBadParityFrames = _RprSpanErrorCurrentBadParityFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 11),
    _RprSpanErrorCurrentBadParityFrames_Type()
)
rprSpanErrorCurrentBadParityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentBadParityFrames.setStatus("current")
_RprSpanErrorCurrentContainedFrames_Type = HCPerfCurrentCount
_RprSpanErrorCurrentContainedFrames_Object = MibTableColumn
rprSpanErrorCurrentContainedFrames = _RprSpanErrorCurrentContainedFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 12),
    _RprSpanErrorCurrentContainedFrames_Type()
)
rprSpanErrorCurrentContainedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentContainedFrames.setStatus("current")
_RprSpanErrorCurrentScffErrors_Type = HCPerfCurrentCount
_RprSpanErrorCurrentScffErrors_Object = MibTableColumn
rprSpanErrorCurrentScffErrors = _RprSpanErrorCurrentScffErrors_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 13),
    _RprSpanErrorCurrentScffErrors_Type()
)
rprSpanErrorCurrentScffErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentScffErrors.setStatus("current")
_RprSpanErrorCurrentErroredSeconds_Type = HCPerfCurrentCount
_RprSpanErrorCurrentErroredSeconds_Object = MibTableColumn
rprSpanErrorCurrentErroredSeconds = _RprSpanErrorCurrentErroredSeconds_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 14),
    _RprSpanErrorCurrentErroredSeconds_Type()
)
rprSpanErrorCurrentErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentErroredSeconds.setStatus("current")
_RprSpanErrorCurrentSeverelyErroredSeconds_Type = HCPerfCurrentCount
_RprSpanErrorCurrentSeverelyErroredSeconds_Object = MibTableColumn
rprSpanErrorCurrentSeverelyErroredSeconds = _RprSpanErrorCurrentSeverelyErroredSeconds_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 15),
    _RprSpanErrorCurrentSeverelyErroredSeconds_Type()
)
rprSpanErrorCurrentSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentSeverelyErroredSeconds.setStatus("current")
_RprSpanErrorCurrentUnavailableSeconds_Type = HCPerfCurrentCount
_RprSpanErrorCurrentUnavailableSeconds_Object = MibTableColumn
rprSpanErrorCurrentUnavailableSeconds = _RprSpanErrorCurrentUnavailableSeconds_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 1, 1, 16),
    _RprSpanErrorCurrentUnavailableSeconds_Type()
)
rprSpanErrorCurrentUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorCurrentUnavailableSeconds.setStatus("current")
_RprSpanErrorCountersIntervalTable_Object = MibTable
rprSpanErrorCountersIntervalTable = _RprSpanErrorCountersIntervalTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    rprSpanErrorCountersIntervalTable.setStatus("current")
_RprSpanErrorCountersIntervalEntry_Object = MibTableRow
rprSpanErrorCountersIntervalEntry = _RprSpanErrorCountersIntervalEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1)
)
rprSpanErrorCountersIntervalEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalIfIndex"),
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalSpan"),
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalNumber"),
)
if mibBuilder.loadTexts:
    rprSpanErrorCountersIntervalEntry.setStatus("current")
_RprSpanErrorIntervalIfIndex_Type = InterfaceIndex
_RprSpanErrorIntervalIfIndex_Object = MibTableColumn
rprSpanErrorIntervalIfIndex = _RprSpanErrorIntervalIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 1),
    _RprSpanErrorIntervalIfIndex_Type()
)
rprSpanErrorIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalIfIndex.setStatus("current")
_RprSpanErrorIntervalSpan_Type = RprSpan
_RprSpanErrorIntervalSpan_Object = MibTableColumn
rprSpanErrorIntervalSpan = _RprSpanErrorIntervalSpan_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 2),
    _RprSpanErrorIntervalSpan_Type()
)
rprSpanErrorIntervalSpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalSpan.setStatus("current")


class _RprSpanErrorIntervalNumber_Type(Unsigned32):
    """Custom type rprSpanErrorIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_RprSpanErrorIntervalNumber_Type.__name__ = "Unsigned32"
_RprSpanErrorIntervalNumber_Object = MibTableColumn
rprSpanErrorIntervalNumber = _RprSpanErrorIntervalNumber_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 3),
    _RprSpanErrorIntervalNumber_Type()
)
rprSpanErrorIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalNumber.setStatus("current")
_RprSpanErrorIntervalValidData_Type = TruthValue
_RprSpanErrorIntervalValidData_Object = MibTableColumn
rprSpanErrorIntervalValidData = _RprSpanErrorIntervalValidData_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 4),
    _RprSpanErrorIntervalValidData_Type()
)
rprSpanErrorIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalValidData.setStatus("current")


class _RprSpanErrorIntervalTimeElapsed_Type(Unsigned32):
    """Custom type rprSpanErrorIntervalTimeElapsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_RprSpanErrorIntervalTimeElapsed_Type.__name__ = "Unsigned32"
_RprSpanErrorIntervalTimeElapsed_Object = MibTableColumn
rprSpanErrorIntervalTimeElapsed = _RprSpanErrorIntervalTimeElapsed_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 5),
    _RprSpanErrorIntervalTimeElapsed_Type()
)
rprSpanErrorIntervalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalTimeElapsed.setUnits("Seconds")
_RprSpanErrorIntervalTtlExpFrames_Type = HCPerfIntervalCount
_RprSpanErrorIntervalTtlExpFrames_Object = MibTableColumn
rprSpanErrorIntervalTtlExpFrames = _RprSpanErrorIntervalTtlExpFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 6),
    _RprSpanErrorIntervalTtlExpFrames_Type()
)
rprSpanErrorIntervalTtlExpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalTtlExpFrames.setStatus("current")
_RprSpanErrorIntervalTooLongFrames_Type = HCPerfIntervalCount
_RprSpanErrorIntervalTooLongFrames_Object = MibTableColumn
rprSpanErrorIntervalTooLongFrames = _RprSpanErrorIntervalTooLongFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 7),
    _RprSpanErrorIntervalTooLongFrames_Type()
)
rprSpanErrorIntervalTooLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalTooLongFrames.setStatus("current")
_RprSpanErrorIntervalTooShortFrames_Type = HCPerfIntervalCount
_RprSpanErrorIntervalTooShortFrames_Object = MibTableColumn
rprSpanErrorIntervalTooShortFrames = _RprSpanErrorIntervalTooShortFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 8),
    _RprSpanErrorIntervalTooShortFrames_Type()
)
rprSpanErrorIntervalTooShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalTooShortFrames.setStatus("current")
_RprSpanErrorIntervalBadHecFrames_Type = HCPerfIntervalCount
_RprSpanErrorIntervalBadHecFrames_Object = MibTableColumn
rprSpanErrorIntervalBadHecFrames = _RprSpanErrorIntervalBadHecFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 9),
    _RprSpanErrorIntervalBadHecFrames_Type()
)
rprSpanErrorIntervalBadHecFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalBadHecFrames.setStatus("current")
_RprSpanErrorIntervalBadFcsFrames_Type = HCPerfIntervalCount
_RprSpanErrorIntervalBadFcsFrames_Object = MibTableColumn
rprSpanErrorIntervalBadFcsFrames = _RprSpanErrorIntervalBadFcsFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 10),
    _RprSpanErrorIntervalBadFcsFrames_Type()
)
rprSpanErrorIntervalBadFcsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalBadFcsFrames.setStatus("current")
_RprSpanErrorIntervalSelfSrcUcastFrames_Type = HCPerfIntervalCount
_RprSpanErrorIntervalSelfSrcUcastFrames_Object = MibTableColumn
rprSpanErrorIntervalSelfSrcUcastFrames = _RprSpanErrorIntervalSelfSrcUcastFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 11),
    _RprSpanErrorIntervalSelfSrcUcastFrames_Type()
)
rprSpanErrorIntervalSelfSrcUcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalSelfSrcUcastFrames.setStatus("current")
_RprSpanErrorIntervalPmdAbortFrames_Type = HCPerfIntervalCount
_RprSpanErrorIntervalPmdAbortFrames_Object = MibTableColumn
rprSpanErrorIntervalPmdAbortFrames = _RprSpanErrorIntervalPmdAbortFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 12),
    _RprSpanErrorIntervalPmdAbortFrames_Type()
)
rprSpanErrorIntervalPmdAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalPmdAbortFrames.setStatus("current")
_RprSpanErrorIntervalBadAddrFrames_Type = HCPerfIntervalCount
_RprSpanErrorIntervalBadAddrFrames_Object = MibTableColumn
rprSpanErrorIntervalBadAddrFrames = _RprSpanErrorIntervalBadAddrFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 13),
    _RprSpanErrorIntervalBadAddrFrames_Type()
)
rprSpanErrorIntervalBadAddrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalBadAddrFrames.setStatus("current")
_RprSpanErrorIntervalBadParityFrames_Type = HCPerfIntervalCount
_RprSpanErrorIntervalBadParityFrames_Object = MibTableColumn
rprSpanErrorIntervalBadParityFrames = _RprSpanErrorIntervalBadParityFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 14),
    _RprSpanErrorIntervalBadParityFrames_Type()
)
rprSpanErrorIntervalBadParityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalBadParityFrames.setStatus("current")
_RprSpanErrorIntervalContainedFrames_Type = HCPerfIntervalCount
_RprSpanErrorIntervalContainedFrames_Object = MibTableColumn
rprSpanErrorIntervalContainedFrames = _RprSpanErrorIntervalContainedFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 15),
    _RprSpanErrorIntervalContainedFrames_Type()
)
rprSpanErrorIntervalContainedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalContainedFrames.setStatus("current")
_RprSpanErrorIntervalScffErrors_Type = HCPerfIntervalCount
_RprSpanErrorIntervalScffErrors_Object = MibTableColumn
rprSpanErrorIntervalScffErrors = _RprSpanErrorIntervalScffErrors_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 16),
    _RprSpanErrorIntervalScffErrors_Type()
)
rprSpanErrorIntervalScffErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalScffErrors.setStatus("current")
_RprSpanErrorIntervalErroredSeconds_Type = HCPerfIntervalCount
_RprSpanErrorIntervalErroredSeconds_Object = MibTableColumn
rprSpanErrorIntervalErroredSeconds = _RprSpanErrorIntervalErroredSeconds_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 17),
    _RprSpanErrorIntervalErroredSeconds_Type()
)
rprSpanErrorIntervalErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalErroredSeconds.setStatus("current")
_RprSpanErrorIntervalSeverelyErroredSeconds_Type = HCPerfIntervalCount
_RprSpanErrorIntervalSeverelyErroredSeconds_Object = MibTableColumn
rprSpanErrorIntervalSeverelyErroredSeconds = _RprSpanErrorIntervalSeverelyErroredSeconds_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 18),
    _RprSpanErrorIntervalSeverelyErroredSeconds_Type()
)
rprSpanErrorIntervalSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalSeverelyErroredSeconds.setStatus("current")
_RprSpanErrorIntervalUnavailableSeconds_Type = HCPerfIntervalCount
_RprSpanErrorIntervalUnavailableSeconds_Object = MibTableColumn
rprSpanErrorIntervalUnavailableSeconds = _RprSpanErrorIntervalUnavailableSeconds_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 2, 1, 19),
    _RprSpanErrorIntervalUnavailableSeconds_Type()
)
rprSpanErrorIntervalUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorIntervalUnavailableSeconds.setStatus("current")
_RprSpanErrorCountersDayTable_Object = MibTable
rprSpanErrorCountersDayTable = _RprSpanErrorCountersDayTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    rprSpanErrorCountersDayTable.setStatus("current")
_RprSpanErrorCountersDayEntry_Object = MibTableRow
rprSpanErrorCountersDayEntry = _RprSpanErrorCountersDayEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1)
)
rprSpanErrorCountersDayEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanErrorDayIfIndex"),
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanErrorDaySpan"),
)
if mibBuilder.loadTexts:
    rprSpanErrorCountersDayEntry.setStatus("current")
_RprSpanErrorDayIfIndex_Type = InterfaceIndex
_RprSpanErrorDayIfIndex_Object = MibTableColumn
rprSpanErrorDayIfIndex = _RprSpanErrorDayIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 1),
    _RprSpanErrorDayIfIndex_Type()
)
rprSpanErrorDayIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanErrorDayIfIndex.setStatus("current")
_RprSpanErrorDaySpan_Type = RprSpan
_RprSpanErrorDaySpan_Object = MibTableColumn
rprSpanErrorDaySpan = _RprSpanErrorDaySpan_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 2),
    _RprSpanErrorDaySpan_Type()
)
rprSpanErrorDaySpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanErrorDaySpan.setStatus("current")
_RprSpanErrorDayTtlExpFrames_Type = HCPerfTotalCount
_RprSpanErrorDayTtlExpFrames_Object = MibTableColumn
rprSpanErrorDayTtlExpFrames = _RprSpanErrorDayTtlExpFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 3),
    _RprSpanErrorDayTtlExpFrames_Type()
)
rprSpanErrorDayTtlExpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorDayTtlExpFrames.setStatus("current")
_RprSpanErrorDayTooLongFrames_Type = HCPerfTotalCount
_RprSpanErrorDayTooLongFrames_Object = MibTableColumn
rprSpanErrorDayTooLongFrames = _RprSpanErrorDayTooLongFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 4),
    _RprSpanErrorDayTooLongFrames_Type()
)
rprSpanErrorDayTooLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorDayTooLongFrames.setStatus("current")
_RprSpanErrorDayTooShortFrames_Type = HCPerfTotalCount
_RprSpanErrorDayTooShortFrames_Object = MibTableColumn
rprSpanErrorDayTooShortFrames = _RprSpanErrorDayTooShortFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 5),
    _RprSpanErrorDayTooShortFrames_Type()
)
rprSpanErrorDayTooShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorDayTooShortFrames.setStatus("current")
_RprSpanErrorDayBadHecFrames_Type = HCPerfTotalCount
_RprSpanErrorDayBadHecFrames_Object = MibTableColumn
rprSpanErrorDayBadHecFrames = _RprSpanErrorDayBadHecFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 6),
    _RprSpanErrorDayBadHecFrames_Type()
)
rprSpanErrorDayBadHecFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorDayBadHecFrames.setStatus("current")
_RprSpanErrorDayBadFcsFrames_Type = HCPerfTotalCount
_RprSpanErrorDayBadFcsFrames_Object = MibTableColumn
rprSpanErrorDayBadFcsFrames = _RprSpanErrorDayBadFcsFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 7),
    _RprSpanErrorDayBadFcsFrames_Type()
)
rprSpanErrorDayBadFcsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorDayBadFcsFrames.setStatus("current")
_RprSpanErrorDaySelfSrcUcastFrames_Type = HCPerfTotalCount
_RprSpanErrorDaySelfSrcUcastFrames_Object = MibTableColumn
rprSpanErrorDaySelfSrcUcastFrames = _RprSpanErrorDaySelfSrcUcastFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 8),
    _RprSpanErrorDaySelfSrcUcastFrames_Type()
)
rprSpanErrorDaySelfSrcUcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorDaySelfSrcUcastFrames.setStatus("current")
_RprSpanErrorDayPmdAbortFrames_Type = HCPerfTotalCount
_RprSpanErrorDayPmdAbortFrames_Object = MibTableColumn
rprSpanErrorDayPmdAbortFrames = _RprSpanErrorDayPmdAbortFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 9),
    _RprSpanErrorDayPmdAbortFrames_Type()
)
rprSpanErrorDayPmdAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorDayPmdAbortFrames.setStatus("current")
_RprSpanErrorDayBadAddrFrames_Type = HCPerfTotalCount
_RprSpanErrorDayBadAddrFrames_Object = MibTableColumn
rprSpanErrorDayBadAddrFrames = _RprSpanErrorDayBadAddrFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 10),
    _RprSpanErrorDayBadAddrFrames_Type()
)
rprSpanErrorDayBadAddrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorDayBadAddrFrames.setStatus("current")
_RprSpanErrorDayBadParityFrames_Type = HCPerfTotalCount
_RprSpanErrorDayBadParityFrames_Object = MibTableColumn
rprSpanErrorDayBadParityFrames = _RprSpanErrorDayBadParityFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 11),
    _RprSpanErrorDayBadParityFrames_Type()
)
rprSpanErrorDayBadParityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorDayBadParityFrames.setStatus("current")
_RprSpanErrorDayContainedFrames_Type = HCPerfTotalCount
_RprSpanErrorDayContainedFrames_Object = MibTableColumn
rprSpanErrorDayContainedFrames = _RprSpanErrorDayContainedFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 12),
    _RprSpanErrorDayContainedFrames_Type()
)
rprSpanErrorDayContainedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorDayContainedFrames.setStatus("current")
_RprSpanErrorDayScffErrors_Type = HCPerfTotalCount
_RprSpanErrorDayScffErrors_Object = MibTableColumn
rprSpanErrorDayScffErrors = _RprSpanErrorDayScffErrors_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 13),
    _RprSpanErrorDayScffErrors_Type()
)
rprSpanErrorDayScffErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorDayScffErrors.setStatus("current")
_RprSpanErrorDayErroredSeconds_Type = HCPerfTotalCount
_RprSpanErrorDayErroredSeconds_Object = MibTableColumn
rprSpanErrorDayErroredSeconds = _RprSpanErrorDayErroredSeconds_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 14),
    _RprSpanErrorDayErroredSeconds_Type()
)
rprSpanErrorDayErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorDayErroredSeconds.setStatus("current")
_RprSpanErrorDaySeverelyErroredSeconds_Type = HCPerfTotalCount
_RprSpanErrorDaySeverelyErroredSeconds_Object = MibTableColumn
rprSpanErrorDaySeverelyErroredSeconds = _RprSpanErrorDaySeverelyErroredSeconds_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 15),
    _RprSpanErrorDaySeverelyErroredSeconds_Type()
)
rprSpanErrorDaySeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorDaySeverelyErroredSeconds.setStatus("current")
_RprSpanErrorDayUnavailableSeconds_Type = HCPerfTotalCount
_RprSpanErrorDayUnavailableSeconds_Object = MibTableColumn
rprSpanErrorDayUnavailableSeconds = _RprSpanErrorDayUnavailableSeconds_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 3, 1, 16),
    _RprSpanErrorDayUnavailableSeconds_Type()
)
rprSpanErrorDayUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorDayUnavailableSeconds.setStatus("current")
_RprSpanErrorCountersStatsTable_Object = MibTable
rprSpanErrorCountersStatsTable = _RprSpanErrorCountersStatsTable_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    rprSpanErrorCountersStatsTable.setStatus("current")
_RprSpanErrorCountersStatsEntry_Object = MibTableRow
rprSpanErrorCountersStatsEntry = _RprSpanErrorCountersStatsEntry_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 4, 1)
)
rprSpanErrorCountersStatsEntry.setIndexNames(
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanErrorStatsIfIndex"),
    (0, "IEEE-802DOT17-RPR-MIB", "rprSpanErrorStatsSpan"),
)
if mibBuilder.loadTexts:
    rprSpanErrorCountersStatsEntry.setStatus("current")
_RprSpanErrorStatsIfIndex_Type = InterfaceIndex
_RprSpanErrorStatsIfIndex_Object = MibTableColumn
rprSpanErrorStatsIfIndex = _RprSpanErrorStatsIfIndex_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 4, 1, 1),
    _RprSpanErrorStatsIfIndex_Type()
)
rprSpanErrorStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanErrorStatsIfIndex.setStatus("current")
_RprSpanErrorStatsSpan_Type = RprSpan
_RprSpanErrorStatsSpan_Object = MibTableColumn
rprSpanErrorStatsSpan = _RprSpanErrorStatsSpan_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 4, 1, 2),
    _RprSpanErrorStatsSpan_Type()
)
rprSpanErrorStatsSpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rprSpanErrorStatsSpan.setStatus("current")
_RprSpanErrorStatsTtlExpFrames_Type = Counter64
_RprSpanErrorStatsTtlExpFrames_Object = MibTableColumn
rprSpanErrorStatsTtlExpFrames = _RprSpanErrorStatsTtlExpFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 4, 1, 3),
    _RprSpanErrorStatsTtlExpFrames_Type()
)
rprSpanErrorStatsTtlExpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorStatsTtlExpFrames.setStatus("current")
_RprSpanErrorStatsTooLongFrames_Type = Counter64
_RprSpanErrorStatsTooLongFrames_Object = MibTableColumn
rprSpanErrorStatsTooLongFrames = _RprSpanErrorStatsTooLongFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 4, 1, 4),
    _RprSpanErrorStatsTooLongFrames_Type()
)
rprSpanErrorStatsTooLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorStatsTooLongFrames.setStatus("current")
_RprSpanErrorStatsTooShortFrames_Type = Counter64
_RprSpanErrorStatsTooShortFrames_Object = MibTableColumn
rprSpanErrorStatsTooShortFrames = _RprSpanErrorStatsTooShortFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 4, 1, 5),
    _RprSpanErrorStatsTooShortFrames_Type()
)
rprSpanErrorStatsTooShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorStatsTooShortFrames.setStatus("current")
_RprSpanErrorStatsBadHecFrames_Type = Counter64
_RprSpanErrorStatsBadHecFrames_Object = MibTableColumn
rprSpanErrorStatsBadHecFrames = _RprSpanErrorStatsBadHecFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 4, 1, 6),
    _RprSpanErrorStatsBadHecFrames_Type()
)
rprSpanErrorStatsBadHecFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorStatsBadHecFrames.setStatus("current")
_RprSpanErrorStatsBadFcsFrames_Type = Counter64
_RprSpanErrorStatsBadFcsFrames_Object = MibTableColumn
rprSpanErrorStatsBadFcsFrames = _RprSpanErrorStatsBadFcsFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 4, 1, 7),
    _RprSpanErrorStatsBadFcsFrames_Type()
)
rprSpanErrorStatsBadFcsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorStatsBadFcsFrames.setStatus("current")
_RprSpanErrorStatsSelfSrcUcastFrames_Type = Counter64
_RprSpanErrorStatsSelfSrcUcastFrames_Object = MibTableColumn
rprSpanErrorStatsSelfSrcUcastFrames = _RprSpanErrorStatsSelfSrcUcastFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 4, 1, 8),
    _RprSpanErrorStatsSelfSrcUcastFrames_Type()
)
rprSpanErrorStatsSelfSrcUcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorStatsSelfSrcUcastFrames.setStatus("current")
_RprSpanErrorStatsPmdAbortFrames_Type = Counter64
_RprSpanErrorStatsPmdAbortFrames_Object = MibTableColumn
rprSpanErrorStatsPmdAbortFrames = _RprSpanErrorStatsPmdAbortFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 4, 1, 9),
    _RprSpanErrorStatsPmdAbortFrames_Type()
)
rprSpanErrorStatsPmdAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorStatsPmdAbortFrames.setStatus("current")
_RprSpanErrorStatsBadAddrFrames_Type = Counter64
_RprSpanErrorStatsBadAddrFrames_Object = MibTableColumn
rprSpanErrorStatsBadAddrFrames = _RprSpanErrorStatsBadAddrFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 4, 1, 10),
    _RprSpanErrorStatsBadAddrFrames_Type()
)
rprSpanErrorStatsBadAddrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorStatsBadAddrFrames.setStatus("current")
_RprSpanErrorStatsBadParityFrames_Type = Counter64
_RprSpanErrorStatsBadParityFrames_Object = MibTableColumn
rprSpanErrorStatsBadParityFrames = _RprSpanErrorStatsBadParityFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 4, 1, 11),
    _RprSpanErrorStatsBadParityFrames_Type()
)
rprSpanErrorStatsBadParityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorStatsBadParityFrames.setStatus("current")
_RprSpanErrorStatsContainedFrames_Type = Counter64
_RprSpanErrorStatsContainedFrames_Object = MibTableColumn
rprSpanErrorStatsContainedFrames = _RprSpanErrorStatsContainedFrames_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 4, 1, 12),
    _RprSpanErrorStatsContainedFrames_Type()
)
rprSpanErrorStatsContainedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorStatsContainedFrames.setStatus("current")
_RprSpanErrorStatsScffErrors_Type = Counter64
_RprSpanErrorStatsScffErrors_Object = MibTableColumn
rprSpanErrorStatsScffErrors = _RprSpanErrorStatsScffErrors_Object(
    (1, 0, 8802, 17, 1, 1, 1, 5, 4, 1, 13),
    _RprSpanErrorStatsScffErrors_Type()
)
rprSpanErrorStatsScffErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rprSpanErrorStatsScffErrors.setStatus("current")
_RprConformance_ObjectIdentity = ObjectIdentity
rprConformance = _RprConformance_ObjectIdentity(
    (1, 0, 8802, 17, 1, 1, 2)
)
_RprGroups_ObjectIdentity = ObjectIdentity
rprGroups = _RprGroups_ObjectIdentity(
    (1, 0, 8802, 17, 1, 1, 2, 1)
)
_RprCompliances_ObjectIdentity = ObjectIdentity
rprCompliances = _RprCompliances_ObjectIdentity(
    (1, 0, 8802, 17, 1, 1, 2, 2)
)

# Managed Objects groups

rprIfGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 1)
)
rprIfGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprIfStationsOnRing"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfReversionMode"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfProtectionWTR"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfProtectionFastTimer"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfProtectionSlowTimer"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfAtdTimer"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfKeepaliveTimeout"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfFairnessAggressive"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfPtqSize"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfStqSize"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfSTQFullThreshold"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfIdleThreshold"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfSesThreshold"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfWrapConfig"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfJumboFramePreferred"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfMacOperModes"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfRingOperModes"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfCurrentStatus"))
)
if mibBuilder.loadTexts:
    rprIfGroup.setStatus("current")

rprIfGroupOpt = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 2)
)
rprIfGroupOpt.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprIfLastChange"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfChanges"))
)
if mibBuilder.loadTexts:
    rprIfGroupOpt.setStatus("current")

rprIfStatsControlGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 3)
)
rprIfStatsControlGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprIfStatsControlPeriodClear"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfStatsControlCountPointClear"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfStatsControlIntervalClear"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfStatsControlCommitClear"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfStatsControlTimeElapsed"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfStatsControlValidIntervals"))
)
if mibBuilder.loadTexts:
    rprIfStatsControlGroup.setStatus("current")

rprSpanGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 4)
)
rprSpanGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprSpanLowerLayerIfIndex"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanTotalRingletReservedRate"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentStatus"))
)
if mibBuilder.loadTexts:
    rprSpanGroup.setStatus("current")

rprSpanGroupOpt = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 5)
)
rprSpanGroupOpt.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprSpanLastChange"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanChanges"))
)
if mibBuilder.loadTexts:
    rprSpanGroupOpt.setStatus("current")

rprSpanProtectionGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 6)
)
rprSpanProtectionGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprSpanProtectionNeighborValid"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanProtectionHoldOffTimer"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanProtectionCommand"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanProtectionCount"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanProtectionDuration"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanProtectionLastActivationTime"))
)
if mibBuilder.loadTexts:
    rprSpanProtectionGroup.setStatus("current")

rprTopoGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 7)
)
rprTopoGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprTopoImageSecMacAddress1"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageSecMacAddress2"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageStationIfIndex"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageStationName"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageInetAddressType"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageInetAddress"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageCapability"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageRinglet0Hops"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageRinglet0ReservedRate"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageRinglet1Hops"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageRinglet1ReservedRate"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageWestProtectionStatus"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageWestWeight"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageEastProtectionStatus"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageEastWeight"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageStatus"))
)
if mibBuilder.loadTexts:
    rprTopoGroup.setStatus("current")

rprFairnessGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 8)
)
rprFairnessGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprFairnessRingletWeight"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessReservedRate"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessMaxAllowed"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessAgeCoef"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessRampCoef"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessLpCoef"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessAdvertisementRatio"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessMcffReportCoef"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessActiveWeightsCoef"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessSTQHighThreshold"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessSTQMedThreshold"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessSTQLowThreshold"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessRateHighThreshold"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessRateLowThreshold"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessResetWaterMarks"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessSTQHighWaterMark"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessSTQLowWaterMark"))
)
if mibBuilder.loadTexts:
    rprFairnessGroup.setStatus("current")

rprFairnessGroupOpt = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 9)
)
rprFairnessGroupOpt.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprFairnessLastChange"),
        ("IEEE-802DOT17-RPR-MIB", "rprFairnessChanges"))
)
if mibBuilder.loadTexts:
    rprFairnessGroupOpt.setStatus("current")

rprOamGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 10)
)
rprOamGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprOamActionType"),
        ("IEEE-802DOT17-RPR-MIB", "rprOamDestAddress"),
        ("IEEE-802DOT17-RPR-MIB", "rprOamRequestRinglet"),
        ("IEEE-802DOT17-RPR-MIB", "rprOamResponseRinglet"),
        ("IEEE-802DOT17-RPR-MIB", "rprOamClassOfService"),
        ("IEEE-802DOT17-RPR-MIB", "rprOamUserData"),
        ("IEEE-802DOT17-RPR-MIB", "rprOamProtected"),
        ("IEEE-802DOT17-RPR-MIB", "rprOamRequestCount"),
        ("IEEE-802DOT17-RPR-MIB", "rprOamTimeout"),
        ("IEEE-802DOT17-RPR-MIB", "rprOamControl"),
        ("IEEE-802DOT17-RPR-MIB", "rprOamResponseCount"),
        ("IEEE-802DOT17-RPR-MIB", "rprOamAvResponseTime"),
        ("IEEE-802DOT17-RPR-MIB", "rprOamResponseStatus"))
)
if mibBuilder.loadTexts:
    rprOamGroup.setStatus("current")

rprIfChangeSummaryGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 11)
)
rprIfChangeSummaryGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprIfChangeSummaryNumInterfaces"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfChangeSummaryIfLastChange"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfChangeSummaryIfChanges"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfChangeSummarySpanLastChange"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfChangeSummarySpanChanges"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfChangeSummaryFairnessLastChange"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfChangeSummaryFairnessChanges"))
)
if mibBuilder.loadTexts:
    rprIfChangeSummaryGroup.setStatus("current")

rprSpanCurrentGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 12)
)
rprSpanCurrentGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentInMcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanCurrentOutMcastClassCOctets"))
)
if mibBuilder.loadTexts:
    rprSpanCurrentGroup.setStatus("current")

rprSpanIntervalGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 13)
)
rprSpanIntervalGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalValidData"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalTimeElapsed"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalStartTime"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalInMcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanIntervalOutMcastClassCOctets"))
)
if mibBuilder.loadTexts:
    rprSpanIntervalGroup.setStatus("current")

rprSpanDayGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 14)
)
rprSpanDayGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprSpanDayInUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayInUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayInUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayInUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayInUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayInUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayInUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayInUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayInMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayInMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayInMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayInMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayInMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayInMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayInMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayInMcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanDayOutMcastClassCOctets"))
)
if mibBuilder.loadTexts:
    rprSpanDayGroup.setStatus("current")

rprSpanStatsGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 15)
)
rprSpanStatsGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInMcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInCtrlFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInOamEchoFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInOamFlushFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInOamOrgFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInTopoAtdFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInTopoChkSumFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsInTopoTpFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutMcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutCtrlFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutOamEchoFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutOamFlushFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutOamOrgFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutTopoAtdFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutTopoChkSumFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanStatsOutTopoTpFrames"))
)
if mibBuilder.loadTexts:
    rprSpanStatsGroup.setStatus("current")

rprClientCurrentGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 16)
)
rprClientCurrentGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentInMcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientCurrentOutMcastClassCOctets"))
)
if mibBuilder.loadTexts:
    rprClientCurrentGroup.setStatus("current")

rprClientIntervalGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 17)
)
rprClientIntervalGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprClientIntervalValidData"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalTimeElapsed"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalInMcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientIntervalOutMcastClassCOctets"))
)
if mibBuilder.loadTexts:
    rprClientIntervalGroup.setStatus("current")

rprClientDayGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 18)
)
rprClientDayGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprClientDayInUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayInUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayInUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayInUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayInUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayInUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayInUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayInUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayInMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayInMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayInMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayInMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayInMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayInMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayInMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayInMcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientDayOutMcastClassCOctets"))
)
if mibBuilder.loadTexts:
    rprClientDayGroup.setStatus("current")

rprClientStatsGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 19)
)
rprClientStatsGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprClientStatsInUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInMcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsInBcastFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutUcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutUcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutUcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutUcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutUcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutUcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutUcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutUcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutMcastClassAFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutMcastClassAOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutMcastClassBCirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutMcastClassBCirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutMcastClassBEirFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutMcastClassBEirOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutMcastClassCFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutMcastClassCOctets"),
        ("IEEE-802DOT17-RPR-MIB", "rprClientStatsOutBcastFrames"))
)
if mibBuilder.loadTexts:
    rprClientStatsGroup.setStatus("current")

rprErrorCurrentGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 20)
)
rprErrorCurrentGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentTtlExpFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentTooLongFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentTooShortFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentBadHecFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentBadFcsFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentSelfSrcUcastFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentPmdAbortFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentBadAddrFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentBadParityFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentContainedFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentScffErrors"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentErroredSeconds"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentSeverelyErroredSeconds"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorCurrentUnavailableSeconds"))
)
if mibBuilder.loadTexts:
    rprErrorCurrentGroup.setStatus("current")

rprErrorIntervalGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 21)
)
rprErrorIntervalGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalValidData"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalTimeElapsed"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalTtlExpFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalTooLongFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalTooShortFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalBadHecFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalBadFcsFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalSelfSrcUcastFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalPmdAbortFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalBadAddrFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalBadParityFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalContainedFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalScffErrors"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalErroredSeconds"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalSeverelyErroredSeconds"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorIntervalUnavailableSeconds"))
)
if mibBuilder.loadTexts:
    rprErrorIntervalGroup.setStatus("current")

rprErrorDayGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 22)
)
rprErrorDayGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprSpanErrorDayTtlExpFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorDayTooLongFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorDayTooShortFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorDayBadHecFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorDayBadFcsFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorDaySelfSrcUcastFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorDayPmdAbortFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorDayBadAddrFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorDayBadParityFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorDayContainedFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorDayScffErrors"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorDayErroredSeconds"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorDaySeverelyErroredSeconds"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorDayUnavailableSeconds"))
)
if mibBuilder.loadTexts:
    rprErrorDayGroup.setStatus("current")

rprErrorStatsGroup = ObjectGroup(
    (1, 0, 8802, 17, 1, 1, 2, 1, 23)
)
rprErrorStatsGroup.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprSpanErrorStatsTtlExpFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorStatsTooLongFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorStatsTooShortFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorStatsBadHecFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorStatsBadFcsFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorStatsSelfSrcUcastFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorStatsPmdAbortFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorStatsBadAddrFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorStatsBadParityFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorStatsContainedFrames"),
        ("IEEE-802DOT17-RPR-MIB", "rprSpanErrorStatsScffErrors"))
)
if mibBuilder.loadTexts:
    rprErrorStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rprModuleTotalStatsCompliance = ModuleCompliance(
    (1, 0, 8802, 17, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rprModuleTotalStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE-802DOT17-RPR-MIB",
    **{"RprSpan": RprSpan,
       "RprProtectionStatus": RprProtectionStatus,
       "RprOamRinglet": RprOamRinglet,
       "ieee802dot17rprMIB": ieee802dot17rprMIB,
       "rprObjects": rprObjects,
       "rprGeneral": rprGeneral,
       "rprIfTable": rprIfTable,
       "rprIfEntry": rprIfEntry,
       "rprIfIndex": rprIfIndex,
       "rprIfStationsOnRing": rprIfStationsOnRing,
       "rprIfReversionMode": rprIfReversionMode,
       "rprIfProtectionWTR": rprIfProtectionWTR,
       "rprIfProtectionFastTimer": rprIfProtectionFastTimer,
       "rprIfProtectionSlowTimer": rprIfProtectionSlowTimer,
       "rprIfAtdTimer": rprIfAtdTimer,
       "rprIfKeepaliveTimeout": rprIfKeepaliveTimeout,
       "rprIfFairnessAggressive": rprIfFairnessAggressive,
       "rprIfPtqSize": rprIfPtqSize,
       "rprIfStqSize": rprIfStqSize,
       "rprIfSTQFullThreshold": rprIfSTQFullThreshold,
       "rprIfIdleThreshold": rprIfIdleThreshold,
       "rprIfSesThreshold": rprIfSesThreshold,
       "rprIfWrapConfig": rprIfWrapConfig,
       "rprIfJumboFramePreferred": rprIfJumboFramePreferred,
       "rprIfMacOperModes": rprIfMacOperModes,
       "rprIfRingOperModes": rprIfRingOperModes,
       "rprIfCurrentStatus": rprIfCurrentStatus,
       "rprIfLastChange": rprIfLastChange,
       "rprIfChanges": rprIfChanges,
       "rprIfStatsControlTable": rprIfStatsControlTable,
       "rprIfStatsControlEntry": rprIfStatsControlEntry,
       "rprIfStatsControlIfIndex": rprIfStatsControlIfIndex,
       "rprIfStatsControlPeriodClear": rprIfStatsControlPeriodClear,
       "rprIfStatsControlCountPointClear": rprIfStatsControlCountPointClear,
       "rprIfStatsControlIntervalClear": rprIfStatsControlIntervalClear,
       "rprIfStatsControlCommitClear": rprIfStatsControlCommitClear,
       "rprIfStatsControlTimeElapsed": rprIfStatsControlTimeElapsed,
       "rprIfStatsControlValidIntervals": rprIfStatsControlValidIntervals,
       "rprSpanTable": rprSpanTable,
       "rprSpanEntry": rprSpanEntry,
       "rprSpanIfIndex": rprSpanIfIndex,
       "rprSpanId": rprSpanId,
       "rprSpanLowerLayerIfIndex": rprSpanLowerLayerIfIndex,
       "rprSpanTotalRingletReservedRate": rprSpanTotalRingletReservedRate,
       "rprSpanCurrentStatus": rprSpanCurrentStatus,
       "rprSpanLastChange": rprSpanLastChange,
       "rprSpanChanges": rprSpanChanges,
       "rprSpanProtectionTable": rprSpanProtectionTable,
       "rprSpanProtectionEntry": rprSpanProtectionEntry,
       "rprSpanProtectionIfIndex": rprSpanProtectionIfIndex,
       "rprSpanProtectionSpan": rprSpanProtectionSpan,
       "rprSpanProtectionNeighborValid": rprSpanProtectionNeighborValid,
       "rprSpanProtectionHoldOffTimer": rprSpanProtectionHoldOffTimer,
       "rprSpanProtectionCommand": rprSpanProtectionCommand,
       "rprSpanProtectionCount": rprSpanProtectionCount,
       "rprSpanProtectionDuration": rprSpanProtectionDuration,
       "rprSpanProtectionLastActivationTime": rprSpanProtectionLastActivationTime,
       "rprIfChangeSummaryObject": rprIfChangeSummaryObject,
       "rprIfChangeSummaryNumInterfaces": rprIfChangeSummaryNumInterfaces,
       "rprIfChangeSummaryIfLastChange": rprIfChangeSummaryIfLastChange,
       "rprIfChangeSummaryIfChanges": rprIfChangeSummaryIfChanges,
       "rprIfChangeSummarySpanLastChange": rprIfChangeSummarySpanLastChange,
       "rprIfChangeSummarySpanChanges": rprIfChangeSummarySpanChanges,
       "rprIfChangeSummaryFairnessLastChange": rprIfChangeSummaryFairnessLastChange,
       "rprIfChangeSummaryFairnessChanges": rprIfChangeSummaryFairnessChanges,
       "rprProtocols": rprProtocols,
       "rprTopoImageTable": rprTopoImageTable,
       "rprTopoImageEntry": rprTopoImageEntry,
       "rprTopoImageIfIndex": rprTopoImageIfIndex,
       "rprTopoImageMacAddress": rprTopoImageMacAddress,
       "rprTopoImageSecMacAddress1": rprTopoImageSecMacAddress1,
       "rprTopoImageSecMacAddress2": rprTopoImageSecMacAddress2,
       "rprTopoImageStationIfIndex": rprTopoImageStationIfIndex,
       "rprTopoImageStationName": rprTopoImageStationName,
       "rprTopoImageInetAddressType": rprTopoImageInetAddressType,
       "rprTopoImageInetAddress": rprTopoImageInetAddress,
       "rprTopoImageCapability": rprTopoImageCapability,
       "rprTopoImageRinglet0Hops": rprTopoImageRinglet0Hops,
       "rprTopoImageRinglet0ReservedRate": rprTopoImageRinglet0ReservedRate,
       "rprTopoImageRinglet1Hops": rprTopoImageRinglet1Hops,
       "rprTopoImageRinglet1ReservedRate": rprTopoImageRinglet1ReservedRate,
       "rprTopoImageWestProtectionStatus": rprTopoImageWestProtectionStatus,
       "rprTopoImageWestWeight": rprTopoImageWestWeight,
       "rprTopoImageEastProtectionStatus": rprTopoImageEastProtectionStatus,
       "rprTopoImageEastWeight": rprTopoImageEastWeight,
       "rprTopoImageStatus": rprTopoImageStatus,
       "rprFairnessTable": rprFairnessTable,
       "rprFairnessEntry": rprFairnessEntry,
       "rprFairnessIfIndex": rprFairnessIfIndex,
       "rprFairnessRinglet": rprFairnessRinglet,
       "rprFairnessRingletWeight": rprFairnessRingletWeight,
       "rprFairnessReservedRate": rprFairnessReservedRate,
       "rprFairnessMaxAllowed": rprFairnessMaxAllowed,
       "rprFairnessAgeCoef": rprFairnessAgeCoef,
       "rprFairnessRampCoef": rprFairnessRampCoef,
       "rprFairnessLpCoef": rprFairnessLpCoef,
       "rprFairnessAdvertisementRatio": rprFairnessAdvertisementRatio,
       "rprFairnessMcffReportCoef": rprFairnessMcffReportCoef,
       "rprFairnessActiveWeightsCoef": rprFairnessActiveWeightsCoef,
       "rprFairnessSTQHighThreshold": rprFairnessSTQHighThreshold,
       "rprFairnessSTQMedThreshold": rprFairnessSTQMedThreshold,
       "rprFairnessSTQLowThreshold": rprFairnessSTQLowThreshold,
       "rprFairnessRateHighThreshold": rprFairnessRateHighThreshold,
       "rprFairnessRateLowThreshold": rprFairnessRateLowThreshold,
       "rprFairnessResetWaterMarks": rprFairnessResetWaterMarks,
       "rprFairnessSTQHighWaterMark": rprFairnessSTQHighWaterMark,
       "rprFairnessSTQLowWaterMark": rprFairnessSTQLowWaterMark,
       "rprFairnessLastChange": rprFairnessLastChange,
       "rprFairnessChanges": rprFairnessChanges,
       "rprOamTable": rprOamTable,
       "rprOamEntry": rprOamEntry,
       "rprOamIfIndex": rprOamIfIndex,
       "rprOamActionType": rprOamActionType,
       "rprOamDestAddress": rprOamDestAddress,
       "rprOamRequestRinglet": rprOamRequestRinglet,
       "rprOamResponseRinglet": rprOamResponseRinglet,
       "rprOamClassOfService": rprOamClassOfService,
       "rprOamUserData": rprOamUserData,
       "rprOamProtected": rprOamProtected,
       "rprOamRequestCount": rprOamRequestCount,
       "rprOamTimeout": rprOamTimeout,
       "rprOamControl": rprOamControl,
       "rprOamResponseCount": rprOamResponseCount,
       "rprOamAvResponseTime": rprOamAvResponseTime,
       "rprOamResponseStatus": rprOamResponseStatus,
       "rprSpanCounters": rprSpanCounters,
       "rprSpanCountersCurrentTable": rprSpanCountersCurrentTable,
       "rprSpanCountersCurrentEntry": rprSpanCountersCurrentEntry,
       "rprSpanCurrentIfIndex": rprSpanCurrentIfIndex,
       "rprSpanCurrentSpan": rprSpanCurrentSpan,
       "rprSpanCurrentInUcastClassAFrames": rprSpanCurrentInUcastClassAFrames,
       "rprSpanCurrentInUcastClassAOctets": rprSpanCurrentInUcastClassAOctets,
       "rprSpanCurrentInUcastClassBCirFrames": rprSpanCurrentInUcastClassBCirFrames,
       "rprSpanCurrentInUcastClassBCirOctets": rprSpanCurrentInUcastClassBCirOctets,
       "rprSpanCurrentInUcastClassBEirFrames": rprSpanCurrentInUcastClassBEirFrames,
       "rprSpanCurrentInUcastClassBEirOctets": rprSpanCurrentInUcastClassBEirOctets,
       "rprSpanCurrentInUcastClassCFrames": rprSpanCurrentInUcastClassCFrames,
       "rprSpanCurrentInUcastClassCOctets": rprSpanCurrentInUcastClassCOctets,
       "rprSpanCurrentInMcastClassAFrames": rprSpanCurrentInMcastClassAFrames,
       "rprSpanCurrentInMcastClassAOctets": rprSpanCurrentInMcastClassAOctets,
       "rprSpanCurrentInMcastClassBCirFrames": rprSpanCurrentInMcastClassBCirFrames,
       "rprSpanCurrentInMcastClassBCirOctets": rprSpanCurrentInMcastClassBCirOctets,
       "rprSpanCurrentInMcastClassBEirFrames": rprSpanCurrentInMcastClassBEirFrames,
       "rprSpanCurrentInMcastClassBEirOctets": rprSpanCurrentInMcastClassBEirOctets,
       "rprSpanCurrentInMcastClassCFrames": rprSpanCurrentInMcastClassCFrames,
       "rprSpanCurrentInMcastClassCOctets": rprSpanCurrentInMcastClassCOctets,
       "rprSpanCurrentOutUcastClassAFrames": rprSpanCurrentOutUcastClassAFrames,
       "rprSpanCurrentOutUcastClassAOctets": rprSpanCurrentOutUcastClassAOctets,
       "rprSpanCurrentOutUcastClassBCirFrames": rprSpanCurrentOutUcastClassBCirFrames,
       "rprSpanCurrentOutUcastClassBCirOctets": rprSpanCurrentOutUcastClassBCirOctets,
       "rprSpanCurrentOutUcastClassBEirFrames": rprSpanCurrentOutUcastClassBEirFrames,
       "rprSpanCurrentOutUcastClassBEirOctets": rprSpanCurrentOutUcastClassBEirOctets,
       "rprSpanCurrentOutUcastClassCFrames": rprSpanCurrentOutUcastClassCFrames,
       "rprSpanCurrentOutUcastClassCOctets": rprSpanCurrentOutUcastClassCOctets,
       "rprSpanCurrentOutMcastClassAFrames": rprSpanCurrentOutMcastClassAFrames,
       "rprSpanCurrentOutMcastClassAOctets": rprSpanCurrentOutMcastClassAOctets,
       "rprSpanCurrentOutMcastClassBCirFrames": rprSpanCurrentOutMcastClassBCirFrames,
       "rprSpanCurrentOutMcastClassBCirOctets": rprSpanCurrentOutMcastClassBCirOctets,
       "rprSpanCurrentOutMcastClassBEirFrames": rprSpanCurrentOutMcastClassBEirFrames,
       "rprSpanCurrentOutMcastClassBEirOctets": rprSpanCurrentOutMcastClassBEirOctets,
       "rprSpanCurrentOutMcastClassCFrames": rprSpanCurrentOutMcastClassCFrames,
       "rprSpanCurrentOutMcastClassCOctets": rprSpanCurrentOutMcastClassCOctets,
       "rprSpanCountersIntervalTable": rprSpanCountersIntervalTable,
       "rprSpanCountersIntervalEntry": rprSpanCountersIntervalEntry,
       "rprSpanIntervalIfIndex": rprSpanIntervalIfIndex,
       "rprSpanIntervalSpan": rprSpanIntervalSpan,
       "rprSpanIntervalNumber": rprSpanIntervalNumber,
       "rprSpanIntervalValidData": rprSpanIntervalValidData,
       "rprSpanIntervalTimeElapsed": rprSpanIntervalTimeElapsed,
       "rprSpanIntervalStartTime": rprSpanIntervalStartTime,
       "rprSpanIntervalInUcastClassAFrames": rprSpanIntervalInUcastClassAFrames,
       "rprSpanIntervalInUcastClassAOctets": rprSpanIntervalInUcastClassAOctets,
       "rprSpanIntervalInUcastClassBCirFrames": rprSpanIntervalInUcastClassBCirFrames,
       "rprSpanIntervalInUcastClassBCirOctets": rprSpanIntervalInUcastClassBCirOctets,
       "rprSpanIntervalInUcastClassBEirFrames": rprSpanIntervalInUcastClassBEirFrames,
       "rprSpanIntervalInUcastClassBEirOctets": rprSpanIntervalInUcastClassBEirOctets,
       "rprSpanIntervalInUcastClassCFrames": rprSpanIntervalInUcastClassCFrames,
       "rprSpanIntervalInUcastClassCOctets": rprSpanIntervalInUcastClassCOctets,
       "rprSpanIntervalInMcastClassAFrames": rprSpanIntervalInMcastClassAFrames,
       "rprSpanIntervalInMcastClassAOctets": rprSpanIntervalInMcastClassAOctets,
       "rprSpanIntervalInMcastClassBCirFrames": rprSpanIntervalInMcastClassBCirFrames,
       "rprSpanIntervalInMcastClassBCirOctets": rprSpanIntervalInMcastClassBCirOctets,
       "rprSpanIntervalInMcastClassBEirFrames": rprSpanIntervalInMcastClassBEirFrames,
       "rprSpanIntervalInMcastClassBEirOctets": rprSpanIntervalInMcastClassBEirOctets,
       "rprSpanIntervalInMcastClassCFrames": rprSpanIntervalInMcastClassCFrames,
       "rprSpanIntervalInMcastClassCOctets": rprSpanIntervalInMcastClassCOctets,
       "rprSpanIntervalOutUcastClassAFrames": rprSpanIntervalOutUcastClassAFrames,
       "rprSpanIntervalOutUcastClassAOctets": rprSpanIntervalOutUcastClassAOctets,
       "rprSpanIntervalOutUcastClassBCirFrames": rprSpanIntervalOutUcastClassBCirFrames,
       "rprSpanIntervalOutUcastClassBCirOctets": rprSpanIntervalOutUcastClassBCirOctets,
       "rprSpanIntervalOutUcastClassBEirFrames": rprSpanIntervalOutUcastClassBEirFrames,
       "rprSpanIntervalOutUcastClassBEirOctets": rprSpanIntervalOutUcastClassBEirOctets,
       "rprSpanIntervalOutUcastClassCFrames": rprSpanIntervalOutUcastClassCFrames,
       "rprSpanIntervalOutUcastClassCOctets": rprSpanIntervalOutUcastClassCOctets,
       "rprSpanIntervalOutMcastClassAFrames": rprSpanIntervalOutMcastClassAFrames,
       "rprSpanIntervalOutMcastClassAOctets": rprSpanIntervalOutMcastClassAOctets,
       "rprSpanIntervalOutMcastClassBCirFrames": rprSpanIntervalOutMcastClassBCirFrames,
       "rprSpanIntervalOutMcastClassBCirOctets": rprSpanIntervalOutMcastClassBCirOctets,
       "rprSpanIntervalOutMcastClassBEirFrames": rprSpanIntervalOutMcastClassBEirFrames,
       "rprSpanIntervalOutMcastClassBEirOctets": rprSpanIntervalOutMcastClassBEirOctets,
       "rprSpanIntervalOutMcastClassCFrames": rprSpanIntervalOutMcastClassCFrames,
       "rprSpanIntervalOutMcastClassCOctets": rprSpanIntervalOutMcastClassCOctets,
       "rprSpanCountersDayTable": rprSpanCountersDayTable,
       "rprSpanCountersDayEntry": rprSpanCountersDayEntry,
       "rprSpanDayIfIndex": rprSpanDayIfIndex,
       "rprSpanDaySpan": rprSpanDaySpan,
       "rprSpanDayInUcastClassAFrames": rprSpanDayInUcastClassAFrames,
       "rprSpanDayInUcastClassAOctets": rprSpanDayInUcastClassAOctets,
       "rprSpanDayInUcastClassBCirFrames": rprSpanDayInUcastClassBCirFrames,
       "rprSpanDayInUcastClassBCirOctets": rprSpanDayInUcastClassBCirOctets,
       "rprSpanDayInUcastClassBEirFrames": rprSpanDayInUcastClassBEirFrames,
       "rprSpanDayInUcastClassBEirOctets": rprSpanDayInUcastClassBEirOctets,
       "rprSpanDayInUcastClassCFrames": rprSpanDayInUcastClassCFrames,
       "rprSpanDayInUcastClassCOctets": rprSpanDayInUcastClassCOctets,
       "rprSpanDayInMcastClassAFrames": rprSpanDayInMcastClassAFrames,
       "rprSpanDayInMcastClassAOctets": rprSpanDayInMcastClassAOctets,
       "rprSpanDayInMcastClassBCirFrames": rprSpanDayInMcastClassBCirFrames,
       "rprSpanDayInMcastClassBCirOctets": rprSpanDayInMcastClassBCirOctets,
       "rprSpanDayInMcastClassBEirFrames": rprSpanDayInMcastClassBEirFrames,
       "rprSpanDayInMcastClassBEirOctets": rprSpanDayInMcastClassBEirOctets,
       "rprSpanDayInMcastClassCFrames": rprSpanDayInMcastClassCFrames,
       "rprSpanDayInMcastClassCOctets": rprSpanDayInMcastClassCOctets,
       "rprSpanDayOutUcastClassAFrames": rprSpanDayOutUcastClassAFrames,
       "rprSpanDayOutUcastClassAOctets": rprSpanDayOutUcastClassAOctets,
       "rprSpanDayOutUcastClassBCirFrames": rprSpanDayOutUcastClassBCirFrames,
       "rprSpanDayOutUcastClassBCirOctets": rprSpanDayOutUcastClassBCirOctets,
       "rprSpanDayOutUcastClassBEirFrames": rprSpanDayOutUcastClassBEirFrames,
       "rprSpanDayOutUcastClassBEirOctets": rprSpanDayOutUcastClassBEirOctets,
       "rprSpanDayOutUcastClassCFrames": rprSpanDayOutUcastClassCFrames,
       "rprSpanDayOutUcastClassCOctets": rprSpanDayOutUcastClassCOctets,
       "rprSpanDayOutMcastClassAFrames": rprSpanDayOutMcastClassAFrames,
       "rprSpanDayOutMcastClassAOctets": rprSpanDayOutMcastClassAOctets,
       "rprSpanDayOutMcastClassBCirFrames": rprSpanDayOutMcastClassBCirFrames,
       "rprSpanDayOutMcastClassBCirOctets": rprSpanDayOutMcastClassBCirOctets,
       "rprSpanDayOutMcastClassBEirFrames": rprSpanDayOutMcastClassBEirFrames,
       "rprSpanDayOutMcastClassBEirOctets": rprSpanDayOutMcastClassBEirOctets,
       "rprSpanDayOutMcastClassCFrames": rprSpanDayOutMcastClassCFrames,
       "rprSpanDayOutMcastClassCOctets": rprSpanDayOutMcastClassCOctets,
       "rprSpanCountersStatsTable": rprSpanCountersStatsTable,
       "rprSpanCountersStatsEntry": rprSpanCountersStatsEntry,
       "rprSpanStatsIfIndex": rprSpanStatsIfIndex,
       "rprSpanStatsSpan": rprSpanStatsSpan,
       "rprSpanStatsInUcastClassAFrames": rprSpanStatsInUcastClassAFrames,
       "rprSpanStatsInUcastClassAOctets": rprSpanStatsInUcastClassAOctets,
       "rprSpanStatsInUcastClassBCirFrames": rprSpanStatsInUcastClassBCirFrames,
       "rprSpanStatsInUcastClassBCirOctets": rprSpanStatsInUcastClassBCirOctets,
       "rprSpanStatsInUcastClassBEirFrames": rprSpanStatsInUcastClassBEirFrames,
       "rprSpanStatsInUcastClassBEirOctets": rprSpanStatsInUcastClassBEirOctets,
       "rprSpanStatsInUcastClassCFrames": rprSpanStatsInUcastClassCFrames,
       "rprSpanStatsInUcastClassCOctets": rprSpanStatsInUcastClassCOctets,
       "rprSpanStatsInMcastClassAFrames": rprSpanStatsInMcastClassAFrames,
       "rprSpanStatsInMcastClassAOctets": rprSpanStatsInMcastClassAOctets,
       "rprSpanStatsInMcastClassBCirFrames": rprSpanStatsInMcastClassBCirFrames,
       "rprSpanStatsInMcastClassBCirOctets": rprSpanStatsInMcastClassBCirOctets,
       "rprSpanStatsInMcastClassBEirFrames": rprSpanStatsInMcastClassBEirFrames,
       "rprSpanStatsInMcastClassBEirOctets": rprSpanStatsInMcastClassBEirOctets,
       "rprSpanStatsInMcastClassCFrames": rprSpanStatsInMcastClassCFrames,
       "rprSpanStatsInMcastClassCOctets": rprSpanStatsInMcastClassCOctets,
       "rprSpanStatsInCtrlFrames": rprSpanStatsInCtrlFrames,
       "rprSpanStatsInOamEchoFrames": rprSpanStatsInOamEchoFrames,
       "rprSpanStatsInOamFlushFrames": rprSpanStatsInOamFlushFrames,
       "rprSpanStatsInOamOrgFrames": rprSpanStatsInOamOrgFrames,
       "rprSpanStatsInTopoAtdFrames": rprSpanStatsInTopoAtdFrames,
       "rprSpanStatsInTopoChkSumFrames": rprSpanStatsInTopoChkSumFrames,
       "rprSpanStatsInTopoTpFrames": rprSpanStatsInTopoTpFrames,
       "rprSpanStatsOutUcastClassAFrames": rprSpanStatsOutUcastClassAFrames,
       "rprSpanStatsOutUcastClassAOctets": rprSpanStatsOutUcastClassAOctets,
       "rprSpanStatsOutUcastClassBCirFrames": rprSpanStatsOutUcastClassBCirFrames,
       "rprSpanStatsOutUcastClassBCirOctets": rprSpanStatsOutUcastClassBCirOctets,
       "rprSpanStatsOutUcastClassBEirFrames": rprSpanStatsOutUcastClassBEirFrames,
       "rprSpanStatsOutUcastClassBEirOctets": rprSpanStatsOutUcastClassBEirOctets,
       "rprSpanStatsOutUcastClassCFrames": rprSpanStatsOutUcastClassCFrames,
       "rprSpanStatsOutUcastClassCOctets": rprSpanStatsOutUcastClassCOctets,
       "rprSpanStatsOutMcastClassAFrames": rprSpanStatsOutMcastClassAFrames,
       "rprSpanStatsOutMcastClassAOctets": rprSpanStatsOutMcastClassAOctets,
       "rprSpanStatsOutMcastClassBCirFrames": rprSpanStatsOutMcastClassBCirFrames,
       "rprSpanStatsOutMcastClassBCirOctets": rprSpanStatsOutMcastClassBCirOctets,
       "rprSpanStatsOutMcastClassBEirFrames": rprSpanStatsOutMcastClassBEirFrames,
       "rprSpanStatsOutMcastClassBEirOctets": rprSpanStatsOutMcastClassBEirOctets,
       "rprSpanStatsOutMcastClassCFrames": rprSpanStatsOutMcastClassCFrames,
       "rprSpanStatsOutMcastClassCOctets": rprSpanStatsOutMcastClassCOctets,
       "rprSpanStatsOutCtrlFrames": rprSpanStatsOutCtrlFrames,
       "rprSpanStatsOutOamEchoFrames": rprSpanStatsOutOamEchoFrames,
       "rprSpanStatsOutOamFlushFrames": rprSpanStatsOutOamFlushFrames,
       "rprSpanStatsOutOamOrgFrames": rprSpanStatsOutOamOrgFrames,
       "rprSpanStatsOutTopoAtdFrames": rprSpanStatsOutTopoAtdFrames,
       "rprSpanStatsOutTopoChkSumFrames": rprSpanStatsOutTopoChkSumFrames,
       "rprSpanStatsOutTopoTpFrames": rprSpanStatsOutTopoTpFrames,
       "rprClientCounters": rprClientCounters,
       "rprClientCountersCurrentTable": rprClientCountersCurrentTable,
       "rprClientCountersCurrentEntry": rprClientCountersCurrentEntry,
       "rprClientCurrentIfIndex": rprClientCurrentIfIndex,
       "rprClientCurrentInUcastClassAFrames": rprClientCurrentInUcastClassAFrames,
       "rprClientCurrentInUcastClassAOctets": rprClientCurrentInUcastClassAOctets,
       "rprClientCurrentInUcastClassBCirFrames": rprClientCurrentInUcastClassBCirFrames,
       "rprClientCurrentInUcastClassBCirOctets": rprClientCurrentInUcastClassBCirOctets,
       "rprClientCurrentInUcastClassBEirFrames": rprClientCurrentInUcastClassBEirFrames,
       "rprClientCurrentInUcastClassBEirOctets": rprClientCurrentInUcastClassBEirOctets,
       "rprClientCurrentInUcastClassCFrames": rprClientCurrentInUcastClassCFrames,
       "rprClientCurrentInUcastClassCOctets": rprClientCurrentInUcastClassCOctets,
       "rprClientCurrentInMcastClassAFrames": rprClientCurrentInMcastClassAFrames,
       "rprClientCurrentInMcastClassAOctets": rprClientCurrentInMcastClassAOctets,
       "rprClientCurrentInMcastClassBCirFrames": rprClientCurrentInMcastClassBCirFrames,
       "rprClientCurrentInMcastClassBCirOctets": rprClientCurrentInMcastClassBCirOctets,
       "rprClientCurrentInMcastClassBEirFrames": rprClientCurrentInMcastClassBEirFrames,
       "rprClientCurrentInMcastClassBEirOctets": rprClientCurrentInMcastClassBEirOctets,
       "rprClientCurrentInMcastClassCFrames": rprClientCurrentInMcastClassCFrames,
       "rprClientCurrentInMcastClassCOctets": rprClientCurrentInMcastClassCOctets,
       "rprClientCurrentOutUcastClassAFrames": rprClientCurrentOutUcastClassAFrames,
       "rprClientCurrentOutUcastClassAOctets": rprClientCurrentOutUcastClassAOctets,
       "rprClientCurrentOutUcastClassBCirFrames": rprClientCurrentOutUcastClassBCirFrames,
       "rprClientCurrentOutUcastClassBCirOctets": rprClientCurrentOutUcastClassBCirOctets,
       "rprClientCurrentOutUcastClassBEirFrames": rprClientCurrentOutUcastClassBEirFrames,
       "rprClientCurrentOutUcastClassBEirOctets": rprClientCurrentOutUcastClassBEirOctets,
       "rprClientCurrentOutUcastClassCFrames": rprClientCurrentOutUcastClassCFrames,
       "rprClientCurrentOutUcastClassCOctets": rprClientCurrentOutUcastClassCOctets,
       "rprClientCurrentOutMcastClassAFrames": rprClientCurrentOutMcastClassAFrames,
       "rprClientCurrentOutMcastClassAOctets": rprClientCurrentOutMcastClassAOctets,
       "rprClientCurrentOutMcastClassBCirFrames": rprClientCurrentOutMcastClassBCirFrames,
       "rprClientCurrentOutMcastClassBCirOctets": rprClientCurrentOutMcastClassBCirOctets,
       "rprClientCurrentOutMcastClassBEirFrames": rprClientCurrentOutMcastClassBEirFrames,
       "rprClientCurrentOutMcastClassBEirOctets": rprClientCurrentOutMcastClassBEirOctets,
       "rprClientCurrentOutMcastClassCFrames": rprClientCurrentOutMcastClassCFrames,
       "rprClientCurrentOutMcastClassCOctets": rprClientCurrentOutMcastClassCOctets,
       "rprClientCountersIntervalTable": rprClientCountersIntervalTable,
       "rprClientCountersIntervalEntry": rprClientCountersIntervalEntry,
       "rprClientIntervalIfIndex": rprClientIntervalIfIndex,
       "rprClientIntervalNumber": rprClientIntervalNumber,
       "rprClientIntervalValidData": rprClientIntervalValidData,
       "rprClientIntervalTimeElapsed": rprClientIntervalTimeElapsed,
       "rprClientIntervalInUcastClassAFrames": rprClientIntervalInUcastClassAFrames,
       "rprClientIntervalInUcastClassAOctets": rprClientIntervalInUcastClassAOctets,
       "rprClientIntervalInUcastClassBCirFrames": rprClientIntervalInUcastClassBCirFrames,
       "rprClientIntervalInUcastClassBCirOctets": rprClientIntervalInUcastClassBCirOctets,
       "rprClientIntervalInUcastClassBEirFrames": rprClientIntervalInUcastClassBEirFrames,
       "rprClientIntervalInUcastClassBEirOctets": rprClientIntervalInUcastClassBEirOctets,
       "rprClientIntervalInUcastClassCFrames": rprClientIntervalInUcastClassCFrames,
       "rprClientIntervalInUcastClassCOctets": rprClientIntervalInUcastClassCOctets,
       "rprClientIntervalInMcastClassAFrames": rprClientIntervalInMcastClassAFrames,
       "rprClientIntervalInMcastClassAOctets": rprClientIntervalInMcastClassAOctets,
       "rprClientIntervalInMcastClassBCirFrames": rprClientIntervalInMcastClassBCirFrames,
       "rprClientIntervalInMcastClassBCirOctets": rprClientIntervalInMcastClassBCirOctets,
       "rprClientIntervalInMcastClassBEirFrames": rprClientIntervalInMcastClassBEirFrames,
       "rprClientIntervalInMcastClassBEirOctets": rprClientIntervalInMcastClassBEirOctets,
       "rprClientIntervalInMcastClassCFrames": rprClientIntervalInMcastClassCFrames,
       "rprClientIntervalInMcastClassCOctets": rprClientIntervalInMcastClassCOctets,
       "rprClientIntervalOutUcastClassAFrames": rprClientIntervalOutUcastClassAFrames,
       "rprClientIntervalOutUcastClassAOctets": rprClientIntervalOutUcastClassAOctets,
       "rprClientIntervalOutUcastClassBCirFrames": rprClientIntervalOutUcastClassBCirFrames,
       "rprClientIntervalOutUcastClassBCirOctets": rprClientIntervalOutUcastClassBCirOctets,
       "rprClientIntervalOutUcastClassBEirFrames": rprClientIntervalOutUcastClassBEirFrames,
       "rprClientIntervalOutUcastClassBEirOctets": rprClientIntervalOutUcastClassBEirOctets,
       "rprClientIntervalOutUcastClassCFrames": rprClientIntervalOutUcastClassCFrames,
       "rprClientIntervalOutUcastClassCOctets": rprClientIntervalOutUcastClassCOctets,
       "rprClientIntervalOutMcastClassAFrames": rprClientIntervalOutMcastClassAFrames,
       "rprClientIntervalOutMcastClassAOctets": rprClientIntervalOutMcastClassAOctets,
       "rprClientIntervalOutMcastClassBCirFrames": rprClientIntervalOutMcastClassBCirFrames,
       "rprClientIntervalOutMcastClassBCirOctets": rprClientIntervalOutMcastClassBCirOctets,
       "rprClientIntervalOutMcastClassBEirFrames": rprClientIntervalOutMcastClassBEirFrames,
       "rprClientIntervalOutMcastClassBEirOctets": rprClientIntervalOutMcastClassBEirOctets,
       "rprClientIntervalOutMcastClassCFrames": rprClientIntervalOutMcastClassCFrames,
       "rprClientIntervalOutMcastClassCOctets": rprClientIntervalOutMcastClassCOctets,
       "rprClientCountersDayTable": rprClientCountersDayTable,
       "rprClientCountersDayEntry": rprClientCountersDayEntry,
       "rprClientDayIfIndex": rprClientDayIfIndex,
       "rprClientDayInUcastClassAFrames": rprClientDayInUcastClassAFrames,
       "rprClientDayInUcastClassAOctets": rprClientDayInUcastClassAOctets,
       "rprClientDayInUcastClassBCirFrames": rprClientDayInUcastClassBCirFrames,
       "rprClientDayInUcastClassBCirOctets": rprClientDayInUcastClassBCirOctets,
       "rprClientDayInUcastClassBEirFrames": rprClientDayInUcastClassBEirFrames,
       "rprClientDayInUcastClassBEirOctets": rprClientDayInUcastClassBEirOctets,
       "rprClientDayInUcastClassCFrames": rprClientDayInUcastClassCFrames,
       "rprClientDayInUcastClassCOctets": rprClientDayInUcastClassCOctets,
       "rprClientDayInMcastClassAFrames": rprClientDayInMcastClassAFrames,
       "rprClientDayInMcastClassAOctets": rprClientDayInMcastClassAOctets,
       "rprClientDayInMcastClassBCirFrames": rprClientDayInMcastClassBCirFrames,
       "rprClientDayInMcastClassBCirOctets": rprClientDayInMcastClassBCirOctets,
       "rprClientDayInMcastClassBEirFrames": rprClientDayInMcastClassBEirFrames,
       "rprClientDayInMcastClassBEirOctets": rprClientDayInMcastClassBEirOctets,
       "rprClientDayInMcastClassCFrames": rprClientDayInMcastClassCFrames,
       "rprClientDayInMcastClassCOctets": rprClientDayInMcastClassCOctets,
       "rprClientDayOutUcastClassAFrames": rprClientDayOutUcastClassAFrames,
       "rprClientDayOutUcastClassAOctets": rprClientDayOutUcastClassAOctets,
       "rprClientDayOutUcastClassBCirFrames": rprClientDayOutUcastClassBCirFrames,
       "rprClientDayOutUcastClassBCirOctets": rprClientDayOutUcastClassBCirOctets,
       "rprClientDayOutUcastClassBEirFrames": rprClientDayOutUcastClassBEirFrames,
       "rprClientDayOutUcastClassBEirOctets": rprClientDayOutUcastClassBEirOctets,
       "rprClientDayOutUcastClassCFrames": rprClientDayOutUcastClassCFrames,
       "rprClientDayOutUcastClassCOctets": rprClientDayOutUcastClassCOctets,
       "rprClientDayOutMcastClassAFrames": rprClientDayOutMcastClassAFrames,
       "rprClientDayOutMcastClassAOctets": rprClientDayOutMcastClassAOctets,
       "rprClientDayOutMcastClassBCirFrames": rprClientDayOutMcastClassBCirFrames,
       "rprClientDayOutMcastClassBCirOctets": rprClientDayOutMcastClassBCirOctets,
       "rprClientDayOutMcastClassBEirFrames": rprClientDayOutMcastClassBEirFrames,
       "rprClientDayOutMcastClassBEirOctets": rprClientDayOutMcastClassBEirOctets,
       "rprClientDayOutMcastClassCFrames": rprClientDayOutMcastClassCFrames,
       "rprClientDayOutMcastClassCOctets": rprClientDayOutMcastClassCOctets,
       "rprClientCountersStatsTable": rprClientCountersStatsTable,
       "rprClientCountersStatsEntry": rprClientCountersStatsEntry,
       "rprClientStatsIfIndex": rprClientStatsIfIndex,
       "rprClientStatsInUcastClassAFrames": rprClientStatsInUcastClassAFrames,
       "rprClientStatsInUcastClassAOctets": rprClientStatsInUcastClassAOctets,
       "rprClientStatsInUcastClassBCirFrames": rprClientStatsInUcastClassBCirFrames,
       "rprClientStatsInUcastClassBCirOctets": rprClientStatsInUcastClassBCirOctets,
       "rprClientStatsInUcastClassBEirFrames": rprClientStatsInUcastClassBEirFrames,
       "rprClientStatsInUcastClassBEirOctets": rprClientStatsInUcastClassBEirOctets,
       "rprClientStatsInUcastClassCFrames": rprClientStatsInUcastClassCFrames,
       "rprClientStatsInUcastClassCOctets": rprClientStatsInUcastClassCOctets,
       "rprClientStatsInMcastClassAFrames": rprClientStatsInMcastClassAFrames,
       "rprClientStatsInMcastClassAOctets": rprClientStatsInMcastClassAOctets,
       "rprClientStatsInMcastClassBCirFrames": rprClientStatsInMcastClassBCirFrames,
       "rprClientStatsInMcastClassBCirOctets": rprClientStatsInMcastClassBCirOctets,
       "rprClientStatsInMcastClassBEirFrames": rprClientStatsInMcastClassBEirFrames,
       "rprClientStatsInMcastClassBEirOctets": rprClientStatsInMcastClassBEirOctets,
       "rprClientStatsInMcastClassCFrames": rprClientStatsInMcastClassCFrames,
       "rprClientStatsInMcastClassCOctets": rprClientStatsInMcastClassCOctets,
       "rprClientStatsInBcastFrames": rprClientStatsInBcastFrames,
       "rprClientStatsOutUcastClassAFrames": rprClientStatsOutUcastClassAFrames,
       "rprClientStatsOutUcastClassAOctets": rprClientStatsOutUcastClassAOctets,
       "rprClientStatsOutUcastClassBCirFrames": rprClientStatsOutUcastClassBCirFrames,
       "rprClientStatsOutUcastClassBCirOctets": rprClientStatsOutUcastClassBCirOctets,
       "rprClientStatsOutUcastClassBEirFrames": rprClientStatsOutUcastClassBEirFrames,
       "rprClientStatsOutUcastClassBEirOctets": rprClientStatsOutUcastClassBEirOctets,
       "rprClientStatsOutUcastClassCFrames": rprClientStatsOutUcastClassCFrames,
       "rprClientStatsOutUcastClassCOctets": rprClientStatsOutUcastClassCOctets,
       "rprClientStatsOutMcastClassAFrames": rprClientStatsOutMcastClassAFrames,
       "rprClientStatsOutMcastClassAOctets": rprClientStatsOutMcastClassAOctets,
       "rprClientStatsOutMcastClassBCirFrames": rprClientStatsOutMcastClassBCirFrames,
       "rprClientStatsOutMcastClassBCirOctets": rprClientStatsOutMcastClassBCirOctets,
       "rprClientStatsOutMcastClassBEirFrames": rprClientStatsOutMcastClassBEirFrames,
       "rprClientStatsOutMcastClassBEirOctets": rprClientStatsOutMcastClassBEirOctets,
       "rprClientStatsOutMcastClassCFrames": rprClientStatsOutMcastClassCFrames,
       "rprClientStatsOutMcastClassCOctets": rprClientStatsOutMcastClassCOctets,
       "rprClientStatsOutBcastFrames": rprClientStatsOutBcastFrames,
       "rprSpanErrorCounters": rprSpanErrorCounters,
       "rprSpanErrorCountersCurrentTable": rprSpanErrorCountersCurrentTable,
       "rprSpanErrorCountersCurrentEntry": rprSpanErrorCountersCurrentEntry,
       "rprSpanErrorCurrentIfIndex": rprSpanErrorCurrentIfIndex,
       "rprSpanErrorCurrentSpan": rprSpanErrorCurrentSpan,
       "rprSpanErrorCurrentTtlExpFrames": rprSpanErrorCurrentTtlExpFrames,
       "rprSpanErrorCurrentTooLongFrames": rprSpanErrorCurrentTooLongFrames,
       "rprSpanErrorCurrentTooShortFrames": rprSpanErrorCurrentTooShortFrames,
       "rprSpanErrorCurrentBadHecFrames": rprSpanErrorCurrentBadHecFrames,
       "rprSpanErrorCurrentBadFcsFrames": rprSpanErrorCurrentBadFcsFrames,
       "rprSpanErrorCurrentSelfSrcUcastFrames": rprSpanErrorCurrentSelfSrcUcastFrames,
       "rprSpanErrorCurrentPmdAbortFrames": rprSpanErrorCurrentPmdAbortFrames,
       "rprSpanErrorCurrentBadAddrFrames": rprSpanErrorCurrentBadAddrFrames,
       "rprSpanErrorCurrentBadParityFrames": rprSpanErrorCurrentBadParityFrames,
       "rprSpanErrorCurrentContainedFrames": rprSpanErrorCurrentContainedFrames,
       "rprSpanErrorCurrentScffErrors": rprSpanErrorCurrentScffErrors,
       "rprSpanErrorCurrentErroredSeconds": rprSpanErrorCurrentErroredSeconds,
       "rprSpanErrorCurrentSeverelyErroredSeconds": rprSpanErrorCurrentSeverelyErroredSeconds,
       "rprSpanErrorCurrentUnavailableSeconds": rprSpanErrorCurrentUnavailableSeconds,
       "rprSpanErrorCountersIntervalTable": rprSpanErrorCountersIntervalTable,
       "rprSpanErrorCountersIntervalEntry": rprSpanErrorCountersIntervalEntry,
       "rprSpanErrorIntervalIfIndex": rprSpanErrorIntervalIfIndex,
       "rprSpanErrorIntervalSpan": rprSpanErrorIntervalSpan,
       "rprSpanErrorIntervalNumber": rprSpanErrorIntervalNumber,
       "rprSpanErrorIntervalValidData": rprSpanErrorIntervalValidData,
       "rprSpanErrorIntervalTimeElapsed": rprSpanErrorIntervalTimeElapsed,
       "rprSpanErrorIntervalTtlExpFrames": rprSpanErrorIntervalTtlExpFrames,
       "rprSpanErrorIntervalTooLongFrames": rprSpanErrorIntervalTooLongFrames,
       "rprSpanErrorIntervalTooShortFrames": rprSpanErrorIntervalTooShortFrames,
       "rprSpanErrorIntervalBadHecFrames": rprSpanErrorIntervalBadHecFrames,
       "rprSpanErrorIntervalBadFcsFrames": rprSpanErrorIntervalBadFcsFrames,
       "rprSpanErrorIntervalSelfSrcUcastFrames": rprSpanErrorIntervalSelfSrcUcastFrames,
       "rprSpanErrorIntervalPmdAbortFrames": rprSpanErrorIntervalPmdAbortFrames,
       "rprSpanErrorIntervalBadAddrFrames": rprSpanErrorIntervalBadAddrFrames,
       "rprSpanErrorIntervalBadParityFrames": rprSpanErrorIntervalBadParityFrames,
       "rprSpanErrorIntervalContainedFrames": rprSpanErrorIntervalContainedFrames,
       "rprSpanErrorIntervalScffErrors": rprSpanErrorIntervalScffErrors,
       "rprSpanErrorIntervalErroredSeconds": rprSpanErrorIntervalErroredSeconds,
       "rprSpanErrorIntervalSeverelyErroredSeconds": rprSpanErrorIntervalSeverelyErroredSeconds,
       "rprSpanErrorIntervalUnavailableSeconds": rprSpanErrorIntervalUnavailableSeconds,
       "rprSpanErrorCountersDayTable": rprSpanErrorCountersDayTable,
       "rprSpanErrorCountersDayEntry": rprSpanErrorCountersDayEntry,
       "rprSpanErrorDayIfIndex": rprSpanErrorDayIfIndex,
       "rprSpanErrorDaySpan": rprSpanErrorDaySpan,
       "rprSpanErrorDayTtlExpFrames": rprSpanErrorDayTtlExpFrames,
       "rprSpanErrorDayTooLongFrames": rprSpanErrorDayTooLongFrames,
       "rprSpanErrorDayTooShortFrames": rprSpanErrorDayTooShortFrames,
       "rprSpanErrorDayBadHecFrames": rprSpanErrorDayBadHecFrames,
       "rprSpanErrorDayBadFcsFrames": rprSpanErrorDayBadFcsFrames,
       "rprSpanErrorDaySelfSrcUcastFrames": rprSpanErrorDaySelfSrcUcastFrames,
       "rprSpanErrorDayPmdAbortFrames": rprSpanErrorDayPmdAbortFrames,
       "rprSpanErrorDayBadAddrFrames": rprSpanErrorDayBadAddrFrames,
       "rprSpanErrorDayBadParityFrames": rprSpanErrorDayBadParityFrames,
       "rprSpanErrorDayContainedFrames": rprSpanErrorDayContainedFrames,
       "rprSpanErrorDayScffErrors": rprSpanErrorDayScffErrors,
       "rprSpanErrorDayErroredSeconds": rprSpanErrorDayErroredSeconds,
       "rprSpanErrorDaySeverelyErroredSeconds": rprSpanErrorDaySeverelyErroredSeconds,
       "rprSpanErrorDayUnavailableSeconds": rprSpanErrorDayUnavailableSeconds,
       "rprSpanErrorCountersStatsTable": rprSpanErrorCountersStatsTable,
       "rprSpanErrorCountersStatsEntry": rprSpanErrorCountersStatsEntry,
       "rprSpanErrorStatsIfIndex": rprSpanErrorStatsIfIndex,
       "rprSpanErrorStatsSpan": rprSpanErrorStatsSpan,
       "rprSpanErrorStatsTtlExpFrames": rprSpanErrorStatsTtlExpFrames,
       "rprSpanErrorStatsTooLongFrames": rprSpanErrorStatsTooLongFrames,
       "rprSpanErrorStatsTooShortFrames": rprSpanErrorStatsTooShortFrames,
       "rprSpanErrorStatsBadHecFrames": rprSpanErrorStatsBadHecFrames,
       "rprSpanErrorStatsBadFcsFrames": rprSpanErrorStatsBadFcsFrames,
       "rprSpanErrorStatsSelfSrcUcastFrames": rprSpanErrorStatsSelfSrcUcastFrames,
       "rprSpanErrorStatsPmdAbortFrames": rprSpanErrorStatsPmdAbortFrames,
       "rprSpanErrorStatsBadAddrFrames": rprSpanErrorStatsBadAddrFrames,
       "rprSpanErrorStatsBadParityFrames": rprSpanErrorStatsBadParityFrames,
       "rprSpanErrorStatsContainedFrames": rprSpanErrorStatsContainedFrames,
       "rprSpanErrorStatsScffErrors": rprSpanErrorStatsScffErrors,
       "rprConformance": rprConformance,
       "rprGroups": rprGroups,
       "rprIfGroup": rprIfGroup,
       "rprIfGroupOpt": rprIfGroupOpt,
       "rprIfStatsControlGroup": rprIfStatsControlGroup,
       "rprSpanGroup": rprSpanGroup,
       "rprSpanGroupOpt": rprSpanGroupOpt,
       "rprSpanProtectionGroup": rprSpanProtectionGroup,
       "rprTopoGroup": rprTopoGroup,
       "rprFairnessGroup": rprFairnessGroup,
       "rprFairnessGroupOpt": rprFairnessGroupOpt,
       "rprOamGroup": rprOamGroup,
       "rprIfChangeSummaryGroup": rprIfChangeSummaryGroup,
       "rprSpanCurrentGroup": rprSpanCurrentGroup,
       "rprSpanIntervalGroup": rprSpanIntervalGroup,
       "rprSpanDayGroup": rprSpanDayGroup,
       "rprSpanStatsGroup": rprSpanStatsGroup,
       "rprClientCurrentGroup": rprClientCurrentGroup,
       "rprClientIntervalGroup": rprClientIntervalGroup,
       "rprClientDayGroup": rprClientDayGroup,
       "rprClientStatsGroup": rprClientStatsGroup,
       "rprErrorCurrentGroup": rprErrorCurrentGroup,
       "rprErrorIntervalGroup": rprErrorIntervalGroup,
       "rprErrorDayGroup": rprErrorDayGroup,
       "rprErrorStatsGroup": rprErrorStatsGroup,
       "rprCompliances": rprCompliances,
       "rprModuleTotalStatsCompliance": rprModuleTotalStatsCompliance}
)
