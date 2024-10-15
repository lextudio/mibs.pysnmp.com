# SNMP MIB module (DTI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DTI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:12 2024
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dtiMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7)
)
dtiMib.setRevisions(
        ("2006-06-28 00:00",
         "2005-08-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DtiCableAdvance(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



# MIB Managed Objects in the order of their OIDs

_DtiNotifications_ObjectIdentity = ObjectIdentity
dtiNotifications = _DtiNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 0)
)
_DtiMibObjects_ObjectIdentity = ObjectIdentity
dtiMibObjects = _DtiMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1)
)
_DtiProtocolObjects_ObjectIdentity = ObjectIdentity
dtiProtocolObjects = _DtiProtocolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1)
)
_DtiProtocolTable_Object = MibTable
dtiProtocolTable = _DtiProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dtiProtocolTable.setStatus("current")
_DtiProtocolEntry_Object = MibTableRow
dtiProtocolEntry = _DtiProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1)
)
dtiProtocolEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dtiProtocolEntry.setStatus("current")


class _DtiProtocolEntityType_Type(Integer32):
    """Custom type dtiProtocolEntityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("client", 3),
          ("root", 1),
          ("server", 2))
    )


_DtiProtocolEntityType_Type.__name__ = "Integer32"
_DtiProtocolEntityType_Object = MibTableColumn
dtiProtocolEntityType = _DtiProtocolEntityType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 1),
    _DtiProtocolEntityType_Type()
)
dtiProtocolEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolEntityType.setStatus("current")


class _DtiProtocolClientClockType_Type(Integer32):
    """Custom type dtiProtocolClientClockType based on Integer32"""
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
        *(("dtiClock", 5),
          ("ituI", 1),
          ("ituII", 2),
          ("ituIII", 3),
          ("st3", 4))
    )


_DtiProtocolClientClockType_Type.__name__ = "Integer32"
_DtiProtocolClientClockType_Object = MibTableColumn
dtiProtocolClientClockType = _DtiProtocolClientClockType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 2),
    _DtiProtocolClientClockType_Type()
)
dtiProtocolClientClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolClientClockType.setStatus("current")


class _DtiProtocolServerStatusFlag_Type(Integer32):
    """Custom type dtiProtocolServerStatusFlag based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("clientStable", 6),
          ("fastTrackingMode", 3),
          ("freerun", 2),
          ("holdoverMode", 5),
          ("normalMode", 4),
          ("testMode", 7),
          ("unknown", 0),
          ("warmup", 1))
    )


_DtiProtocolServerStatusFlag_Type.__name__ = "Integer32"
_DtiProtocolServerStatusFlag_Object = MibTableColumn
dtiProtocolServerStatusFlag = _DtiProtocolServerStatusFlag_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 3),
    _DtiProtocolServerStatusFlag_Type()
)
dtiProtocolServerStatusFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolServerStatusFlag.setStatus("current")


class _DtiProtocolClientStatusFlag_Type(Integer32):
    """Custom type dtiProtocolClientStatusFlag based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("bridgingMode", 6),
          ("fastTrackingMode", 3),
          ("freerun", 2),
          ("holdoverMode", 5),
          ("normalMode", 4),
          ("testMode", 7),
          ("unknown", 0),
          ("warmup", 1))
    )


_DtiProtocolClientStatusFlag_Type.__name__ = "Integer32"
_DtiProtocolClientStatusFlag_Object = MibTableColumn
dtiProtocolClientStatusFlag = _DtiProtocolClientStatusFlag_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 4),
    _DtiProtocolClientStatusFlag_Type()
)
dtiProtocolClientStatusFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolClientStatusFlag.setStatus("current")


class _DtiProtocolServerToDState_Type(Integer32):
    """Custom type dtiProtocolServerToDState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_DtiProtocolServerToDState_Type.__name__ = "Integer32"
_DtiProtocolServerToDState_Object = MibTableColumn
dtiProtocolServerToDState = _DtiProtocolServerToDState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 5),
    _DtiProtocolServerToDState_Type()
)
dtiProtocolServerToDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolServerToDState.setStatus("current")


class _DtiProtocolServerToDType_Type(Integer32):
    """Custom type dtiProtocolServerToDType based on Integer32"""
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
          ("gps", 4),
          ("ntpv4", 3),
          ("userTime", 2))
    )


_DtiProtocolServerToDType_Type.__name__ = "Integer32"
_DtiProtocolServerToDType_Object = MibTableColumn
dtiProtocolServerToDType = _DtiProtocolServerToDType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 6),
    _DtiProtocolServerToDType_Type()
)
dtiProtocolServerToDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolServerToDType.setStatus("current")


