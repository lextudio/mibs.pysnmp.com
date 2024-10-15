# SNMP MIB module (Wellfleet-DSX3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-DSX3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:08 2024
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

(wfDsx3Group,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfDsx3Group")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfDsx3ConfigTable_Object = MibTable
wfDsx3ConfigTable = _WfDsx3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 1)
)
if mibBuilder.loadTexts:
    wfDsx3ConfigTable.setStatus("mandatory")
_WfDsx3ConfigEntry_Object = MibTableRow
wfDsx3ConfigEntry = _WfDsx3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 1, 1)
)
wfDsx3ConfigEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3LineIndex"),
)
if mibBuilder.loadTexts:
    wfDsx3ConfigEntry.setStatus("mandatory")


class _WfDsx3LineIndex_Type(Integer32):
    """Custom type wfDsx3LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfDsx3LineIndex_Type.__name__ = "Integer32"
_WfDsx3LineIndex_Object = MibTableColumn
wfDsx3LineIndex = _WfDsx3LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 1, 1, 1),
    _WfDsx3LineIndex_Type()
)
wfDsx3LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3LineIndex.setStatus("mandatory")
_WfDsx3IfIndex_Type = Integer32
_WfDsx3IfIndex_Object = MibTableColumn
wfDsx3IfIndex = _WfDsx3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 1, 1, 2),
    _WfDsx3IfIndex_Type()
)
wfDsx3IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IfIndex.setStatus("mandatory")
_WfDsx3TimeElapsed_Type = Integer32
_WfDsx3TimeElapsed_Object = MibTableColumn
wfDsx3TimeElapsed = _WfDsx3TimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 1, 1, 3),
    _WfDsx3TimeElapsed_Type()
)
wfDsx3TimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TimeElapsed.setStatus("mandatory")
_WfDsx3ValidIntervals_Type = Integer32
_WfDsx3ValidIntervals_Object = MibTableColumn
wfDsx3ValidIntervals = _WfDsx3ValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 1, 1, 4),
    _WfDsx3ValidIntervals_Type()
)
wfDsx3ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3ValidIntervals.setStatus("mandatory")


class _WfDsx3LineType_Type(Integer32):
    """Custom type wfDsx3LineType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ds3cbitparity", 4),
          ("ds3clearchannel", 5),
          ("ds3m23", 2),
          ("ds3other", 1),
          ("ds3syntran", 3),
          ("e3framed", 7),
          ("e3other", 6),
          ("e3plcp", 8))
    )


_WfDsx3LineType_Type.__name__ = "Integer32"
_WfDsx3LineType_Object = MibTableColumn
wfDsx3LineType = _WfDsx3LineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 1, 1, 5),
    _WfDsx3LineType_Type()
)
wfDsx3LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3LineType.setStatus("mandatory")


class _WfDsx3LineCoding_Type(Integer32):
    """Custom type wfDsx3LineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b3zs", 2),
          ("hdb3", 3),
          ("other", 1))
    )


_WfDsx3LineCoding_Type.__name__ = "Integer32"
_WfDsx3LineCoding_Object = MibTableColumn
wfDsx3LineCoding = _WfDsx3LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 1, 1, 6),
    _WfDsx3LineCoding_Type()
)
wfDsx3LineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3LineCoding.setStatus("mandatory")


class _WfDsx3SendCode_Type(Integer32):
    """Custom type wfDsx3SendCode based on Integer32"""
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
        *(("ds1loopcode", 5),
          ("linecode", 2),
          ("nocode", 1),
          ("payloadcode", 3),
          ("resetcode", 4),
          ("testpattern", 6))
    )


_WfDsx3SendCode_Type.__name__ = "Integer32"
_WfDsx3SendCode_Object = MibTableColumn
wfDsx3SendCode = _WfDsx3SendCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 1, 1, 7),
    _WfDsx3SendCode_Type()
)
wfDsx3SendCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3SendCode.setStatus("mandatory")
_WfDsx3CircuitIdentifier_Type = DisplayString
_WfDsx3CircuitIdentifier_Object = MibTableColumn
wfDsx3CircuitIdentifier = _WfDsx3CircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 1, 1, 8),
    _WfDsx3CircuitIdentifier_Type()
)
wfDsx3CircuitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CircuitIdentifier.setStatus("mandatory")


class _WfDsx3LoopbackConfig_Type(Integer32):
    """Custom type wfDsx3LoopbackConfig based on Integer32"""
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
        *(("lineloop", 3),
          ("noloop", 1),
          ("otherloop", 4),
          ("payloadloop", 2))
    )


_WfDsx3LoopbackConfig_Type.__name__ = "Integer32"
_WfDsx3LoopbackConfig_Object = MibTableColumn
wfDsx3LoopbackConfig = _WfDsx3LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 1, 1, 9),
    _WfDsx3LoopbackConfig_Type()
)
wfDsx3LoopbackConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3LoopbackConfig.setStatus("mandatory")


class _WfDsx3LineStatus_Type(Integer32):
    """Custom type wfDsx3LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512)
        )
    )
    namedValues = NamedValues(
        *(("lof", 32),
          ("loopback", 128),
          ("los", 64),
          ("noalarm", 1),
          ("otherfailure", 512),
          ("rcais", 8),
          ("rcrai", 2),
          ("rctestcode", 256),
          ("txais", 16),
          ("txrai", 4))
    )


_WfDsx3LineStatus_Type.__name__ = "Integer32"
_WfDsx3LineStatus_Object = MibTableColumn
wfDsx3LineStatus = _WfDsx3LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 1, 1, 10),
    _WfDsx3LineStatus_Type()
)
wfDsx3LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3LineStatus.setStatus("mandatory")


class _WfDsx3TransmitClockSource_Type(Integer32):
    """Custom type wfDsx3TransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localtiming", 2),
          ("looptiming", 1),
          ("throughtiming", 3))
    )


_WfDsx3TransmitClockSource_Type.__name__ = "Integer32"
_WfDsx3TransmitClockSource_Object = MibTableColumn
wfDsx3TransmitClockSource = _WfDsx3TransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 1, 1, 11),
    _WfDsx3TransmitClockSource_Type()
)
wfDsx3TransmitClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TransmitClockSource.setStatus("mandatory")
_WfDsx3CurrentTable_Object = MibTable
wfDsx3CurrentTable = _WfDsx3CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2)
)
if mibBuilder.loadTexts:
    wfDsx3CurrentTable.setStatus("mandatory")
_WfDsx3CurrentEntry_Object = MibTableRow
wfDsx3CurrentEntry = _WfDsx3CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1)
)
wfDsx3CurrentEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3CurrentIndex"),
)
if mibBuilder.loadTexts:
    wfDsx3CurrentEntry.setStatus("mandatory")


class _WfDsx3CurrentIndex_Type(Integer32):
    """Custom type wfDsx3CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfDsx3CurrentIndex_Type.__name__ = "Integer32"
_WfDsx3CurrentIndex_Object = MibTableColumn
wfDsx3CurrentIndex = _WfDsx3CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 1),
    _WfDsx3CurrentIndex_Type()
)
wfDsx3CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentIndex.setStatus("mandatory")
_WfDsx3CurrentPESs_Type = Gauge32
_WfDsx3CurrentPESs_Object = MibTableColumn
wfDsx3CurrentPESs = _WfDsx3CurrentPESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 2),
    _WfDsx3CurrentPESs_Type()
)
wfDsx3CurrentPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentPESs.setStatus("mandatory")
_WfDsx3CurrentPSESs_Type = Gauge32
_WfDsx3CurrentPSESs_Object = MibTableColumn
wfDsx3CurrentPSESs = _WfDsx3CurrentPSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 3),
    _WfDsx3CurrentPSESs_Type()
)
wfDsx3CurrentPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentPSESs.setStatus("mandatory")
_WfDsx3CurrentSEFSs_Type = Gauge32
_WfDsx3CurrentSEFSs_Object = MibTableColumn
wfDsx3CurrentSEFSs = _WfDsx3CurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 4),
    _WfDsx3CurrentSEFSs_Type()
)
wfDsx3CurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentSEFSs.setStatus("mandatory")
_WfDsx3CurrentUASs_Type = Gauge32
_WfDsx3CurrentUASs_Object = MibTableColumn
wfDsx3CurrentUASs = _WfDsx3CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 5),
    _WfDsx3CurrentUASs_Type()
)
wfDsx3CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentUASs.setStatus("mandatory")
_WfDsx3CurrentLCVs_Type = Gauge32
_WfDsx3CurrentLCVs_Object = MibTableColumn
wfDsx3CurrentLCVs = _WfDsx3CurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 6),
    _WfDsx3CurrentLCVs_Type()
)
wfDsx3CurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentLCVs.setStatus("mandatory")
_WfDsx3CurrentPCVs_Type = Gauge32
_WfDsx3CurrentPCVs_Object = MibTableColumn
wfDsx3CurrentPCVs = _WfDsx3CurrentPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 7),
    _WfDsx3CurrentPCVs_Type()
)
wfDsx3CurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentPCVs.setStatus("mandatory")
_WfDsx3CurrentLESs_Type = Gauge32
_WfDsx3CurrentLESs_Object = MibTableColumn
wfDsx3CurrentLESs = _WfDsx3CurrentLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 8),
    _WfDsx3CurrentLESs_Type()
)
wfDsx3CurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentLESs.setStatus("mandatory")
_WfDsx3CurrentCCVs_Type = Gauge32
_WfDsx3CurrentCCVs_Object = MibTableColumn
wfDsx3CurrentCCVs = _WfDsx3CurrentCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 9),
    _WfDsx3CurrentCCVs_Type()
)
wfDsx3CurrentCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentCCVs.setStatus("mandatory")
_WfDsx3CurrentCESs_Type = Gauge32
_WfDsx3CurrentCESs_Object = MibTableColumn
wfDsx3CurrentCESs = _WfDsx3CurrentCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 10),
    _WfDsx3CurrentCESs_Type()
)
wfDsx3CurrentCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentCESs.setStatus("mandatory")
_WfDsx3CurrentCSESs_Type = Gauge32
_WfDsx3CurrentCSESs_Object = MibTableColumn
wfDsx3CurrentCSESs = _WfDsx3CurrentCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 11),
    _WfDsx3CurrentCSESs_Type()
)
wfDsx3CurrentCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentCSESs.setStatus("mandatory")
_WfDsx3CurrentSASs_Type = Gauge32
_WfDsx3CurrentSASs_Object = MibTableColumn
wfDsx3CurrentSASs = _WfDsx3CurrentSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 12),
    _WfDsx3CurrentSASs_Type()
)
wfDsx3CurrentSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentSASs.setStatus("mandatory")
_WfDsx3CurrentAISSs_Type = Gauge32
_WfDsx3CurrentAISSs_Object = MibTableColumn
wfDsx3CurrentAISSs = _WfDsx3CurrentAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 13),
    _WfDsx3CurrentAISSs_Type()
)
wfDsx3CurrentAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentAISSs.setStatus("mandatory")
_WfDsx3CurrentFCs_Type = Gauge32
_WfDsx3CurrentFCs_Object = MibTableColumn
wfDsx3CurrentFCs = _WfDsx3CurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 14),
    _WfDsx3CurrentFCs_Type()
)
wfDsx3CurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentFCs.setStatus("mandatory")
_WfDsx3CurrentTimeElapsed_Type = Integer32
_WfDsx3CurrentTimeElapsed_Object = MibTableColumn
wfDsx3CurrentTimeElapsed = _WfDsx3CurrentTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 15),
    _WfDsx3CurrentTimeElapsed_Type()
)
wfDsx3CurrentTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentTimeElapsed.setStatus("mandatory")
_WfDsx3CurrentValidIntervals_Type = Integer32
_WfDsx3CurrentValidIntervals_Object = MibTableColumn
wfDsx3CurrentValidIntervals = _WfDsx3CurrentValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 16),
    _WfDsx3CurrentValidIntervals_Type()
)
wfDsx3CurrentValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentValidIntervals.setStatus("mandatory")


class _WfDsx3CurrentValidFlag_Type(Integer32):
    """Custom type wfDsx3CurrentValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDsx3CurrentValidFlag_Type.__name__ = "Integer32"
_WfDsx3CurrentValidFlag_Object = MibTableColumn
wfDsx3CurrentValidFlag = _WfDsx3CurrentValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 2, 1, 17),
    _WfDsx3CurrentValidFlag_Type()
)
wfDsx3CurrentValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3CurrentValidFlag.setStatus("mandatory")
_WfDsx3IntervalTable_Object = MibTable
wfDsx3IntervalTable = _WfDsx3IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3)
)
if mibBuilder.loadTexts:
    wfDsx3IntervalTable.setStatus("mandatory")
_WfDsx3IntervalEntry_Object = MibTableRow
wfDsx3IntervalEntry = _WfDsx3IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1)
)
wfDsx3IntervalEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3IntervalIndex"),
    (0, "Wellfleet-DSX3-MIB", "wfDsx3IntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDsx3IntervalEntry.setStatus("mandatory")


class _WfDsx3IntervalIndex_Type(Integer32):
    """Custom type wfDsx3IntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfDsx3IntervalIndex_Type.__name__ = "Integer32"
_WfDsx3IntervalIndex_Object = MibTableColumn
wfDsx3IntervalIndex = _WfDsx3IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 1),
    _WfDsx3IntervalIndex_Type()
)
wfDsx3IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalIndex.setStatus("mandatory")


class _WfDsx3IntervalNumber_Type(Integer32):
    """Custom type wfDsx3IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_WfDsx3IntervalNumber_Type.__name__ = "Integer32"
_WfDsx3IntervalNumber_Object = MibTableColumn
wfDsx3IntervalNumber = _WfDsx3IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 2),
    _WfDsx3IntervalNumber_Type()
)
wfDsx3IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalNumber.setStatus("mandatory")
_WfDsx3IntervalPESs_Type = Gauge32
_WfDsx3IntervalPESs_Object = MibTableColumn
wfDsx3IntervalPESs = _WfDsx3IntervalPESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 3),
    _WfDsx3IntervalPESs_Type()
)
wfDsx3IntervalPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalPESs.setStatus("mandatory")
_WfDsx3IntervalPSESs_Type = Gauge32
_WfDsx3IntervalPSESs_Object = MibTableColumn
wfDsx3IntervalPSESs = _WfDsx3IntervalPSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 4),
    _WfDsx3IntervalPSESs_Type()
)
wfDsx3IntervalPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalPSESs.setStatus("mandatory")
_WfDsx3IntervalSEFSs_Type = Gauge32
_WfDsx3IntervalSEFSs_Object = MibTableColumn
wfDsx3IntervalSEFSs = _WfDsx3IntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 5),
    _WfDsx3IntervalSEFSs_Type()
)
wfDsx3IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalSEFSs.setStatus("mandatory")
_WfDsx3IntervalUASs_Type = Gauge32
_WfDsx3IntervalUASs_Object = MibTableColumn
wfDsx3IntervalUASs = _WfDsx3IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 6),
    _WfDsx3IntervalUASs_Type()
)
wfDsx3IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalUASs.setStatus("mandatory")
_WfDsx3IntervalLCVs_Type = Gauge32
_WfDsx3IntervalLCVs_Object = MibTableColumn
wfDsx3IntervalLCVs = _WfDsx3IntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 7),
    _WfDsx3IntervalLCVs_Type()
)
wfDsx3IntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalLCVs.setStatus("mandatory")
_WfDsx3IntervalPCVs_Type = Gauge32
_WfDsx3IntervalPCVs_Object = MibTableColumn
wfDsx3IntervalPCVs = _WfDsx3IntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 8),
    _WfDsx3IntervalPCVs_Type()
)
wfDsx3IntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalPCVs.setStatus("mandatory")
_WfDsx3IntervalLESs_Type = Gauge32
_WfDsx3IntervalLESs_Object = MibTableColumn
wfDsx3IntervalLESs = _WfDsx3IntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 9),
    _WfDsx3IntervalLESs_Type()
)
wfDsx3IntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalLESs.setStatus("mandatory")
_WfDsx3IntervalCCVs_Type = Gauge32
_WfDsx3IntervalCCVs_Object = MibTableColumn
wfDsx3IntervalCCVs = _WfDsx3IntervalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 10),
    _WfDsx3IntervalCCVs_Type()
)
wfDsx3IntervalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalCCVs.setStatus("mandatory")
_WfDsx3IntervalCESs_Type = Gauge32
_WfDsx3IntervalCESs_Object = MibTableColumn
wfDsx3IntervalCESs = _WfDsx3IntervalCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 11),
    _WfDsx3IntervalCESs_Type()
)
wfDsx3IntervalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalCESs.setStatus("mandatory")
_WfDsx3IntervalCSESs_Type = Gauge32
_WfDsx3IntervalCSESs_Object = MibTableColumn
wfDsx3IntervalCSESs = _WfDsx3IntervalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 12),
    _WfDsx3IntervalCSESs_Type()
)
wfDsx3IntervalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalCSESs.setStatus("mandatory")
_WfDsx3IntervalSASs_Type = Gauge32
_WfDsx3IntervalSASs_Object = MibTableColumn
wfDsx3IntervalSASs = _WfDsx3IntervalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 13),
    _WfDsx3IntervalSASs_Type()
)
wfDsx3IntervalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalSASs.setStatus("mandatory")
_WfDsx3IntervalAISSs_Type = Gauge32
_WfDsx3IntervalAISSs_Object = MibTableColumn
wfDsx3IntervalAISSs = _WfDsx3IntervalAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 14),
    _WfDsx3IntervalAISSs_Type()
)
wfDsx3IntervalAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalAISSs.setStatus("mandatory")
_WfDsx3IntervalFCs_Type = Gauge32
_WfDsx3IntervalFCs_Object = MibTableColumn
wfDsx3IntervalFCs = _WfDsx3IntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 15),
    _WfDsx3IntervalFCs_Type()
)
wfDsx3IntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalFCs.setStatus("mandatory")


class _WfDsx3IntervalValidFlag_Type(Integer32):
    """Custom type wfDsx3IntervalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDsx3IntervalValidFlag_Type.__name__ = "Integer32"