class _DtiProtocolServerToDValue_Type(OctetString):
    """Custom type dtiProtocolServerToDValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(33, 33),
    )


_DtiProtocolServerToDValue_Type.__name__ = "OctetString"
_DtiProtocolServerToDValue_Object = MibTableColumn
dtiProtocolServerToDValue = _DtiProtocolServerToDValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 7),
    _DtiProtocolServerToDValue_Type()
)
dtiProtocolServerToDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolServerToDValue.setStatus("current")


class _DtiProtocolServerCableAdvanceFlag_Type(Integer32):
    """Custom type dtiProtocolServerCableAdvanceFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("manual", 3),
          ("valid", 1))
    )


_DtiProtocolServerCableAdvanceFlag_Type.__name__ = "Integer32"
_DtiProtocolServerCableAdvanceFlag_Object = MibTableColumn
dtiProtocolServerCableAdvanceFlag = _DtiProtocolServerCableAdvanceFlag_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 8),
    _DtiProtocolServerCableAdvanceFlag_Type()
)
dtiProtocolServerCableAdvanceFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolServerCableAdvanceFlag.setStatus("current")
_DtiProtocolServerCableAdvanceValue_Type = DtiCableAdvance
_DtiProtocolServerCableAdvanceValue_Object = MibTableColumn
dtiProtocolServerCableAdvanceValue = _DtiProtocolServerCableAdvanceValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 9),
    _DtiProtocolServerCableAdvanceValue_Type()
)
dtiProtocolServerCableAdvanceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtiProtocolServerCableAdvanceValue.setStatus("current")
if mibBuilder.loadTexts:
    dtiProtocolServerCableAdvanceValue.setUnits("clockSamples")


class _DtiProtocolClientPhaseError_Type(Integer32):
    """Custom type dtiProtocolClientPhaseError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_DtiProtocolClientPhaseError_Type.__name__ = "Integer32"
_DtiProtocolClientPhaseError_Object = MibTableColumn
dtiProtocolClientPhaseError = _DtiProtocolClientPhaseError_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 10),
    _DtiProtocolClientPhaseError_Type()
)
dtiProtocolClientPhaseError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolClientPhaseError.setStatus("current")


class _DtiProtocolClientVersion_Type(Unsigned32):
    """Custom type dtiProtocolClientVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DtiProtocolClientVersion_Type.__name__ = "Unsigned32"
_DtiProtocolClientVersion_Object = MibTableColumn
dtiProtocolClientVersion = _DtiProtocolClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 11),
    _DtiProtocolClientVersion_Type()
)
dtiProtocolClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolClientVersion.setStatus("current")


class _DtiProtocolClientPathTraceability_Type(Unsigned32):
    """Custom type dtiProtocolClientPathTraceability based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DtiProtocolClientPathTraceability_Type.__name__ = "Unsigned32"
_DtiProtocolClientPathTraceability_Object = MibTableColumn
dtiProtocolClientPathTraceability = _DtiProtocolClientPathTraceability_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 12),
    _DtiProtocolClientPathTraceability_Type()
)
dtiProtocolClientPathTraceability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolClientPathTraceability.setStatus("current")


class _DtiProtocolServerClientStableFlag_Type(Integer32):
    """Custom type dtiProtocolServerClientStableFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_DtiProtocolServerClientStableFlag_Type.__name__ = "Integer32"
_DtiProtocolServerClientStableFlag_Object = MibTableColumn
dtiProtocolServerClientStableFlag = _DtiProtocolServerClientStableFlag_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 1, 1, 13),
    _DtiProtocolServerClientStableFlag_Type()
)
dtiProtocolServerClientStableFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolServerClientStableFlag.setStatus("current")
_DtiProtocolControlTable_Object = MibTable
dtiProtocolControlTable = _DtiProtocolControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dtiProtocolControlTable.setStatus("current")
_DtiProtocolControlEntry_Object = MibTableRow
dtiProtocolControlEntry = _DtiProtocolControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 2, 1)
)
dtiProtocolControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dtiProtocolControlEntry.setStatus("current")


class _DtiProtocolControlTimeInterval_Type(Unsigned32):
    """Custom type dtiProtocolControlTimeInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_DtiProtocolControlTimeInterval_Type.__name__ = "Unsigned32"
_DtiProtocolControlTimeInterval_Object = MibTableColumn
dtiProtocolControlTimeInterval = _DtiProtocolControlTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 2, 1, 1),
    _DtiProtocolControlTimeInterval_Type()
)
dtiProtocolControlTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtiProtocolControlTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    dtiProtocolControlTimeInterval.setUnits("seconds")


class _DtiProtocolControlErrorRateInterval_Type(Unsigned32):
    """Custom type dtiProtocolControlErrorRateInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_DtiProtocolControlErrorRateInterval_Type.__name__ = "Unsigned32"
_DtiProtocolControlErrorRateInterval_Object = MibTableColumn
dtiProtocolControlErrorRateInterval = _DtiProtocolControlErrorRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 2, 1, 2),
    _DtiProtocolControlErrorRateInterval_Type()
)
dtiProtocolControlErrorRateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtiProtocolControlErrorRateInterval.setStatus("current")
if mibBuilder.loadTexts:
    dtiProtocolControlErrorRateInterval.setUnits("seconds")