_WfDsx3IntervalValidFlag_Object = MibTableColumn
wfDsx3IntervalValidFlag = _WfDsx3IntervalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 3, 1, 16),
    _WfDsx3IntervalValidFlag_Type()
)
wfDsx3IntervalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3IntervalValidFlag.setStatus("mandatory")
_WfDsx3TotalTable_Object = MibTable
wfDsx3TotalTable = _WfDsx3TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4)
)
if mibBuilder.loadTexts:
    wfDsx3TotalTable.setStatus("mandatory")
_WfDsx3TotalEntry_Object = MibTableRow
wfDsx3TotalEntry = _WfDsx3TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1)
)
wfDsx3TotalEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3TotalIndex"),
)
if mibBuilder.loadTexts:
    wfDsx3TotalEntry.setStatus("mandatory")


class _WfDsx3TotalIndex_Type(Integer32):
    """Custom type wfDsx3TotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfDsx3TotalIndex_Type.__name__ = "Integer32"
_WfDsx3TotalIndex_Object = MibTableColumn
wfDsx3TotalIndex = _WfDsx3TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1, 1),
    _WfDsx3TotalIndex_Type()
)
wfDsx3TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TotalIndex.setStatus("mandatory")
_WfDsx3TotalPESs_Type = Gauge32
_WfDsx3TotalPESs_Object = MibTableColumn
wfDsx3TotalPESs = _WfDsx3TotalPESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1, 2),
    _WfDsx3TotalPESs_Type()
)
wfDsx3TotalPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TotalPESs.setStatus("mandatory")
_WfDsx3TotalPSESs_Type = Gauge32
_WfDsx3TotalPSESs_Object = MibTableColumn
wfDsx3TotalPSESs = _WfDsx3TotalPSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1, 3),
    _WfDsx3TotalPSESs_Type()
)
wfDsx3TotalPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TotalPSESs.setStatus("mandatory")
_WfDsx3TotalSEFSs_Type = Gauge32
_WfDsx3TotalSEFSs_Object = MibTableColumn
wfDsx3TotalSEFSs = _WfDsx3TotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1, 4),
    _WfDsx3TotalSEFSs_Type()
)
wfDsx3TotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TotalSEFSs.setStatus("mandatory")
_WfDsx3TotalUASs_Type = Gauge32
_WfDsx3TotalUASs_Object = MibTableColumn
wfDsx3TotalUASs = _WfDsx3TotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1, 5),
    _WfDsx3TotalUASs_Type()
)
wfDsx3TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TotalUASs.setStatus("mandatory")
_WfDsx3TotalLCVs_Type = Gauge32
_WfDsx3TotalLCVs_Object = MibTableColumn
wfDsx3TotalLCVs = _WfDsx3TotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1, 6),
    _WfDsx3TotalLCVs_Type()
)
wfDsx3TotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TotalLCVs.setStatus("mandatory")
_WfDsx3TotalPCVs_Type = Gauge32
_WfDsx3TotalPCVs_Object = MibTableColumn
wfDsx3TotalPCVs = _WfDsx3TotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1, 7),
    _WfDsx3TotalPCVs_Type()
)
wfDsx3TotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TotalPCVs.setStatus("mandatory")
_WfDsx3TotalLESs_Type = Gauge32
_WfDsx3TotalLESs_Object = MibTableColumn
wfDsx3TotalLESs = _WfDsx3TotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1, 8),
    _WfDsx3TotalLESs_Type()
)
wfDsx3TotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TotalLESs.setStatus("mandatory")
_WfDsx3TotalCCVs_Type = Gauge32
_WfDsx3TotalCCVs_Object = MibTableColumn
wfDsx3TotalCCVs = _WfDsx3TotalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1, 9),
    _WfDsx3TotalCCVs_Type()
)
wfDsx3TotalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TotalCCVs.setStatus("mandatory")
_WfDsx3TotalCESs_Type = Gauge32
_WfDsx3TotalCESs_Object = MibTableColumn
wfDsx3TotalCESs = _WfDsx3TotalCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1, 10),
    _WfDsx3TotalCESs_Type()
)
wfDsx3TotalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TotalCESs.setStatus("mandatory")
_WfDsx3TotalCSESs_Type = Gauge32
_WfDsx3TotalCSESs_Object = MibTableColumn
wfDsx3TotalCSESs = _WfDsx3TotalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1, 11),
    _WfDsx3TotalCSESs_Type()
)
wfDsx3TotalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TotalCSESs.setStatus("mandatory")
_WfDsx3TotalSASs_Type = Gauge32
_WfDsx3TotalSASs_Object = MibTableColumn
wfDsx3TotalSASs = _WfDsx3TotalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1, 12),
    _WfDsx3TotalSASs_Type()
)
wfDsx3TotalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TotalSASs.setStatus("mandatory")
_WfDsx3TotalAISSs_Type = Gauge32
_WfDsx3TotalAISSs_Object = MibTableColumn
wfDsx3TotalAISSs = _WfDsx3TotalAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1, 13),
    _WfDsx3TotalAISSs_Type()
)
wfDsx3TotalAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TotalAISSs.setStatus("mandatory")
_WfDsx3TotalFCs_Type = Gauge32
_WfDsx3TotalFCs_Object = MibTableColumn
wfDsx3TotalFCs = _WfDsx3TotalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1, 14),
    _WfDsx3TotalFCs_Type()
)
wfDsx3TotalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TotalFCs.setStatus("mandatory")


class _WfDsx3TotalValidFlag_Type(Integer32):
    """Custom type wfDsx3TotalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDsx3TotalValidFlag_Type.__name__ = "Integer32"
_WfDsx3TotalValidFlag_Object = MibTableColumn
wfDsx3TotalValidFlag = _WfDsx3TotalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 4, 1, 15),
    _WfDsx3TotalValidFlag_Type()
)
wfDsx3TotalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3TotalValidFlag.setStatus("mandatory")
_WfDsx3FarEndConfigTable_Object = MibTable
wfDsx3FarEndConfigTable = _WfDsx3FarEndConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 5)
)
if mibBuilder.loadTexts:
    wfDsx3FarEndConfigTable.setStatus("mandatory")
_WfDsx3FarEndConfigEntry_Object = MibTableRow
wfDsx3FarEndConfigEntry = _WfDsx3FarEndConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 5, 1)
)
wfDsx3FarEndConfigEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3FarEndLineIndex"),
)
if mibBuilder.loadTexts:
    wfDsx3FarEndConfigEntry.setStatus("mandatory")


class _WfDsx3FarEndLineIndex_Type(Integer32):
    """Custom type wfDsx3FarEndLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfDsx3FarEndLineIndex_Type.__name__ = "Integer32"
_WfDsx3FarEndLineIndex_Object = MibTableColumn
wfDsx3FarEndLineIndex = _WfDsx3FarEndLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 5, 1, 1),
    _WfDsx3FarEndLineIndex_Type()
)
wfDsx3FarEndLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndLineIndex.setStatus("mandatory")
_WfDsx3FarEndEquipCode_Type = DisplayString
_WfDsx3FarEndEquipCode_Object = MibTableColumn
wfDsx3FarEndEquipCode = _WfDsx3FarEndEquipCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 5, 1, 2),
    _WfDsx3FarEndEquipCode_Type()
)
wfDsx3FarEndEquipCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndEquipCode.setStatus("mandatory")
_WfDsx3FarEndLocationIDCode_Type = DisplayString
_WfDsx3FarEndLocationIDCode_Object = MibTableColumn
wfDsx3FarEndLocationIDCode = _WfDsx3FarEndLocationIDCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 5, 1, 3),
    _WfDsx3FarEndLocationIDCode_Type()
)
wfDsx3FarEndLocationIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndLocationIDCode.setStatus("mandatory")
_WfDsx3FarEndFrameIDCode_Type = DisplayString
_WfDsx3FarEndFrameIDCode_Object = MibTableColumn
wfDsx3FarEndFrameIDCode = _WfDsx3FarEndFrameIDCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 5, 1, 4),
    _WfDsx3FarEndFrameIDCode_Type()
)
wfDsx3FarEndFrameIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndFrameIDCode.setStatus("mandatory")
_WfDsx3FarEndUnitCode_Type = DisplayString
_WfDsx3FarEndUnitCode_Object = MibTableColumn
wfDsx3FarEndUnitCode = _WfDsx3FarEndUnitCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 5, 1, 5),
    _WfDsx3FarEndUnitCode_Type()
)
wfDsx3FarEndUnitCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndUnitCode.setStatus("mandatory")
_WfDsx3FarEndFacilityIDCode_Type = DisplayString
_WfDsx3FarEndFacilityIDCode_Object = MibTableColumn
wfDsx3FarEndFacilityIDCode = _WfDsx3FarEndFacilityIDCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 5, 1, 6),
    _WfDsx3FarEndFacilityIDCode_Type()
)
wfDsx3FarEndFacilityIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndFacilityIDCode.setStatus("mandatory")
_WfDsx3FarEndCurrentTable_Object = MibTable
wfDsx3FarEndCurrentTable = _WfDsx3FarEndCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 6)
)
if mibBuilder.loadTexts:
    wfDsx3FarEndCurrentTable.setStatus("mandatory")
_WfDsx3FarEndCurrentEntry_Object = MibTableRow
wfDsx3FarEndCurrentEntry = _WfDsx3FarEndCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 6, 1)
)
wfDsx3FarEndCurrentEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3FarEndCurrentIndex"),
)
if mibBuilder.loadTexts:
    wfDsx3FarEndCurrentEntry.setStatus("mandatory")


class _WfDsx3FarEndCurrentIndex_Type(Integer32):
    """Custom type wfDsx3FarEndCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDsx3FarEndCurrentIndex_Type.__name__ = "Integer32"
_WfDsx3FarEndCurrentIndex_Object = MibTableColumn
wfDsx3FarEndCurrentIndex = _WfDsx3FarEndCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 6, 1, 1),
    _WfDsx3FarEndCurrentIndex_Type()
)
wfDsx3FarEndCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndCurrentIndex.setStatus("mandatory")
_WfDsx3FarEndTimeElapsed_Type = Integer32
_WfDsx3FarEndTimeElapsed_Object = MibTableColumn
wfDsx3FarEndTimeElapsed = _WfDsx3FarEndTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 6, 1, 2),
    _WfDsx3FarEndTimeElapsed_Type()
)
wfDsx3FarEndTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndTimeElapsed.setStatus("mandatory")
_WfDsx3FarEndValidIntervals_Type = Integer32
_WfDsx3FarEndValidIntervals_Object = MibTableColumn
wfDsx3FarEndValidIntervals = _WfDsx3FarEndValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 6, 1, 3),
    _WfDsx3FarEndValidIntervals_Type()
)
wfDsx3FarEndValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndValidIntervals.setStatus("mandatory")
_WfDsx3FarEndCurrentCESs_Type = Gauge32
_WfDsx3FarEndCurrentCESs_Object = MibTableColumn
wfDsx3FarEndCurrentCESs = _WfDsx3FarEndCurrentCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 6, 1, 4),
    _WfDsx3FarEndCurrentCESs_Type()
)
wfDsx3FarEndCurrentCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndCurrentCESs.setStatus("mandatory")
_WfDsx3FarEndCurrentCSESs_Type = Gauge32
_WfDsx3FarEndCurrentCSESs_Object = MibTableColumn
wfDsx3FarEndCurrentCSESs = _WfDsx3FarEndCurrentCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 6, 1, 5),
    _WfDsx3FarEndCurrentCSESs_Type()
)
wfDsx3FarEndCurrentCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndCurrentCSESs.setStatus("mandatory")
_WfDsx3FarEndCurrentCCVs_Type = Gauge32
_WfDsx3FarEndCurrentCCVs_Object = MibTableColumn
wfDsx3FarEndCurrentCCVs = _WfDsx3FarEndCurrentCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 6, 1, 6),
    _WfDsx3FarEndCurrentCCVs_Type()
)
wfDsx3FarEndCurrentCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndCurrentCCVs.setStatus("mandatory")
_WfDsx3FarEndCurrentUASs_Type = Gauge32
_WfDsx3FarEndCurrentUASs_Object = MibTableColumn
wfDsx3FarEndCurrentUASs = _WfDsx3FarEndCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 6, 1, 7),
    _WfDsx3FarEndCurrentUASs_Type()
)
wfDsx3FarEndCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndCurrentUASs.setStatus("mandatory")
_WfDsx3FarEndCurrentSASs_Type = Gauge32
_WfDsx3FarEndCurrentSASs_Object = MibTableColumn
wfDsx3FarEndCurrentSASs = _WfDsx3FarEndCurrentSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 6, 1, 8),
    _WfDsx3FarEndCurrentSASs_Type()
)
wfDsx3FarEndCurrentSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndCurrentSASs.setStatus("mandatory")
_WfDsx3FarEndCurrentFCs_Type = Gauge32
_WfDsx3FarEndCurrentFCs_Object = MibTableColumn
wfDsx3FarEndCurrentFCs = _WfDsx3FarEndCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 6, 1, 9),
    _WfDsx3FarEndCurrentFCs_Type()
)
wfDsx3FarEndCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndCurrentFCs.setStatus("mandatory")


class _WfDsx3FarEndCurrentValidFlag_Type(Integer32):
    """Custom type wfDsx3FarEndCurrentValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDsx3FarEndCurrentValidFlag_Type.__name__ = "Integer32"
_WfDsx3FarEndCurrentValidFlag_Object = MibTableColumn
wfDsx3FarEndCurrentValidFlag = _WfDsx3FarEndCurrentValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 6, 1, 10),
    _WfDsx3FarEndCurrentValidFlag_Type()
)
wfDsx3FarEndCurrentValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndCurrentValidFlag.setStatus("mandatory")
_WfDsx3FarEndIntervalTable_Object = MibTable
wfDsx3FarEndIntervalTable = _WfDsx3FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 7)
)
if mibBuilder.loadTexts:
    wfDsx3FarEndIntervalTable.setStatus("mandatory")
_WfDsx3FarEndIntervalEntry_Object = MibTableRow
wfDsx3FarEndIntervalEntry = _WfDsx3FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 7, 1)
)
wfDsx3FarEndIntervalEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3FarEndIntervalIndex"),
    (0, "Wellfleet-DSX3-MIB", "wfDsx3FarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDsx3FarEndIntervalEntry.setStatus("mandatory")


class _WfDsx3FarEndIntervalIndex_Type(Integer32):
    """Custom type wfDsx3FarEndIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfDsx3FarEndIntervalIndex_Type.__name__ = "Integer32"
_WfDsx3FarEndIntervalIndex_Object = MibTableColumn
wfDsx3FarEndIntervalIndex = _WfDsx3FarEndIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 7, 1, 1),
    _WfDsx3FarEndIntervalIndex_Type()
)
wfDsx3FarEndIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndIntervalIndex.setStatus("mandatory")


class _WfDsx3FarEndIntervalNumber_Type(Integer32):
    """Custom type wfDsx3FarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_WfDsx3FarEndIntervalNumber_Type.__name__ = "Integer32"
_WfDsx3FarEndIntervalNumber_Object = MibTableColumn
wfDsx3FarEndIntervalNumber = _WfDsx3FarEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 7, 1, 2),
    _WfDsx3FarEndIntervalNumber_Type()
)
wfDsx3FarEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndIntervalNumber.setStatus("mandatory")
_WfDsx3FarEndIntervalCESs_Type = Gauge32
_WfDsx3FarEndIntervalCESs_Object = MibTableColumn
wfDsx3FarEndIntervalCESs = _WfDsx3FarEndIntervalCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 7, 1, 3),
    _WfDsx3FarEndIntervalCESs_Type()
)
wfDsx3FarEndIntervalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndIntervalCESs.setStatus("mandatory")
_WfDsx3FarEndIntervalCSESs_Type = Gauge32
_WfDsx3FarEndIntervalCSESs_Object = MibTableColumn
wfDsx3FarEndIntervalCSESs = _WfDsx3FarEndIntervalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 7, 1, 4),
    _WfDsx3FarEndIntervalCSESs_Type()
)
wfDsx3FarEndIntervalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndIntervalCSESs.setStatus("mandatory")
_WfDsx3FarEndIntervalCCVs_Type = Gauge32
_WfDsx3FarEndIntervalCCVs_Object = MibTableColumn
wfDsx3FarEndIntervalCCVs = _WfDsx3FarEndIntervalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 7, 1, 5),
    _WfDsx3FarEndIntervalCCVs_Type()
)
wfDsx3FarEndIntervalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndIntervalCCVs.setStatus("mandatory")
_WfDsx3FarEndIntervalUASs_Type = Gauge32
_WfDsx3FarEndIntervalUASs_Object = MibTableColumn
wfDsx3FarEndIntervalUASs = _WfDsx3FarEndIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 7, 1, 6),
    _WfDsx3FarEndIntervalUASs_Type()
)
wfDsx3FarEndIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndIntervalUASs.setStatus("mandatory")
_WfDsx3FarEndIntervalSASs_Type = Gauge32
_WfDsx3FarEndIntervalSASs_Object = MibTableColumn
wfDsx3FarEndIntervalSASs = _WfDsx3FarEndIntervalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 7, 1, 7),
    _WfDsx3FarEndIntervalSASs_Type()
)
wfDsx3FarEndIntervalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndIntervalSASs.setStatus("mandatory")
_WfDsx3FarEndIntervalFCs_Type = Gauge32
_WfDsx3FarEndIntervalFCs_Object = MibTableColumn
wfDsx3FarEndIntervalFCs = _WfDsx3FarEndIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 7, 1, 8),
    _WfDsx3FarEndIntervalFCs_Type()
)
wfDsx3FarEndIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndIntervalFCs.setStatus("mandatory")


class _WfDsx3FarEndIntervalValidFlag_Type(Integer32):
    """Custom type wfDsx3FarEndIntervalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDsx3FarEndIntervalValidFlag_Type.__name__ = "Integer32"
_WfDsx3FarEndIntervalValidFlag_Object = MibTableColumn
wfDsx3FarEndIntervalValidFlag = _WfDsx3FarEndIntervalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 7, 1, 9),
    _WfDsx3FarEndIntervalValidFlag_Type()
)
wfDsx3FarEndIntervalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndIntervalValidFlag.setStatus("mandatory")
_WfDsx3FarEndTotalTable_Object = MibTable
wfDsx3FarEndTotalTable = _WfDsx3FarEndTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 8)
)
if mibBuilder.loadTexts:
    wfDsx3FarEndTotalTable.setStatus("mandatory")
_WfDsx3FarEndTotalEntry_Object = MibTableRow
wfDsx3FarEndTotalEntry = _WfDsx3FarEndTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 8, 1)
)
wfDsx3FarEndTotalEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3FarEndTotalIndex"),
)
if mibBuilder.loadTexts:
    wfDsx3FarEndTotalEntry.setStatus("mandatory")


class _WfDsx3FarEndTotalIndex_Type(Integer32):
    """Custom type wfDsx3FarEndTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfDsx3FarEndTotalIndex_Type.__name__ = "Integer32"
_WfDsx3FarEndTotalIndex_Object = MibTableColumn
wfDsx3FarEndTotalIndex = _WfDsx3FarEndTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 8, 1, 1),
    _WfDsx3FarEndTotalIndex_Type()
)
wfDsx3FarEndTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndTotalIndex.setStatus("mandatory")
_WfDsx3FarEndTotalCESs_Type = Gauge32
_WfDsx3FarEndTotalCESs_Object = MibTableColumn
wfDsx3FarEndTotalCESs = _WfDsx3FarEndTotalCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 8, 1, 2),
    _WfDsx3FarEndTotalCESs_Type()
)
wfDsx3FarEndTotalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndTotalCESs.setStatus("mandatory")
_WfDsx3FarEndTotalCSESs_Type = Gauge32
_WfDsx3FarEndTotalCSESs_Object = MibTableColumn
wfDsx3FarEndTotalCSESs = _WfDsx3FarEndTotalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 8, 1, 3),
    _WfDsx3FarEndTotalCSESs_Type()
)
wfDsx3FarEndTotalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndTotalCSESs.setStatus("mandatory")
_WfDsx3FarEndTotalCCVs_Type = Gauge32
_WfDsx3FarEndTotalCCVs_Object = MibTableColumn
wfDsx3FarEndTotalCCVs = _WfDsx3FarEndTotalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 8, 1, 4),
    _WfDsx3FarEndTotalCCVs_Type()
)
wfDsx3FarEndTotalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndTotalCCVs.setStatus("mandatory")
_WfDsx3FarEndTotalUASs_Type = Gauge32
_WfDsx3FarEndTotalUASs_Object = MibTableColumn
wfDsx3FarEndTotalUASs = _WfDsx3FarEndTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 8, 1, 5),
    _WfDsx3FarEndTotalUASs_Type()
)
wfDsx3FarEndTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndTotalUASs.setStatus("mandatory")
_WfDsx3FarEndTotalSASs_Type = Gauge32
_WfDsx3FarEndTotalSASs_Object = MibTableColumn
wfDsx3FarEndTotalSASs = _WfDsx3FarEndTotalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 8, 1, 6),
    _WfDsx3FarEndTotalSASs_Type()
)
wfDsx3FarEndTotalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndTotalSASs.setStatus("mandatory")
_WfDsx3FarEndTotalFCs_Type = Gauge32
_WfDsx3FarEndTotalFCs_Object = MibTableColumn
wfDsx3FarEndTotalFCs = _WfDsx3FarEndTotalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 8, 1, 7),
    _WfDsx3FarEndTotalFCs_Type()
)
wfDsx3FarEndTotalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndTotalFCs.setStatus("mandatory")


class _WfDsx3FarEndTotalValidFlag_Type(Integer32):
    """Custom type wfDsx3FarEndTotalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDsx3FarEndTotalValidFlag_Type.__name__ = "Integer32"
_WfDsx3FarEndTotalValidFlag_Object = MibTableColumn
wfDsx3FarEndTotalValidFlag = _WfDsx3FarEndTotalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 8, 1, 8),
    _WfDsx3FarEndTotalValidFlag_Type()
)
wfDsx3FarEndTotalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndTotalValidFlag.setStatus("mandatory")
_WfAtmInterfaceDs3PlcpTable_Object = MibTable
wfAtmInterfaceDs3PlcpTable = _WfAtmInterfaceDs3PlcpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 9)
)
if mibBuilder.loadTexts:
    wfAtmInterfaceDs3PlcpTable.setStatus("mandatory")
_WfAtmInterfaceDs3PlcpEntry_Object = MibTableRow
wfAtmInterfaceDs3PlcpEntry = _WfAtmInterfaceDs3PlcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 9, 1)
)
wfAtmInterfaceDs3PlcpEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfAtmInterfaceDs3PlcpIndex"),
)
if mibBuilder.loadTexts:
    wfAtmInterfaceDs3PlcpEntry.setStatus("mandatory")


class _WfAtmInterfaceDs3PlcpIndex_Type(Integer32):
    """Custom type wfAtmInterfaceDs3PlcpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfAtmInterfaceDs3PlcpIndex_Type.__name__ = "Integer32"
_WfAtmInterfaceDs3PlcpIndex_Object = MibTableColumn
wfAtmInterfaceDs3PlcpIndex = _WfAtmInterfaceDs3PlcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 9, 1, 1),
    _WfAtmInterfaceDs3PlcpIndex_Type()
)
wfAtmInterfaceDs3PlcpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceDs3PlcpIndex.setStatus("mandatory")
_WfAtmInterfaceDs3PlcpSEFSs_Type = Gauge32
_WfAtmInterfaceDs3PlcpSEFSs_Object = MibTableColumn
wfAtmInterfaceDs3PlcpSEFSs = _WfAtmInterfaceDs3PlcpSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 9, 1, 2),
    _WfAtmInterfaceDs3PlcpSEFSs_Type()
)
wfAtmInterfaceDs3PlcpSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceDs3PlcpSEFSs.setStatus("mandatory")


class _WfAtmInterfaceDs3PlcpAlarmState_Type(Integer32):
    """Custom type wfAtmInterfaceDs3PlcpAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("farendalarm", 2),
          ("lof", 3),
          ("noalarm", 1))
    )


_WfAtmInterfaceDs3PlcpAlarmState_Type.__name__ = "Integer32"
_WfAtmInterfaceDs3PlcpAlarmState_Object = MibTableColumn
wfAtmInterfaceDs3PlcpAlarmState = _WfAtmInterfaceDs3PlcpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 9, 1, 3),
    _WfAtmInterfaceDs3PlcpAlarmState_Type()
)
wfAtmInterfaceDs3PlcpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceDs3PlcpAlarmState.setStatus("mandatory")
_WfAtmInterfaceDs3PlcpUASs_Type = Gauge32
_WfAtmInterfaceDs3PlcpUASs_Object = MibTableColumn
wfAtmInterfaceDs3PlcpUASs = _WfAtmInterfaceDs3PlcpUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 9, 1, 4),
    _WfAtmInterfaceDs3PlcpUASs_Type()
)
wfAtmInterfaceDs3PlcpUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmInterfaceDs3PlcpUASs.setStatus("mandatory")
_WfDsx3DayCurrentTable_Object = MibTable
wfDsx3DayCurrentTable = _WfDsx3DayCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11)
)
if mibBuilder.loadTexts:
    wfDsx3DayCurrentTable.setStatus("mandatory")
_WfDsx3DayCurrentEntry_Object = MibTableRow
wfDsx3DayCurrentEntry = _WfDsx3DayCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1)
)
wfDsx3DayCurrentEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3DayCurrentIndex"),
)
if mibBuilder.loadTexts:
    wfDsx3DayCurrentEntry.setStatus("mandatory")


class _WfDsx3DayCurrentIndex_Type(Integer32):
    """Custom type wfDsx3DayCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfDsx3DayCurrentIndex_Type.__name__ = "Integer32"
_WfDsx3DayCurrentIndex_Object = MibTableColumn
wfDsx3DayCurrentIndex = _WfDsx3DayCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 1),
    _WfDsx3DayCurrentIndex_Type()
)
wfDsx3DayCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentIndex.setStatus("mandatory")
_WfDsx3DayCurrentPESs_Type = Gauge32
_WfDsx3DayCurrentPESs_Object = MibTableColumn
wfDsx3DayCurrentPESs = _WfDsx3DayCurrentPESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 2),
    _WfDsx3DayCurrentPESs_Type()
)
wfDsx3DayCurrentPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentPESs.setStatus("mandatory")
_WfDsx3DayCurrentPSESs_Type = Gauge32
_WfDsx3DayCurrentPSESs_Object = MibTableColumn
wfDsx3DayCurrentPSESs = _WfDsx3DayCurrentPSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 3),
    _WfDsx3DayCurrentPSESs_Type()
)
wfDsx3DayCurrentPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentPSESs.setStatus("mandatory")
_WfDsx3DayCurrentSEFSs_Type = Gauge32
_WfDsx3DayCurrentSEFSs_Object = MibTableColumn
wfDsx3DayCurrentSEFSs = _WfDsx3DayCurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 4),
    _WfDsx3DayCurrentSEFSs_Type()
)
wfDsx3DayCurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentSEFSs.setStatus("mandatory")
_WfDsx3DayCurrentUASs_Type = Gauge32
_WfDsx3DayCurrentUASs_Object = MibTableColumn
wfDsx3DayCurrentUASs = _WfDsx3DayCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 5),
    _WfDsx3DayCurrentUASs_Type()
)
wfDsx3DayCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentUASs.setStatus("mandatory")
_WfDsx3DayCurrentLCVs_Type = Gauge32
_WfDsx3DayCurrentLCVs_Object = MibTableColumn
wfDsx3DayCurrentLCVs = _WfDsx3DayCurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 6),
    _WfDsx3DayCurrentLCVs_Type()
)
wfDsx3DayCurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentLCVs.setStatus("mandatory")
_WfDsx3DayCurrentPCVs_Type = Gauge32
_WfDsx3DayCurrentPCVs_Object = MibTableColumn
wfDsx3DayCurrentPCVs = _WfDsx3DayCurrentPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 7),
    _WfDsx3DayCurrentPCVs_Type()
)
wfDsx3DayCurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentPCVs.setStatus("mandatory")
_WfDsx3DayCurrentLESs_Type = Gauge32
_WfDsx3DayCurrentLESs_Object = MibTableColumn
wfDsx3DayCurrentLESs = _WfDsx3DayCurrentLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 8),
    _WfDsx3DayCurrentLESs_Type()
)
wfDsx3DayCurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentLESs.setStatus("mandatory")
_WfDsx3DayCurrentCCVs_Type = Gauge32
_WfDsx3DayCurrentCCVs_Object = MibTableColumn
wfDsx3DayCurrentCCVs = _WfDsx3DayCurrentCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 9),
    _WfDsx3DayCurrentCCVs_Type()
)
wfDsx3DayCurrentCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentCCVs.setStatus("mandatory")
_WfDsx3DayCurrentCESs_Type = Gauge32
_WfDsx3DayCurrentCESs_Object = MibTableColumn
wfDsx3DayCurrentCESs = _WfDsx3DayCurrentCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 10),
    _WfDsx3DayCurrentCESs_Type()
)
wfDsx3DayCurrentCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentCESs.setStatus("mandatory")
_WfDsx3DayCurrentCSESs_Type = Gauge32
_WfDsx3DayCurrentCSESs_Object = MibTableColumn
wfDsx3DayCurrentCSESs = _WfDsx3DayCurrentCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 11),
    _WfDsx3DayCurrentCSESs_Type()
)
wfDsx3DayCurrentCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentCSESs.setStatus("mandatory")
_WfDsx3DayCurrentSASs_Type = Gauge32
_WfDsx3DayCurrentSASs_Object = MibTableColumn
wfDsx3DayCurrentSASs = _WfDsx3DayCurrentSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 12),
    _WfDsx3DayCurrentSASs_Type()
)
wfDsx3DayCurrentSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentSASs.setStatus("mandatory")
_WfDsx3DayCurrentAISSs_Type = Gauge32
_WfDsx3DayCurrentAISSs_Object = MibTableColumn
wfDsx3DayCurrentAISSs = _WfDsx3DayCurrentAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 13),
    _WfDsx3DayCurrentAISSs_Type()
)
wfDsx3DayCurrentAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentAISSs.setStatus("mandatory")
_WfDsx3DayCurrentFCs_Type = Gauge32
_WfDsx3DayCurrentFCs_Object = MibTableColumn
wfDsx3DayCurrentFCs = _WfDsx3DayCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 14),
    _WfDsx3DayCurrentFCs_Type()
)
wfDsx3DayCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentFCs.setStatus("mandatory")
_WfDsx3DayCurrentTimeElapsed_Type = Integer32
_WfDsx3DayCurrentTimeElapsed_Object = MibTableColumn
wfDsx3DayCurrentTimeElapsed = _WfDsx3DayCurrentTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 15),
    _WfDsx3DayCurrentTimeElapsed_Type()
)
wfDsx3DayCurrentTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentTimeElapsed.setStatus("mandatory")
_WfDsx3DayCurrentValidIntervals_Type = Integer32
_WfDsx3DayCurrentValidIntervals_Object = MibTableColumn
wfDsx3DayCurrentValidIntervals = _WfDsx3DayCurrentValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 16),
    _WfDsx3DayCurrentValidIntervals_Type()
)
wfDsx3DayCurrentValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentValidIntervals.setStatus("mandatory")


class _WfDsx3DayCurrentValidFlag_Type(Integer32):
    """Custom type wfDsx3DayCurrentValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDsx3DayCurrentValidFlag_Type.__name__ = "Integer32"