class _DtiProtocolControlJitterTimeInterval_Type(Unsigned32):
    """Custom type dtiProtocolControlJitterTimeInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_DtiProtocolControlJitterTimeInterval_Type.__name__ = "Unsigned32"
_DtiProtocolControlJitterTimeInterval_Object = MibTableColumn
dtiProtocolControlJitterTimeInterval = _DtiProtocolControlJitterTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 2, 1, 3),
    _DtiProtocolControlJitterTimeInterval_Type()
)
dtiProtocolControlJitterTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtiProtocolControlJitterTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    dtiProtocolControlJitterTimeInterval.setUnits("seconds")
_DtiProtocolControlTestMode_Type = TruthValue
_DtiProtocolControlTestMode_Object = MibTableColumn
dtiProtocolControlTestMode = _DtiProtocolControlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 2, 1, 4),
    _DtiProtocolControlTestMode_Type()
)
dtiProtocolControlTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtiProtocolControlTestMode.setStatus("current")


class _DtiProtocolControlToDValue_Type(OctetString):
    """Custom type dtiProtocolControlToDValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(33, 33),
    )


_DtiProtocolControlToDValue_Type.__name__ = "OctetString"
_DtiProtocolControlToDValue_Object = MibTableColumn
dtiProtocolControlToDValue = _DtiProtocolControlToDValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 2, 1, 5),
    _DtiProtocolControlToDValue_Type()
)
dtiProtocolControlToDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtiProtocolControlToDValue.setStatus("current")
_DtiProtocolPerformanceTable_Object = MibTable
dtiProtocolPerformanceTable = _DtiProtocolPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dtiProtocolPerformanceTable.setStatus("current")
_DtiProtocolPerformanceEntry_Object = MibTableRow
dtiProtocolPerformanceEntry = _DtiProtocolPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 3, 1)
)
dtiProtocolPerformanceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dtiProtocolPerformanceEntry.setStatus("current")
_DtiProtocolPerformanceDelay_Type = Unsigned32
_DtiProtocolPerformanceDelay_Object = MibTableColumn
dtiProtocolPerformanceDelay = _DtiProtocolPerformanceDelay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 3, 1, 1),
    _DtiProtocolPerformanceDelay_Type()
)
dtiProtocolPerformanceDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolPerformanceDelay.setStatus("current")
if mibBuilder.loadTexts:
    dtiProtocolPerformanceDelay.setUnits("nanoseconds")
_DtiProtocolPerformanceFrameErrorRate_Type = Unsigned32
_DtiProtocolPerformanceFrameErrorRate_Object = MibTableColumn
dtiProtocolPerformanceFrameErrorRate = _DtiProtocolPerformanceFrameErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 3, 1, 2),
    _DtiProtocolPerformanceFrameErrorRate_Type()
)
dtiProtocolPerformanceFrameErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolPerformanceFrameErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    dtiProtocolPerformanceFrameErrorRate.setUnits("FER")


class _DtiProtocolPerformancePeakToPeakJitter_Type(Integer32):
    """Custom type dtiProtocolPerformancePeakToPeakJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_DtiProtocolPerformancePeakToPeakJitter_Type.__name__ = "Integer32"
_DtiProtocolPerformancePeakToPeakJitter_Object = MibTableColumn
dtiProtocolPerformancePeakToPeakJitter = _DtiProtocolPerformancePeakToPeakJitter_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 3, 1, 3),
    _DtiProtocolPerformancePeakToPeakJitter_Type()
)
dtiProtocolPerformancePeakToPeakJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolPerformancePeakToPeakJitter.setStatus("current")
if mibBuilder.loadTexts:
    dtiProtocolPerformancePeakToPeakJitter.setUnits("picoseconds")


class _DtiProtocolPerformanceWander35Second_Type(Unsigned32):
    """Custom type dtiProtocolPerformanceWander35Second based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DtiProtocolPerformanceWander35Second_Type.__name__ = "Unsigned32"
_DtiProtocolPerformanceWander35Second_Object = MibTableColumn
dtiProtocolPerformanceWander35Second = _DtiProtocolPerformanceWander35Second_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 3, 1, 4),
    _DtiProtocolPerformanceWander35Second_Type()
)
dtiProtocolPerformanceWander35Second.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolPerformanceWander35Second.setStatus("current")
if mibBuilder.loadTexts:
    dtiProtocolPerformanceWander35Second.setUnits("picoseconds")


class _DtiProtocolPerformanceWanderTSeconds_Type(Unsigned32):
    """Custom type dtiProtocolPerformanceWanderTSeconds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DtiProtocolPerformanceWanderTSeconds_Type.__name__ = "Unsigned32"
_DtiProtocolPerformanceWanderTSeconds_Object = MibTableColumn
dtiProtocolPerformanceWanderTSeconds = _DtiProtocolPerformanceWanderTSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 3, 1, 5),
    _DtiProtocolPerformanceWanderTSeconds_Type()
)
dtiProtocolPerformanceWanderTSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolPerformanceWanderTSeconds.setStatus("current")
if mibBuilder.loadTexts:
    dtiProtocolPerformanceWanderTSeconds.setUnits("picoseconds")
_DtiPathTraceabilityTable_Object = MibTable
dtiPathTraceabilityTable = _DtiPathTraceabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dtiPathTraceabilityTable.setStatus("current")
_DtiPathTraceabilityEntry_Object = MibTableRow
dtiPathTraceabilityEntry = _DtiPathTraceabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1)
)
dtiPathTraceabilityEntry.setIndexNames(
    (0, "DTI-MIB", "dtiPathTraceabilityIndex"),
)
if mibBuilder.loadTexts:
    dtiPathTraceabilityEntry.setStatus("current")


class _DtiPathTraceabilityIndex_Type(Unsigned32):
    """Custom type dtiPathTraceabilityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DtiPathTraceabilityIndex_Type.__name__ = "Unsigned32"
_DtiPathTraceabilityIndex_Object = MibTableColumn
dtiPathTraceabilityIndex = _DtiPathTraceabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 1),
    _DtiPathTraceabilityIndex_Type()
)
dtiPathTraceabilityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dtiPathTraceabilityIndex.setStatus("current")
_DtiPathTraceabilityRootServerInetAddrType_Type = InetAddressType
_DtiPathTraceabilityRootServerInetAddrType_Object = MibTableColumn
dtiPathTraceabilityRootServerInetAddrType = _DtiPathTraceabilityRootServerInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 2),
    _DtiPathTraceabilityRootServerInetAddrType_Type()
)
dtiPathTraceabilityRootServerInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiPathTraceabilityRootServerInetAddrType.setStatus("current")
_DtiPathTraceabilityRootServerInetAddr_Type = InetAddress
_DtiPathTraceabilityRootServerInetAddr_Object = MibTableColumn
dtiPathTraceabilityRootServerInetAddr = _DtiPathTraceabilityRootServerInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 3),
    _DtiPathTraceabilityRootServerInetAddr_Type()
)
dtiPathTraceabilityRootServerInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiPathTraceabilityRootServerInetAddr.setStatus("current")
_DtiPathTraceabilityRootServerOutPhyIdx_Type = PhysicalIndex
_DtiPathTraceabilityRootServerOutPhyIdx_Object = MibTableColumn
dtiPathTraceabilityRootServerOutPhyIdx = _DtiPathTraceabilityRootServerOutPhyIdx_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 4),
    _DtiPathTraceabilityRootServerOutPhyIdx_Type()
)
dtiPathTraceabilityRootServerOutPhyIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiPathTraceabilityRootServerOutPhyIdx.setStatus("current")
_DtiPathTraceabilityServerInetAddrType_Type = InetAddressType
_DtiPathTraceabilityServerInetAddrType_Object = MibTableColumn
dtiPathTraceabilityServerInetAddrType = _DtiPathTraceabilityServerInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 5),
    _DtiPathTraceabilityServerInetAddrType_Type()
)
dtiPathTraceabilityServerInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiPathTraceabilityServerInetAddrType.setStatus("current")
_DtiPathTraceabilityServerInetAddr_Type = InetAddress
_DtiPathTraceabilityServerInetAddr_Object = MibTableColumn
dtiPathTraceabilityServerInetAddr = _DtiPathTraceabilityServerInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 6),
    _DtiPathTraceabilityServerInetAddr_Type()
)
dtiPathTraceabilityServerInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiPathTraceabilityServerInetAddr.setStatus("current")
_DtiPathTraceabilityServerOutPhyIdx_Type = PhysicalIndex
_DtiPathTraceabilityServerOutPhyIdx_Object = MibTableColumn
dtiPathTraceabilityServerOutPhyIdx = _DtiPathTraceabilityServerOutPhyIdx_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 7),
    _DtiPathTraceabilityServerOutPhyIdx_Type()
)
dtiPathTraceabilityServerOutPhyIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiPathTraceabilityServerOutPhyIdx.setStatus("current")
_DtiPathTraceabilityRootServerProtVersion_Type = Unsigned32
_DtiPathTraceabilityRootServerProtVersion_Object = MibTableColumn
dtiPathTraceabilityRootServerProtVersion = _DtiPathTraceabilityRootServerProtVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 8),
    _DtiPathTraceabilityRootServerProtVersion_Type()
)
dtiPathTraceabilityRootServerProtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiPathTraceabilityRootServerProtVersion.setStatus("current")
_DtiPathTraceabilityServerProtVersion_Type = Unsigned32
_DtiPathTraceabilityServerProtVersion_Object = MibTableColumn
dtiPathTraceabilityServerProtVersion = _DtiPathTraceabilityServerProtVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 4, 1, 9),
    _DtiPathTraceabilityServerProtVersion_Type()
)
dtiPathTraceabilityServerProtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiPathTraceabilityServerProtVersion.setStatus("current")
_DtiProtocolClientFsmStatsTable_Object = MibTable
dtiProtocolClientFsmStatsTable = _DtiProtocolClientFsmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6)
)
if mibBuilder.loadTexts:
    dtiProtocolClientFsmStatsTable.setStatus("current")