_WfDsx3DayCurrentValidFlag_Object = MibTableColumn
wfDsx3DayCurrentValidFlag = _WfDsx3DayCurrentValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 11, 1, 17),
    _WfDsx3DayCurrentValidFlag_Type()
)
wfDsx3DayCurrentValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayCurrentValidFlag.setStatus("mandatory")
_WfDsx3DayIntervalTable_Object = MibTable
wfDsx3DayIntervalTable = _WfDsx3DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12)
)
if mibBuilder.loadTexts:
    wfDsx3DayIntervalTable.setStatus("mandatory")
_WfDsx3DayIntervalEntry_Object = MibTableRow
wfDsx3DayIntervalEntry = _WfDsx3DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1)
)
wfDsx3DayIntervalEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3DayIntervalIndex"),
    (0, "Wellfleet-DSX3-MIB", "wfDsx3DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDsx3DayIntervalEntry.setStatus("mandatory")


class _WfDsx3DayIntervalIndex_Type(Integer32):
    """Custom type wfDsx3DayIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfDsx3DayIntervalIndex_Type.__name__ = "Integer32"
_WfDsx3DayIntervalIndex_Object = MibTableColumn
wfDsx3DayIntervalIndex = _WfDsx3DayIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 1),
    _WfDsx3DayIntervalIndex_Type()
)
wfDsx3DayIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalIndex.setStatus("mandatory")


class _WfDsx3DayIntervalNumber_Type(Integer32):
    """Custom type wfDsx3DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_WfDsx3DayIntervalNumber_Type.__name__ = "Integer32"
_WfDsx3DayIntervalNumber_Object = MibTableColumn
wfDsx3DayIntervalNumber = _WfDsx3DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 2),
    _WfDsx3DayIntervalNumber_Type()
)
wfDsx3DayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalNumber.setStatus("mandatory")
_WfDsx3DayIntervalPESs_Type = Gauge32
_WfDsx3DayIntervalPESs_Object = MibTableColumn
wfDsx3DayIntervalPESs = _WfDsx3DayIntervalPESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 3),
    _WfDsx3DayIntervalPESs_Type()
)
wfDsx3DayIntervalPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalPESs.setStatus("mandatory")
_WfDsx3DayIntervalPSESs_Type = Gauge32
_WfDsx3DayIntervalPSESs_Object = MibTableColumn
wfDsx3DayIntervalPSESs = _WfDsx3DayIntervalPSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 4),
    _WfDsx3DayIntervalPSESs_Type()
)
wfDsx3DayIntervalPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalPSESs.setStatus("mandatory")
_WfDsx3DayIntervalSEFSs_Type = Gauge32
_WfDsx3DayIntervalSEFSs_Object = MibTableColumn
wfDsx3DayIntervalSEFSs = _WfDsx3DayIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 5),
    _WfDsx3DayIntervalSEFSs_Type()
)
wfDsx3DayIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalSEFSs.setStatus("mandatory")
_WfDsx3DayIntervalUASs_Type = Gauge32
_WfDsx3DayIntervalUASs_Object = MibTableColumn
wfDsx3DayIntervalUASs = _WfDsx3DayIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 6),
    _WfDsx3DayIntervalUASs_Type()
)
wfDsx3DayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalUASs.setStatus("mandatory")
_WfDsx3DayIntervalLCVs_Type = Gauge32
_WfDsx3DayIntervalLCVs_Object = MibTableColumn
wfDsx3DayIntervalLCVs = _WfDsx3DayIntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 7),
    _WfDsx3DayIntervalLCVs_Type()
)
wfDsx3DayIntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalLCVs.setStatus("mandatory")
_WfDsx3DayIntervalPCVs_Type = Gauge32
_WfDsx3DayIntervalPCVs_Object = MibTableColumn
wfDsx3DayIntervalPCVs = _WfDsx3DayIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 8),
    _WfDsx3DayIntervalPCVs_Type()
)
wfDsx3DayIntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalPCVs.setStatus("mandatory")
_WfDsx3DayIntervalLESs_Type = Gauge32
_WfDsx3DayIntervalLESs_Object = MibTableColumn
wfDsx3DayIntervalLESs = _WfDsx3DayIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 9),
    _WfDsx3DayIntervalLESs_Type()
)
wfDsx3DayIntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalLESs.setStatus("mandatory")
_WfDsx3DayIntervalCCVs_Type = Gauge32
_WfDsx3DayIntervalCCVs_Object = MibTableColumn
wfDsx3DayIntervalCCVs = _WfDsx3DayIntervalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 10),
    _WfDsx3DayIntervalCCVs_Type()
)
wfDsx3DayIntervalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalCCVs.setStatus("mandatory")
_WfDsx3DayIntervalCESs_Type = Gauge32
_WfDsx3DayIntervalCESs_Object = MibTableColumn
wfDsx3DayIntervalCESs = _WfDsx3DayIntervalCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 11),
    _WfDsx3DayIntervalCESs_Type()
)
wfDsx3DayIntervalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalCESs.setStatus("mandatory")
_WfDsx3DayIntervalCSESs_Type = Gauge32
_WfDsx3DayIntervalCSESs_Object = MibTableColumn
wfDsx3DayIntervalCSESs = _WfDsx3DayIntervalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 12),
    _WfDsx3DayIntervalCSESs_Type()
)
wfDsx3DayIntervalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalCSESs.setStatus("mandatory")
_WfDsx3DayIntervalSASs_Type = Gauge32
_WfDsx3DayIntervalSASs_Object = MibTableColumn
wfDsx3DayIntervalSASs = _WfDsx3DayIntervalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 13),
    _WfDsx3DayIntervalSASs_Type()
)
wfDsx3DayIntervalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalSASs.setStatus("mandatory")
_WfDsx3DayIntervalAISSs_Type = Gauge32
_WfDsx3DayIntervalAISSs_Object = MibTableColumn
wfDsx3DayIntervalAISSs = _WfDsx3DayIntervalAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 14),
    _WfDsx3DayIntervalAISSs_Type()
)
wfDsx3DayIntervalAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalAISSs.setStatus("mandatory")
_WfDsx3DayIntervalFCs_Type = Gauge32
_WfDsx3DayIntervalFCs_Object = MibTableColumn
wfDsx3DayIntervalFCs = _WfDsx3DayIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 15),
    _WfDsx3DayIntervalFCs_Type()
)
wfDsx3DayIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalFCs.setStatus("mandatory")


class _WfDsx3DayIntervalValidFlag_Type(Integer32):
    """Custom type wfDsx3DayIntervalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDsx3DayIntervalValidFlag_Type.__name__ = "Integer32"
_WfDsx3DayIntervalValidFlag_Object = MibTableColumn
wfDsx3DayIntervalValidFlag = _WfDsx3DayIntervalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 12, 1, 16),
    _WfDsx3DayIntervalValidFlag_Type()
)
wfDsx3DayIntervalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayIntervalValidFlag.setStatus("mandatory")
_WfDsx3DayTotalTable_Object = MibTable
wfDsx3DayTotalTable = _WfDsx3DayTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13)
)
if mibBuilder.loadTexts:
    wfDsx3DayTotalTable.setStatus("mandatory")
_WfDsx3DayTotalEntry_Object = MibTableRow
wfDsx3DayTotalEntry = _WfDsx3DayTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1)
)
wfDsx3DayTotalEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3DayTotalIndex"),
)
if mibBuilder.loadTexts:
    wfDsx3DayTotalEntry.setStatus("mandatory")


class _WfDsx3DayTotalIndex_Type(Integer32):
    """Custom type wfDsx3DayTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfDsx3DayTotalIndex_Type.__name__ = "Integer32"
_WfDsx3DayTotalIndex_Object = MibTableColumn
wfDsx3DayTotalIndex = _WfDsx3DayTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1, 1),
    _WfDsx3DayTotalIndex_Type()
)
wfDsx3DayTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayTotalIndex.setStatus("mandatory")
_WfDsx3DayTotalPESs_Type = Gauge32
_WfDsx3DayTotalPESs_Object = MibTableColumn
wfDsx3DayTotalPESs = _WfDsx3DayTotalPESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1, 2),
    _WfDsx3DayTotalPESs_Type()
)
wfDsx3DayTotalPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayTotalPESs.setStatus("mandatory")
_WfDsx3DayTotalPSESs_Type = Gauge32
_WfDsx3DayTotalPSESs_Object = MibTableColumn
wfDsx3DayTotalPSESs = _WfDsx3DayTotalPSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1, 3),
    _WfDsx3DayTotalPSESs_Type()
)
wfDsx3DayTotalPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayTotalPSESs.setStatus("mandatory")
_WfDsx3DayTotalSEFSs_Type = Gauge32
_WfDsx3DayTotalSEFSs_Object = MibTableColumn
wfDsx3DayTotalSEFSs = _WfDsx3DayTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1, 4),
    _WfDsx3DayTotalSEFSs_Type()
)
wfDsx3DayTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayTotalSEFSs.setStatus("mandatory")
_WfDsx3DayTotalUASs_Type = Gauge32
_WfDsx3DayTotalUASs_Object = MibTableColumn
wfDsx3DayTotalUASs = _WfDsx3DayTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1, 5),
    _WfDsx3DayTotalUASs_Type()
)
wfDsx3DayTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayTotalUASs.setStatus("mandatory")
_WfDsx3DayTotalLCVs_Type = Gauge32
_WfDsx3DayTotalLCVs_Object = MibTableColumn
wfDsx3DayTotalLCVs = _WfDsx3DayTotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1, 6),
    _WfDsx3DayTotalLCVs_Type()
)
wfDsx3DayTotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayTotalLCVs.setStatus("mandatory")
_WfDsx3DayTotalPCVs_Type = Gauge32
_WfDsx3DayTotalPCVs_Object = MibTableColumn
wfDsx3DayTotalPCVs = _WfDsx3DayTotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1, 7),
    _WfDsx3DayTotalPCVs_Type()
)
wfDsx3DayTotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayTotalPCVs.setStatus("mandatory")
_WfDsx3DayTotalLESs_Type = Gauge32
_WfDsx3DayTotalLESs_Object = MibTableColumn
wfDsx3DayTotalLESs = _WfDsx3DayTotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1, 8),
    _WfDsx3DayTotalLESs_Type()
)
wfDsx3DayTotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayTotalLESs.setStatus("mandatory")
_WfDsx3DayTotalCCVs_Type = Gauge32
_WfDsx3DayTotalCCVs_Object = MibTableColumn
wfDsx3DayTotalCCVs = _WfDsx3DayTotalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1, 9),
    _WfDsx3DayTotalCCVs_Type()
)
wfDsx3DayTotalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayTotalCCVs.setStatus("mandatory")
_WfDsx3DayTotalCESs_Type = Gauge32
_WfDsx3DayTotalCESs_Object = MibTableColumn
wfDsx3DayTotalCESs = _WfDsx3DayTotalCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1, 10),
    _WfDsx3DayTotalCESs_Type()
)
wfDsx3DayTotalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayTotalCESs.setStatus("mandatory")
_WfDsx3DayTotalCSESs_Type = Gauge32
_WfDsx3DayTotalCSESs_Object = MibTableColumn
wfDsx3DayTotalCSESs = _WfDsx3DayTotalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1, 11),
    _WfDsx3DayTotalCSESs_Type()
)
wfDsx3DayTotalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayTotalCSESs.setStatus("mandatory")
_WfDsx3DayTotalSASs_Type = Gauge32
_WfDsx3DayTotalSASs_Object = MibTableColumn
wfDsx3DayTotalSASs = _WfDsx3DayTotalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1, 12),
    _WfDsx3DayTotalSASs_Type()
)
wfDsx3DayTotalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayTotalSASs.setStatus("mandatory")
_WfDsx3DayTotalAISSs_Type = Gauge32
_WfDsx3DayTotalAISSs_Object = MibTableColumn
wfDsx3DayTotalAISSs = _WfDsx3DayTotalAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1, 13),
    _WfDsx3DayTotalAISSs_Type()
)
wfDsx3DayTotalAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayTotalAISSs.setStatus("mandatory")
_WfDsx3DayTotalFCs_Type = Gauge32
_WfDsx3DayTotalFCs_Object = MibTableColumn
wfDsx3DayTotalFCs = _WfDsx3DayTotalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1, 14),
    _WfDsx3DayTotalFCs_Type()
)
wfDsx3DayTotalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayTotalFCs.setStatus("mandatory")


class _WfDsx3DayTotalValidFlag_Type(Integer32):
    """Custom type wfDsx3DayTotalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDsx3DayTotalValidFlag_Type.__name__ = "Integer32"
_WfDsx3DayTotalValidFlag_Object = MibTableColumn
wfDsx3DayTotalValidFlag = _WfDsx3DayTotalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 13, 1, 15),
    _WfDsx3DayTotalValidFlag_Type()
)
wfDsx3DayTotalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayTotalValidFlag.setStatus("mandatory")
_WfDsx3FarEndDayCurrentTable_Object = MibTable
wfDsx3FarEndDayCurrentTable = _WfDsx3FarEndDayCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 14)
)
if mibBuilder.loadTexts:
    wfDsx3FarEndDayCurrentTable.setStatus("mandatory")
_WfDsx3FarEndDayCurrentEntry_Object = MibTableRow
wfDsx3FarEndDayCurrentEntry = _WfDsx3FarEndDayCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 14, 1)
)
wfDsx3FarEndDayCurrentEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3FarEndDayCurrentIndex"),
)
if mibBuilder.loadTexts:
    wfDsx3FarEndDayCurrentEntry.setStatus("mandatory")


class _WfDsx3FarEndDayCurrentIndex_Type(Integer32):
    """Custom type wfDsx3FarEndDayCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDsx3FarEndDayCurrentIndex_Type.__name__ = "Integer32"
_WfDsx3FarEndDayCurrentIndex_Object = MibTableColumn
wfDsx3FarEndDayCurrentIndex = _WfDsx3FarEndDayCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 14, 1, 1),
    _WfDsx3FarEndDayCurrentIndex_Type()
)
wfDsx3FarEndDayCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayCurrentIndex.setStatus("mandatory")
_WfDsx3FarEndDayTimeElapsed_Type = Integer32
_WfDsx3FarEndDayTimeElapsed_Object = MibTableColumn
wfDsx3FarEndDayTimeElapsed = _WfDsx3FarEndDayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 14, 1, 2),
    _WfDsx3FarEndDayTimeElapsed_Type()
)
wfDsx3FarEndDayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayTimeElapsed.setStatus("mandatory")
_WfDsx3FarEndDayValidIntervals_Type = Integer32
_WfDsx3FarEndDayValidIntervals_Object = MibTableColumn
wfDsx3FarEndDayValidIntervals = _WfDsx3FarEndDayValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 14, 1, 3),
    _WfDsx3FarEndDayValidIntervals_Type()
)
wfDsx3FarEndDayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayValidIntervals.setStatus("mandatory")
_WfDsx3FarEndDayCurrentCESs_Type = Gauge32
_WfDsx3FarEndDayCurrentCESs_Object = MibTableColumn
wfDsx3FarEndDayCurrentCESs = _WfDsx3FarEndDayCurrentCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 14, 1, 4),
    _WfDsx3FarEndDayCurrentCESs_Type()
)
wfDsx3FarEndDayCurrentCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayCurrentCESs.setStatus("mandatory")
_WfDsx3FarEndDayCurrentCSESs_Type = Gauge32
_WfDsx3FarEndDayCurrentCSESs_Object = MibTableColumn
wfDsx3FarEndDayCurrentCSESs = _WfDsx3FarEndDayCurrentCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 14, 1, 5),
    _WfDsx3FarEndDayCurrentCSESs_Type()
)
wfDsx3FarEndDayCurrentCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayCurrentCSESs.setStatus("mandatory")
_WfDsx3FarEndDayCurrentCCVs_Type = Gauge32
_WfDsx3FarEndDayCurrentCCVs_Object = MibTableColumn
wfDsx3FarEndDayCurrentCCVs = _WfDsx3FarEndDayCurrentCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 14, 1, 6),
    _WfDsx3FarEndDayCurrentCCVs_Type()
)
wfDsx3FarEndDayCurrentCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayCurrentCCVs.setStatus("mandatory")
_WfDsx3FarEndDayCurrentUASs_Type = Gauge32
_WfDsx3FarEndDayCurrentUASs_Object = MibTableColumn
wfDsx3FarEndDayCurrentUASs = _WfDsx3FarEndDayCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 14, 1, 7),
    _WfDsx3FarEndDayCurrentUASs_Type()
)
wfDsx3FarEndDayCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayCurrentUASs.setStatus("mandatory")
_WfDsx3FarEndDayCurrentSASs_Type = Gauge32
_WfDsx3FarEndDayCurrentSASs_Object = MibTableColumn
wfDsx3FarEndDayCurrentSASs = _WfDsx3FarEndDayCurrentSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 14, 1, 8),
    _WfDsx3FarEndDayCurrentSASs_Type()
)
wfDsx3FarEndDayCurrentSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayCurrentSASs.setStatus("mandatory")
_WfDsx3FarEndDayCurrentFCs_Type = Gauge32
_WfDsx3FarEndDayCurrentFCs_Object = MibTableColumn
wfDsx3FarEndDayCurrentFCs = _WfDsx3FarEndDayCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 14, 1, 9),
    _WfDsx3FarEndDayCurrentFCs_Type()
)
wfDsx3FarEndDayCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayCurrentFCs.setStatus("mandatory")


class _WfDsx3FarEndDayCurrentValidFlag_Type(Integer32):
    """Custom type wfDsx3FarEndDayCurrentValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDsx3FarEndDayCurrentValidFlag_Type.__name__ = "Integer32"
_WfDsx3FarEndDayCurrentValidFlag_Object = MibTableColumn
wfDsx3FarEndDayCurrentValidFlag = _WfDsx3FarEndDayCurrentValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 14, 1, 10),
    _WfDsx3FarEndDayCurrentValidFlag_Type()
)
wfDsx3FarEndDayCurrentValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayCurrentValidFlag.setStatus("mandatory")
_WfDsx3FarEndDayIntervalTable_Object = MibTable
wfDsx3FarEndDayIntervalTable = _WfDsx3FarEndDayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 15)
)
if mibBuilder.loadTexts:
    wfDsx3FarEndDayIntervalTable.setStatus("mandatory")
_WfDsx3FarEndDayIntervalEntry_Object = MibTableRow
wfDsx3FarEndDayIntervalEntry = _WfDsx3FarEndDayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 15, 1)
)
wfDsx3FarEndDayIntervalEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3FarEndDayIntervalIndex"),
    (0, "Wellfleet-DSX3-MIB", "wfDsx3FarEndDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDsx3FarEndDayIntervalEntry.setStatus("mandatory")


class _WfDsx3FarEndDayIntervalIndex_Type(Integer32):
    """Custom type wfDsx3FarEndDayIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfDsx3FarEndDayIntervalIndex_Type.__name__ = "Integer32"
_WfDsx3FarEndDayIntervalIndex_Object = MibTableColumn
wfDsx3FarEndDayIntervalIndex = _WfDsx3FarEndDayIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 15, 1, 1),
    _WfDsx3FarEndDayIntervalIndex_Type()
)
wfDsx3FarEndDayIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayIntervalIndex.setStatus("mandatory")


class _WfDsx3FarEndDayIntervalNumber_Type(Integer32):
    """Custom type wfDsx3FarEndDayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_WfDsx3FarEndDayIntervalNumber_Type.__name__ = "Integer32"
_WfDsx3FarEndDayIntervalNumber_Object = MibTableColumn
wfDsx3FarEndDayIntervalNumber = _WfDsx3FarEndDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 15, 1, 2),
    _WfDsx3FarEndDayIntervalNumber_Type()
)
wfDsx3FarEndDayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayIntervalNumber.setStatus("mandatory")
_WfDsx3FarEndDayIntervalCESs_Type = Gauge32
_WfDsx3FarEndDayIntervalCESs_Object = MibTableColumn
wfDsx3FarEndDayIntervalCESs = _WfDsx3FarEndDayIntervalCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 15, 1, 3),
    _WfDsx3FarEndDayIntervalCESs_Type()
)
wfDsx3FarEndDayIntervalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayIntervalCESs.setStatus("mandatory")
_WfDsx3FarEndDayIntervalCSESs_Type = Gauge32
_WfDsx3FarEndDayIntervalCSESs_Object = MibTableColumn
wfDsx3FarEndDayIntervalCSESs = _WfDsx3FarEndDayIntervalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 15, 1, 4),
    _WfDsx3FarEndDayIntervalCSESs_Type()
)
wfDsx3FarEndDayIntervalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayIntervalCSESs.setStatus("mandatory")
_WfDsx3FarEndDayIntervalCCVs_Type = Gauge32
_WfDsx3FarEndDayIntervalCCVs_Object = MibTableColumn
wfDsx3FarEndDayIntervalCCVs = _WfDsx3FarEndDayIntervalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 15, 1, 5),
    _WfDsx3FarEndDayIntervalCCVs_Type()
)
wfDsx3FarEndDayIntervalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayIntervalCCVs.setStatus("mandatory")
_WfDsx3FarEndDayIntervalUASs_Type = Gauge32
_WfDsx3FarEndDayIntervalUASs_Object = MibTableColumn
wfDsx3FarEndDayIntervalUASs = _WfDsx3FarEndDayIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 15, 1, 6),
    _WfDsx3FarEndDayIntervalUASs_Type()
)
wfDsx3FarEndDayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayIntervalUASs.setStatus("mandatory")
_WfDsx3FarEndDayIntervalSASs_Type = Gauge32
_WfDsx3FarEndDayIntervalSASs_Object = MibTableColumn
wfDsx3FarEndDayIntervalSASs = _WfDsx3FarEndDayIntervalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 15, 1, 7),
    _WfDsx3FarEndDayIntervalSASs_Type()
)
wfDsx3FarEndDayIntervalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayIntervalSASs.setStatus("mandatory")
_WfDsx3FarEndDayIntervalFCs_Type = Gauge32
_WfDsx3FarEndDayIntervalFCs_Object = MibTableColumn
wfDsx3FarEndDayIntervalFCs = _WfDsx3FarEndDayIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 15, 1, 8),
    _WfDsx3FarEndDayIntervalFCs_Type()
)
wfDsx3FarEndDayIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayIntervalFCs.setStatus("mandatory")


class _WfDsx3FarEndDayIntervalValidFlag_Type(Integer32):
    """Custom type wfDsx3FarEndDayIntervalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDsx3FarEndDayIntervalValidFlag_Type.__name__ = "Integer32"
_WfDsx3FarEndDayIntervalValidFlag_Object = MibTableColumn
wfDsx3FarEndDayIntervalValidFlag = _WfDsx3FarEndDayIntervalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 15, 1, 9),
    _WfDsx3FarEndDayIntervalValidFlag_Type()
)
wfDsx3FarEndDayIntervalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayIntervalValidFlag.setStatus("mandatory")
_WfDsx3FarEndDayTotalTable_Object = MibTable
wfDsx3FarEndDayTotalTable = _WfDsx3FarEndDayTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 16)
)
if mibBuilder.loadTexts:
    wfDsx3FarEndDayTotalTable.setStatus("mandatory")
_WfDsx3FarEndDayTotalEntry_Object = MibTableRow
wfDsx3FarEndDayTotalEntry = _WfDsx3FarEndDayTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 16, 1)
)
wfDsx3FarEndDayTotalEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3FarEndDayTotalIndex"),
)
if mibBuilder.loadTexts:
    wfDsx3FarEndDayTotalEntry.setStatus("mandatory")


class _WfDsx3FarEndDayTotalIndex_Type(Integer32):
    """Custom type wfDsx3FarEndDayTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfDsx3FarEndDayTotalIndex_Type.__name__ = "Integer32"
_WfDsx3FarEndDayTotalIndex_Object = MibTableColumn
wfDsx3FarEndDayTotalIndex = _WfDsx3FarEndDayTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 16, 1, 1),
    _WfDsx3FarEndDayTotalIndex_Type()
)
wfDsx3FarEndDayTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayTotalIndex.setStatus("mandatory")
_WfDsx3FarEndDayTotalCESs_Type = Gauge32
_WfDsx3FarEndDayTotalCESs_Object = MibTableColumn
wfDsx3FarEndDayTotalCESs = _WfDsx3FarEndDayTotalCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 16, 1, 2),
    _WfDsx3FarEndDayTotalCESs_Type()
)
wfDsx3FarEndDayTotalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayTotalCESs.setStatus("mandatory")
_WfDsx3FarEndDayTotalCSESs_Type = Gauge32
_WfDsx3FarEndDayTotalCSESs_Object = MibTableColumn
wfDsx3FarEndDayTotalCSESs = _WfDsx3FarEndDayTotalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 16, 1, 3),
    _WfDsx3FarEndDayTotalCSESs_Type()
)
wfDsx3FarEndDayTotalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayTotalCSESs.setStatus("mandatory")
_WfDsx3FarEndDayTotalCCVs_Type = Gauge32
_WfDsx3FarEndDayTotalCCVs_Object = MibTableColumn
wfDsx3FarEndDayTotalCCVs = _WfDsx3FarEndDayTotalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 16, 1, 4),
    _WfDsx3FarEndDayTotalCCVs_Type()
)
wfDsx3FarEndDayTotalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayTotalCCVs.setStatus("mandatory")
_WfDsx3FarEndDayTotalUASs_Type = Gauge32
_WfDsx3FarEndDayTotalUASs_Object = MibTableColumn
wfDsx3FarEndDayTotalUASs = _WfDsx3FarEndDayTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 16, 1, 5),
    _WfDsx3FarEndDayTotalUASs_Type()
)
wfDsx3FarEndDayTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayTotalUASs.setStatus("mandatory")
_WfDsx3FarEndDayTotalSASs_Type = Gauge32
_WfDsx3FarEndDayTotalSASs_Object = MibTableColumn
wfDsx3FarEndDayTotalSASs = _WfDsx3FarEndDayTotalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 16, 1, 6),
    _WfDsx3FarEndDayTotalSASs_Type()
)
wfDsx3FarEndDayTotalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayTotalSASs.setStatus("mandatory")
_WfDsx3FarEndDayTotalFCs_Type = Gauge32
_WfDsx3FarEndDayTotalFCs_Object = MibTableColumn
wfDsx3FarEndDayTotalFCs = _WfDsx3FarEndDayTotalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 16, 1, 7),
    _WfDsx3FarEndDayTotalFCs_Type()
)
wfDsx3FarEndDayTotalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayTotalFCs.setStatus("mandatory")


class _WfDsx3FarEndDayTotalValidFlag_Type(Integer32):
    """Custom type wfDsx3FarEndDayTotalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDsx3FarEndDayTotalValidFlag_Type.__name__ = "Integer32"
_WfDsx3FarEndDayTotalValidFlag_Object = MibTableColumn
wfDsx3FarEndDayTotalValidFlag = _WfDsx3FarEndDayTotalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 16, 1, 8),
    _WfDsx3FarEndDayTotalValidFlag_Type()
)
wfDsx3FarEndDayTotalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayTotalValidFlag.setStatus("mandatory")
_WfDsx3ThrAlrtTable_Object = MibTable
wfDsx3ThrAlrtTable = _WfDsx3ThrAlrtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18)
)
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtTable.setStatus("mandatory")
_WfDsx3ThrAlrtEntry_Object = MibTableRow
wfDsx3ThrAlrtEntry = _WfDsx3ThrAlrtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1)
)
wfDsx3ThrAlrtEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3ThrAlrtIndex"),
)
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtEntry.setStatus("mandatory")