_DtiProtocolClientFsmStatsEntry_Object = MibTableRow
dtiProtocolClientFsmStatsEntry = _DtiProtocolClientFsmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6, 1)
)
dtiProtocolClientFsmStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dtiProtocolClientFsmStatsEntry.setStatus("current")
_DtiProtocolClientFsmStatsT3Count_Type = Counter32
_DtiProtocolClientFsmStatsT3Count_Object = MibTableColumn
dtiProtocolClientFsmStatsT3Count = _DtiProtocolClientFsmStatsT3Count_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6, 1, 1),
    _DtiProtocolClientFsmStatsT3Count_Type()
)
dtiProtocolClientFsmStatsT3Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolClientFsmStatsT3Count.setStatus("current")
_DtiProtocolClientFsmStatsT4Count_Type = Counter32
_DtiProtocolClientFsmStatsT4Count_Object = MibTableColumn
dtiProtocolClientFsmStatsT4Count = _DtiProtocolClientFsmStatsT4Count_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6, 1, 2),
    _DtiProtocolClientFsmStatsT4Count_Type()
)
dtiProtocolClientFsmStatsT4Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolClientFsmStatsT4Count.setStatus("current")
_DtiProtocolClientFsmStatsT6Count_Type = Counter32
_DtiProtocolClientFsmStatsT6Count_Object = MibTableColumn
dtiProtocolClientFsmStatsT6Count = _DtiProtocolClientFsmStatsT6Count_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6, 1, 3),
    _DtiProtocolClientFsmStatsT6Count_Type()
)
dtiProtocolClientFsmStatsT6Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolClientFsmStatsT6Count.setStatus("current")
_DtiProtocolClientFsmStatsT7Count_Type = Counter32
_DtiProtocolClientFsmStatsT7Count_Object = MibTableColumn
dtiProtocolClientFsmStatsT7Count = _DtiProtocolClientFsmStatsT7Count_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6, 1, 4),
    _DtiProtocolClientFsmStatsT7Count_Type()
)
dtiProtocolClientFsmStatsT7Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolClientFsmStatsT7Count.setStatus("current")
_DtiProtocolClientFsmStatsNormalActiveTime_Type = Counter32
_DtiProtocolClientFsmStatsNormalActiveTime_Object = MibTableColumn
dtiProtocolClientFsmStatsNormalActiveTime = _DtiProtocolClientFsmStatsNormalActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6, 1, 5),
    _DtiProtocolClientFsmStatsNormalActiveTime_Type()
)
dtiProtocolClientFsmStatsNormalActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolClientFsmStatsNormalActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    dtiProtocolClientFsmStatsNormalActiveTime.setUnits("milliseconds")
_DtiProtocolClientFsmStatsHoldoverActiveTime_Type = Counter32
_DtiProtocolClientFsmStatsHoldoverActiveTime_Object = MibTableColumn
dtiProtocolClientFsmStatsHoldoverActiveTime = _DtiProtocolClientFsmStatsHoldoverActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 1, 6, 1, 6),
    _DtiProtocolClientFsmStatsHoldoverActiveTime_Type()
)
dtiProtocolClientFsmStatsHoldoverActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiProtocolClientFsmStatsHoldoverActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    dtiProtocolClientFsmStatsHoldoverActiveTime.setUnits("milliseconds")
_DtiServerObjects_ObjectIdentity = ObjectIdentity
dtiServerObjects = _DtiServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2)
)
_DtiServerProperties_ObjectIdentity = ObjectIdentity
dtiServerProperties = _DtiServerProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 1)
)


class _DtiServerRootClockType_Type(Integer32):
    """Custom type dtiServerRootClockType based on Integer32"""
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
        *(("ituI", 1),
          ("ituII", 2),
          ("ituIII", 3),
          ("st3", 4))
    )


_DtiServerRootClockType_Type.__name__ = "Integer32"
_DtiServerRootClockType_Object = MibScalar
dtiServerRootClockType = _DtiServerRootClockType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 1, 1),
    _DtiServerRootClockType_Type()
)
dtiServerRootClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiServerRootClockType.setStatus("current")


class _DtiServerHopCount_Type(Integer32):
    """Custom type dtiServerHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proxy", 2),
          ("root", 1))
    )


_DtiServerHopCount_Type.__name__ = "Integer32"
_DtiServerHopCount_Object = MibScalar
dtiServerHopCount = _DtiServerHopCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 1, 2),
    _DtiServerHopCount_Type()
)
dtiServerHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiServerHopCount.setStatus("current")


class _DtiServerExternalTimingSource_Type(Integer32):
    """Custom type dtiServerExternalTimingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gps", 2),
          ("network", 3),
          ("noExternal", 1))
    )