class _WfDsx3ThrAlrtDelete_Type(Integer32):
    """Custom type wfDsx3ThrAlrtDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDsx3ThrAlrtDelete_Type.__name__ = "Integer32"
_WfDsx3ThrAlrtDelete_Object = MibTableColumn
wfDsx3ThrAlrtDelete = _WfDsx3ThrAlrtDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1, 1),
    _WfDsx3ThrAlrtDelete_Type()
)
wfDsx3ThrAlrtDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtDelete.setStatus("mandatory")
_WfDsx3ThrAlrtIndex_Type = Integer32
_WfDsx3ThrAlrtIndex_Object = MibTableColumn
wfDsx3ThrAlrtIndex = _WfDsx3ThrAlrtIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1, 2),
    _WfDsx3ThrAlrtIndex_Type()
)
wfDsx3ThrAlrtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtIndex.setStatus("mandatory")


class _WfDsx3ThrAlrtPESs_Type(Gauge32):
    """Custom type wfDsx3ThrAlrtPESs based on Gauge32"""
    defaultValue = 25


_WfDsx3ThrAlrtPESs_Object = MibTableColumn
wfDsx3ThrAlrtPESs = _WfDsx3ThrAlrtPESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1, 3),
    _WfDsx3ThrAlrtPESs_Type()
)
wfDsx3ThrAlrtPESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtPESs.setStatus("mandatory")


class _WfDsx3ThrAlrtPSESs_Type(Gauge32):
    """Custom type wfDsx3ThrAlrtPSESs based on Gauge32"""
    defaultValue = 4


_WfDsx3ThrAlrtPSESs_Object = MibTableColumn
wfDsx3ThrAlrtPSESs = _WfDsx3ThrAlrtPSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1, 4),
    _WfDsx3ThrAlrtPSESs_Type()
)
wfDsx3ThrAlrtPSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtPSESs.setStatus("mandatory")


class _WfDsx3ThrAlrtSEFSs_Type(Gauge32):
    """Custom type wfDsx3ThrAlrtSEFSs based on Gauge32"""
    defaultValue = 0


_WfDsx3ThrAlrtSEFSs_Object = MibTableColumn
wfDsx3ThrAlrtSEFSs = _WfDsx3ThrAlrtSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1, 5),
    _WfDsx3ThrAlrtSEFSs_Type()
)
wfDsx3ThrAlrtSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtSEFSs.setStatus("mandatory")


class _WfDsx3ThrAlrtUASs_Type(Gauge32):
    """Custom type wfDsx3ThrAlrtUASs based on Gauge32"""
    defaultValue = 10


_WfDsx3ThrAlrtUASs_Object = MibTableColumn
wfDsx3ThrAlrtUASs = _WfDsx3ThrAlrtUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1, 6),
    _WfDsx3ThrAlrtUASs_Type()
)
wfDsx3ThrAlrtUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtUASs.setStatus("mandatory")


class _WfDsx3ThrAlrtLCVs_Type(Gauge32):
    """Custom type wfDsx3ThrAlrtLCVs based on Gauge32"""
    defaultValue = 387


_WfDsx3ThrAlrtLCVs_Object = MibTableColumn
wfDsx3ThrAlrtLCVs = _WfDsx3ThrAlrtLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1, 7),
    _WfDsx3ThrAlrtLCVs_Type()
)
wfDsx3ThrAlrtLCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtLCVs.setStatus("mandatory")


class _WfDsx3ThrAlrtPCVs_Type(Gauge32):
    """Custom type wfDsx3ThrAlrtPCVs based on Gauge32"""
    defaultValue = 382


_WfDsx3ThrAlrtPCVs_Object = MibTableColumn
wfDsx3ThrAlrtPCVs = _WfDsx3ThrAlrtPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1, 8),
    _WfDsx3ThrAlrtPCVs_Type()
)
wfDsx3ThrAlrtPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtPCVs.setStatus("mandatory")


class _WfDsx3ThrAlrtLESs_Type(Gauge32):
    """Custom type wfDsx3ThrAlrtLESs based on Gauge32"""
    defaultValue = 25


_WfDsx3ThrAlrtLESs_Object = MibTableColumn
wfDsx3ThrAlrtLESs = _WfDsx3ThrAlrtLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1, 9),
    _WfDsx3ThrAlrtLESs_Type()
)
wfDsx3ThrAlrtLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtLESs.setStatus("mandatory")


class _WfDsx3ThrAlrtCCVs_Type(Gauge32):
    """Custom type wfDsx3ThrAlrtCCVs based on Gauge32"""
    defaultValue = 382


_WfDsx3ThrAlrtCCVs_Object = MibTableColumn
wfDsx3ThrAlrtCCVs = _WfDsx3ThrAlrtCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1, 10),
    _WfDsx3ThrAlrtCCVs_Type()
)
wfDsx3ThrAlrtCCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtCCVs.setStatus("mandatory")


class _WfDsx3ThrAlrtCESs_Type(Gauge32):
    """Custom type wfDsx3ThrAlrtCESs based on Gauge32"""
    defaultValue = 25


_WfDsx3ThrAlrtCESs_Object = MibTableColumn
wfDsx3ThrAlrtCESs = _WfDsx3ThrAlrtCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1, 11),
    _WfDsx3ThrAlrtCESs_Type()
)
wfDsx3ThrAlrtCESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtCESs.setStatus("mandatory")


class _WfDsx3ThrAlrtCSESs_Type(Gauge32):
    """Custom type wfDsx3ThrAlrtCSESs based on Gauge32"""
    defaultValue = 4


_WfDsx3ThrAlrtCSESs_Object = MibTableColumn
wfDsx3ThrAlrtCSESs = _WfDsx3ThrAlrtCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1, 12),
    _WfDsx3ThrAlrtCSESs_Type()
)
wfDsx3ThrAlrtCSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtCSESs.setStatus("mandatory")


class _WfDsx3ThrAlrtSASs_Type(Gauge32):
    """Custom type wfDsx3ThrAlrtSASs based on Gauge32"""
    defaultValue = 0


_WfDsx3ThrAlrtSASs_Object = MibTableColumn
wfDsx3ThrAlrtSASs = _WfDsx3ThrAlrtSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1, 13),
    _WfDsx3ThrAlrtSASs_Type()
)
wfDsx3ThrAlrtSASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtSASs.setStatus("mandatory")


class _WfDsx3ThrAlrtAISSs_Type(Gauge32):
    """Custom type wfDsx3ThrAlrtAISSs based on Gauge32"""
    defaultValue = 0


_WfDsx3ThrAlrtAISSs_Object = MibTableColumn
wfDsx3ThrAlrtAISSs = _WfDsx3ThrAlrtAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1, 14),
    _WfDsx3ThrAlrtAISSs_Type()
)
wfDsx3ThrAlrtAISSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtAISSs.setStatus("mandatory")


class _WfDsx3ThrAlrtFCs_Type(Gauge32):
    """Custom type wfDsx3ThrAlrtFCs based on Gauge32"""
    defaultValue = 0


_WfDsx3ThrAlrtFCs_Object = MibTableColumn
wfDsx3ThrAlrtFCs = _WfDsx3ThrAlrtFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 18, 1, 15),
    _WfDsx3ThrAlrtFCs_Type()
)
wfDsx3ThrAlrtFCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3ThrAlrtFCs.setStatus("mandatory")
_WfDsx3FarEndThrAlrtTable_Object = MibTable
wfDsx3FarEndThrAlrtTable = _WfDsx3FarEndThrAlrtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 19)
)
if mibBuilder.loadTexts:
    wfDsx3FarEndThrAlrtTable.setStatus("mandatory")
_WfDsx3FarEndThrAlrtEntry_Object = MibTableRow
wfDsx3FarEndThrAlrtEntry = _WfDsx3FarEndThrAlrtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 19, 1)
)
wfDsx3FarEndThrAlrtEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3FarEndThrAlrtIndex"),
)
if mibBuilder.loadTexts:
    wfDsx3FarEndThrAlrtEntry.setStatus("mandatory")


class _WfDsx3FarEndThrAlrtDelete_Type(Integer32):
    """Custom type wfDsx3FarEndThrAlrtDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDsx3FarEndThrAlrtDelete_Type.__name__ = "Integer32"
_WfDsx3FarEndThrAlrtDelete_Object = MibTableColumn
wfDsx3FarEndThrAlrtDelete = _WfDsx3FarEndThrAlrtDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 19, 1, 1),
    _WfDsx3FarEndThrAlrtDelete_Type()
)
wfDsx3FarEndThrAlrtDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndThrAlrtDelete.setStatus("mandatory")
_WfDsx3FarEndThrAlrtIndex_Type = Integer32
_WfDsx3FarEndThrAlrtIndex_Object = MibTableColumn
wfDsx3FarEndThrAlrtIndex = _WfDsx3FarEndThrAlrtIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 19, 1, 2),
    _WfDsx3FarEndThrAlrtIndex_Type()
)
wfDsx3FarEndThrAlrtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndThrAlrtIndex.setStatus("mandatory")


class _WfDsx3FarEndThrAlrtCESs_Type(Gauge32):
    """Custom type wfDsx3FarEndThrAlrtCESs based on Gauge32"""
    defaultValue = 25


_WfDsx3FarEndThrAlrtCESs_Object = MibTableColumn
wfDsx3FarEndThrAlrtCESs = _WfDsx3FarEndThrAlrtCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 19, 1, 3),
    _WfDsx3FarEndThrAlrtCESs_Type()
)
wfDsx3FarEndThrAlrtCESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndThrAlrtCESs.setStatus("mandatory")


class _WfDsx3FarEndThrAlrtCSESs_Type(Gauge32):
    """Custom type wfDsx3FarEndThrAlrtCSESs based on Gauge32"""
    defaultValue = 4


_WfDsx3FarEndThrAlrtCSESs_Object = MibTableColumn
wfDsx3FarEndThrAlrtCSESs = _WfDsx3FarEndThrAlrtCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 19, 1, 4),
    _WfDsx3FarEndThrAlrtCSESs_Type()
)
wfDsx3FarEndThrAlrtCSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndThrAlrtCSESs.setStatus("mandatory")


class _WfDsx3FarEndThrAlrtCCVs_Type(Gauge32):
    """Custom type wfDsx3FarEndThrAlrtCCVs based on Gauge32"""
    defaultValue = 382


_WfDsx3FarEndThrAlrtCCVs_Object = MibTableColumn
wfDsx3FarEndThrAlrtCCVs = _WfDsx3FarEndThrAlrtCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 19, 1, 5),
    _WfDsx3FarEndThrAlrtCCVs_Type()
)
wfDsx3FarEndThrAlrtCCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndThrAlrtCCVs.setStatus("mandatory")


class _WfDsx3FarEndThrAlrtUASs_Type(Gauge32):
    """Custom type wfDsx3FarEndThrAlrtUASs based on Gauge32"""
    defaultValue = 10


_WfDsx3FarEndThrAlrtUASs_Object = MibTableColumn
wfDsx3FarEndThrAlrtUASs = _WfDsx3FarEndThrAlrtUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 19, 1, 6),
    _WfDsx3FarEndThrAlrtUASs_Type()
)
wfDsx3FarEndThrAlrtUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndThrAlrtUASs.setStatus("mandatory")


class _WfDsx3FarEndThrAlrtSASs_Type(Gauge32):
    """Custom type wfDsx3FarEndThrAlrtSASs based on Gauge32"""
    defaultValue = 0


_WfDsx3FarEndThrAlrtSASs_Object = MibTableColumn
wfDsx3FarEndThrAlrtSASs = _WfDsx3FarEndThrAlrtSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 19, 1, 7),
    _WfDsx3FarEndThrAlrtSASs_Type()
)
wfDsx3FarEndThrAlrtSASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndThrAlrtSASs.setStatus("mandatory")


class _WfDsx3FarEndThrAlrtFCs_Type(Gauge32):
    """Custom type wfDsx3FarEndThrAlrtFCs based on Gauge32"""
    defaultValue = 0


_WfDsx3FarEndThrAlrtFCs_Object = MibTableColumn
wfDsx3FarEndThrAlrtFCs = _WfDsx3FarEndThrAlrtFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 19, 1, 8),
    _WfDsx3FarEndThrAlrtFCs_Type()
)
wfDsx3FarEndThrAlrtFCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndThrAlrtFCs.setStatus("mandatory")
_WfDsx3DayThrAlrtTable_Object = MibTable
wfDsx3DayThrAlrtTable = _WfDsx3DayThrAlrtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20)
)
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtTable.setStatus("mandatory")
_WfDsx3DayThrAlrtEntry_Object = MibTableRow
wfDsx3DayThrAlrtEntry = _WfDsx3DayThrAlrtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1)
)
wfDsx3DayThrAlrtEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3DayThrAlrtIndex"),
)
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtEntry.setStatus("mandatory")


class _WfDsx3DayThrAlrtDelete_Type(Integer32):
    """Custom type wfDsx3DayThrAlrtDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDsx3DayThrAlrtDelete_Type.__name__ = "Integer32"
_WfDsx3DayThrAlrtDelete_Object = MibTableColumn
wfDsx3DayThrAlrtDelete = _WfDsx3DayThrAlrtDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1, 1),
    _WfDsx3DayThrAlrtDelete_Type()
)
wfDsx3DayThrAlrtDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtDelete.setStatus("mandatory")
_WfDsx3DayThrAlrtIndex_Type = Integer32
_WfDsx3DayThrAlrtIndex_Object = MibTableColumn
wfDsx3DayThrAlrtIndex = _WfDsx3DayThrAlrtIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1, 2),
    _WfDsx3DayThrAlrtIndex_Type()
)
wfDsx3DayThrAlrtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtIndex.setStatus("mandatory")


class _WfDsx3DayThrAlrtPESs_Type(Gauge32):
    """Custom type wfDsx3DayThrAlrtPESs based on Gauge32"""
    defaultValue = 250


_WfDsx3DayThrAlrtPESs_Object = MibTableColumn
wfDsx3DayThrAlrtPESs = _WfDsx3DayThrAlrtPESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1, 3),
    _WfDsx3DayThrAlrtPESs_Type()
)
wfDsx3DayThrAlrtPESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtPESs.setStatus("mandatory")


class _WfDsx3DayThrAlrtPSESs_Type(Gauge32):
    """Custom type wfDsx3DayThrAlrtPSESs based on Gauge32"""
    defaultValue = 40


_WfDsx3DayThrAlrtPSESs_Object = MibTableColumn
wfDsx3DayThrAlrtPSESs = _WfDsx3DayThrAlrtPSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1, 4),
    _WfDsx3DayThrAlrtPSESs_Type()
)
wfDsx3DayThrAlrtPSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtPSESs.setStatus("mandatory")


class _WfDsx3DayThrAlrtSEFSs_Type(Gauge32):
    """Custom type wfDsx3DayThrAlrtSEFSs based on Gauge32"""
    defaultValue = 0


_WfDsx3DayThrAlrtSEFSs_Object = MibTableColumn
wfDsx3DayThrAlrtSEFSs = _WfDsx3DayThrAlrtSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1, 5),
    _WfDsx3DayThrAlrtSEFSs_Type()
)
wfDsx3DayThrAlrtSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtSEFSs.setStatus("mandatory")


class _WfDsx3DayThrAlrtUASs_Type(Gauge32):
    """Custom type wfDsx3DayThrAlrtUASs based on Gauge32"""
    defaultValue = 10


_WfDsx3DayThrAlrtUASs_Object = MibTableColumn
wfDsx3DayThrAlrtUASs = _WfDsx3DayThrAlrtUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1, 6),
    _WfDsx3DayThrAlrtUASs_Type()
)
wfDsx3DayThrAlrtUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtUASs.setStatus("mandatory")


class _WfDsx3DayThrAlrtLCVs_Type(Gauge32):
    """Custom type wfDsx3DayThrAlrtLCVs based on Gauge32"""
    defaultValue = 3865


_WfDsx3DayThrAlrtLCVs_Object = MibTableColumn
wfDsx3DayThrAlrtLCVs = _WfDsx3DayThrAlrtLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1, 7),
    _WfDsx3DayThrAlrtLCVs_Type()
)
wfDsx3DayThrAlrtLCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtLCVs.setStatus("mandatory")


class _WfDsx3DayThrAlrtPCVs_Type(Gauge32):
    """Custom type wfDsx3DayThrAlrtPCVs based on Gauge32"""
    defaultValue = 3820


_WfDsx3DayThrAlrtPCVs_Object = MibTableColumn
wfDsx3DayThrAlrtPCVs = _WfDsx3DayThrAlrtPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1, 8),
    _WfDsx3DayThrAlrtPCVs_Type()
)
wfDsx3DayThrAlrtPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtPCVs.setStatus("mandatory")


class _WfDsx3DayThrAlrtLESs_Type(Gauge32):
    """Custom type wfDsx3DayThrAlrtLESs based on Gauge32"""
    defaultValue = 250


_WfDsx3DayThrAlrtLESs_Object = MibTableColumn
wfDsx3DayThrAlrtLESs = _WfDsx3DayThrAlrtLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1, 9),
    _WfDsx3DayThrAlrtLESs_Type()
)
wfDsx3DayThrAlrtLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtLESs.setStatus("mandatory")


class _WfDsx3DayThrAlrtCCVs_Type(Gauge32):
    """Custom type wfDsx3DayThrAlrtCCVs based on Gauge32"""
    defaultValue = 3820


_WfDsx3DayThrAlrtCCVs_Object = MibTableColumn
wfDsx3DayThrAlrtCCVs = _WfDsx3DayThrAlrtCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1, 10),
    _WfDsx3DayThrAlrtCCVs_Type()
)
wfDsx3DayThrAlrtCCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtCCVs.setStatus("mandatory")


class _WfDsx3DayThrAlrtCESs_Type(Gauge32):
    """Custom type wfDsx3DayThrAlrtCESs based on Gauge32"""
    defaultValue = 250


_WfDsx3DayThrAlrtCESs_Object = MibTableColumn
wfDsx3DayThrAlrtCESs = _WfDsx3DayThrAlrtCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1, 11),
    _WfDsx3DayThrAlrtCESs_Type()
)
wfDsx3DayThrAlrtCESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtCESs.setStatus("mandatory")


class _WfDsx3DayThrAlrtCSESs_Type(Gauge32):
    """Custom type wfDsx3DayThrAlrtCSESs based on Gauge32"""
    defaultValue = 0


_WfDsx3DayThrAlrtCSESs_Object = MibTableColumn
wfDsx3DayThrAlrtCSESs = _WfDsx3DayThrAlrtCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1, 12),
    _WfDsx3DayThrAlrtCSESs_Type()
)
wfDsx3DayThrAlrtCSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtCSESs.setStatus("mandatory")


class _WfDsx3DayThrAlrtSASs_Type(Gauge32):
    """Custom type wfDsx3DayThrAlrtSASs based on Gauge32"""
    defaultValue = 8


_WfDsx3DayThrAlrtSASs_Object = MibTableColumn
wfDsx3DayThrAlrtSASs = _WfDsx3DayThrAlrtSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1, 13),
    _WfDsx3DayThrAlrtSASs_Type()
)
wfDsx3DayThrAlrtSASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtSASs.setStatus("mandatory")


class _WfDsx3DayThrAlrtAISSs_Type(Gauge32):
    """Custom type wfDsx3DayThrAlrtAISSs based on Gauge32"""
    defaultValue = 0


_WfDsx3DayThrAlrtAISSs_Object = MibTableColumn
wfDsx3DayThrAlrtAISSs = _WfDsx3DayThrAlrtAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1, 14),
    _WfDsx3DayThrAlrtAISSs_Type()
)
wfDsx3DayThrAlrtAISSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtAISSs.setStatus("mandatory")


class _WfDsx3DayThrAlrtFCs_Type(Gauge32):
    """Custom type wfDsx3DayThrAlrtFCs based on Gauge32"""
    defaultValue = 0


_WfDsx3DayThrAlrtFCs_Object = MibTableColumn
wfDsx3DayThrAlrtFCs = _WfDsx3DayThrAlrtFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 20, 1, 15),
    _WfDsx3DayThrAlrtFCs_Type()
)
wfDsx3DayThrAlrtFCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3DayThrAlrtFCs.setStatus("mandatory")
_WfDsx3FarEndDayThrAlrtTable_Object = MibTable
wfDsx3FarEndDayThrAlrtTable = _WfDsx3FarEndDayThrAlrtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 21)
)
if mibBuilder.loadTexts:
    wfDsx3FarEndDayThrAlrtTable.setStatus("mandatory")
_WfDsx3FarEndDayThrAlrtEntry_Object = MibTableRow
wfDsx3FarEndDayThrAlrtEntry = _WfDsx3FarEndDayThrAlrtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 21, 1)
)
wfDsx3FarEndDayThrAlrtEntry.setIndexNames(
    (0, "Wellfleet-DSX3-MIB", "wfDsx3FarEndDayThrAlrtIndex"),
)
if mibBuilder.loadTexts:
    wfDsx3FarEndDayThrAlrtEntry.setStatus("mandatory")


class _WfDsx3FarEndDayThrAlrtDelete_Type(Integer32):
    """Custom type wfDsx3FarEndDayThrAlrtDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDsx3FarEndDayThrAlrtDelete_Type.__name__ = "Integer32"
_WfDsx3FarEndDayThrAlrtDelete_Object = MibTableColumn
wfDsx3FarEndDayThrAlrtDelete = _WfDsx3FarEndDayThrAlrtDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 21, 1, 1),
    _WfDsx3FarEndDayThrAlrtDelete_Type()
)
wfDsx3FarEndDayThrAlrtDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayThrAlrtDelete.setStatus("mandatory")
_WfDsx3FarEndDayThrAlrtIndex_Type = Integer32
_WfDsx3FarEndDayThrAlrtIndex_Object = MibTableColumn
wfDsx3FarEndDayThrAlrtIndex = _WfDsx3FarEndDayThrAlrtIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 21, 1, 2),
    _WfDsx3FarEndDayThrAlrtIndex_Type()
)
wfDsx3FarEndDayThrAlrtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayThrAlrtIndex.setStatus("mandatory")


class _WfDsx3FarEndDayThrAlrtCESs_Type(Gauge32):
    """Custom type wfDsx3FarEndDayThrAlrtCESs based on Gauge32"""
    defaultValue = 250


_WfDsx3FarEndDayThrAlrtCESs_Object = MibTableColumn
wfDsx3FarEndDayThrAlrtCESs = _WfDsx3FarEndDayThrAlrtCESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 21, 1, 3),
    _WfDsx3FarEndDayThrAlrtCESs_Type()
)
wfDsx3FarEndDayThrAlrtCESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayThrAlrtCESs.setStatus("mandatory")


class _WfDsx3FarEndDayThrAlrtCSESs_Type(Gauge32):
    """Custom type wfDsx3FarEndDayThrAlrtCSESs based on Gauge32"""
    defaultValue = 0


_WfDsx3FarEndDayThrAlrtCSESs_Object = MibTableColumn
wfDsx3FarEndDayThrAlrtCSESs = _WfDsx3FarEndDayThrAlrtCSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 21, 1, 4),
    _WfDsx3FarEndDayThrAlrtCSESs_Type()
)
wfDsx3FarEndDayThrAlrtCSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayThrAlrtCSESs.setStatus("mandatory")


class _WfDsx3FarEndDayThrAlrtCCVs_Type(Gauge32):
    """Custom type wfDsx3FarEndDayThrAlrtCCVs based on Gauge32"""
    defaultValue = 3820


_WfDsx3FarEndDayThrAlrtCCVs_Object = MibTableColumn
wfDsx3FarEndDayThrAlrtCCVs = _WfDsx3FarEndDayThrAlrtCCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 21, 1, 5),
    _WfDsx3FarEndDayThrAlrtCCVs_Type()
)
wfDsx3FarEndDayThrAlrtCCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayThrAlrtCCVs.setStatus("mandatory")


class _WfDsx3FarEndDayThrAlrtUASs_Type(Gauge32):
    """Custom type wfDsx3FarEndDayThrAlrtUASs based on Gauge32"""
    defaultValue = 10


_WfDsx3FarEndDayThrAlrtUASs_Object = MibTableColumn
wfDsx3FarEndDayThrAlrtUASs = _WfDsx3FarEndDayThrAlrtUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 21, 1, 6),
    _WfDsx3FarEndDayThrAlrtUASs_Type()
)
wfDsx3FarEndDayThrAlrtUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayThrAlrtUASs.setStatus("mandatory")


class _WfDsx3FarEndDayThrAlrtSASs_Type(Gauge32):
    """Custom type wfDsx3FarEndDayThrAlrtSASs based on Gauge32"""
    defaultValue = 8


_WfDsx3FarEndDayThrAlrtSASs_Object = MibTableColumn
wfDsx3FarEndDayThrAlrtSASs = _WfDsx3FarEndDayThrAlrtSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 21, 1, 7),
    _WfDsx3FarEndDayThrAlrtSASs_Type()
)
wfDsx3FarEndDayThrAlrtSASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayThrAlrtSASs.setStatus("mandatory")


class _WfDsx3FarEndDayThrAlrtFCs_Type(Gauge32):
    """Custom type wfDsx3FarEndDayThrAlrtFCs based on Gauge32"""
    defaultValue = 0