_DtiServerExternalTimingSource_Type.__name__ = "Integer32"
_DtiServerExternalTimingSource_Object = MibScalar
dtiServerExternalTimingSource = _DtiServerExternalTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 1, 3),
    _DtiServerExternalTimingSource_Type()
)
dtiServerExternalTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiServerExternalTimingSource.setStatus("current")


class _DtiServerToDSources_Type(Bits):
    """Custom type dtiServerToDSources based on Bits"""
    namedValues = NamedValues(
        *(("default", 0),
          ("gps", 3),
          ("ntpv4", 2),
          ("userTime", 1))
    )

_DtiServerToDSources_Type.__name__ = "Bits"
_DtiServerToDSources_Object = MibScalar
dtiServerToDSources = _DtiServerToDSources_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 1, 4),
    _DtiServerToDSources_Type()
)
dtiServerToDSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtiServerToDSources.setStatus("current")
_DtiServerGlobalParameters_ObjectIdentity = ObjectIdentity
dtiServerGlobalParameters = _DtiServerGlobalParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 2)
)


class _DtiServerGlobalTimeInterval_Type(Unsigned32):
    """Custom type dtiServerGlobalTimeInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_DtiServerGlobalTimeInterval_Type.__name__ = "Unsigned32"
_DtiServerGlobalTimeInterval_Object = MibScalar
dtiServerGlobalTimeInterval = _DtiServerGlobalTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 2, 1),
    _DtiServerGlobalTimeInterval_Type()
)
dtiServerGlobalTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtiServerGlobalTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    dtiServerGlobalTimeInterval.setUnits("seconds")


class _DtiServerGlobalErrorRateInterval_Type(Unsigned32):
    """Custom type dtiServerGlobalErrorRateInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_DtiServerGlobalErrorRateInterval_Type.__name__ = "Unsigned32"
_DtiServerGlobalErrorRateInterval_Object = MibScalar
dtiServerGlobalErrorRateInterval = _DtiServerGlobalErrorRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 2, 2),
    _DtiServerGlobalErrorRateInterval_Type()
)
dtiServerGlobalErrorRateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtiServerGlobalErrorRateInterval.setStatus("current")
if mibBuilder.loadTexts:
    dtiServerGlobalErrorRateInterval.setUnits("seconds")


class _DtiServerGlobalJitterTimeInterval_Type(Unsigned32):
    """Custom type dtiServerGlobalJitterTimeInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_DtiServerGlobalJitterTimeInterval_Type.__name__ = "Unsigned32"
_DtiServerGlobalJitterTimeInterval_Object = MibScalar
dtiServerGlobalJitterTimeInterval = _DtiServerGlobalJitterTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 2, 3),
    _DtiServerGlobalJitterTimeInterval_Type()
)
dtiServerGlobalJitterTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtiServerGlobalJitterTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    dtiServerGlobalJitterTimeInterval.setUnits("seconds")


class _DtiServerGlobalToDMethod_Type(Integer32):
    """Custom type dtiServerGlobalToDMethod based on Integer32"""
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
          ("gps", 4),
          ("ntpv4", 3),
          ("userTime", 2))
    )


_DtiServerGlobalToDMethod_Type.__name__ = "Integer32"
_DtiServerGlobalToDMethod_Object = MibScalar
dtiServerGlobalToDMethod = _DtiServerGlobalToDMethod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 2, 4),
    _DtiServerGlobalToDMethod_Type()
)
dtiServerGlobalToDMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtiServerGlobalToDMethod.setStatus("current")


class _DtiServerGlobalToDValue_Type(OctetString):
    """Custom type dtiServerGlobalToDValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(33, 33),
    )


_DtiServerGlobalToDValue_Type.__name__ = "OctetString"
_DtiServerGlobalToDValue_Object = MibScalar
dtiServerGlobalToDValue = _DtiServerGlobalToDValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 2, 2, 5),
    _DtiServerGlobalToDValue_Type()
)
dtiServerGlobalToDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtiServerGlobalToDValue.setStatus("current")
_DtiClientObjects_ObjectIdentity = ObjectIdentity
dtiClientObjects = _DtiClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 1, 3)
)
_DtiMibConformance_ObjectIdentity = ObjectIdentity
dtiMibConformance = _DtiMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 2)
)
_DtiMibCompliances_ObjectIdentity = ObjectIdentity
dtiMibCompliances = _DtiMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 2, 1)
)
_DtiMibGroups_ObjectIdentity = ObjectIdentity
dtiMibGroups = _DtiMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 2, 2)
)

# Managed Objects groups

dtiBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 2, 2, 1)
)
dtiBaseGroup.setObjects(
      *(("DTI-MIB", "dtiProtocolServerToDState"),
        ("DTI-MIB", "dtiProtocolEntityType"),
        ("DTI-MIB", "dtiProtocolClientClockType"),
        ("DTI-MIB", "dtiProtocolServerStatusFlag"),
        ("DTI-MIB", "dtiProtocolClientStatusFlag"),
        ("DTI-MIB", "dtiProtocolServerToDType"),
        ("DTI-MIB", "dtiProtocolServerToDValue"),
        ("DTI-MIB", "dtiProtocolServerCableAdvanceFlag"),
        ("DTI-MIB", "dtiProtocolServerCableAdvanceValue"),
        ("DTI-MIB", "dtiProtocolClientPhaseError"),
        ("DTI-MIB", "dtiProtocolClientVersion"),
        ("DTI-MIB", "dtiProtocolClientPathTraceability"),
        ("DTI-MIB", "dtiPathTraceabilityRootServerInetAddrType"),
        ("DTI-MIB", "dtiPathTraceabilityRootServerInetAddr"),
        ("DTI-MIB", "dtiPathTraceabilityRootServerOutPhyIdx"),
        ("DTI-MIB", "dtiPathTraceabilityServerInetAddrType"),
        ("DTI-MIB", "dtiPathTraceabilityServerInetAddr"),
        ("DTI-MIB", "dtiPathTraceabilityServerOutPhyIdx"),
        ("DTI-MIB", "dtiPathTraceabilityRootServerProtVersion"),
        ("DTI-MIB", "dtiPathTraceabilityServerProtVersion"),
        ("DTI-MIB", "dtiProtocolPerformanceDelay"),
        ("DTI-MIB", "dtiProtocolPerformanceFrameErrorRate"),
        ("DTI-MIB", "dtiProtocolPerformancePeakToPeakJitter"),
        ("DTI-MIB", "dtiProtocolPerformanceWander35Second"),
        ("DTI-MIB", "dtiProtocolPerformanceWanderTSeconds"),
        ("DTI-MIB", "dtiProtocolServerClientStableFlag"))
)
if mibBuilder.loadTexts:
    dtiBaseGroup.setStatus("current")

dtiServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 2, 2, 2)
)
dtiServerGroup.setObjects(
      *(("DTI-MIB", "dtiProtocolControlTimeInterval"),
        ("DTI-MIB", "dtiProtocolControlErrorRateInterval"),
        ("DTI-MIB", "dtiProtocolControlJitterTimeInterval"),
        ("DTI-MIB", "dtiProtocolControlTestMode"),
        ("DTI-MIB", "dtiProtocolControlToDValue"),
        ("DTI-MIB", "dtiServerRootClockType"),
        ("DTI-MIB", "dtiServerHopCount"),
        ("DTI-MIB", "dtiServerExternalTimingSource"),
        ("DTI-MIB", "dtiServerToDSources"),
        ("DTI-MIB", "dtiServerGlobalTimeInterval"),
        ("DTI-MIB", "dtiServerGlobalErrorRateInterval"),
        ("DTI-MIB", "dtiServerGlobalJitterTimeInterval"),
        ("DTI-MIB", "dtiServerGlobalToDMethod"),
        ("DTI-MIB", "dtiServerGlobalToDValue"))
)
if mibBuilder.loadTexts:
    dtiServerGroup.setStatus("current")

dtiClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 2, 2, 3)
)
dtiClientGroup.setObjects(
      *(("DTI-MIB", "dtiProtocolClientFsmStatsT3Count"),
        ("DTI-MIB", "dtiProtocolClientFsmStatsT4Count"),
        ("DTI-MIB", "dtiProtocolClientFsmStatsT6Count"),
        ("DTI-MIB", "dtiProtocolClientFsmStatsT7Count"),
        ("DTI-MIB", "dtiProtocolClientFsmStatsNormalActiveTime"),
        ("DTI-MIB", "dtiProtocolClientFsmStatsHoldoverActiveTime"))
)
if mibBuilder.loadTexts:
    dtiClientGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dtiMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dtiMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DTI-MIB",
    **{"DtiCableAdvance": DtiCableAdvance,
       "dtiMib": dtiMib,
       "dtiNotifications": dtiNotifications,
       "dtiMibObjects": dtiMibObjects,
       "dtiProtocolObjects": dtiProtocolObjects,
       "dtiProtocolTable": dtiProtocolTable,
       "dtiProtocolEntry": dtiProtocolEntry,
       "dtiProtocolEntityType": dtiProtocolEntityType,
       "dtiProtocolClientClockType": dtiProtocolClientClockType,
       "dtiProtocolServerStatusFlag": dtiProtocolServerStatusFlag,
       "dtiProtocolClientStatusFlag": dtiProtocolClientStatusFlag,
       "dtiProtocolServerToDState": dtiProtocolServerToDState,
       "dtiProtocolServerToDType": dtiProtocolServerToDType,
       "dtiProtocolServerToDValue": dtiProtocolServerToDValue,
       "dtiProtocolServerCableAdvanceFlag": dtiProtocolServerCableAdvanceFlag,
       "dtiProtocolServerCableAdvanceValue": dtiProtocolServerCableAdvanceValue,
       "dtiProtocolClientPhaseError": dtiProtocolClientPhaseError,
       "dtiProtocolClientVersion": dtiProtocolClientVersion,
       "dtiProtocolClientPathTraceability": dtiProtocolClientPathTraceability,
       "dtiProtocolServerClientStableFlag": dtiProtocolServerClientStableFlag,
       "dtiProtocolControlTable": dtiProtocolControlTable,
       "dtiProtocolControlEntry": dtiProtocolControlEntry,
       "dtiProtocolControlTimeInterval": dtiProtocolControlTimeInterval,
       "dtiProtocolControlErrorRateInterval": dtiProtocolControlErrorRateInterval,
       "dtiProtocolControlJitterTimeInterval": dtiProtocolControlJitterTimeInterval,
       "dtiProtocolControlTestMode": dtiProtocolControlTestMode,
       "dtiProtocolControlToDValue": dtiProtocolControlToDValue,
       "dtiProtocolPerformanceTable": dtiProtocolPerformanceTable,
       "dtiProtocolPerformanceEntry": dtiProtocolPerformanceEntry,
       "dtiProtocolPerformanceDelay": dtiProtocolPerformanceDelay,
       "dtiProtocolPerformanceFrameErrorRate": dtiProtocolPerformanceFrameErrorRate,
       "dtiProtocolPerformancePeakToPeakJitter": dtiProtocolPerformancePeakToPeakJitter,
       "dtiProtocolPerformanceWander35Second": dtiProtocolPerformanceWander35Second,
       "dtiProtocolPerformanceWanderTSeconds": dtiProtocolPerformanceWanderTSeconds,
       "dtiPathTraceabilityTable": dtiPathTraceabilityTable,
       "dtiPathTraceabilityEntry": dtiPathTraceabilityEntry,
       "dtiPathTraceabilityIndex": dtiPathTraceabilityIndex,
       "dtiPathTraceabilityRootServerInetAddrType": dtiPathTraceabilityRootServerInetAddrType,
       "dtiPathTraceabilityRootServerInetAddr": dtiPathTraceabilityRootServerInetAddr,
       "dtiPathTraceabilityRootServerOutPhyIdx": dtiPathTraceabilityRootServerOutPhyIdx,
       "dtiPathTraceabilityServerInetAddrType": dtiPathTraceabilityServerInetAddrType,
       "dtiPathTraceabilityServerInetAddr": dtiPathTraceabilityServerInetAddr,
       "dtiPathTraceabilityServerOutPhyIdx": dtiPathTraceabilityServerOutPhyIdx,
       "dtiPathTraceabilityRootServerProtVersion": dtiPathTraceabilityRootServerProtVersion,
       "dtiPathTraceabilityServerProtVersion": dtiPathTraceabilityServerProtVersion,
       "dtiProtocolClientFsmStatsTable": dtiProtocolClientFsmStatsTable,
       "dtiProtocolClientFsmStatsEntry": dtiProtocolClientFsmStatsEntry,
       "dtiProtocolClientFsmStatsT3Count": dtiProtocolClientFsmStatsT3Count,
       "dtiProtocolClientFsmStatsT4Count": dtiProtocolClientFsmStatsT4Count,
       "dtiProtocolClientFsmStatsT6Count": dtiProtocolClientFsmStatsT6Count,
       "dtiProtocolClientFsmStatsT7Count": dtiProtocolClientFsmStatsT7Count,
       "dtiProtocolClientFsmStatsNormalActiveTime": dtiProtocolClientFsmStatsNormalActiveTime,
       "dtiProtocolClientFsmStatsHoldoverActiveTime": dtiProtocolClientFsmStatsHoldoverActiveTime,
       "dtiServerObjects": dtiServerObjects,
       "dtiServerProperties": dtiServerProperties,
       "dtiServerRootClockType": dtiServerRootClockType,
       "dtiServerHopCount": dtiServerHopCount,
       "dtiServerExternalTimingSource": dtiServerExternalTimingSource,
       "dtiServerToDSources": dtiServerToDSources,
       "dtiServerGlobalParameters": dtiServerGlobalParameters,
       "dtiServerGlobalTimeInterval": dtiServerGlobalTimeInterval,
       "dtiServerGlobalErrorRateInterval": dtiServerGlobalErrorRateInterval,
       "dtiServerGlobalJitterTimeInterval": dtiServerGlobalJitterTimeInterval,
       "dtiServerGlobalToDMethod": dtiServerGlobalToDMethod,
       "dtiServerGlobalToDValue": dtiServerGlobalToDValue,
       "dtiClientObjects": dtiClientObjects,
       "dtiMibConformance": dtiMibConformance,
       "dtiMibCompliances": dtiMibCompliances,
       "dtiMibCompliance": dtiMibCompliance,
       "dtiMibGroups": dtiMibGroups,
       "dtiBaseGroup": dtiBaseGroup,
       "dtiServerGroup": dtiServerGroup,
       "dtiClientGroup": dtiClientGroup}
)