_WfDsx3FarEndDayThrAlrtFCs_Object = MibTableColumn
wfDsx3FarEndDayThrAlrtFCs = _WfDsx3FarEndDayThrAlrtFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 21, 1, 8),
    _WfDsx3FarEndDayThrAlrtFCs_Type()
)
wfDsx3FarEndDayThrAlrtFCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsx3FarEndDayThrAlrtFCs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-DSX3-MIB",
    **{"wfDsx3ConfigTable": wfDsx3ConfigTable,
       "wfDsx3ConfigEntry": wfDsx3ConfigEntry,
       "wfDsx3LineIndex": wfDsx3LineIndex,
       "wfDsx3IfIndex": wfDsx3IfIndex,
       "wfDsx3TimeElapsed": wfDsx3TimeElapsed,
       "wfDsx3ValidIntervals": wfDsx3ValidIntervals,
       "wfDsx3LineType": wfDsx3LineType,
       "wfDsx3LineCoding": wfDsx3LineCoding,
       "wfDsx3SendCode": wfDsx3SendCode,
       "wfDsx3CircuitIdentifier": wfDsx3CircuitIdentifier,
       "wfDsx3LoopbackConfig": wfDsx3LoopbackConfig,
       "wfDsx3LineStatus": wfDsx3LineStatus,
       "wfDsx3TransmitClockSource": wfDsx3TransmitClockSource,
       "wfDsx3CurrentTable": wfDsx3CurrentTable,
       "wfDsx3CurrentEntry": wfDsx3CurrentEntry,
       "wfDsx3CurrentIndex": wfDsx3CurrentIndex,
       "wfDsx3CurrentPESs": wfDsx3CurrentPESs,
       "wfDsx3CurrentPSESs": wfDsx3CurrentPSESs,
       "wfDsx3CurrentSEFSs": wfDsx3CurrentSEFSs,
       "wfDsx3CurrentUASs": wfDsx3CurrentUASs,
       "wfDsx3CurrentLCVs": wfDsx3CurrentLCVs,
       "wfDsx3CurrentPCVs": wfDsx3CurrentPCVs,
       "wfDsx3CurrentLESs": wfDsx3CurrentLESs,
       "wfDsx3CurrentCCVs": wfDsx3CurrentCCVs,
       "wfDsx3CurrentCESs": wfDsx3CurrentCESs,
       "wfDsx3CurrentCSESs": wfDsx3CurrentCSESs,
       "wfDsx3CurrentSASs": wfDsx3CurrentSASs,
       "wfDsx3CurrentAISSs": wfDsx3CurrentAISSs,
       "wfDsx3CurrentFCs": wfDsx3CurrentFCs,
       "wfDsx3CurrentTimeElapsed": wfDsx3CurrentTimeElapsed,
       "wfDsx3CurrentValidIntervals": wfDsx3CurrentValidIntervals,
       "wfDsx3CurrentValidFlag": wfDsx3CurrentValidFlag,
       "wfDsx3IntervalTable": wfDsx3IntervalTable,
       "wfDsx3IntervalEntry": wfDsx3IntervalEntry,
       "wfDsx3IntervalIndex": wfDsx3IntervalIndex,
       "wfDsx3IntervalNumber": wfDsx3IntervalNumber,
       "wfDsx3IntervalPESs": wfDsx3IntervalPESs,
       "wfDsx3IntervalPSESs": wfDsx3IntervalPSESs,
       "wfDsx3IntervalSEFSs": wfDsx3IntervalSEFSs,
       "wfDsx3IntervalUASs": wfDsx3IntervalUASs,
       "wfDsx3IntervalLCVs": wfDsx3IntervalLCVs,
       "wfDsx3IntervalPCVs": wfDsx3IntervalPCVs,
       "wfDsx3IntervalLESs": wfDsx3IntervalLESs,
       "wfDsx3IntervalCCVs": wfDsx3IntervalCCVs,
       "wfDsx3IntervalCESs": wfDsx3IntervalCESs,
       "wfDsx3IntervalCSESs": wfDsx3IntervalCSESs,
       "wfDsx3IntervalSASs": wfDsx3IntervalSASs,
       "wfDsx3IntervalAISSs": wfDsx3IntervalAISSs,
       "wfDsx3IntervalFCs": wfDsx3IntervalFCs,
       "wfDsx3IntervalValidFlag": wfDsx3IntervalValidFlag,
       "wfDsx3TotalTable": wfDsx3TotalTable,
       "wfDsx3TotalEntry": wfDsx3TotalEntry,
       "wfDsx3TotalIndex": wfDsx3TotalIndex,
       "wfDsx3TotalPESs": wfDsx3TotalPESs,
       "wfDsx3TotalPSESs": wfDsx3TotalPSESs,
       "wfDsx3TotalSEFSs": wfDsx3TotalSEFSs,
       "wfDsx3TotalUASs": wfDsx3TotalUASs,
       "wfDsx3TotalLCVs": wfDsx3TotalLCVs,
       "wfDsx3TotalPCVs": wfDsx3TotalPCVs,
       "wfDsx3TotalLESs": wfDsx3TotalLESs,
       "wfDsx3TotalCCVs": wfDsx3TotalCCVs,
       "wfDsx3TotalCESs": wfDsx3TotalCESs,
       "wfDsx3TotalCSESs": wfDsx3TotalCSESs,
       "wfDsx3TotalSASs": wfDsx3TotalSASs,
       "wfDsx3TotalAISSs": wfDsx3TotalAISSs,
       "wfDsx3TotalFCs": wfDsx3TotalFCs,
       "wfDsx3TotalValidFlag": wfDsx3TotalValidFlag,
       "wfDsx3FarEndConfigTable": wfDsx3FarEndConfigTable,
       "wfDsx3FarEndConfigEntry": wfDsx3FarEndConfigEntry,
       "wfDsx3FarEndLineIndex": wfDsx3FarEndLineIndex,
       "wfDsx3FarEndEquipCode": wfDsx3FarEndEquipCode,
       "wfDsx3FarEndLocationIDCode": wfDsx3FarEndLocationIDCode,
       "wfDsx3FarEndFrameIDCode": wfDsx3FarEndFrameIDCode,
       "wfDsx3FarEndUnitCode": wfDsx3FarEndUnitCode,
       "wfDsx3FarEndFacilityIDCode": wfDsx3FarEndFacilityIDCode,
       "wfDsx3FarEndCurrentTable": wfDsx3FarEndCurrentTable,
       "wfDsx3FarEndCurrentEntry": wfDsx3FarEndCurrentEntry,
       "wfDsx3FarEndCurrentIndex": wfDsx3FarEndCurrentIndex,
       "wfDsx3FarEndTimeElapsed": wfDsx3FarEndTimeElapsed,
       "wfDsx3FarEndValidIntervals": wfDsx3FarEndValidIntervals,
       "wfDsx3FarEndCurrentCESs": wfDsx3FarEndCurrentCESs,
       "wfDsx3FarEndCurrentCSESs": wfDsx3FarEndCurrentCSESs,
       "wfDsx3FarEndCurrentCCVs": wfDsx3FarEndCurrentCCVs,
       "wfDsx3FarEndCurrentUASs": wfDsx3FarEndCurrentUASs,
       "wfDsx3FarEndCurrentSASs": wfDsx3FarEndCurrentSASs,
       "wfDsx3FarEndCurrentFCs": wfDsx3FarEndCurrentFCs,
       "wfDsx3FarEndCurrentValidFlag": wfDsx3FarEndCurrentValidFlag,
       "wfDsx3FarEndIntervalTable": wfDsx3FarEndIntervalTable,
       "wfDsx3FarEndIntervalEntry": wfDsx3FarEndIntervalEntry,
       "wfDsx3FarEndIntervalIndex": wfDsx3FarEndIntervalIndex,
       "wfDsx3FarEndIntervalNumber": wfDsx3FarEndIntervalNumber,
       "wfDsx3FarEndIntervalCESs": wfDsx3FarEndIntervalCESs,
       "wfDsx3FarEndIntervalCSESs": wfDsx3FarEndIntervalCSESs,
       "wfDsx3FarEndIntervalCCVs": wfDsx3FarEndIntervalCCVs,
       "wfDsx3FarEndIntervalUASs": wfDsx3FarEndIntervalUASs,
       "wfDsx3FarEndIntervalSASs": wfDsx3FarEndIntervalSASs,
       "wfDsx3FarEndIntervalFCs": wfDsx3FarEndIntervalFCs,
       "wfDsx3FarEndIntervalValidFlag": wfDsx3FarEndIntervalValidFlag,
       "wfDsx3FarEndTotalTable": wfDsx3FarEndTotalTable,
       "wfDsx3FarEndTotalEntry": wfDsx3FarEndTotalEntry,
       "wfDsx3FarEndTotalIndex": wfDsx3FarEndTotalIndex,
       "wfDsx3FarEndTotalCESs": wfDsx3FarEndTotalCESs,
       "wfDsx3FarEndTotalCSESs": wfDsx3FarEndTotalCSESs,
       "wfDsx3FarEndTotalCCVs": wfDsx3FarEndTotalCCVs,
       "wfDsx3FarEndTotalUASs": wfDsx3FarEndTotalUASs,
       "wfDsx3FarEndTotalSASs": wfDsx3FarEndTotalSASs,
       "wfDsx3FarEndTotalFCs": wfDsx3FarEndTotalFCs,
       "wfDsx3FarEndTotalValidFlag": wfDsx3FarEndTotalValidFlag,
       "wfAtmInterfaceDs3PlcpTable": wfAtmInterfaceDs3PlcpTable,
       "wfAtmInterfaceDs3PlcpEntry": wfAtmInterfaceDs3PlcpEntry,
       "wfAtmInterfaceDs3PlcpIndex": wfAtmInterfaceDs3PlcpIndex,
       "wfAtmInterfaceDs3PlcpSEFSs": wfAtmInterfaceDs3PlcpSEFSs,
       "wfAtmInterfaceDs3PlcpAlarmState": wfAtmInterfaceDs3PlcpAlarmState,
       "wfAtmInterfaceDs3PlcpUASs": wfAtmInterfaceDs3PlcpUASs,
       "wfDsx3DayCurrentTable": wfDsx3DayCurrentTable,
       "wfDsx3DayCurrentEntry": wfDsx3DayCurrentEntry,
       "wfDsx3DayCurrentIndex": wfDsx3DayCurrentIndex,
       "wfDsx3DayCurrentPESs": wfDsx3DayCurrentPESs,
       "wfDsx3DayCurrentPSESs": wfDsx3DayCurrentPSESs,
       "wfDsx3DayCurrentSEFSs": wfDsx3DayCurrentSEFSs,
       "wfDsx3DayCurrentUASs": wfDsx3DayCurrentUASs,
       "wfDsx3DayCurrentLCVs": wfDsx3DayCurrentLCVs,
       "wfDsx3DayCurrentPCVs": wfDsx3DayCurrentPCVs,
       "wfDsx3DayCurrentLESs": wfDsx3DayCurrentLESs,
       "wfDsx3DayCurrentCCVs": wfDsx3DayCurrentCCVs,
       "wfDsx3DayCurrentCESs": wfDsx3DayCurrentCESs,
       "wfDsx3DayCurrentCSESs": wfDsx3DayCurrentCSESs,
       "wfDsx3DayCurrentSASs": wfDsx3DayCurrentSASs,
       "wfDsx3DayCurrentAISSs": wfDsx3DayCurrentAISSs,
       "wfDsx3DayCurrentFCs": wfDsx3DayCurrentFCs,
       "wfDsx3DayCurrentTimeElapsed": wfDsx3DayCurrentTimeElapsed,
       "wfDsx3DayCurrentValidIntervals": wfDsx3DayCurrentValidIntervals,
       "wfDsx3DayCurrentValidFlag": wfDsx3DayCurrentValidFlag,
       "wfDsx3DayIntervalTable": wfDsx3DayIntervalTable,
       "wfDsx3DayIntervalEntry": wfDsx3DayIntervalEntry,
       "wfDsx3DayIntervalIndex": wfDsx3DayIntervalIndex,
       "wfDsx3DayIntervalNumber": wfDsx3DayIntervalNumber,
       "wfDsx3DayIntervalPESs": wfDsx3DayIntervalPESs,
       "wfDsx3DayIntervalPSESs": wfDsx3DayIntervalPSESs,
       "wfDsx3DayIntervalSEFSs": wfDsx3DayIntervalSEFSs,
       "wfDsx3DayIntervalUASs": wfDsx3DayIntervalUASs,
       "wfDsx3DayIntervalLCVs": wfDsx3DayIntervalLCVs,
       "wfDsx3DayIntervalPCVs": wfDsx3DayIntervalPCVs,
       "wfDsx3DayIntervalLESs": wfDsx3DayIntervalLESs,
       "wfDsx3DayIntervalCCVs": wfDsx3DayIntervalCCVs,
       "wfDsx3DayIntervalCESs": wfDsx3DayIntervalCESs,
       "wfDsx3DayIntervalCSESs": wfDsx3DayIntervalCSESs,
       "wfDsx3DayIntervalSASs": wfDsx3DayIntervalSASs,
       "wfDsx3DayIntervalAISSs": wfDsx3DayIntervalAISSs,
       "wfDsx3DayIntervalFCs": wfDsx3DayIntervalFCs,
       "wfDsx3DayIntervalValidFlag": wfDsx3DayIntervalValidFlag,
       "wfDsx3DayTotalTable": wfDsx3DayTotalTable,
       "wfDsx3DayTotalEntry": wfDsx3DayTotalEntry,
       "wfDsx3DayTotalIndex": wfDsx3DayTotalIndex,
       "wfDsx3DayTotalPESs": wfDsx3DayTotalPESs,
       "wfDsx3DayTotalPSESs": wfDsx3DayTotalPSESs,
       "wfDsx3DayTotalSEFSs": wfDsx3DayTotalSEFSs,
       "wfDsx3DayTotalUASs": wfDsx3DayTotalUASs,
       "wfDsx3DayTotalLCVs": wfDsx3DayTotalLCVs,
       "wfDsx3DayTotalPCVs": wfDsx3DayTotalPCVs,
       "wfDsx3DayTotalLESs": wfDsx3DayTotalLESs,
       "wfDsx3DayTotalCCVs": wfDsx3DayTotalCCVs,
       "wfDsx3DayTotalCESs": wfDsx3DayTotalCESs,
       "wfDsx3DayTotalCSESs": wfDsx3DayTotalCSESs,
       "wfDsx3DayTotalSASs": wfDsx3DayTotalSASs,
       "wfDsx3DayTotalAISSs": wfDsx3DayTotalAISSs,
       "wfDsx3DayTotalFCs": wfDsx3DayTotalFCs,
       "wfDsx3DayTotalValidFlag": wfDsx3DayTotalValidFlag,
       "wfDsx3FarEndDayCurrentTable": wfDsx3FarEndDayCurrentTable,
       "wfDsx3FarEndDayCurrentEntry": wfDsx3FarEndDayCurrentEntry,
       "wfDsx3FarEndDayCurrentIndex": wfDsx3FarEndDayCurrentIndex,
       "wfDsx3FarEndDayTimeElapsed": wfDsx3FarEndDayTimeElapsed,
       "wfDsx3FarEndDayValidIntervals": wfDsx3FarEndDayValidIntervals,
       "wfDsx3FarEndDayCurrentCESs": wfDsx3FarEndDayCurrentCESs,
       "wfDsx3FarEndDayCurrentCSESs": wfDsx3FarEndDayCurrentCSESs,
       "wfDsx3FarEndDayCurrentCCVs": wfDsx3FarEndDayCurrentCCVs,
       "wfDsx3FarEndDayCurrentUASs": wfDsx3FarEndDayCurrentUASs,
       "wfDsx3FarEndDayCurrentSASs": wfDsx3FarEndDayCurrentSASs,
       "wfDsx3FarEndDayCurrentFCs": wfDsx3FarEndDayCurrentFCs,
       "wfDsx3FarEndDayCurrentValidFlag": wfDsx3FarEndDayCurrentValidFlag,
       "wfDsx3FarEndDayIntervalTable": wfDsx3FarEndDayIntervalTable,
       "wfDsx3FarEndDayIntervalEntry": wfDsx3FarEndDayIntervalEntry,
       "wfDsx3FarEndDayIntervalIndex": wfDsx3FarEndDayIntervalIndex,
       "wfDsx3FarEndDayIntervalNumber": wfDsx3FarEndDayIntervalNumber,
       "wfDsx3FarEndDayIntervalCESs": wfDsx3FarEndDayIntervalCESs,
       "wfDsx3FarEndDayIntervalCSESs": wfDsx3FarEndDayIntervalCSESs,
       "wfDsx3FarEndDayIntervalCCVs": wfDsx3FarEndDayIntervalCCVs,
       "wfDsx3FarEndDayIntervalUASs": wfDsx3FarEndDayIntervalUASs,
       "wfDsx3FarEndDayIntervalSASs": wfDsx3FarEndDayIntervalSASs,
       "wfDsx3FarEndDayIntervalFCs": wfDsx3FarEndDayIntervalFCs,
       "wfDsx3FarEndDayIntervalValidFlag": wfDsx3FarEndDayIntervalValidFlag,
       "wfDsx3FarEndDayTotalTable": wfDsx3FarEndDayTotalTable,
       "wfDsx3FarEndDayTotalEntry": wfDsx3FarEndDayTotalEntry,
       "wfDsx3FarEndDayTotalIndex": wfDsx3FarEndDayTotalIndex,
       "wfDsx3FarEndDayTotalCESs": wfDsx3FarEndDayTotalCESs,
       "wfDsx3FarEndDayTotalCSESs": wfDsx3FarEndDayTotalCSESs,
       "wfDsx3FarEndDayTotalCCVs": wfDsx3FarEndDayTotalCCVs,
       "wfDsx3FarEndDayTotalUASs": wfDsx3FarEndDayTotalUASs,
       "wfDsx3FarEndDayTotalSASs": wfDsx3FarEndDayTotalSASs,
       "wfDsx3FarEndDayTotalFCs": wfDsx3FarEndDayTotalFCs,
       "wfDsx3FarEndDayTotalValidFlag": wfDsx3FarEndDayTotalValidFlag,
       "wfDsx3ThrAlrtTable": wfDsx3ThrAlrtTable,
       "wfDsx3ThrAlrtEntry": wfDsx3ThrAlrtEntry,
       "wfDsx3ThrAlrtDelete": wfDsx3ThrAlrtDelete,
       "wfDsx3ThrAlrtIndex": wfDsx3ThrAlrtIndex,
       "wfDsx3ThrAlrtPESs": wfDsx3ThrAlrtPESs,
       "wfDsx3ThrAlrtPSESs": wfDsx3ThrAlrtPSESs,
       "wfDsx3ThrAlrtSEFSs": wfDsx3ThrAlrtSEFSs,
       "wfDsx3ThrAlrtUASs": wfDsx3ThrAlrtUASs,
       "wfDsx3ThrAlrtLCVs": wfDsx3ThrAlrtLCVs,
       "wfDsx3ThrAlrtPCVs": wfDsx3ThrAlrtPCVs,
       "wfDsx3ThrAlrtLESs": wfDsx3ThrAlrtLESs,
       "wfDsx3ThrAlrtCCVs": wfDsx3ThrAlrtCCVs,
       "wfDsx3ThrAlrtCESs": wfDsx3ThrAlrtCESs,
       "wfDsx3ThrAlrtCSESs": wfDsx3ThrAlrtCSESs,
       "wfDsx3ThrAlrtSASs": wfDsx3ThrAlrtSASs,
       "wfDsx3ThrAlrtAISSs": wfDsx3ThrAlrtAISSs,
       "wfDsx3ThrAlrtFCs": wfDsx3ThrAlrtFCs,
       "wfDsx3FarEndThrAlrtTable": wfDsx3FarEndThrAlrtTable,
       "wfDsx3FarEndThrAlrtEntry": wfDsx3FarEndThrAlrtEntry,
       "wfDsx3FarEndThrAlrtDelete": wfDsx3FarEndThrAlrtDelete,
       "wfDsx3FarEndThrAlrtIndex": wfDsx3FarEndThrAlrtIndex,
       "wfDsx3FarEndThrAlrtCESs": wfDsx3FarEndThrAlrtCESs,
       "wfDsx3FarEndThrAlrtCSESs": wfDsx3FarEndThrAlrtCSESs,
       "wfDsx3FarEndThrAlrtCCVs": wfDsx3FarEndThrAlrtCCVs,
       "wfDsx3FarEndThrAlrtUASs": wfDsx3FarEndThrAlrtUASs,
       "wfDsx3FarEndThrAlrtSASs": wfDsx3FarEndThrAlrtSASs,
       "wfDsx3FarEndThrAlrtFCs": wfDsx3FarEndThrAlrtFCs,
       "wfDsx3DayThrAlrtTable": wfDsx3DayThrAlrtTable,
       "wfDsx3DayThrAlrtEntry": wfDsx3DayThrAlrtEntry,
       "wfDsx3DayThrAlrtDelete": wfDsx3DayThrAlrtDelete,
       "wfDsx3DayThrAlrtIndex": wfDsx3DayThrAlrtIndex,
       "wfDsx3DayThrAlrtPESs": wfDsx3DayThrAlrtPESs,
       "wfDsx3DayThrAlrtPSESs": wfDsx3DayThrAlrtPSESs,
       "wfDsx3DayThrAlrtSEFSs": wfDsx3DayThrAlrtSEFSs,
       "wfDsx3DayThrAlrtUASs": wfDsx3DayThrAlrtUASs,
       "wfDsx3DayThrAlrtLCVs": wfDsx3DayThrAlrtLCVs,
       "wfDsx3DayThrAlrtPCVs": wfDsx3DayThrAlrtPCVs,
       "wfDsx3DayThrAlrtLESs": wfDsx3DayThrAlrtLESs,
       "wfDsx3DayThrAlrtCCVs": wfDsx3DayThrAlrtCCVs,
       "wfDsx3DayThrAlrtCESs": wfDsx3DayThrAlrtCESs,
       "wfDsx3DayThrAlrtCSESs": wfDsx3DayThrAlrtCSESs,
       "wfDsx3DayThrAlrtSASs": wfDsx3DayThrAlrtSASs,
       "wfDsx3DayThrAlrtAISSs": wfDsx3DayThrAlrtAISSs,
       "wfDsx3DayThrAlrtFCs": wfDsx3DayThrAlrtFCs,
       "wfDsx3FarEndDayThrAlrtTable": wfDsx3FarEndDayThrAlrtTable,
       "wfDsx3FarEndDayThrAlrtEntry": wfDsx3FarEndDayThrAlrtEntry,
       "wfDsx3FarEndDayThrAlrtDelete": wfDsx3FarEndDayThrAlrtDelete,
       "wfDsx3FarEndDayThrAlrtIndex": wfDsx3FarEndDayThrAlrtIndex,
       "wfDsx3FarEndDayThrAlrtCESs": wfDsx3FarEndDayThrAlrtCESs,
       "wfDsx3FarEndDayThrAlrtCSESs": wfDsx3FarEndDayThrAlrtCSESs,
       "wfDsx3FarEndDayThrAlrtCCVs": wfDsx3FarEndDayThrAlrtCCVs,
       "wfDsx3FarEndDayThrAlrtUASs": wfDsx3FarEndDayThrAlrtUASs,
       "wfDsx3FarEndDayThrAlrtSASs": wfDsx3FarEndDayThrAlrtSASs,
       "wfDsx3FarEndDayThrAlrtFCs": wfDsx3FarEndDayThrAlrtFCs}
)
